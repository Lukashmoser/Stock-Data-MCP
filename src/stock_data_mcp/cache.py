"""SQLite key/value cache with per-entry TTL and stale fallback.

Values are JSON, zlib-compressed (EDGAR companyfacts can be tens of MB raw).
Expired entries are kept so they can be served when the upstream is down.
"""

from __future__ import annotations

import json
import logging
import sqlite3
import threading
import time
import zlib
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import NotFound, SourceError

log = logging.getLogger(__name__)

# TTLs in seconds, shared by the sources.
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR


@dataclass
class CacheResult:
    value: Any
    stale: bool = False


class Cache:
    def __init__(self, path: Path | str):
        self.path = Path(path)
        if str(path) != ":memory:":
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._conn = sqlite3.connect(str(path), check_same_thread=False)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS cache ("
            " key TEXT PRIMARY KEY, value BLOB NOT NULL,"
            " fetched_at REAL NOT NULL, ttl REAL NOT NULL)"
        )
        self._conn.commit()

    def get(self, key: str, *, allow_expired: bool = False) -> CacheResult | None:
        with self._lock:
            row = self._conn.execute(
                "SELECT value, fetched_at, ttl FROM cache WHERE key = ?", (key,)
            ).fetchone()
        if row is None:
            return None
        blob, fetched_at, ttl = row
        expired = time.time() - fetched_at > ttl
        if expired and not allow_expired:
            return None
        return CacheResult(json.loads(zlib.decompress(blob)), stale=expired)

    def set(self, key: str, value: Any, ttl: float) -> None:
        blob = zlib.compress(json.dumps(value, separators=(",", ":")).encode())
        with self._lock:
            self._conn.execute(
                "INSERT OR REPLACE INTO cache (key, value, fetched_at, ttl) VALUES (?, ?, ?, ?)",
                (key, blob, time.time(), ttl),
            )
            self._conn.commit()

    async def get_or_fetch(
        self,
        key: str,
        ttl: float,
        fetch: Callable[[], Awaitable[Any]],
        *,
        allow_stale: bool = True,
    ) -> CacheResult:
        """Return a fresh cached value, else fetch and store it.

        If the fetch fails with a SourceError (other than NotFound) and an
        expired entry exists, that entry is returned with ``stale=True``.
        """
        hit = self.get(key)
        if hit is not None:
            return hit
        try:
            value = await fetch()
        except NotFound:
            raise
        except SourceError as exc:
            old = self.get(key, allow_expired=True) if allow_stale else None
            if old is None:
                raise
            log.warning("serving stale cache for %s: %s", key, exc)
            return CacheResult(old.value, stale=True)
        self.set(key, value, ttl)
        return CacheResult(value)

    def prune(self, max_age_days: float = 30) -> int:
        """Delete entries that expired more than ``max_age_days`` ago."""
        cutoff = time.time() - max_age_days * DAY
        with self._lock:
            cur = self._conn.execute("DELETE FROM cache WHERE fetched_at + ttl < ?", (cutoff,))
            self._conn.commit()
        return cur.rowcount

    def close(self) -> None:
        self._conn.close()
