"""Prices and quotes via yfinance (unofficial; every call is guarded and cached)."""

from __future__ import annotations

import asyncio
import logging
import math
from datetime import UTC, datetime
from typing import Any, Protocol

from ..cache import HOUR, MINUTE, Cache
from ..errors import NotFound, SourceError

log = logging.getLogger(__name__)

SOURCE = "Yahoo Finance"
PERIODS = ("1d", "5d", "1mo", "3mo", "6mo", "ytd", "1y", "2y", "5y", "10y", "max")
INTERVALS = ("1d", "1wk", "1mo")
MAX_ROWS = 1500


class PriceSource(Protocol):
    """What the server needs from a price provider; lets another source slot in later."""

    async def quote(self, ticker: str) -> dict[str, Any]: ...
    async def history(self, ticker: str, period: str, interval: str) -> dict[str, Any]: ...


def yahoo_symbol(ticker: str) -> str:
    """Yahoo uses '-' for share classes: BRK.B -> BRK-B."""
    return ticker.strip().upper().replace(".", "-").replace("/", "-")


def auto_interval(period: str) -> str:
    if period in ("5y", "10y"):
        return "1wk"
    if period == "max":
        return "1mo"
    return "1d"


def _num(v: Any, digits: int = 2) -> float | None:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    if math.isnan(f) or math.isinf(f):
        return None
    return round(f, digits if abs(f) >= 1 else 6)


def _fetch_quote(symbol: str) -> dict[str, Any]:
    import yfinance as yf

    fi = yf.Ticker(symbol).fast_info

    def opt(key: str) -> Any:
        # Secondary fields (e.g. market cap for ETFs) can fail on their own; don't lose the quote.
        try:
            return fi[key]
        except Exception:
            return None

    raw_price = _num(fi["lastPrice"], 6)
    price = _num(raw_price)
    if price is None:
        raise NotFound(
            f"No quote for '{symbol}'", hint="Check the ticker (Yahoo format, e.g. BRK-B, SHOP.TO)."
        )
    prev = _num(opt("previousClose"), 6)
    change = raw_price - prev if prev else None
    return {
        "ticker": symbol,
        "price": price,
        "change": _num(change, 4),
        "change_pct": round(change / prev * 100, 2) if change is not None and prev else None,
        "prev_close": _num(prev),
        "open": _num(opt("open")),
        "day_high": _num(opt("dayHigh")),
        "day_low": _num(opt("dayLow")),
        "volume": int(v) if (v := _num(opt("lastVolume"))) is not None else None,
        "market_cap": int(m) if (m := _num(opt("marketCap"))) is not None else None,
        "high_52w": _num(opt("yearHigh")),
        "low_52w": _num(opt("yearLow")),
        "currency": opt("currency"),
        "exchange": opt("exchange"),
        "fetched_at": datetime.now(UTC).isoformat(timespec="seconds"),
    }


def _fetch_history(symbol: str, period: str, interval: str) -> dict[str, Any]:
    import yfinance as yf

    df = yf.Ticker(symbol).history(period=period, interval=interval, auto_adjust=False, actions=False)
    if df is None or df.empty:
        raise NotFound(f"No price history for '{symbol}'", hint="Check the ticker (Yahoo format).")
    rows = []
    for ts, r in df.iterrows():
        vol = _num(r.get("Volume"))
        rows.append([
            ts.strftime("%Y-%m-%d"),
            _num(r.get("Open")), _num(r.get("High")), _num(r.get("Low")),
            _num(r.get("Close")), _num(r.get("Adj Close")),
            int(vol) if vol is not None else None,
        ])  # fmt: skip
    return {"rows": rows}


async def _guarded(fn, *args) -> Any:
    try:
        return await asyncio.to_thread(fn, *args)
    except SourceError:
        raise
    except Exception as exc:  # yfinance raises a wide variety of errors
        log.warning("yfinance failed: %r", exc)
        msg = str(exc)
        if "Too Many Requests" in msg or "Rate limit" in msg:
            raise SourceError(
                f"{SOURCE} rate limited", hint="Wait a few minutes; cached data is used when available."
            ) from exc
        raise SourceError(f"{SOURCE} error: {type(exc).__name__}: {msg[:200]}") from exc


class Yahoo:
    def __init__(self, cache: Cache):
        self.cache = cache

    async def quote(self, ticker: str) -> dict[str, Any]:
        sym = yahoo_symbol(ticker)
        res = await self.cache.get_or_fetch(f"yahoo:quote:{sym}", MINUTE, lambda: _guarded(_fetch_quote, sym))
        return {**res.value, "stale": True} if res.stale else res.value

    async def history(self, ticker: str, period: str = "1y", interval: str = "auto") -> dict[str, Any]:
        sym = yahoo_symbol(ticker)
        period = period.lower()
        if period not in PERIODS:
            raise ValueError(f"period must be one of {list(PERIODS)}")
        interval = auto_interval(period) if interval in ("auto", "", None) else interval.lower()
        if interval not in INTERVALS:
            raise ValueError(f"interval must be 'auto' or one of {list(INTERVALS)}")
        ttl = 5 * MINUTE if period in ("1d", "5d") else 12 * HOUR
        res = await self.cache.get_or_fetch(
            f"yahoo:hist:{sym}:{period}:{interval}",
            ttl,
            lambda: _guarded(_fetch_history, sym, period, interval),
        )
        rows = res.value["rows"]
        out: dict[str, Any] = {"ticker": sym, "period": period, "interval": interval}
        if len(rows) > MAX_ROWS:
            rows = rows[-MAX_ROWS:]
            out["truncated"] = True
        out["columns"] = ["date", "open", "high", "low", "close", "adj_close", "volume"]
        out["count"] = len(rows)
        out["rows"] = rows
        if res.stale:
            out["stale"] = True
        return out
