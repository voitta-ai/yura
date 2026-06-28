"""LLM-judged commit analysis.

Each sampled commit's diff + message is sent to the configured provider
(OpenAI or Anthropic) and scored on three axes:

  - quality       (0-100): code & commit-message craftsmanship
  - authenticity  (0-100): substantive real work vs. trivial/padding/fake noise
  - ai_likelihood (0-100): how AI-generated the change looks, from style cues

Calls run concurrently (bounded by a semaphore) so a few hundred commits finish
in a reasonable time. A progress callback fires after each commit so the caller
can stream rich real-time feedback. Token usage is tracked for a live cost
estimate.
"""
from __future__ import annotations

import asyncio
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Awaitable, Callable

from app.services import git_service
from app.services import static_analysis
from app.services.git_service import Commit

MAX_DIFF_CHARS = 6000
CONCURRENCY = 6
MAX_RETRIES = 2

# Rough public prices, USD per 1M tokens: (input, output). Used for a live
# cost estimate only — unknown models fall back to a generic default.
PRICES: dict[str, tuple[float, float]] = {
    "gpt-4o": (2.5, 10.0),
    "gpt-4o-mini": (0.15, 0.6),
    "gpt-4.1": (2.0, 8.0),
    "gpt-4.1-mini": (0.4, 1.6),
    "gpt-4.1-nano": (0.1, 0.4),
    "o3": (2.0, 8.0),
    "o4-mini": (1.1, 4.4),
    "claude-fable-5": (10.0, 50.0),
    "claude-opus-4-8": (5.0, 25.0),
    "claude-opus-4-7": (5.0, 25.0),
    "claude-opus-4-6": (5.0, 25.0),
    "claude-sonnet-4-6": (3.0, 15.0),
    "claude-haiku-4-5": (1.0, 5.0),
}
_DEFAULT_PRICE = (1.0, 5.0)

# RACE dimensions (Readability, mAintainability, Correctness, Efficiency) +
# authenticity + AI-likelihood. Anchored, gradeable criteria per axis — the
# fix for the vague-rubric unreliability documented in arXiv 2512.20159 (AXIOM).
# Static-analysis findings are supplied as EVIDENCE and the judge is told to
# ground its scores in them (arXiv 2508.14419).
_SYSTEM = (
    "You are a meticulous staff engineer auditing a git commit to assess a "
    "developer's work. You are given the commit message, change statistics, a "
    "(possibly truncated) unified diff, and — when available — objective static-"
    "analysis findings for the changed code. Ground your scores in that "
    "evidence; do not invent flaws the evidence does not support, and do not "
    "ignore flaws it does. Judge honestly and skeptically. Reply with ONLY a "
    "JSON object, no prose."
)

_SCHEMA_HINT = (
    "Score each axis 0-100 (higher is better) using these anchors:\n"
    "- readability: naming, structure, comments where useful, no dead code. "
    "(<40: cryptic/unstructured; >80: clear and idiomatic.)\n"
    "- maintainability: low complexity, small focused functions, no needless "
    "duplication or over-long signatures. Lower scores when static analysis "
    "reports high cyclomatic complexity or long functions.\n"
    "- correctness: the change looks logically sound and complete for its stated "
    "intent; no obvious bugs, error-handling gaps, or lint-flagged defects. "
    "(Down-weight when static analysis flags bug-prone patterns.)\n"
    "- efficiency: no obvious wasteful work, redundant passes, or pathological "
    "patterns; reasonable data structures. Use 70 as neutral when not assessable.\n"
    "- authenticity: 100 for substantive real engineering; low for trivial, "
    "padding, whitespace-only, auto-generated, or fake busy-work commits.\n"
    "- ai_likelihood: how likely the code was AI-generated, from style cues.\n"
    'Return JSON exactly like: {"readability": <int>, "maintainability": <int>, '
    '"correctness": <int>, "efficiency": <int>, "authenticity": <int>, '
    '"ai_likelihood": <int>, "rationale": "<one concise sentence citing the '
    'most important evidence>"}.'
)


def price_for(model: str) -> tuple[float, float]:
    if model in PRICES:
        return PRICES[model]
    # prefix match (e.g. "gpt-4o-2024-08-06")
    for key, val in PRICES.items():
        if model.startswith(key):
            return val
    return _DEFAULT_PRICE


def price_known(model: str) -> bool:
    """True if we have a real price for this model (not the generic fallback)."""
    return model in PRICES or any(model.startswith(k) for k in PRICES)


# Cost-estimate calibration. Input tokens are measured per-repo from a real
# prompt sample; output is small (the JSON verdict) so a constant + range
# covers the variance honestly. ~4 chars/token is a good English+code rule.
EST_CHARS_PER_TOKEN = 4
EST_OUTPUT_TOKENS = 150
EST_OUTPUT_LOW = 110
EST_OUTPUT_HIGH = 500


def estimate_run(
    commits: list[Commit],
    repo_path: Path,
    model: str,
    cap: int,
    sample_n: int = 10,
    strategy: str = "uniform",
) -> dict:
    """Estimate the cost of an LLM run without calling the API.

    Samples a few commits, builds their real prompts to size input tokens, and
    prices `judged` commits against the model's rate. Returns a best estimate
    plus a low–high range.
    """
    non_merge = [c for c in commits if not c.is_merge]
    judged = min(len(non_merge), cap)
    in_price, out_price = price_for(model)
    base = {
        "total_commits": len(non_merge),
        "judged": judged,
        "sampled": judged < len(non_merge),
        "cap": cap,
        "strategy": strategy if strategy in STRATEGIES else "uniform",
        "in_price": in_price,
        "out_price": out_price,
        "price_known": price_known(model),
    }
    if judged == 0:
        return {**base, "avg_input_tokens": 0, "est_input_tokens": 0,
                "est_output_tokens": 0, "cost": 0.0, "cost_low": 0.0,
                "cost_high": 0.0}

    sample = sample_commits(commits, min(sample_n, judged), strategy)
    total_chars = 0
    for c in sample:
        diff = git_service.get_commit_diff(repo_path, c.hash, MAX_DIFF_CHARS)
        total_chars += len(_SYSTEM) + len(_build_prompt(c, diff))
    avg_input_tok = (total_chars / len(sample)) / EST_CHARS_PER_TOKEN
    in_total = judged * avg_input_tok

    def cost(out_per: float) -> float:
        return in_total / 1e6 * in_price + judged * out_per / 1e6 * out_price

    return {
        **base,
        "avg_input_tokens": round(avg_input_tok),
        "est_input_tokens": round(in_total),
        "est_output_tokens": judged * EST_OUTPUT_TOKENS,
        "cost": round(cost(EST_OUTPUT_TOKENS), 4),
        "cost_low": round(cost(EST_OUTPUT_LOW), 4),
        "cost_high": round(cost(EST_OUTPUT_HIGH), 4),
    }


@dataclass
class JudgeTotals:
    judged: int = 0
    errors: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    by_hash: dict[str, dict] = field(default_factory=dict)


STRATEGIES = ("uniform", "last")


def sample_commits(
    commits: list[Commit], cap: int, strategy: str = "uniform"
) -> list[Commit]:
    """Pick up to `cap` non-merge commits according to `strategy`.

    - "uniform": round-robins newest-first across authors so every contributor
      gets coverage rather than the cap being eaten by the most prolific dev.
    - "last": simply the `cap` most-recent commits, regardless of author.
    """
    non_merge = [c for c in commits if not c.is_merge]
    if len(non_merge) <= cap:
        return non_merge

    if strategy == "last":
        return sorted(non_merge, key=lambda c: c.committer_ts, reverse=True)[:cap]

    # "uniform" (default): stratified round-robin across authors.
    by_author: dict[str, list[Commit]] = defaultdict(list)
    for c in non_merge:
        by_author[c.author_email].append(c)
    for cs in by_author.values():
        cs.sort(key=lambda c: c.committer_ts, reverse=True)

    # Authors ordered by their most-recent commit (most recently active first).
    authors = sorted(
        by_author, key=lambda e: by_author[e][0].committer_ts, reverse=True
    )
    picked: list[Commit] = []
    idx = 0
    while len(picked) < cap and any(idx < len(by_author[a]) for a in authors):
        for a in authors:
            if idx < len(by_author[a]):
                picked.append(by_author[a][idx])
                if len(picked) >= cap:
                    break
        idx += 1
    return picked


def _build_prompt(commit: Commit, diff: str, evidence: str = "") -> str:
    body = (commit.body or "").strip()
    body_part = f"\n{body[:500]}" if body else ""
    evidence_part = (
        f"\nStatic-analysis evidence (objective, from the changed code):\n{evidence}\n"
        if evidence
        else ""
    )
    return (
        f"Commit {commit.hash[:10]} by {commit.author_name}\n"
        f"Message: {commit.subject}{body_part}\n"
        f"Stats: +{commit.insertions} -{commit.deletions} across "
        f"{commit.files_changed} file(s)\n"
        f"{evidence_part}\n"
        f"Diff:\n{diff or '(no textual diff)'}\n\n"
        f"{_SCHEMA_HINT}"
    )


# RACE blend → a single 0-100 "quality" for the composite score. Maintainability
# and correctness weighted most; efficiency least (often not assessable).
QUALITY_WEIGHTS = {
    "readability": 0.25,
    "maintainability": 0.30,
    "correctness": 0.30,
    "efficiency": 0.15,
}
RACE_AXES = ("readability", "maintainability", "correctness", "efficiency")


def _normalize(data: dict) -> dict:
    def clamp(v, default=50) -> int:
        try:
            return max(0, min(100, int(round(float(v)))))
        except (TypeError, ValueError):
            return default

    out = {
        "readability": clamp(data.get("readability")),
        "maintainability": clamp(data.get("maintainability")),
        "correctness": clamp(data.get("correctness")),
        "efficiency": clamp(data.get("efficiency"), default=70),
        "authenticity": clamp(data.get("authenticity")),
        "ai_likelihood": clamp(data.get("ai_likelihood")),
        "rationale": str(data.get("rationale", ""))[:240],
    }
    # Blended quality for backward-compatible composite scoring.
    out["quality"] = round(
        sum(QUALITY_WEIGHTS[a] * out[a] for a in RACE_AXES)
    )
    return out


def _is_param_error(exc: Exception) -> bool:
    """True if the error looks like an unsupported-parameter rejection (400)."""
    msg = str(exc).lower()
    return any(
        k in msg
        for k in (
            "unsupported",
            "max_tokens",
            "max_completion_tokens",
            "temperature",
            "response_format",
            "not supported",
            "unknown parameter",
        )
    )


_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_json(text: str) -> dict:
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        m = _JSON_RE.search(text or "")
        if m:
            return json.loads(m.group(0))
        raise


# --- provider adapters: each returns (judgment_dict, (in_tokens, out_tokens)) ---


def _make_judge(provider: str, api_key: str, model: str):
    if provider == "openai":
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=api_key)
        # Param support differs across families: classic chat models take
        # `max_tokens` + `temperature`; reasoning models (o-series, gpt-5*)
        # require `max_completion_tokens` and reject custom temperature.
        # Try richest first, then lock in whichever variant the model accepts.
        variants = [
            {"temperature": 0, "max_tokens": 400,
             "response_format": {"type": "json_object"}},
            {"max_completion_tokens": 2000,
             "response_format": {"type": "json_object"}},
            {"max_completion_tokens": 2000},
            {},
        ]
        locked: dict = {"params": None}

        async def _call(extra: dict, commit: Commit, diff: str, evidence: str):
            resp = await client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": _SYSTEM},
                    {"role": "user", "content": _build_prompt(commit, diff, evidence)},
                ],
                **extra,
            )
            data = _parse_json(resp.choices[0].message.content)
            u = resp.usage
            return _normalize(data), (u.prompt_tokens, u.completion_tokens)

        async def judge(commit: Commit, diff: str, evidence: str = ""):
            if locked["params"] is not None:
                return await _call(locked["params"], commit, diff, evidence)
            last: Exception | None = None
            for extra in variants:
                try:
                    result = await _call(extra, commit, diff, evidence)
                    locked["params"] = extra  # this variant works; reuse it
                    return result
                except Exception as exc:  # param-rejection → try the next variant
                    last = exc
                    if not _is_param_error(exc):
                        raise
            raise last  # type: ignore[misc]

        return judge

    # default: anthropic
    from anthropic import AsyncAnthropic

    client = AsyncAnthropic(api_key=api_key)

    async def judge(commit: Commit, diff: str, evidence: str = ""):
        resp = await client.messages.create(
            model=model,
            max_tokens=600,
            system=_SYSTEM,
            messages=[
                {
                    "role": "user",
                    "content": _build_prompt(commit, diff, evidence)
                    + "\n\nReturn only the JSON object.",
                }
            ],
        )
        text = "".join(b.text for b in resp.content if b.type == "text")
        data = _parse_json(text)
        return _normalize(data), (resp.usage.input_tokens, resp.usage.output_tokens)

    return judge


async def complete_json(
    provider: str, api_key: str, model: str, system: str, user: str, max_out: int = 900
) -> dict:
    """One-shot JSON completion, provider-adaptive (same param fallback as judge)."""
    if provider == "openai":
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=api_key)
        variants = [
            {"temperature": 0, "max_tokens": max_out,
             "response_format": {"type": "json_object"}},
            {"max_completion_tokens": max(max_out, 1500),
             "response_format": {"type": "json_object"}},
            {"max_completion_tokens": max(max_out, 1500)},
            {},
        ]
        last: Exception | None = None
        for extra in variants:
            try:
                resp = await client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    **extra,
                )
                return _parse_json(resp.choices[0].message.content)
            except Exception as exc:
                last = exc
                if not _is_param_error(exc):
                    raise
        raise last  # type: ignore[misc]

    from anthropic import AsyncAnthropic

    client = AsyncAnthropic(api_key=api_key)
    resp = await client.messages.create(
        model=model,
        max_tokens=max(max_out, 1024),
        system=system,
        messages=[{"role": "user", "content": user + "\n\nReturn only the JSON object."}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text")
    return _parse_json(text)


_SYNTH_SYSTEM = (
    "You are a principal engineering advisor writing the executive summary of a "
    "developer-performance review for engineering leadership. Be specific — use "
    "names and numbers. Be candid but fair. No filler, no hedging, no praise that "
    "the data doesn't support."
)


async def synthesize_narrative(
    report: dict, provider: str, api_key: str, model: str
) -> dict | None:
    """Have the model write the executive story from the aggregated results.

    Returns {headline, narrative, findings, by_llm} or None on failure (caller
    keeps the deterministic story).
    """
    devs = report["developers"][:8]
    lines = []
    for d in devs:
        line = (
            f"{d['rank']}. {d['name']} — score {d['score']} "
            f"(commits {d['commits']}, churn {d['churn']}"
        )
        llm = d.get("llm", {})
        if llm.get("judged"):
            line += (
                f", quality {llm['avg_quality']}, authenticity "
                f"{llm['avg_authenticity']}, ai-likelihood {llm['avg_ai_likelihood']}"
            )
        lines.append(line + ")")

    t = report["totals"]
    lt = report.get("llm_totals", {})
    flagged = "; ".join(
        f"\"{c['subject']}\" (authenticity {c['authenticity']})"
        for c in report.get("flagged_commits", [])[:5]
    )
    context = (
        f"Repository scope: {t['developers']} contributors, {t['commits']} commits, "
        f"{t['first_date']} to {t['last_date']}.\n\n"
        f"Top contributors (ranked by blended score):\n" + "\n".join(lines) + "\n"
    )
    if lt:
        context += (
            f"\nModel-judged totals: {lt.get('judged', 0)} commits reviewed; "
            f"mean quality {lt.get('avg_quality')}, mean authenticity "
            f"{lt.get('avg_authenticity')}, mean AI-likelihood "
            f"{lt.get('avg_ai_likelihood')}; {lt.get('fake', 0)} flagged low-effort, "
            f"{lt.get('ai', 0)} showing AI assistance.\n"
        )
    if flagged:
        context += f"\nLowest-authenticity commits: {flagged}.\n"

    user = (
        context
        + "\nWrite the executive summary as JSON: {\"headline\": a single punchy "
        "sentence (max 18 words), \"narrative\": a 2–4 sentence paragraph telling "
        "the story of this team's performance — who's carrying it, the quality and "
        "authenticity picture, and anything leadership should watch, "
        "\"findings\": an array of 3–5 specific, number-backed bullet strings}."
    )
    try:
        data = await complete_json(
            provider, api_key, model, _SYNTH_SYSTEM, user, max_out=900
        )
    except Exception:
        return None
    headline = str(data.get("headline", "")).strip()
    narrative = str(data.get("narrative", "")).strip()
    findings = [str(x).strip() for x in (data.get("findings") or []) if str(x).strip()]
    if not headline or not narrative:
        return None
    return {
        "headline": headline[:200],
        "narrative": narrative[:1400],
        "findings": findings[:6],
        "by_llm": True,
    }


ProgressCB = Callable[[JudgeTotals, Commit, dict | None], None]


async def judge_commits(
    commits: list[Commit],
    repo_path: Path,
    provider: str,
    api_key: str,
    model: str,
    on_progress: ProgressCB,
    concurrency: int = CONCURRENCY,
) -> JudgeTotals:
    """Judge every commit in `commits` concurrently; fire on_progress per result."""
    judge = _make_judge(provider, api_key, model)
    in_price, out_price = price_for(model)
    sem = asyncio.Semaphore(concurrency)
    totals = JudgeTotals()

    async def worker(commit: Commit) -> None:
        async with sem:
            # Diff + static analysis run together off the event loop.
            diff = await asyncio.to_thread(
                git_service.get_commit_diff, repo_path, commit.hash, MAX_DIFF_CHARS
            )
            analysis = await asyncio.to_thread(
                static_analysis.analyze_commit, repo_path, commit
            )
            evidence = analysis.to_evidence()

            judgment: dict | None = None
            last_err: Exception | None = None
            for attempt in range(MAX_RETRIES + 1):
                try:
                    judgment, (itk, otk) = await judge(commit, diff, evidence)
                    totals.input_tokens += itk
                    totals.output_tokens += otk
                    totals.cost_usd = (
                        totals.input_tokens / 1e6 * in_price
                        + totals.output_tokens / 1e6 * out_price
                    )
                    break
                except Exception as exc:  # transient API / parse error
                    last_err = exc
                    if attempt < MAX_RETRIES:
                        await asyncio.sleep(1.5 * (attempt + 1))

            if judgment is None:
                totals.errors += 1
                judgment = {
                    "readability": 50, "maintainability": 50, "correctness": 50,
                    "efficiency": 50, "quality": 50, "authenticity": 50,
                    "ai_likelihood": 50,
                    "rationale": f"judge failed: {type(last_err).__name__}",
                    "error": True,
                }
            # Attach objective static-analysis summary alongside the judgment.
            judgment["static"] = analysis.to_dict()
            totals.judged += 1
            totals.by_hash[commit.hash] = judgment
            on_progress(totals, commit, judgment)

    await asyncio.gather(*(worker(c) for c in commits))
    return totals
