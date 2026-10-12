"""FRED (St. Louis Fed) macro series."""

from __future__ import annotations

import httpx

from ..cache import DAY, HOUR, Cache
from ..errors import NotFound, SourceError
from ..http import get_json

SOURCE = "FRED"
BASE = "https://api.stlouisfed.org/fred"
FREQUENCIES = {"d", "w", "bw", "m", "q", "sa", "a"}
AGGREGATIONS = {"avg", "sum", "eop"}
MAX_OBS = 2500


class Fred:
    def __init__(self, client: httpx.AsyncClient, cache: Cache, api_key: str | None):
        self.client = client
        self.cache = cache
        self.api_key = api_key

    async def _get(self, path: str, **params) -> dict:
        if not self.api_key:
            raise SourceError(
                "FRED_API_KEY is not set",
                hint="Get a free key at https://fred.stlouisfed.org/docs/api/api_key.html, add to .env.",
            )
        q = {"api_key": self.api_key, "file_type": "json", **{k: v for k, v in params.items() if v}}
        try:
            return await get_json(self.client, f"{BASE}/{path}", source=SOURCE, params=q)
        except SourceError as exc:
            if "does not exist" in str(exc):
                raise NotFound(
                    f"FRED series '{params.get('series_id')}' does not exist",
                    hint="Check the ID on fred.stlouisfed.org (e.g. DGS10, CPIAUCSL, UNRATE).",
                ) from exc
            raise

    async def series(
        self,
        series_id: str,
        start: str | None = None,
        end: str | None = None,
        frequency: str | None = None,
        aggregation: str = "avg",
    ) -> dict:
        sid = series_id.strip().upper()
        freq = frequency.lower() if frequency else None
        if freq and freq not in FREQUENCIES:
            raise ValueError(f"frequency must be one of {sorted(FREQUENCIES)}")
        if aggregation not in AGGREGATIONS:
            raise ValueError(f"aggregation must be one of {sorted(AGGREGATIONS)}")

        async def fetch_meta() -> dict:
            raw = await self._get("series", series_id=sid)
            s = (raw.get("seriess") or [{}])[0]
            return {
                "title": s.get("title"),
                "units": s.get("units"),
                "frequency": s.get("frequency"),
                "seasonal_adjustment": s.get("seasonal_adjustment_short"),
                "last_updated": s.get("last_updated"),
            }

        async def fetch_obs() -> list:
            raw = await self._get(
                "series/observations",
                series_id=sid,
                observation_start=start,
                observation_end=end,
                frequency=freq,
                aggregation_method=aggregation if freq else None,
            )
            return [
                [o["date"], None if o["value"] in (".", "") else float(o["value"])]
                for o in raw.get("observations", [])
            ]

        meta = await self.cache.get_or_fetch(f"fred:meta:{sid}", 7 * DAY, fetch_meta)
        key = f"fred:obs:{sid}:{start}:{end}:{freq}:{aggregation if freq else ''}"
        obs = await self.cache.get_or_fetch(key, 6 * HOUR, fetch_obs)

        rows = obs.value
        out = {"series_id": sid, **meta.value}
        if freq:
            out["frequency"] = f"{out.get('frequency')} -> {freq} ({aggregation})"
        if len(rows) > MAX_OBS:
            rows = rows[-MAX_OBS:]
            out["truncated"] = True
            out["hint"] = "Showing latest observations; pass frequency='m' or 'q', or a later start."
        out["count"] = len(rows)
        out["observations"] = rows
        if meta.stale or obs.stale:
            out["stale"] = True
        return out
