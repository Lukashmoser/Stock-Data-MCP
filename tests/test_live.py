"""Smoke tests against the real APIs. Run with: uv run pytest -m live

Needs SEC_USER_AGENT (and FRED_API_KEY for the FRED test) in .env.
"""

import pytest

from stock_data_mcp import server

pytestmark = pytest.mark.live


@pytest.fixture(autouse=True)
def fresh_services(monkeypatch):
    monkeypatch.setattr(server, "_services", None)


async def test_edgar_live():
    edgar = server.services().edgar
    cik, _ = await edgar.resolve("AAPL")
    assert cik == "0000320193"
    filings = await edgar.filings("AAPL", "10-K", limit=2)
    assert filings["count"] == 2


async def test_financials_live():
    out = await server.get_financials("AAPL", "income", 3, "quarterly")
    assert '"revenue"' in out and '"error"' not in out, out[:500]


async def test_yahoo_live():
    q = await server.services().yahoo.quote("AAPL")
    assert q["price"] > 0


async def test_fred_live():
    svc = server.services()
    if not svc.fred.api_key:
        pytest.skip("FRED_API_KEY not set")
    out = await svc.fred.series("DGS10", start="2024-01-01")
    assert out["count"] > 100
