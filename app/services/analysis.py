"""Aggregate parsed commits into per-developer metrics and a ranking.

This is the "local" analysis pass — pure git statistics, no LLM. Phase 2 layers
LLM-judged commit-quality / AI-usage scores on top of the same structure.
"""
from __future__ import annotations

import datetime as dt
import re
from collections import defaultdict

from app.services.git_service import Commit

# Generic low-effort commit subjects used by the local "shitty commit" heuristic.
_GENERIC_RE = re.compile(
    r"^\s*(wip|fix|fixes|fixed|update|updates|updated|changes?|stuff|test|tests|"
    r"misc|tmp|temp|asdf|\.+|minor|cleanup|edit|commit)\s*$",
    re.IGNORECASE,
)
# Signals that AI assistance was involved (local heuristic only; LLM refines this).
_AI_RE = re.compile(
    r"(co-?authored-by:.*(copilot|claude|gpt|cursor|codex))|"
    r"\b(copilot|chatgpt|claude code|cursor|codegen|ai[- ]generated)\b",
    re.IGNORECASE,
)

# Composite-score weights (transparent, shown in the report).
WEIGHTS = {"volume": 0.40, "consistency": 0.25, "quality": 0.35}

# When LLM judgments are present, the composite reweights to give the
# model-judged quality real weight.
WEIGHTS_LLM = {
    "volume": 0.30,
    "consistency": 0.15,
    "quality": 0.20,
    "ai_quality": 0.35,
}

# Small-sample shrinkage constant: score *= commits / (commits + K).
CREDIBILITY_K = 8

# Thresholds for the LLM heuristics surfaced in the report.
FAKE_AUTHENTICITY = 40  # authenticity below this == flagged "fake/low-effort"
AI_LIKELIHOOD = 60  # ai_likelihood above this == counted as AI-assisted


def _month(ts: int) -> str:
    return dt.datetime.utcfromtimestamp(ts).strftime("%Y-%m")


def _is_shitty(c: Commit) -> bool:
    """Local heuristic: empty/generic message, or a trivial 1-line touch."""
    if not c.subject.strip():
        return True
    if _GENERIC_RE.match(c.subject):
        return True
    if c.message_len <= 5 and c.insertions + c.deletions <= 1:
        return True
    return False


def _norm(value: float, lo: float, hi: float) -> float:
    if hi <= lo:
        return 0.0
    return max(0.0, min(1.0, (value - lo) / (hi - lo)))


def analyze(commits: list[Commit]) -> dict:
    """Return the full report payload consumed by templates and chart builders."""
    non_merge = [c for c in commits if not c.is_merge]

    # --- group by author identity (email is the stable key) ---
    by_email: dict[str, list[Commit]] = defaultdict(list)
    for c in non_merge:
        by_email[c.author_email].append(c)

    months_all: set[str] = set()
    devs: list[dict] = []

    for email, cs in by_email.items():
        # Most frequent display name for this email.
        name_counts: dict[str, int] = defaultdict(int)
        for c in cs:
            name_counts[c.author_name] += 1
        name = max(name_counts, key=name_counts.get)

        insertions = sum(c.insertions for c in cs)
        deletions = sum(c.deletions for c in cs)
        churn = insertions + deletions
        files = sum(c.files_changed for c in cs)
        timestamps = [c.author_ts for c in cs if c.author_ts]
        active_days = {dt.datetime.utcfromtimestamp(t).date() for t in timestamps}
        months = {_month(t) for t in timestamps}
        months_all |= months
        shitty = sum(1 for c in cs if _is_shitty(c))
        ai = sum(1 for c in cs if _AI_RE.search(c.subject + "\n" + (c.body or "")))
        first = min(timestamps) if timestamps else 0
        last = max(timestamps) if timestamps else 0

        devs.append(
            {
                "name": name,
                "email": email,
                "commits": len(cs),
                "insertions": insertions,
                "deletions": deletions,
                "churn": churn,
                "net": insertions - deletions,
                "files_changed": files,
                "avg_commit_size": round(churn / len(cs), 1) if cs else 0,
                "avg_msg_len": round(
                    sum(c.message_len for c in cs) / len(cs), 1
                )
                if cs
                else 0,
                "active_days": len(active_days),
                "active_months": sorted(months),
                "first_ts": first,
                "last_ts": last,
                "tenure_days": max(1, (last - first) // 86400) if first else 0,
                "shitty_commits": shitty,
                "shitty_ratio": round(shitty / len(cs), 3) if cs else 0,
                "ai_signal_commits": ai,
                "_ts": sorted(timestamps),
            }
        )

    _score(devs)
    devs.sort(key=lambda d: d["score"], reverse=True)
    for i, d in enumerate(devs, 1):
        d["rank"] = i
        d.pop("_ts", None)

    timeline = _build_timeline(non_merge, by_email, months_all, devs)
    totals = _build_totals(commits, non_merge, devs)

    report = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": "local",
        "weights": WEIGHTS,
        "totals": totals,
        "developers": devs,
        "timeline": timeline,
    }
    _narrate(report)
    return report


def _score(devs: list[dict]) -> None:
    """Normalize metrics across the cohort and compute a 0–100 composite."""
    if not devs:
        return
    max_commits = max(d["commits"] for d in devs)
    max_churn = max(d["churn"] for d in devs) or 1
    max_active = max(d["active_days"] for d in devs) or 1
    max_msg = max(d["avg_msg_len"] for d in devs) or 1

    for d in devs:
        volume = 0.6 * _norm(d["commits"], 0, max_commits) + 0.4 * _norm(
            d["churn"], 0, max_churn
        )
        # Consistency: how spread out activity is + cadence within tenure.
        cadence = d["active_days"] / max(1, d["tenure_days"]) * 7  # active days/week
        consistency = 0.6 * _norm(d["active_days"], 0, max_active) + 0.4 * _norm(
            cadence, 0, 7
        )
        # Quality: low shitty ratio + reasonable message discipline.
        quality = 0.65 * (1 - d["shitty_ratio"]) + 0.35 * _norm(
            d["avg_msg_len"], 0, max_msg
        )

        # Credibility dampener: a 1-commit drive-by shouldn't out-rank a
        # sustained contributor on a lucky "perfect cadence". Shrinks small
        # samples toward zero (commits/(commits+K)); negligible for prolific devs.
        credibility = d["commits"] / (d["commits"] + CREDIBILITY_K)

        d["score_breakdown"] = {
            "volume": round(volume * 100, 1),
            "consistency": round(consistency * 100, 1),
            "quality": round(quality * 100, 1),
        }
        d["credibility"] = round(credibility, 3)
        d["score"] = round(
            (
                WEIGHTS["volume"] * volume
                + WEIGHTS["consistency"] * consistency
                + WEIGHTS["quality"] * quality
            )
            * credibility
            * 100,
            1,
        )


def _build_timeline(
    non_merge: list[Commit],
    by_email: dict[str, list[Commit]],
    months_all: set[str],
    devs: list[dict],
) -> dict:
    labels = sorted(months_all)
    idx = {m: i for i, m in enumerate(labels)}
    total = [0] * len(labels)
    by_dev: dict[str, list[int]] = {}

    for c in non_merge:
        if c.author_ts:
            total[idx[_month(c.author_ts)]] += 1

    # Track the top contributors individually for the small-multiples chart.
    for d in devs[:6]:
        series = [0] * len(labels)
        for c in by_email[d["email"]]:
            if c.author_ts:
                series[idx[_month(c.author_ts)]] += 1
        by_dev[d["email"]] = series

    return {"labels": labels, "total": total, "by_dev": by_dev}


def _build_totals(
    commits: list[Commit], non_merge: list[Commit], devs: list[dict]
) -> dict:
    ts = [c.author_ts for c in commits if c.author_ts]
    first = min(ts) if ts else 0
    last = max(ts) if ts else 0
    return {
        "commits": len(non_merge),
        "merges": len(commits) - len(non_merge),
        "developers": len(devs),
        "insertions": sum(d["insertions"] for d in devs),
        "deletions": sum(d["deletions"] for d in devs),
        "churn": sum(d["churn"] for d in devs),
        "files_changed": sum(d["files_changed"] for d in devs),
        "shitty_commits": sum(d["shitty_commits"] for d in devs),
        "first_date": dt.datetime.utcfromtimestamp(first).strftime("%Y-%m-%d")
        if first
        else "—",
        "last_date": dt.datetime.utcfromtimestamp(last).strftime("%Y-%m-%d")
        if last
        else "—",
        "span_days": (last - first) // 86400 if first else 0,
    }


def apply_llm_scores(
    report: dict, judgments: dict[str, dict], commits: list[Commit]
) -> None:
    """Fold per-commit LLM judgments into the report in place.

    Aggregates judged commits per developer, recomputes a blended composite
    score (local metrics + model-judged quality), re-ranks, and attaches the
    most-notable flagged commits for the report.
    """
    hash_author = {c.hash: c.author_email for c in commits}
    hash_meta = {c.hash: c for c in commits}

    per_dev: dict[str, list[dict]] = defaultdict(list)
    for h, j in judgments.items():
        email = hash_author.get(h)
        if email:
            per_dev[email].append(j)

    devs = report["developers"]
    for d in devs:
        js = per_dev.get(d["email"], [])
        if js:
            n = len(js)
            avg_q = sum(j["quality"] for j in js) / n
            avg_auth = sum(j["authenticity"] for j in js) / n
            avg_ai = sum(j["ai_likelihood"] for j in js) / n
            d["llm"] = {
                "judged": n,
                "avg_quality": round(avg_q, 1),
                "avg_authenticity": round(avg_auth, 1),
                "avg_ai_likelihood": round(avg_ai, 1),
                "fake_commits": sum(
                    1 for j in js if j["authenticity"] < FAKE_AUTHENTICITY
                ),
                "ai_commits": sum(1 for j in js if j["ai_likelihood"] > AI_LIKELIHOOD),
            }
            # Model-judged quality: craftsmanship weighted with authenticity.
            ai_quality = (0.6 * avg_q + 0.4 * avg_auth) / 100.0
        else:
            d["llm"] = {"judged": 0}
            # No judged commits — fall back to local quality so the dev isn't
            # unfairly penalized for not being sampled.
            ai_quality = d["score_breakdown"]["quality"] / 100.0

        sb = d["score_breakdown"]
        sb["ai_quality"] = round(ai_quality * 100, 1)
        blended = (
            WEIGHTS_LLM["volume"] * sb["volume"] / 100
            + WEIGHTS_LLM["consistency"] * sb["consistency"] / 100
            + WEIGHTS_LLM["quality"] * sb["quality"] / 100
            + WEIGHTS_LLM["ai_quality"] * ai_quality
        )
        d["score"] = round(blended * d.get("credibility", 1.0) * 100, 1)

    devs.sort(key=lambda d: d["score"], reverse=True)
    for i, d in enumerate(devs, 1):
        d["rank"] = i

    report["mode"] = "llm"
    report["weights"] = WEIGHTS_LLM

    # Notable commits: lowest-authenticity (flagged) and most AI-looking.
    enriched = []
    for h, j in judgments.items():
        c = hash_meta.get(h)
        if c is None:
            continue
        enriched.append(
            {
                "hash": h[:8],
                "author": c.author_name,
                "subject": c.subject[:80],
                "quality": j["quality"],
                "authenticity": j["authenticity"],
                "ai_likelihood": j["ai_likelihood"],
                "rationale": j.get("rationale", ""),
            }
        )
    report["flagged_commits"] = sorted(
        enriched, key=lambda e: e["authenticity"]
    )[:8]
    report["ai_commits"] = sorted(
        enriched, key=lambda e: e["ai_likelihood"], reverse=True
    )[:8]
    report["llm_totals"] = {
        "judged": len(judgments),
        "fake": sum(1 for e in enriched if e["authenticity"] < FAKE_AUTHENTICITY),
        "ai": sum(1 for e in enriched if e["ai_likelihood"] > AI_LIKELIHOOD),
        "avg_quality": round(
            sum(e["quality"] for e in enriched) / len(enriched), 1
        )
        if enriched
        else 0,
        "avg_authenticity": round(
            sum(e["authenticity"] for e in enriched) / len(enriched), 1
        )
        if enriched
        else 0,
        "avg_ai_likelihood": round(
            sum(e["ai_likelihood"] for e in enriched) / len(enriched), 1
        )
        if enriched
        else 0,
    }
    _narrate(report)  # refresh story + captions now that LLM data is present


def _narrate(report: dict) -> None:
    """Compute the data-driven executive story + per-section captions.

    Always sets a deterministic story; the LLM synthesis step (if it runs)
    overwrites report['story'] afterwards with richer prose.
    """
    devs = report["developers"]
    t = report["totals"]
    caps: dict[str, str] = {}

    if not devs:
        report["captions"] = caps
        report["story"] = {
            "headline": "No contributors found in this history.",
            "narrative": "",
            "findings": [],
            "by_llm": False,
        }
        return

    leader = devs[0]
    second = devs[1] if len(devs) > 1 else None
    total_commits = sum(d["commits"] for d in devs) or 1
    top3 = sum(d["commits"] for d in devs[:3])
    conc = round(top3 / total_commits * 100)
    top_commit = max(devs, key=lambda d: d["commits"])
    top_churn = max(devs, key=lambda d: d["churn"])

    tl = report["timeline"]
    if tl["total"]:
        peak_i = max(range(len(tl["total"])), key=lambda i: tl["total"][i])
        peak_month, peak_n = tl["labels"][peak_i], tl["total"][peak_i]
    else:
        peak_month, peak_n = "—", 0

    caps["ranking"] = (
        f"{leader['name']} leads with {leader['score']}"
        + (
            f", {round(leader['score'] - second['score'], 1)} points clear of "
            f"{second['name']}"
            if second
            else ""
        )
        + f". The top 3 contributors account for {conc}% of all commits."
    )
    caps["breakdown"] = (
        "Volume, consistency, and quality rarely move together — the "
        "highest-output contributor isn't always the most disciplined."
    )
    caps["output"] = (
        f"{top_commit['name']} leads on raw commits ({top_commit['commits']}), "
        f"while {top_churn['name']} moved the most code "
        f"({top_churn['churn']:,} lines)."
    )
    caps["cadence"] = f"Team activity peaked in {peak_month} with {peak_n} commits."

    findings = [caps["ranking"], caps["output"]]

    if report.get("mode") == "llm" and report.get("llm_totals"):
        lt = report["llm_totals"]
        judged_devs = [d for d in devs if d.get("llm", {}).get("judged")]
        best_q = (
            max(judged_devs, key=lambda d: d["llm"]["avg_quality"])
            if judged_devs
            else None
        )
        top_ai = (
            max(judged_devs, key=lambda d: d["llm"]["avg_ai_likelihood"])
            if judged_devs
            else None
        )
        fake_pct = round(lt["fake"] / lt["judged"] * 100) if lt["judged"] else 0
        caps["quality"] = (
            f"Across {lt['judged']} model-judged commits, mean quality is "
            f"{lt['avg_quality']}"
            + (
                f"; {best_q['name']} sets the bar at "
                f"{best_q['llm']['avg_quality']}."
                if best_q
                else "."
            )
        )
        caps["authenticity"] = (
            f"{lt['fake']} commits ({fake_pct}%) scored below the authenticity "
            "bar — trivial, padding, or noise."
        )
        caps["ai"] = (
            f"AI-assistance signal averages {lt['avg_ai_likelihood']}"
            + (
                f", most pronounced for {top_ai['name']} "
                f"({top_ai['llm']['avg_ai_likelihood']})."
                if top_ai
                else "."
            )
        )
        caps["watchlist"] = (
            "The model's least-convincing commits — worth a human look before "
            "they count toward anyone's record."
        )
        findings += [caps["quality"], caps["authenticity"], caps["ai"]]
        headline = (
            f"{leader['name']} leads {t['developers']} contributors on a "
            "model-judged performance review."
        )
        narrative = (
            f"{leader['name']} tops the cohort with a blended score of "
            f"{leader['score']}, pairing {leader['commits']} commits with strong "
            f"model-judged quality. Across {lt['judged']} commits reviewed by the "
            f"model, the team averages {lt['avg_quality']} on quality and "
            f"{lt['avg_authenticity']} on authenticity — with {lt['fake']} commits "
            f"flagged as low-effort and {lt['ai']} showing signs of AI assistance."
        )
    else:
        headline = (
            f"{leader['name']} leads a {t['developers']}-contributor team across "
            f"{t['commits']} commits."
        )
        narrative = (
            f"{leader['name']} tops the cohort with a composite score of "
            f"{leader['score']}, ahead of "
            f"{second['name'] if second else 'the field'}. The top three "
            f"contributors account for {conc}% of all commits, with activity "
            f"peaking in {peak_month}."
        )
        findings += [caps["cadence"]]

    report["captions"] = caps
    report["story"] = {
        "headline": headline,
        "narrative": narrative,
        "findings": findings,
        "by_llm": False,
    }
