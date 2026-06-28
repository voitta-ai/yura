"""Relevance-rank the harvested pool and top up the corpus with the strongest
on-topic papers recency-sort missed. Reuses manifest.json metadata (no API
calls); only downloads PDFs we don't already have. Rewrites index.md ranked
by relevance.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import fetch  # local module: download_pdf, _write_index, slug

ROOT = Path(__file__).resolve().parent
TARGET_TOTAL = 165

# Relevance lexicon — weighted phrase hits in title (3x) + abstract (1x).
CORE = {
    "code quality": 5, "code review": 4, "llm-as-a-judge": 5, "llm as a judge": 5,
    "ai-generated code": 5, "machine-generated code": 5, "llm-generated code": 5,
    "generated code": 2, "code generation": 1, "code smell": 5,
    "automated code review": 5, "code evaluation": 4, "evaluating code": 3,
    "code correctness": 4, "software quality": 4, "vulnerability detection": 3,
    "program repair": 3, "authorship attribution": 4, "code clone": 3,
    "commit message": 3, "pull request": 3, "technical debt": 3,
    "reward model": 2, "static analysis": 2, "code understanding": 2,
    "detect": 1, "assess": 1, "quality assessment": 5, "benchmark": 1,
    "code review automation": 5, "copilot": 2, "chatgpt": 1,
}
SE_BONUS = {"cs.SE": 4, "cs.CR": 1, "cs.PL": 2}


def score(p: dict) -> float:
    title = p["title"].lower()
    abs = p["abstract"].lower()
    s = 0.0
    for term, w in CORE.items():
        if term in title:
            s += w * 3
        if term in abs:
            s += w
    for cat in p["categories"][:2]:
        s += SE_BONUS.get(cat, 0)
    return s


def main() -> None:
    m = json.loads((ROOT / "manifest.json").read_text())
    papers = m["papers"]
    for p in papers:
        p["relevance"] = score(p)

    have = {p["id"] for p in papers if p.get("status") in ("downloaded", "cached")}
    ranked = sorted(papers, key=lambda p: (p["relevance"], p["published"]), reverse=True)

    # Top up with the highest-relevance papers we don't yet have.
    missing = [p for p in ranked if p["id"] not in have and p["relevance"] >= 8]
    need = max(0, TARGET_TOTAL - len(have))
    to_get = missing[:need]
    print(f"have {len(have)} · topping up with {len(to_get)} high-relevance papers\n")

    added = 0
    for p in to_get:
        if fetch.download_pdf(p):
            added += 1
            print(f"[+{added:3}] rel={p['relevance']:4.0f} {p['id']:14} {p['title'][:60]}")
            if p.get("status") == "downloaded":
                time.sleep(1.2)

    downloaded = [p for p in papers if p.get("status") in ("downloaded", "cached")]
    m["downloaded"] = len(downloaded)
    (ROOT / "manifest.json").write_text(json.dumps(m, indent=2))

    # Rewrite index.md ranked by relevance (most useful first).
    downloaded.sort(key=lambda p: (p["relevance"], p["published"]), reverse=True)
    fetch._write_index(downloaded)
    print(f"\n== corpus now {len(downloaded)} PDFs · index.md ranked by relevance ==")
    print("top 10 by relevance:")
    for p in downloaded[:10]:
        print(f"  rel={p['relevance']:4.0f}  {p['title'][:68]}")


if __name__ == "__main__":
    main()
