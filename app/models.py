"""Database models."""
from __future__ import annotations

import datetime as dt
from typing import Optional

from sqlalchemy import JSON, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


def _utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


class Setting(Base):
    """Simple key/value store for API keys, provider choice, model names, budget."""

    __tablename__ = "settings"

    key: Mapped[str] = mapped_column(String(64), primary_key=True)
    value: Mapped[str] = mapped_column(Text, default="")
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True), default=_utcnow, onupdate=_utcnow
    )


class Repository(Base):
    __tablename__ = "repositories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String(512), nullable=False)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    branch: Mapped[Optional[str]] = mapped_column(String(256), default=None)

    # lifecycle: added -> cloning -> ready / error
    clone_status: Mapped[str] = mapped_column(String(32), default="added")
    clone_message: Mapped[str] = mapped_column(Text, default="")
    local_path: Mapped[Optional[str]] = mapped_column(String(512), default=None)

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True), default=_utcnow
    )

    runs: Mapped[list["AnalysisRun"]] = relationship(
        back_populates="repository",
        cascade="all, delete-orphan",
        order_by="desc(AnalysisRun.created_at)",
    )


class AnalysisRun(Base):
    __tablename__ = "analysis_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    repository_id: Mapped[int] = mapped_column(
        ForeignKey("repositories.id", ondelete="CASCADE")
    )

    # queued -> running -> done / error
    status: Mapped[str] = mapped_column(String(32), default="queued")
    message: Mapped[str] = mapped_column(Text, default="")

    # "local" (git stats only) or "llm" (LLM-judged) — phase 2 uses "llm".
    mode: Mapped[str] = mapped_column(String(16), default="local")

    # Full computed report payload (dict): developers, totals, exhibits data.
    result: Mapped[Optional[dict]] = mapped_column(JSON, default=None)

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True), default=_utcnow
    )
    finished_at: Mapped[Optional[dt.datetime]] = mapped_column(
        DateTime(timezone=True), default=None
    )

    repository: Mapped["Repository"] = relationship(back_populates="runs")
