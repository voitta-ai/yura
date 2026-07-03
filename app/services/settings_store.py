"""Read/write the key/value Setting table (API keys, provider, model, budget)."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.models import Setting

DEFAULTS: dict[str, str] = {
    "llm_provider": "anthropic",  # "anthropic" | "openai"
    "anthropic_api_key": "",
    "openai_api_key": "",
    "anthropic_model": "claude-opus-4-8",
    "openai_model": "gpt-4o",
    "max_commits_per_run": "300",  # cost guard for phase-2 LLM judging
    # Multi-judge panel (opt-in): each commit judged by N models for reliability.
    # Format: comma-separated "provider:model" (e.g. "openai:gpt-4o,anthropic:claude-haiku-4-5").
    "judge_panel": "off",  # "off" | "on"
    "panel_models": "",
}

# Keys treated as secrets (masked in the UI).
SECRET_KEYS = {"anthropic_api_key", "openai_api_key"}


def get_all(db: Session) -> dict[str, str]:
    rows = {s.key: s.value for s in db.query(Setting).all()}
    return {**DEFAULTS, **rows}


def get(db: Session, key: str) -> str:
    row = db.get(Setting, key)
    if row is not None:
        return row.value
    return DEFAULTS.get(key, "")


def set_many(db: Session, values: dict[str, str]) -> None:
    for key, value in values.items():
        row = db.get(Setting, key)
        if row is None:
            db.add(Setting(key=key, value=value))
        else:
            row.value = value
    db.commit()


def masked(key: str, value: str) -> str:
    """Return a display-safe value for secrets."""
    if key in SECRET_KEYS and value:
        return value[:3] + "…" + value[-4:] if len(value) > 8 else "••••"
    return value
