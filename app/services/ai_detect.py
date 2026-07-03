"""Deterministic, model-free AI-generated-code detection via stylometry.

A weak-but-honest heuristic that reads structural style cues rather than asking
an LLM (which is circular — a model rating its own style). Features follow the
feature-based detection literature (e.g. "Whitespaces Don't Lie", arXiv
2601.19264): AI-written code tends to be *more uniform* than human code —
regular indentation, consistent blank-line rhythm, heavy explanatory comments,
little trailing whitespace, low line-length variance, and consistent naming.

Output is a 0-100 "AI-likelihood" with the contributing signals exposed for
transparency. This is intentionally presented as a *signal*, not a verdict.
"""
from __future__ import annotations

import re
from statistics import pstdev

_IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,}")
_SNAKE_RE = re.compile(r"^[a-z][a-z0-9_]*$")
_CAMEL_RE = re.compile(r"^[a-z]+(?:[A-Z][a-z0-9]*)+$")


def score_text(text: str) -> dict:
    """Return {ai_score: 0-100, signals: {...}} for a single source file."""
    lines = text.splitlines()
    code = [ln for ln in lines if ln.strip()]
    if len(code) < 8:
        return {"ai_score": None, "signals": {}}  # too small to judge

    n = len(lines)
    # 1. Trailing whitespace — humans leave more; AI almost none.
    trailing = sum(1 for ln in lines if ln != ln.rstrip())
    trailing_ratio = trailing / n
    sig_no_trailing = 1.0 - min(1.0, trailing_ratio * 25)  # ~0 trailing → ~1

    # 2. Indentation regularity — AI indents very consistently.
    indents = [len(ln) - len(ln.lstrip()) for ln in code if ln.startswith((" ", "\t"))]
    if indents:
        steps = [i for i in indents if i > 0]
        # fraction of indents that are clean multiples of the dominant unit
        unit = min(steps) if steps else 4
        clean = sum(1 for i in steps if unit and i % unit == 0)
        indent_regularity = clean / len(steps) if steps else 1.0
    else:
        indent_regularity = 0.5

    # 3. Comment density — AI over-explains.
    comment_lines = sum(
        1 for ln in code if ln.lstrip().startswith(("#", "//", "/*", "*", "--"))
    )
    comment_ratio = comment_lines / len(code)
    sig_comments = min(1.0, comment_ratio * 4)  # 25%+ comments → 1

    # 4. Line-length uniformity — AI lines cluster; humans vary.
    lengths = [len(ln) for ln in code]
    mean_len = sum(lengths) / len(lengths)
    spread = pstdev(lengths) if len(lengths) > 1 else 0
    cv = spread / mean_len if mean_len else 1.0  # coefficient of variation
    sig_uniform_len = 1.0 - min(1.0, cv)  # low variance → AI-ish

    # 5. Naming consistency — humans mix snake/camel more.
    idents = _IDENT_RE.findall(text)
    if idents:
        snake = sum(1 for w in idents if _SNAKE_RE.match(w))
        camel = sum(1 for w in idents if _CAMEL_RE.match(w))
        dominant = max(snake, camel)
        naming_consistency = dominant / (snake + camel) if (snake + camel) else 0.5
    else:
        naming_consistency = 0.5

    # 6. Blank-line rhythm — AI uses regular single blank separators.
    blanks = sum(1 for ln in lines if not ln.strip())
    blank_ratio = blanks / n
    sig_blank_rhythm = 1.0 - min(1.0, abs(blank_ratio - 0.18) * 4)  # ~18% is AI-typical

    signals = {
        "no_trailing_ws": round(sig_no_trailing, 2),
        "indent_regularity": round(indent_regularity, 2),
        "comment_density": round(sig_comments, 2),
        "line_uniformity": round(sig_uniform_len, 2),
        "naming_consistency": round(naming_consistency, 2),
        "blank_rhythm": round(sig_blank_rhythm, 2),
    }
    # Weighted blend → 0-100. Weights favor the strongest literature signals.
    score = (
        0.22 * sig_no_trailing
        + 0.20 * indent_regularity
        + 0.20 * sig_comments
        + 0.18 * sig_uniform_len
        + 0.12 * naming_consistency
        + 0.08 * sig_blank_rhythm
    )
    return {"ai_score": round(score * 100), "signals": signals}


def score_files(files: list[tuple[str, str]]) -> dict:
    """Aggregate stylometry across (path, content) pairs for one commit.

    Returns {ai_score: 0-100 | None, files_scored: int}.
    """
    scores = []
    for _path, content in files:
        r = score_text(content)
        if r["ai_score"] is not None:
            scores.append(r["ai_score"])
    if not scores:
        return {"ai_score": None, "files_scored": 0}
    return {
        "ai_score": round(sum(scores) / len(scores)),
        "files_scored": len(scores),
    }
