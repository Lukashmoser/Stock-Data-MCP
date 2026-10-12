"""End-to-end through the MCP tool layer with mocked upstreams."""

import json

import pytest
import respx

from stock_data_mcp import server
from stock_data_mcp.cache import Cache
from stock_data_mcp.config import Settings
from stock_data_mcp.sources.edgar import FACTS_URL, SUBMISSIONS_URL, TICKERS_URL

from .conftest import load
from .factories import companyfacts


@pytest.fixture(autouse=True)
def svc(tmp_path, monkeypatch):
    settings = Settings(
        sec_user_agent="Test test@example.com", fred_api_key=None, cache_path=tmp_path / "c.db"
    )
    monkeypatch.setattr(server, "get_settings", lambda: settings)
    monkeypatch.setattr(server, "_services", None)
    yield
    if server._services:
        server._services.cache.close()


@pytest.fixture
def sec():
    with respx.mock(assert_all_called=False) as mock:
        mock.get(TICKERS_URL).respond(json=load("company_tickers.json"))
        mock.get(SUBMISSIONS_URL.format(cik="0001234567")).respond(json=load("submissions_tco.json"))
        mock.get(FACTS_URL.format(cik="0001234567")).respond(json=companyfacts())
        yield mock


async def call(name: str, **args) -> dict:
    result = await server.mcp.call_tool(name, args)
    blocks = result[0] if isinstance(result, tuple) else result
    blocks = getattr(blocks, "content", blocks)
    text = blocks[0].text
    assert "\n" not in text  # compact JSON
    return json.loads(text)


async def test_lists_five_tools():
    names = {t.name for t in await server.mcp.list_tools()}
    assert names == {"get_quote", "get_price_history", "get_financials", "get_filings", "get_macro_series"}


async def test_get_financials_tool(sec):
    out = await call("get_financials", ticker="TCO", statement="cashflow", years=1, period="quarterly")
    assert out["company"] == "TestCo Inc." and out["cik"] == "0001234567"
    assert out["periods"] == ["FY2024Q1", "FY2024Q2", "FY2024Q3", "FY2024Q4"]  # no FY2025 cash flow


async def test_get_filings_tool(sec):
    out = await call("get_filings", ticker="TCO", form_type="10-Q", limit=1)
    assert out["count"] == 1 and out["filings"][0]["period"] == "2025-03-29"


async def test_errors_are_json(sec):
    out = await call("get_filings", ticker="NOPE")
    assert "not found" in out["error"] and "hint" in out
    out = await call("get_macro_series", series_id="DGS10")
    assert "FRED_API_KEY" in out["error"]


async def test_unexpected_exception_is_contained(monkeypatch):
    async def boom(*a, **kw):
        raise RuntimeError("kaboom")

    monkeypatch.setattr(Cache, "get_or_fetch", boom)
    out = await call("get_quote", ticker="AAPL")
    assert out["error"].startswith("internal error: RuntimeError")
