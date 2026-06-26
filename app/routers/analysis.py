"""Analysis runs: kick off local or LLM-judged analysis with live WS progress."""
from __future__ import annotations

import asyncio
import datetime as dt
from pathlib import Path

from fastapi import APIRouter, Depends, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.db import SessionLocal, get_db
from app.models import AnalysisRun, Repository
from app.services import analysis as analysis_svc
from app.services import charts, git_service, llm
from app.services import settings_store as store
from app.services.progress import broker
from app.templating import templates

router = APIRouter(tags=["analysis"])

# Keep strong refs to in-flight tasks so they aren't garbage-collected.
_tasks: set[asyncio.Task] = set()

CAP_MIN, CAP_MAX = 1, 5000


def _clamp_cap(cap: int | None) -> int | None:
    if cap is None:
        return None
    return max(CAP_MIN, min(CAP_MAX, cap))


def _norm_strategy(strategy: str | None) -> str:
    return strategy if strategy in llm.STRATEGIES else "uniform"


@router.post("/repos/{repo_id}/analyze")
async def run_analysis(
    repo_id: int,
    mode: str = "local",
    cap: int | None = None,
    provider: str | None = None,
    model: str | None = None,
    strategy: str | None = None,
    db: Session = Depends(get_db),
):
    repo = db.get(Repository, repo_id)
    if repo is None or repo.clone_status != "ready":
        return RedirectResponse(url=f"/repos/{repo_id}", status_code=303)
    mode = "llm" if mode == "llm" else "local"
    run = AnalysisRun(repository_id=repo.id, status="queued", mode=mode)
    db.add(run)
    db.commit()
    db.refresh(run)

    task = asyncio.create_task(
        _run_analysis(
            run.id, mode, _clamp_cap(cap), provider, model, _norm_strategy(strategy)
        )
    )
    _tasks.add(task)
    task.add_done_callback(_tasks.discard)

    return RedirectResponse(url=f"/runs/{run.id}", status_code=303)


def _resolve_llm(s: dict, provider: str | None, model: str | None) -> dict:
    """Pick provider/model/api_key from saved settings, honoring per-run overrides."""
    eff_provider = provider if provider in ("anthropic", "openai") else s["llm_provider"]
    if model:
        eff_model = model
    else:
        eff_model = s["anthropic_model"] if eff_provider == "anthropic" else s["openai_model"]
    api_key = s["anthropic_api_key"] if eff_provider == "anthropic" else s["openai_api_key"]
    return {"provider": eff_provider, "model": eff_model, "api_key": api_key}


@router.get("/repos/{repo_id}/estimate")
def estimate_cost(
    repo_id: int,
    cap: int | None = None,
    provider: str | None = None,
    model: str | None = None,
    strategy: str | None = None,
    db: Session = Depends(get_db),
):
    """Pre-run cost estimate (JSON).

    `cap` overrides the saved scan limit; `provider`/`model` override the saved
    LLM choice; `strategy` selects which commits are sampled (uniform | last).
    """
    repo = db.get(Repository, repo_id)
    if repo is None or repo.clone_status != "ready":
        return JSONResponse({"error": "Repository is not cloned yet."}, status_code=400)
    s = store.get_all(db)
    llm_cfg = _resolve_llm(s, provider, model)
    eff_cap = _clamp_cap(cap) or int(s.get("max_commits_per_run") or 300)
    commits = git_service.parse_log(Path(repo.local_path), repo.branch)
    est = llm.estimate_run(
        commits, Path(repo.local_path), llm_cfg["model"], eff_cap,
        strategy=_norm_strategy(strategy),
    )
    est.update({
        "provider": llm_cfg["provider"],
        "model": llm_cfg["model"],
        "has_key": bool(llm_cfg["api_key"]),
    })
    return JSONResponse(est)


@router.post("/runs/{run_id}/delete")
def delete_run(run_id: int, db: Session = Depends(get_db)):
    run = db.get(AnalysisRun, run_id)
    repo_id = run.repository_id if run else None
    if run is not None:
        broker.clear(run_id)
        db.delete(run)
        db.commit()
    return RedirectResponse(url=f"/repos/{repo_id}" if repo_id else "/", status_code=303)


@router.post("/repos/{repo_id}/runs/clear")
def clear_runs(repo_id: int, db: Session = Depends(get_db)):
    runs = db.query(AnalysisRun).filter_by(repository_id=repo_id).all()
    for r in runs:
        broker.clear(r.id)
        db.delete(r)
    db.commit()
    return RedirectResponse(url=f"/repos/{repo_id}", status_code=303)


@router.get("/runs/{run_id}", response_class=HTMLResponse)
def view_run(run_id: int, request: Request, db: Session = Depends(get_db)):
    run = db.get(AnalysisRun, run_id)
    if run is None:
        return RedirectResponse(url="/", status_code=303)
    repo = run.repository

    if run.status != "done":
        return templates.TemplateResponse(
            "running.html", {"request": request, "run": run, "repo": repo}
        )

    exhibits = _build_exhibits(run.result)
    return templates.TemplateResponse(
        "report.html",
        {
            "request": request,
            "run": run,
            "repo": repo,
            "report": run.result,
            "exhibits": exhibits,
        },
    )


@router.websocket("/ws/runs/{run_id}")
async def ws_run(websocket: WebSocket, run_id: int):
    """Stream progress events for a run: replay history, then tail live."""
    await websocket.accept()
    # Replay everything emitted so far (covers late connect / reconnect).
    for event in broker.history(run_id):
        await websocket.send_json(event)
    if broker.is_done(run_id):
        await websocket.close()
        return

    queue = broker.subscribe(run_id)
    try:
        while True:
            event = await queue.get()
            await websocket.send_json(event)
            if event.get("type") in ("done", "error"):
                break
    except WebSocketDisconnect:
        pass
    finally:
        broker.unsubscribe(run_id, queue)
        try:
            await websocket.close()
        except RuntimeError:
            pass


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #


async def _run_analysis(
    run_id: int,
    mode: str,
    cap_override: int | None = None,
    provider_override: str | None = None,
    model_override: str | None = None,
    strategy: str = "uniform",
) -> None:
    """Run the analysis on the event loop, emitting progress as it goes."""

    def emit(event: dict) -> None:
        broker.publish(run_id, {"ts": _now_iso(), **event})

    await asyncio.to_thread(_set_status, run_id, "running", "")
    emit({"type": "status", "phase": "start", "mode": mode,
          "message": "Starting analysis…"})

    try:
        ctx = await asyncio.to_thread(
            _load_ctx, run_id, provider_override, model_override
        )
        if cap_override:
            ctx["cap"] = cap_override
        ctx["strategy"] = strategy
        repo_path = Path(ctx["local_path"])
        branch = ctx["branch"]

        emit({"type": "status", "phase": "parsing",
              "message": "Reading the full commit history…"})
        commits = await asyncio.to_thread(git_service.parse_log, repo_path, branch)

        report = analysis_svc.analyze(commits)
        t = report["totals"]
        emit({
            "type": "meta",
            "developers": t["developers"],
            "commits": t["commits"],
            "churn": t["churn"],
            "message": f"{t['commits']} commits · {t['developers']} contributors.",
        })

        if mode == "llm":
            await _run_llm_phase(run_id, emit, report, commits, ctx, repo_path)
            message = f"LLM analysis complete · {report['llm_totals']['judged']} commits judged"
        else:
            message = f"{t['commits']} commits analyzed"

        report["finished_mode"] = mode
        await asyncio.to_thread(_save_result, run_id, report, message)
        emit({
            "type": "done",
            "redirect": f"/runs/{run_id}",
            "message": message,
        })
    except Exception as exc:  # surface any failure to the user
        msg = f"{type(exc).__name__}: {exc}"
        await asyncio.to_thread(_set_status, run_id, "error", msg)
        emit({"type": "error", "message": msg})


async def _run_llm_phase(run_id, emit, report, commits, ctx, repo_path) -> None:
    provider = ctx["provider"]
    model = ctx["model"]
    api_key = ctx["api_key"]
    cap = ctx["cap"]
    strategy = ctx.get("strategy", "uniform")

    if not api_key:
        raise RuntimeError(
            f"No {provider} API key configured — set one in Settings."
        )

    sample = llm.sample_commits(commits, cap, strategy)
    total = len(sample)
    skipped = report["totals"]["commits"] - total
    strat_label = "most recent" if strategy == "last" else "across contributors"
    emit({
        "type": "status",
        "phase": "judging",
        "provider": provider,
        "model": model,
        "total": total,
        "cap": cap,
        "strategy": strategy,
        "skipped": max(0, skipped),
        "message": (
            f"Judging {total} commit(s) with {provider}/{model}"
            + (f" ({strat_label}, sampled from {report['totals']['commits']}, cap {cap})"
               if skipped > 0 else "")
            + "…"
        ),
    })

    def on_progress(totals: llm.JudgeTotals, commit, judgment) -> None:
        emit({
            "type": "progress",
            "done": totals.judged,
            "total": total,
            "percent": round(totals.judged / total * 100, 1) if total else 100,
            "errors": totals.errors,
            "tokens": {"in": totals.input_tokens, "out": totals.output_tokens},
            "cost": round(totals.cost_usd, 4),
            "commit": {
                "hash": commit.hash[:8],
                "author": commit.author_name,
                "subject": commit.subject[:90],
            },
            "judgment": judgment,
        })

    totals = await llm.judge_commits(
        sample, repo_path, provider, api_key, model, on_progress
    )

    emit({
        "type": "status",
        "phase": "aggregating",
        "message": "Aggregating model judgments and re-ranking contributors…",
    })
    analysis_svc.apply_llm_scores(report, totals.by_hash, commits)

    emit({
        "type": "status",
        "phase": "writing",
        "message": "Writing the executive summary…",
    })
    story = await llm.synthesize_narrative(report, provider, api_key, model)
    if story:
        report["story"] = story

    report["llm_meta"] = {
        "provider": provider,
        "model": model,
        "judged": totals.judged,
        "errors": totals.errors,
        "input_tokens": totals.input_tokens,
        "output_tokens": totals.output_tokens,
        "cost_usd": round(totals.cost_usd, 4),
        "cap": cap,
        "strategy": strategy,
        "sampled": total < report["totals"]["commits"],
    }


# --------------------------------------------------------------------------- #
# Blocking helpers (run via asyncio.to_thread)
# --------------------------------------------------------------------------- #


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _set_status(run_id: int, status: str, message: str) -> None:
    db = SessionLocal()
    try:
        run = db.get(AnalysisRun, run_id)
        if run:
            run.status = status
            run.message = message
            if status in ("done", "error"):
                run.finished_at = dt.datetime.now(dt.timezone.utc)
            db.commit()
    finally:
        db.close()


def _load_ctx(
    run_id: int,
    provider_override: str | None = None,
    model_override: str | None = None,
) -> dict:
    db = SessionLocal()
    try:
        run = db.get(AnalysisRun, run_id)
        repo = run.repository
        s = store.get_all(db)
        llm_cfg = _resolve_llm(s, provider_override, model_override)
        return {
            "local_path": repo.local_path,
            "branch": repo.branch,
            "provider": llm_cfg["provider"],
            "model": llm_cfg["model"],
            "api_key": llm_cfg["api_key"],
            "cap": int(s.get("max_commits_per_run") or 300),
        }
    finally:
        db.close()


def _save_result(run_id: int, result: dict, message: str) -> None:
    db = SessionLocal()
    try:
        run = db.get(AnalysisRun, run_id)
        if run:
            run.result = result
            run.status = "done"
            run.message = message
            run.finished_at = dt.datetime.now(dt.timezone.utc)
            db.commit()
    finally:
        db.close()


def _build_exhibits(report: dict) -> dict:
    """Precompute the SVG exhibits the report template embeds."""
    devs = report["developers"]
    top = devs[:12]
    exhibits = {
        "ranking": charts.hbar(
            [{"label": d["name"], "value": d["score"]} for d in top]
        ),
        "commits": charts.hbar(
            [{"label": d["name"], "value": d["commits"]} for d in top]
        ),
        "churn": charts.hbar(
            [
                {
                    "label": d["name"],
                    "value": d["churn"],
                    "sub": f'+{d["insertions"]:,} / −{d["deletions"]:,}',
                }
                for d in top
            ]
        ),
        "breakdown": charts.grouped_score(
            [{"label": d["name"], "values": d["score_breakdown"]} for d in top[:8]]
        ),
        "timeline": charts.line(
            report["timeline"]["labels"], report["timeline"]["total"]
        ),
    }
    if report.get("mode") == "llm":
        judged = [d for d in top if d.get("llm", {}).get("judged")]
        exhibits["quality"] = charts.hbar(
            [
                {"label": d["name"], "value": d["llm"]["avg_quality"]}
                for d in judged
            ]
        )
        exhibits["authenticity"] = charts.hbar(
            [
                {"label": d["name"], "value": d["llm"]["avg_authenticity"]}
                for d in judged
            ]
        )
        exhibits["ai_usage"] = charts.hbar(
            [
                {"label": d["name"], "value": d["llm"]["avg_ai_likelihood"]}
                for d in judged
            ]
        )
    return exhibits
