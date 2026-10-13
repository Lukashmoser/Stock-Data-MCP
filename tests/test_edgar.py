import httpx
import pytest
import respx

from stock_data_mcp.errors import NotFound, SourceError
from stock_data_mcp.sources.edgar import FACTS_URL, SUBMISSIONS_URL, TICKERS_URL, normalize_ticker

from .conftest import load
from .factories import companyfacts

CIK = "0001234567"


@pytest.fixture
def sec():
    with respx.mock(assert_all_called=False) as mock:
        mock.get(TICKERS_URL).respond(json=load("company_tickers.json"))
        mock.get(SUBMISSIONS_URL.format(cik=CIK)).respond(json=load("submissions_tco.json"))
        mock.get(FACTS_URL.format(cik=CIK)).respond(json=companyfacts())
        yield mock


@pytest.mark.parametrize("raw,expected", [("brk.b", "BRK-B"), ("BRK/B", "BRK-B"), (" aapl ", "AAPL")])
def test_normalize_ticker(raw, expected):
    assert normalize_ticker(raw) == expected


async def test_resolve(sec, edgar):
    assert await edgar.resolve("tco") == (CIK, "TestCo Inc.")
    assert (await edgar.resolve("brk.b"))[0] == "0001067983"
    assert (await edgar.resolve("320193"))[0] == "0000320193"
    with pytest.raises(NotFound):
        await edgar.resolve("NOPE")


async def test_ticker_map_cached(sec, edgar):
    await edgar.resolve("TCO")
    await edgar.resolve("BRK-B")
    assert sec.routes[0].call_count == 1


async def test_user_agent_sent(sec, edgar):
    await edgar.resolve("TCO")
    assert sec.calls.last.request.headers["User-Agent"] == "Test test@example.com"


async def test_filings_filter_and_amendments(sec, edgar):
    out = await edgar.filings("TCO", "10-K")
    assert [f["form"] for f in out["filings"]] == ["10-K/A", "10-K"]
    assert out["company"] == "TestCo Inc."
    out = await edgar.filings("TCO", "10-k", include_amendments=False)
    assert [f["form"] for f in out["filings"]] == ["10-K"]
    f = out["filings"][0]
    assert f == {
        "form": "10-K",
        "filed": "2024-11-01",
        "period": "2024-09-28",
        "accession": "0001234567-24-000039",
        "url": "https://www.sec.gov/Archives/edgar/data/1234567/000123456724000039/tco-20240928.htm",
    }


async def test_filings_8k_items_and_limit(sec, edgar):
    out = await edgar.filings("TCO", "8-K")
    assert out["filings"][0]["items"] == "2.02,9.01"
    out = await edgar.filings("TCO", limit=2)
    assert out["count"] == 2 and out["filings"][0]["form"] == "10-Q"


async def test_company_facts_trimmed(sec, edgar):
    res = await edgar.company_facts(CIK)
    facts = res.value["facts"]
    assert "SomeUnmappedConcept" not in facts
    rev = facts["RevenueFromContractWithCustomerExcludingAssessedTax"]["USD"]
    assert all(r[5] in ("10-K", "10-Q") for r in rev)  # 8-K row dropped
    assert ["2023-10-01", "2024-09-28", 410_000_000, 2024, "FY", "10-K", "2024-11-01", "A24"] in rev


async def test_403_gives_user_agent_hint(edgar):
    with respx.mock() as mock:
        mock.get(TICKERS_URL).respond(403)
        with pytest.raises(SourceError) as exc:
            await edgar.resolve("TCO")
    assert "SEC_USER_AGENT" in exc.value.hint


async def test_retries_5xx_then_succeeds(edgar):
    with respx.mock() as mock:
        route = mock.get(TICKERS_URL)
        route.side_effect = [httpx.Response(503), httpx.Response(200, json=load("company_tickers.json"))]
        assert (await edgar.resolve("TCO"))[0] == CIK
        assert route.call_count == 2
