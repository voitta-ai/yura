"""Multi-language static analysis to ground the LLM judge in objective evidence.

Two layers, both run on the *changed files at the commit's revision*:

  - lizard (in-process, ~20 languages): cyclomatic complexity, function length,
    parameter count, NLOC. Universal maintainability/readability anchors with
    zero config and no subprocess startup cost.
  - language-specific linters (best-effort, batched one process per commit):
    ruff for Python (bugs/security/style). A registry makes adding eslint /
    go vet / semgrep later a one-entry change; missing tools are skipped.

Findings are normalized and mapped to the RACE quality dimensions so they can be
injected into the judge prompt as evidence (per "Static Analysis as a Feedback
Loop", arXiv 2508.14419). The whole module degrades gracefully: if a tool is
absent or a language is unsupported, it simply contributes no findings.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from app.services import git_service
from app.services.git_service import Commit

# Complexity thresholds → maintainability/readability flags.
CCN_WARN = 15  # cyclomatic complexity per function
LEN_WARN = 80  # NLOC per function
PARAM_WARN = 6  # parameters per function

MAX_FILES_PER_COMMIT = 12  # bound cost on huge commits (largest churn first)

# Source extensions worth analyzing (lizard-supported + common). Anything else
# is skipped (configs, docs, data).
ANALYZABLE_EXT = {
    ".py", ".pyi", ".js", ".jsx", ".ts", ".tsx", ".vue", ".go", ".java",
    ".kt", ".kts", ".rb", ".php", ".c", ".h", ".cc", ".cpp", ".cxx", ".hpp",
    ".cs", ".swift", ".rs", ".scala", ".m", ".mm", ".lua", ".pl", ".r",
    ".sol", ".zig",
}

# RACE dimensions a finding can bear on.
DIM_READABILITY = "readability"
DIM_MAINTAINABILITY = "maintainability"
DIM_CORRECTNESS = "correctness"
DIM_SECURITY = "security"


@dataclass
class Finding:
    tool: str
    dimension: str
    severity: str  # "high" | "medium" | "low"
    message: str
    file: str = ""
    line: int | None = None


@dataclass
class CommitAnalysis:
    files_analyzed: int = 0
    languages: list[str] = field(default_factory=list)
    max_ccn: int = 0
    avg_ccn: float = 0.0
    complex_functions: list[str] = field(default_factory=list)  # "name (ccn N)"
    findings: list[Finding] = field(default_factory=list)
    available: bool = True  # False only if nothing could be analyzed

    def dim_counts(self) -> dict[str, int]:
        c: Counter = Counter()
        for f in self.findings:
            c[f.dimension] += 1
        return dict(c)

    def to_evidence(self) -> str:
        """Compact, judge-readable summary. Empty string if no signal."""
        if not self.files_analyzed:
            return ""
        parts = [
            f"Static analysis of {self.files_analyzed} changed file(s)"
            + (f" [{', '.join(self.languages)}]" if self.languages else "")
            + ":"
        ]
        if self.max_ccn:
            parts.append(
                f"- complexity: max cyclomatic {self.max_ccn}, avg {self.avg_ccn:.1f}"
                + (
                    f"; over-complex: {', '.join(self.complex_functions[:5])}"
                    if self.complex_functions
                    else ""
                )
            )
        # Group findings by dimension for a tight summary.
        by_dim: dict[str, list[Finding]] = {}
        for f in self.findings:
            by_dim.setdefault(f.dimension, []).append(f)
        for dim, fs in by_dim.items():
            sample = "; ".join(
                f"{x.message}" + (f" ({x.file}:{x.line})" if x.line else "")
                for x in fs[:4]
            )
            parts.append(f"- {dim}: {len(fs)} issue(s) — {sample}")
        if len(parts) == 1:
            parts.append("- no complexity or lint issues detected in changed code.")
        return "\n".join(parts)

    def to_dict(self) -> dict:
        return {
            "files_analyzed": self.files_analyzed,
            "languages": self.languages,
            "max_ccn": self.max_ccn,
            "avg_ccn": round(self.avg_ccn, 1),
            "complex_functions": self.complex_functions[:10],
            "dim_counts": self.dim_counts(),
            "n_findings": len(self.findings),
        }


# --------------------------------------------------------------------------- #
# Tool availability (probed once)
# --------------------------------------------------------------------------- #

_HAS_RUFF = shutil.which("ruff") is not None
try:
    import lizard as _lizard  # noqa: F401

    _HAS_LIZARD = True
except ImportError:  # pragma: no cover
    _HAS_LIZARD = False


def tools_available() -> dict[str, bool]:
    return {"lizard": _HAS_LIZARD, "ruff": _HAS_RUFF}


# --------------------------------------------------------------------------- #
# Core: analyze one commit's changed files
# --------------------------------------------------------------------------- #


def analyze_commit(repo_path: Path, commit: Commit) -> CommitAnalysis:
    """Materialize the commit's changed source files and run the analyzers."""
    analysis = CommitAnalysis()
    paths = [p for p in commit.files if Path(p).suffix.lower() in ANALYZABLE_EXT]
    if not paths:
        analysis.available = bool(_HAS_LIZARD or _HAS_RUFF)
        return analysis
    paths = paths[:MAX_FILES_PER_COMMIT]

    with tempfile.TemporaryDirectory(prefix="yura-sa-") as tmp:
        tmp_dir = Path(tmp)
        local: list[tuple[str, Path]] = []  # (repo-relative path, temp file)
        for rel in paths:
            content = git_service.get_file_at_revision(repo_path, commit.hash, rel)
            if content is None:
                continue
            dest = tmp_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8", errors="replace")
            local.append((rel, dest))

        if not local:
            return analysis
        analysis.files_analyzed = len(local)
        analysis.languages = sorted(
            {_lang_for(rel) for rel, _ in local if _lang_for(rel)}
        )

        if _HAS_LIZARD:
            _run_lizard(local, analysis)
        if _HAS_RUFF:
            _run_ruff(tmp_dir, local, analysis)

    return analysis


def _lang_for(path: str) -> str:
    ext = Path(path).suffix.lower()
    return {
        ".py": "python", ".pyi": "python", ".js": "javascript",
        ".jsx": "javascript", ".ts": "typescript", ".tsx": "typescript",
        ".vue": "vue", ".go": "go", ".java": "java", ".kt": "kotlin",
        ".rb": "ruby", ".php": "php", ".c": "c", ".h": "c", ".cc": "cpp",
        ".cpp": "cpp", ".cxx": "cpp", ".hpp": "cpp", ".cs": "csharp",
        ".swift": "swift", ".rs": "rust", ".scala": "scala", ".lua": "lua",
        ".r": "r", ".sol": "solidity", ".zig": "zig",
    }.get(ext, "")


def _run_lizard(local: list[tuple[str, Path]], analysis: CommitAnalysis) -> None:
    import lizard

    ccns: list[int] = []
    for rel, dest in local:
        try:
            info = lizard.analyze_file(str(dest))
        except Exception:  # lizard can choke on exotic syntax
            continue
        for fn in info.function_list:
            ccns.append(fn.cyclomatic_complexity)
            if fn.cyclomatic_complexity > CCN_WARN:
                analysis.complex_functions.append(
                    f"{fn.name} (ccn {fn.cyclomatic_complexity})"
                )
                analysis.findings.append(
                    Finding(
                        "lizard", DIM_MAINTAINABILITY, "medium",
                        f"high cyclomatic complexity {fn.cyclomatic_complexity}",
                        rel, fn.start_line,
                    )
                )
            if fn.nloc > LEN_WARN:
                analysis.findings.append(
                    Finding(
                        "lizard", DIM_READABILITY, "low",
                        f"long function ({fn.nloc} lines)", rel, fn.start_line,
                    )
                )
            if fn.parameter_count > PARAM_WARN:
                analysis.findings.append(
                    Finding(
                        "lizard", DIM_MAINTAINABILITY, "low",
                        f"too many parameters ({fn.parameter_count})",
                        rel, fn.start_line,
                    )
                )
    if ccns:
        analysis.max_ccn = max(ccns)
        analysis.avg_ccn = sum(ccns) / len(ccns)
    # Sort over-complex functions worst-first.
    analysis.complex_functions.sort(
        key=lambda s: int(s.rsplit("ccn ", 1)[-1].rstrip(")")), reverse=True
    )


# ruff rule prefix → (dimension, severity). S=flake8-bandit (security),
# B=bugbear, E9/F=syntax/pyflakes (correctness), others readability.
def _ruff_dim(code: str) -> tuple[str, str]:
    if code.startswith("S"):
        return DIM_SECURITY, "high"
    if code.startswith(("E9", "F8", "F6", "F7")):
        return DIM_CORRECTNESS, "high"
    if code.startswith(("B", "F")):
        return DIM_CORRECTNESS, "medium"
    return DIM_READABILITY, "low"


def _run_ruff(
    tmp_dir: Path, local: list[tuple[str, Path]], analysis: CommitAnalysis
) -> None:
    py = [str(dest) for rel, dest in local if dest.suffix.lower() in (".py", ".pyi")]
    if not py:
        return
    try:
        proc = subprocess.run(
            ["ruff", "check", "--select", "E9,F,B,S", "--output-format", "json",
             "--no-cache", "--isolated", "--quiet", *py],
            capture_output=True, text=True, timeout=60, cwd=str(tmp_dir),
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return
    out = proc.stdout.strip()
    if not out:
        return
    try:
        issues = json.loads(out)
    except json.JSONDecodeError:
        return
    rel_for = {str(dest): rel for rel, dest in local}
    for it in issues:
        code = it.get("code") or ""
        if not code:
            continue
        dim, sev = _ruff_dim(code)
        rel = rel_for.get(it.get("filename", ""), os.path.basename(it.get("filename", "")))
        analysis.findings.append(
            Finding(
                "ruff", dim, sev,
                f"{code}: {it.get('message', '')}",
                rel, (it.get("location") or {}).get("row"),
            )
        )
