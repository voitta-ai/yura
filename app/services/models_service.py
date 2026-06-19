"""Discover available LLM model IDs from each provider's live /v1/models API.

Strategy: if an API key is configured, query the provider's models endpoint
(Anthropic and OpenAI both expose `GET /v1/models`). Cache the result in-process
for a while. Fall back to a curated static list when there's no key or the call
fails, so the dropdowns are always populated. The currently-saved model is
always included even if the API doesn't list it.
"""
from __future__ import annotations

import time

import httpx

# Curated fallbacks — current as of mid-2026. Used when no key / API unreachable.
# Order = preferred-first; the UI selects the saved value regardless.
FALLBACK_ANTHROPIC = [
    "claude-opus-4-8",
    "claude-opus-4-7",
    "claude-opus-4-6",
    "claude-sonnet-4-6",
    "claude-haiku-4-5",
    "claude-fable-5",
]
FALLBACK_OPENAI = [
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4.1",
    "gpt-4.1-mini",
    "o3",
    "o4-mini",
]

_CACHE_TTL = 60 * 60  # 1 hour
# provider -> (timestamp, [model_ids])
_cache: dict[str, tuple[float, list[str]]] = {}


def _anthropic_priority(model_id: str) -> tuple:
    """Sort by family (opus/fable first), then version descending within family."""
    family = {"opus": 0, "fable": 0, "sonnet": 1, "haiku": 2}
    fam_rank = next((r for k, r in family.items() if k in model_id), 9)
    # Negate per-char so higher version strings (opus-4-8 > opus-4-7) sort first.
    return (fam_rank, tuple(-ord(c) for c in model_id))


def _fetch_anthropic(api_key: str) -> list[str]:
    resp = httpx.get(
        "https://api.anthropic.com/v1/models",
        headers={"x-api-key": api_key, "anthropic-version": "2023-06-01"},
        params={"limit": 100},
        timeout=8.0,
    )
    resp.raise_for_status()
    ids = [m["id"] for m in resp.json().get("data", [])]
    ids.sort(key=_anthropic_priority)
    return ids


def _fetch_openai(api_key: str) -> list[str]:
    resp = httpx.get(
        "https://api.openai.com/v1/models",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=8.0,
    )
    resp.raise_for_status()
    ids = [m["id"] for m in resp.json().get("data", [])]
    # Keep chat-capable families; drop embeddings/audio/image/moderation/etc.
    keep = [
        m
        for m in ids
        if (m.startswith("gpt-") or m.startswith("o1") or m.startswith("o3") or m.startswith("o4"))
        and not any(x in m for x in ("audio", "realtime", "transcribe", "tts", "image", "search", "embedding"))
    ]
    keep.sort(reverse=True)
    return keep or ids


_FETCHERS = {"anthropic": _fetch_anthropic, "openai": _fetch_openai}
_FALLBACKS = {"anthropic": FALLBACK_ANTHROPIC, "openai": FALLBACK_OPENAI}


def list_models(
    provider: str, api_key: str, *, force: bool = False, current: str = ""
) -> tuple[list[str], str]:
    """Return (model_ids, source) where source is 'live' | 'fallback' | 'cache'.

    The current saved value is always present in the returned list.
    """
    provider = provider if provider in _FETCHERS else "anthropic"
    fallback = _FALLBACKS[provider]

    def _finalize(ids: list[str], source: str) -> tuple[list[str], str]:
        if current and current not in ids:
            ids = [current, *ids]
        return ids, source

    if not api_key:
        return _finalize(list(fallback), "fallback")

    if not force:
        cached = _cache.get(provider)
        if cached and (time.monotonic() - cached[0]) < _CACHE_TTL:
            return _finalize(list(cached[1]), "cache")

    try:
        ids = _FETCHERS[provider](api_key)
        if ids:
            _cache[provider] = (time.monotonic(), ids)
            return _finalize(ids, "live")
    except (httpx.HTTPError, KeyError, ValueError):
        pass

    return _finalize(list(fallback), "fallback")
