"""Git operations: branch discovery, full-history clone, and log parsing.

We shell out to the `git` binary (more reliable than libgit bindings for full
history + committer identities) and parse a machine-friendly log format.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

# Field + record separators chosen to (almost) never collide with commit text.
_FS = "\x1f"  # unit separator between fields
_RS = "\x1e"  # record separator between commits

# Each record is prefixed with _RS so we can split cleanly; numstat follows.
_PRETTY = _RS + _FS.join(
    [
        "%H",  # full hash
        "%an",  # author name
        "%ae",  # author email
        "%cn",  # committer name
        "%ce",  # committer email
        "%at",  # author timestamp (unix)
        "%ct",  # committer timestamp (unix)
        "%P",  # parent hashes (space separated)
        "%s",  # subject
        "%b",  # body
    ]
)


class GitError(RuntimeError):
    pass


@dataclass
class Commit:
    hash: str
    author_name: str
    author_email: str
    committer_name: str
    committer_email: str
    author_ts: int
    committer_ts: int
    parents: list[str]
    subject: str
    body: str
    insertions: int = 0
    deletions: int = 0
    files_changed: int = 0

    @property
    def is_merge(self) -> bool:
        return len(self.parents) > 1

    @property
    def message_len(self) -> int:
        return len(self.subject) + (len(self.body) if self.body else 0)


def _run(args: list[str], cwd: Path | None = None, timeout: int = 600) -> str:
    try:
        proc = subprocess.run(
            args,
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except FileNotFoundError as exc:  # git not installed
        raise GitError("git executable not found on PATH") from exc
    except subprocess.TimeoutExpired as exc:
        raise GitError(f"git command timed out: {' '.join(args)}") from exc
    if proc.returncode != 0:
        raise GitError(proc.stderr.strip() or f"git failed: {' '.join(args)}")
    return proc.stdout


def derive_repo_name(url: str) -> str:
    """Extract a human name from an https or git@ URL."""
    cleaned = url.strip().rstrip("/")
    cleaned = re.sub(r"\.git$", "", cleaned)
    # git@host:owner/repo  or  https://host/owner/repo
    tail = re.split(r"[/:]", cleaned)
    parts = [p for p in tail if p]
    if len(parts) >= 2:
        return f"{parts[-2]}/{parts[-1]}"
    return parts[-1] if parts else cleaned


def list_remote_branches(url: str) -> list[str]:
    """`git ls-remote --heads` — works for https and git@ without cloning."""
    out = _run(["git", "ls-remote", "--heads", url.strip()], timeout=60)
    branches: list[str] = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        # <sha>\trefs/heads/<branch>
        _, _, ref = line.partition("\t")
        if ref.startswith("refs/heads/"):
            branches.append(ref[len("refs/heads/") :])
    # Sort with common default branches first.
    priority = {"main": 0, "master": 1, "develop": 2, "dev": 3}
    branches.sort(key=lambda b: (priority.get(b, 99), b))
    return branches


def clone_repo(url: str, branch: str, dest: Path) -> Path:
    """Full (non-shallow) clone of a single branch so all history is present."""
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    _run(
        [
            "git",
            "clone",
            "--branch",
            branch,
            "--single-branch",
            "--no-tags",
            url.strip(),
            str(dest),
        ],
        timeout=1800,
    )
    return dest


def get_commit_diff(repo_path: Path, commit_hash: str, max_chars: int = 6000) -> str:
    """Return the unified diff for a single commit, truncated to max_chars.

    Merge commits show nothing with the default `git show`; callers should skip
    merges (we do, in sampling).
    """
    out = _run(
        [
            "git",
            "-C",
            str(repo_path),
            "show",
            commit_hash,
            "--no-color",
            "--format=",  # diff only, no commit header
            "--unified=2",
        ],
        timeout=60,
    )
    if len(out) > max_chars:
        out = out[:max_chars] + f"\n… [diff truncated at {max_chars} characters]"
    return out


def parse_log(repo_path: Path, branch: str | None = None) -> list[Commit]:
    """Parse `git log --numstat` of the given branch into Commit records."""
    args = [
        "git",
        "-C",
        str(repo_path),
        "log",
        f"--pretty=format:{_PRETTY}",
        "--numstat",
    ]
    if branch:
        args.append(branch)
    out = _run(args, timeout=600)

    commits: list[Commit] = []
    # Records are separated by _RS; the first split element is empty.
    for raw in out.split(_RS):
        raw = raw.strip("\n")
        if not raw:
            continue
        # Header line (fields) then numstat lines follow on subsequent lines.
        header, _, rest = raw.partition("\n")
        fields = header.split(_FS)
        if len(fields) < 10:
            continue
        (
            h,
            an,
            ae,
            cn,
            ce,
            at,
            ct,
            parents,
            subject,
            body,
        ) = fields[:10]
        commit = Commit(
            hash=h,
            author_name=an,
            author_email=ae.lower(),
            committer_name=cn,
            committer_email=ce.lower(),
            author_ts=int(at) if at.isdigit() else 0,
            committer_ts=int(ct) if ct.isdigit() else 0,
            parents=parents.split() if parents else [],
            subject=subject,
            body=body,
        )
        # The body (%b) may itself contain newlines; numstat lines are the ones
        # matching "<num>\t<num>\t<path>". Scan the remainder for those.
        for line in rest.splitlines():
            m = re.match(r"^(-|\d+)\t(-|\d+)\t(.+)$", line)
            if not m:
                continue
            ins = 0 if m.group(1) == "-" else int(m.group(1))
            dels = 0 if m.group(2) == "-" else int(m.group(2))
            commit.insertions += ins
            commit.deletions += dels
            commit.files_changed += 1
        commits.append(commit)
    return commits
