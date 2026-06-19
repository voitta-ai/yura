"""Settings page: LLM provider, API keys, models, cost guard."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.db import get_db
from app.services import models_service
from app.services import settings_store as store
from app.templating import templates

router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("", response_class=HTMLResponse)
def settings_page(request: Request, db: Session = Depends(get_db)):
    values = store.get_all(db)
    anthropic_models, a_src = models_service.list_models(
        "anthropic", values["anthropic_api_key"], current=values["anthropic_model"]
    )
    openai_models, o_src = models_service.list_models(
        "openai", values["openai_api_key"], current=values["openai_model"]
    )
    return templates.TemplateResponse(
        "settings.html",
        {
            "request": request,
            "values": values,
            "masked": {k: store.masked(k, v) for k, v in values.items()},
            "secret_keys": store.SECRET_KEYS,
            "anthropic_models": anthropic_models,
            "anthropic_source": a_src,
            "openai_models": openai_models,
            "openai_source": o_src,
        },
    )


@router.get("/models")
def fetch_models(provider: str, db: Session = Depends(get_db)):
    """Live model-list refresh for the 'Fetch latest' button (JSON)."""
    values = store.get_all(db)
    key = values.get(f"{provider}_api_key", "")
    current = values.get(f"{provider}_model", "")
    models, source = models_service.list_models(
        provider, key, force=True, current=current
    )
    return JSONResponse({"provider": provider, "models": models, "source": source})


@router.post("")
def save_settings(
    db: Session = Depends(get_db),
    llm_provider: str = Form("anthropic"),
    anthropic_api_key: str = Form(""),
    openai_api_key: str = Form(""),
    anthropic_model: str = Form("claude-opus-4-8"),
    openai_model: str = Form("gpt-4o"),
    max_commits_per_run: str = Form("300"),
):
    current = store.get_all(db)
    # Empty secret field => keep existing key (don't clobber with blank).
    payload = {
        "llm_provider": llm_provider,
        "anthropic_model": anthropic_model,
        "openai_model": openai_model,
        "max_commits_per_run": max_commits_per_run,
        "anthropic_api_key": anthropic_api_key or current["anthropic_api_key"],
        "openai_api_key": openai_api_key or current["openai_api_key"],
    }
    store.set_many(db, payload)
    return RedirectResponse(url="/settings?saved=1", status_code=303)
