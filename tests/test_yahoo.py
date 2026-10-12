import pandas as pd
import pytest

from stock_data_mcp.errors import NotFound, SourceError
from stock_data_mcp.sources import yahoo
from stock_data_mcp.sources.yahoo import Yahoo, auto_interval, yahoo_symbol

FAST_INFO = {
    "lastPrice": 227.523,
    "previousClose": 225.0,
    "open": 226.0,
    "dayHigh": 228.1,
    "dayLow": 225.5,
    "lastVolume": 41_000_000.0,
    "marketCap": 3.45e12,
    "yearHigh": 237.49,
    "yearLow": 164.08,
    "currency": "USD",
    "exchange": "NMS",
}


class FakeFastInfo(dict):
    def __getitem__(self, k):
        if k == "marketCap" and self.get("broken_cap"):
            raise KeyError("marketCap")
        return super().__getitem__(k)


class FakeTicker:
    fail: Exception | None = None
    info: dict = FAST_INFO
    frame: pd.DataFrame | None = None

    def __init__(self, symbol):
        if FakeTicker.fail:
            raise FakeTicker.fail
        self.symbol = symbol
        self.fast_info = FakeFastInfo(FakeTicker.info)

    def history(self, **kw):
        FakeTicker.last_kwargs = kw
        return FakeTicker.frame


@pytest.fixture(autouse=True)
def fake_yf(monkeypatch):
    import yfinance

    monkeypatch.setattr(yfinance, "Ticker", FakeTicker)
    FakeTicker.fail = None
    FakeTicker.info = FAST_INFO
    idx = pd.DatetimeIndex(["2025-01-02", "2025-01-03"], tz="America/New_York")
    FakeTicker.frame = pd.DataFrame(
        {
            "Open": [100.0, 101.0],
            "High": [102.0, 103.5],
            "Low": [99.0, 100.25],
            "Close": [101.5, 103.0],
            "Adj Close": [101.123456, 102.6],
            "Volume": [1_000_000, 1_200_000],
        },
        index=idx,
    )


def test_symbol_and_interval():
    assert yahoo_symbol("brk.b") == "BRK-B"
    assert auto_interval("1y") == "1d" and auto_interval("5y") == "1wk" and auto_interval("max") == "1mo"


async def test_quote(cache):
    q = await Yahoo(cache).quote("aapl")
    assert q["ticker"] == "AAPL" and q["price"] == 227.52
    assert q["change"] == 2.523 and q["change_pct"] == 1.12
    assert q["market_cap"] == 3_450_000_000_000 and q["volume"] == 41_000_000
    assert "stale" not in q


async def test_quote_survives_broken_secondary_field(cache):
    FakeTicker.info = {**FAST_INFO, "broken_cap": True}
    q = await Yahoo(cache).quote("AAPL")
    assert q["market_cap"] is None and q["price"] == 227.52


async def test_quote_not_found(cache):
    FakeTicker.info = {**FAST_INFO, "lastPrice": None}
    with pytest.raises(NotFound):
        await Yahoo(cache).quote("ZZZZ")


async def test_quote_failure_serves_stale(cache):
    src = Yahoo(cache)
    await src.quote("AAPL")
    cache._conn.execute("UPDATE cache SET ttl = -1")  # expire everything
    FakeTicker.fail = RuntimeError("Too Many Requests. Rate limited. Try after a while.")
    q = await src.quote("AAPL")
    assert q["stale"] is True and q["price"] == 227.52


async def test_quote_failure_without_cache(cache):
    FakeTicker.fail = RuntimeError("Too Many Requests")
    with pytest.raises(SourceError, match="rate limited"):
        await Yahoo(cache).quote("AAPL")


async def test_history(cache):
    out = await Yahoo(cache).history("AAPL", "5y")
    assert out["interval"] == "1wk"
    assert FakeTicker.last_kwargs["interval"] == "1wk" and FakeTicker.last_kwargs["auto_adjust"] is False
    assert out["columns"][5] == "adj_close"
    assert out["rows"][0] == ["2025-01-02", 100.0, 102.0, 99.0, 101.5, 101.12, 1_000_000]


async def test_history_validation_and_empty(cache):
    src = Yahoo(cache)
    with pytest.raises(ValueError):
        await src.history("AAPL", "7y")
    with pytest.raises(ValueError):
        await src.history("AAPL", "1y", "1h")
    FakeTicker.frame = pd.DataFrame()
    with pytest.raises(NotFound):
        await src.history("ZZZZ", "1y")


async def test_history_row_cap(cache, monkeypatch):
    monkeypatch.setattr(yahoo, "MAX_ROWS", 1)
    out = await Yahoo(cache).history("AAPL", "1mo")
    assert out["truncated"] and out["count"] == 1 and out["rows"][0][0] == "2025-01-03"
