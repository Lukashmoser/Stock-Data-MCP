import httpx
import pytest
import respx

from stock_data_mcp.errors import NotFound, SourceError
from stock_data_mcp.sources.fred import BASE, Fred

from .conftest import load


@pytest.fixture
def api():
    with respx.mock(assert_all_called=False) as mock:
        mock.get(f"{BASE}/series").respond(json=load("fred_series_dgs10.json"))
        mock.get(f"{BASE}/series/observations").respond(json=load("fred_obs_dgs10.json"))
        yield mock


async def test_series(api, fred):
    out = await fred.series("dgs10", start="2025-01-01")
    assert out["series_id"] == "DGS10"
    assert out["units"] == "Percent" and out["frequency"] == "Daily"
    assert out["observations"][:2] == [["2025-01-01", None], ["2025-01-02", 4.57]]
    assert out["count"] == 5
    req = api.routes[1].calls.last.request
    assert req.url.params["observation_start"] == "2025-01-01"
    assert req.url.params["api_key"] == "test-key"
    assert "frequency" not in req.url.params


async def test_frequency_passthrough(api, fred):
    out = await fred.series("DGS10", frequency="m", aggregation="eop")
    params = api.routes[1].calls.last.request.url.params
    assert params["frequency"] == "m" and params["aggregation_method"] == "eop"
    assert out["frequency"] == "Daily -> m (eop)"


async def test_bad_frequency(fred):
    with pytest.raises(ValueError):
        await fred.series("DGS10", frequency="hourly")


async def test_unknown_series(fred):
    body = {"error_code": 400, "error_message": "Bad Request.  The series does not exist."}
    with respx.mock() as mock:
        mock.get(f"{BASE}/series").respond(400, json=body)
        with pytest.raises(NotFound):
            await fred.series("NOPE")


async def test_missing_key(http, cache):
    with pytest.raises(SourceError, match="FRED_API_KEY"):
        await Fred(http, cache, api_key=None).series("DGS10")


async def test_truncates_long_series(fred):
    obs = [{"date": f"2000-01-{i:05d}", "value": "1"} for i in range(3000)]
    with respx.mock() as mock:
        mock.get(f"{BASE}/series").respond(json=load("fred_series_dgs10.json"))
        mock.get(f"{BASE}/series/observations").mock(
            return_value=httpx.Response(200, json={"observations": obs})
        )
        out = await fred.series("DGS10")
    assert out["truncated"] and out["count"] == 2500
    assert out["observations"][-1][0] == "2000-01-02999"
