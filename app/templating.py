"""Shared Jinja2 templates instance with a few helpers."""
from __future__ import annotations

import datetime as dt
from pathlib import Path

from fastapi.templating import Jinja2Templates

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


def _fmt_int(n) -> str:
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return str(n)


def _fmt_dt(value: str) -> str:
    try:
        return dt.datetime.fromisoformat(value).strftime("%d %b %Y, %H:%M")
    except (TypeError, ValueError):
        return value or "—"


templates.env.filters["intcomma"] = _fmt_int
templates.env.filters["humandt"] = _fmt_dt
templates.env.globals["now"] = lambda: dt.datetime.now(dt.timezone.utc)
