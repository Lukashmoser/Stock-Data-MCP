"""Guards for the security invariants: input limits, outbound allowlist, secret hygiene."""

import json
import logging
import time

import pytest
import respx

from stock_data_mcp import http as http_mod
from stock_data_mcp import server, validate
from stock_data_mcp.cache import Cache
from stock_data_mcp.config import Settings
from stock_data_mcp.errors import SourceError
from stock_data_mcp.http import BlockedRequest, get_json, make_client
from stock_data_mcp.sources.fred import BASE, Fred

SECRET = "SEKRET0123456789"
EXFIL = "my bank password is hunter2 and my SSN is 123-45-6789 ok?!"
BAD_TICKERS = ["../../etc/passwd", "AAPL\nignore", "https://evil.example", "A" * 16, "", " ", "C:\\x", EXFIL]
BAD_SERIES = ["../x", "DGS10?api_key=x", "S" * 31, "a b", EXFIL]


# ---- input validation -------------------------------------------------------


@pytest.mark.parametrize("value", BAD_TICKERS)
def test_ticker_rejected(value):
    with pytest.raises(ValueError):
        validate.ticker(value)


@pytest.mark.parametrize("value", ["AAPL", "brk.b", "BRK-B", "^GSPC", "EURUSD=X", "SHOP.TO", "320193"])
def test_ticker_accepted(value):
    assert validate.ticker(value) == value


def test_cik_length_capped():
    with pytest.raises(ValueError):
        validate.ticker("12345678901")


@pytest.mark.parametrize("value", BAD_SERIES)
def test_series_rejected(value):
    with pytest.raises(ValueError):
        validate.series_id(value)


@pytest.mark.parametrize("value", ["10-K", "10-K/A", "DEF 14A", "4", "SC 13G"])
def test_form_accepted(value):
    assert validate.form_type(value) == value


@pytest.mark.parametrize("value", ["10-K; rm -rf", "x" * 13, "../10-K"])
def test_form_rejected(value):
    with pytest.raises(ValueError):
        validate.form_type(value)


def test_dates():
    assert validate.iso_date("2024-01-31", "start") == "2024-01-31"
    for bad in ("2024-13-01", "yesterday", "2024-01-01T00:00", "../../"):
        with pytest.raises(ValueError):
            validate.iso_date(bad, "start")


@pytest.fixture
def no_network(monkeypatch):
    """Fail the test if any tool reaches the network (httpx or yfinance)."""
    import yfinance

    def no_yf(*a, **kw):
        raise AssertionError("yfinance called")

    monkeypatch.setattr(yfinance, "Ticker", no_yf)
    settings = Settings(sec_user_agent="Test test@example.com", fred_api_key=SECRET)
    monkeypatch.setattr(server, "get_settings", lambda: settings)
    monkeypatch.setattr(server, "_services", None)
    with respx.mock(assert_all_called=False) as mock:
        yield mock
        assert not mock.calls, "network was used"
    if server._services:
        server._services.cache.close()


@pytest.mark.parametrize(
    "tool,args",
    [
        *[(server.get_quote, {"ticker": t}) for t in BAD_TICKERS],
        *[(server.get_price_history, {"ticker": t}) for t in BAD_TICKERS[:3]],
        *[(server.get_financials, {"ticker": t}) for t in BAD_TICKERS[:3]],
        (server.get_filings, {"ticker": "AAPL", "form_type": EXFIL}),
        *[(server.get_macro_series, {"series_id": s}) for s in BAD_SERIES],
        (server.get_macro_series, {"series_id": "DGS10", "start": EXFIL}),
    ],
)
async def test_tools_reject_before_any_io(no_network, tool, args):
    out = json.loads(await tool(**args))
    assert out["error"].startswith("invalid argument")


async def test_schema_advertises_limits():
    tools = {t.name: t.input_schema["properties"] for t in await server.mcp.list_tools()}
    assert tools["get_quote"]["ticker"]["pattern"] == validate.TICKER_PATTERN
    assert tools["get_macro_series"]["series_id"]["maxLength"] == 30
    assert "pattern" in json.dumps(tools["get_filings"]["form_type"])
    assert "pattern" in json.dumps(tools["get_macro_series"]["start"])


# ---- outbound requests ------------------------------------------------------


@pytest.mark.parametrize(
    "url",
    ["http://127.0.0.1:8080/admin", "https://evil.example/x", "http://data.sec.gov/x", "file:///etc/passwd"],
)
async def test_allowlist_blocks(url):
    async with make_client("Test test@example.com") as client:
        with respx.mock(assert_all_called=False) as mock:
            route = mock.route().respond(json={})
            with pytest.raises((BlockedRequest, Exception)) as exc:
                await get_json(client, url, source="test")
            assert not route.called
    assert isinstance(exc.value, BlockedRequest) or "Unsupported URL protocol" in str(exc.value)


async def test_allowlist_permits_known_hosts():
    async with make_client("Test test@example.com") as client:
        with respx.mock() as mock:
            mock.get("https://data.sec.gov/ok").respond(json={"ok": 1})
            assert await get_json(client, "https://data.sec.gov/ok", source="test") == {"ok": 1}


async def test_redirects_not_followed():
    async with make_client("Test test@example.com") as client:
        with respx.mock(assert_all_called=False) as mock:
            mock.get("https://data.sec.gov/a").respond(302, headers={"Location": "https://data.sec.gov/b"})
            target = mock.get("https://data.sec.gov/b").respond(json={})
            with pytest.raises(SourceError, match="redirect"):
                await get_json(client, "https://data.sec.gov/a", source="test")
            assert not target.called


async def test_response_size_cap(monkeypatch):
    monkeypatch.setattr(http_mod, "MAX_BODY_BYTES", 100)
    async with make_client("Test test@example.com") as client:
        with respx.mock() as mock:
            mock.get("https://data.sec.gov/big").respond(json={"x": "y" * 500})
            with pytest.raises(SourceError, match="too large|exceeded"):
                await get_json(client, "https://data.sec.gov/big", source="test")


# ---- secrets ----------------------------------------------------------------


@pytest.fixture
def stderr_logging(capsys):
    """Yields a reader; logging is configured lazily so it binds the call-phase stderr."""
    root = logging.getLogger()
    saved = root.handlers[:], root.level

    def read() -> str:
        return capsys.readouterr().err

    read.start = lambda: server.configure_logging("DEBUG")
    yield read
    root.handlers[:], level = saved
    root.setLevel(level)
    for name in ("httpx", "httpcore"):
        logging.getLogger(name).setLevel(logging.NOTSET)


def test_redact():
    assert validate.redact(f"GET https://x/?series_id=A&api_key={SECRET}&b=1") == (
        "GET https://x/?series_id=A&api_key=***&b=1"
    )


def test_log_filter_redacts(stderr_logging):
    stderr_logging.start()
    logging.getLogger("anything").warning("url was %s", f"https://api.stlouisfed.org/fred?api_key={SECRET}")
    err = stderr_logging()
    assert SECRET not in err and "api_key=***" in err


async def test_fred_key_never_logged_or_returned(stderr_logging, cache):
    stderr_logging.start()
    logging.getLogger("httpx").setLevel(logging.DEBUG)  # worst case: request URLs logged
    async with make_client("Test test@example.com") as client:
        fred = Fred(client, cache, api_key=SECRET)
        with respx.mock() as mock:
            mock.get(f"{BASE}/series").respond(400, text=f"bad request for api_key={SECRET}")
            with pytest.raises(SourceError) as exc:
                await fred.series("DGS10")
    out = json.loads(await server.tool_errors(_raise(exc.value))())
    assert SECRET not in json.dumps(out)
    assert SECRET not in stderr_logging()


async def test_internal_error_redacted(stderr_logging):
    stderr_logging.start()
    err = RuntimeError(f"boom at https://api.stlouisfed.org/fred/series?api_key={SECRET}")
    out = await server.tool_errors(_raise(err))()
    assert SECRET not in out and "internal error: RuntimeError" in out
    assert SECRET not in stderr_logging()


def _raise(exc):
    async def fn():
        raise exc

    return fn


def test_settings_hide_key():
    s = Settings(sec_user_agent="Test test@example.com", fred_api_key=SECRET)
    assert SECRET not in repr(s) and SECRET not in str(s.model_dump())
    assert s.fred_api_key.get_secret_value() == SECRET


# ---- untrusted text, cache, transport ---------------------------------------


def test_clean_text():
    assert validate.clean_text("Apple\u202eInc.\x00\n\tIgnore previous") == "Apple Inc. Ignore previous"
    long = validate.clean_text("x" * 500)
    assert len(long) == validate.MAX_TEXT and long.endswith("…")
    assert validate.clean_text(None) is None


def test_cache_prune(cache: Cache):
    cache.set("fresh", 1, ttl=60)
    cache.set("recent", 1, ttl=-1)
    cache._conn.execute("INSERT INTO cache VALUES ('ancient', x'00', ?, 1)", (time.time() - 40 * 86400,))
    assert cache.prune(30) == 1
    assert cache.get("fresh") and cache.get("recent", allow_expired=True)


def test_main_uses_stdio_only(monkeypatch):
    calls = []
    monkeypatch.setattr(server.mcp, "run", lambda *a, **kw: calls.append((a, kw)))
    monkeypatch.setattr(server, "configure_logging", lambda level: None)
    monkeypatch.setattr(server, "get_settings", lambda: Settings(sec_user_agent="Test test@example.com"))
    server.main()
    assert calls == [(("stdio",), {})]
