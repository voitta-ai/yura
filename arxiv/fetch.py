"""Harvest 2024-2026 arXiv papers on LLM-based code-quality assessment.

Self-contained (stdlib only). Queries the arXiv API across many themes,
dedupes, filters to 2024-2026, downloads PDFs, and writes a manifest +
human-readable index. Respects arXiv rate limits (≥3s between API calls,
short delay between PDF downloads) and is resumable — already-downloaded
PDFs are skipped on re-run.

Usage:  python3 arxiv/fetch.py [--target N]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PDF_DIR = ROOT / "pdfs"
API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"

UA = "yura-research-harvester/1.0 (academic literature review; contact: local)"
DATE_FROM = datetime(2024, 1, 1, tzinfo=timezone.utc)

# Search themes — each is an arXiv query string. Grouped to maximize recall on
# LLM code-quality assessment, AI-code detection, and automated review.
QUERIES = [
    'all:"large language model" AND all:"code quality"',
    'all:"LLM" AND all:"code review"',
    'all:"large language model" AND all:"code review"',
    'abs:"LLM-as-a-judge" AND abs:code',
    'all:"LLM as a judge" AND all:code',
    'all:"automated code review" AND all:"language model"',
    'abs:"machine-generated code" AND abs:detection',
    'abs:"AI-generated code" AND abs:detection',
    'all:"detecting LLM-generated code"',
    'all:"ChatGPT" AND all:"generated code" AND all:detection',
    'all:"Copilot" AND all:"code quality"',
    'all:"code smell" AND all:"large language model"',
    'all:"code smell" AND all:"deep learning"',
    'abs:"code quality" AND abs:"deep learning" AND cat:cs.SE',
    'all:"vulnerability detection" AND all:"large language model" AND all:code',
    'all:"code evaluation" AND all:"large language model" AND all:benchmark',
    'all:"code correctness" AND all:"language model"',
    'abs:"LLM" AND abs:"software quality"',
    'all:"automated program repair" AND all:"large language model"',
    'all:"code generation" AND all:"evaluation metric" AND all:"language model"',
    'abs:"authorship attribution" AND abs:"source code" AND abs:"language model"',
    'all:"pull request" AND all:"large language model" AND all:review',
    'all:"commit message" AND all:"large language model" AND all:quality',
    'abs:"technical debt" AND abs:"machine learning" AND abs:code',
    'all:"code clone detection" AND all:"language model"',
    'abs:"reward model" AND abs:code AND abs:"language model"',
]

PER_QUERY = 60
SLUG_RE = re.compile(r"[^a-z0-9]+")


def slug(text: str, n: int = 70) -> str:
    s = SLUG_RE.sub("-", text.lower()).strip("-")
    return s[:n].strip("-")


def fetch_query(query: str) -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": PER_QUERY,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                raw = r.read()
            break
        except Exception as exc:  # transient network / 503
            if attempt == 3:
                print(f"  ! query failed: {exc}")
                return []
            time.sleep(5 * (attempt + 1))
    else:
        return []

    root = ET.fromstring(raw)
    out = []
    for e in root.findall(f"{ATOM}entry"):
        idu = e.findtext(f"{ATOM}id", "")
        m = re.search(r"arxiv\.org/abs/([^v]+)(v\d+)?", idu)
        if not m:
            continue
        aid = m.group(1)
        published = e.findtext(f"{ATOM}published", "")
        try:
            pub_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
        except ValueError:
            continue
        if pub_dt < DATE_FROM:
            continue
        title = " ".join((e.findtext(f"{ATOM}title", "") or "").split())
        summary = " ".join((e.findtext(f"{ATOM}summary", "") or "").split())
        authors = [
            a.findtext(f"{ATOM}name", "") for a in e.findall(f"{ATOM}author")
        ]
        cats = [
            c.attrib.get("term", "")
            for c in e.findall("{http://arxiv.org/schemas/atom}primary_category")
        ] or [c.attrib.get("term", "") for c in e.findall(f"{ATOM}category")]
        pdf = ""
        for link in e.findall(f"{ATOM}link"):
            if link.attrib.get("title") == "pdf":
                pdf = link.attrib.get("href", "")
        if not pdf:
            pdf = f"https://arxiv.org/pdf/{aid}"
        out.append(
            {
                "id": aid,
                "title": title,
                "authors": authors,
                "published": published[:10],
                "categories": cats,
                "abstract": summary,
                "pdf_url": pdf,
            }
        )
    return out


def download_pdf(paper: dict) -> bool:
    fname = f"{paper['id'].replace('/', '_')}_{slug(paper['title'])}.pdf"
    dest = PDF_DIR / fname
    paper["file"] = f"pdfs/{fname}"
    if dest.exists() and dest.stat().st_size > 20_000:
        paper["status"] = "cached"
        return True
    url = paper["pdf_url"]
    if not url.endswith(".pdf"):
        url = url + ".pdf"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 20_000 or not data[:5] == b"%PDF-":
                raise ValueError(f"not a valid PDF ({len(data)} bytes)")
            dest.write_bytes(data)
            paper["status"] = "downloaded"
            paper["bytes"] = len(data)
            return True
        except Exception as exc:
            if attempt == 2:
                paper["status"] = f"failed: {exc}"
                return False
            time.sleep(3 * (attempt + 1))
    return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=120)
    args = ap.parse_args()

    print(f"== harvesting metadata across {len(QUERIES)} themes ==")
    pool: dict[str, dict] = {}
    for i, q in enumerate(QUERIES, 1):
        hits = fetch_query(q)
        new = sum(1 for h in hits if h["id"] not in pool)
        for h in hits:
            pool.setdefault(h["id"], h)
        print(f"[{i:2}/{len(QUERIES)}] +{new:2} new ({len(hits)} hits) · pool={len(pool)} · {q[:48]}")
        time.sleep(3.1)  # arXiv API courtesy: ≥3s between calls

    papers = sorted(pool.values(), key=lambda p: p["published"], reverse=True)
    print(f"\n== {len(papers)} unique 2024-2026 papers found; downloading up to {args.target} ==\n")

    ok = 0
    for i, p in enumerate(papers, 1):
        if ok >= args.target:
            break
        success = download_pdf(p)
        if success:
            ok += 1
        flag = "✓" if success else "✗"
        print(f"[{ok:3}/{args.target}] {flag} {p['status']:11} {p['id']:14} {p['title'][:60]}")
        if p.get("status") == "downloaded":
            time.sleep(1.2)  # courtesy delay between fresh downloads

    downloaded = [p for p in papers if p.get("status") in ("downloaded", "cached")]
    (ROOT / "manifest.json").write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "query_themes": QUERIES,
                "total_unique": len(papers),
                "downloaded": len(downloaded),
                "papers": papers,
            },
            indent=2,
        )
    )
    _write_index(downloaded)
    print(f"\n== done: {len(downloaded)} PDFs in {PDF_DIR} ==")
    print(f"   manifest.json + index.md written to {ROOT}")


def _write_index(papers: list[dict]) -> None:
    lines = [
        "# arXiv corpus — LLM-based code-quality assessment (2024–2026)\n",
        f"{len(papers)} papers. Generated {datetime.now(timezone.utc):%Y-%m-%d}.\n",
    ]
    for p in sorted(papers, key=lambda x: x["published"], reverse=True):
        authors = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
        lines.append(
            f"### {p['title']}\n"
            f"- **{p['id']}** · {p['published']} · {', '.join(p['categories'][:3])}\n"
            f"- {authors}\n"
            f"- [`{p.get('file', '')}`]({p.get('file', '')}) · "
            f"[abs](https://arxiv.org/abs/{p['id']})\n\n"
            f"{p['abstract'][:500]}…\n"
        )
    (ROOT / "index.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
