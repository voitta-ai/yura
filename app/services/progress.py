"""In-process pub/sub for analysis-run progress events.

Single-process (uvicorn) local tool: an in-memory broker is sufficient. Each run
keeps a full event history so a WebSocket that connects late (or reconnects)
replays everything and never misses an event. All access happens on the asyncio
event loop, so the asyncio.Queue fan-out is safe without locks.
"""
from __future__ import annotations

import asyncio
from collections import defaultdict


class ProgressBroker:
    def __init__(self) -> None:
        self._subs: dict[int, set[asyncio.Queue]] = defaultdict(set)
        self._history: dict[int, list[dict]] = defaultdict(list)
        self._done: set[int] = set()

    def publish(self, run_id: int, event: dict) -> None:
        """Record an event and fan it out to live subscribers. Sync + cheap."""
        self._history[run_id].append(event)
        if event.get("type") in ("done", "error"):
            self._done.add(run_id)
        for q in list(self._subs[run_id]):
            q.put_nowait(event)

    def history(self, run_id: int) -> list[dict]:
        return list(self._history[run_id])

    def is_done(self, run_id: int) -> bool:
        return run_id in self._done

    def subscribe(self, run_id: int) -> asyncio.Queue:
        q: asyncio.Queue = asyncio.Queue()
        self._subs[run_id].add(q)
        return q

    def unsubscribe(self, run_id: int, q: asyncio.Queue) -> None:
        self._subs[run_id].discard(q)

    def clear(self, run_id: int) -> None:
        self._history.pop(run_id, None)
        self._done.discard(run_id)
        self._subs.pop(run_id, None)


broker = ProgressBroker()
