"""MCP server exposing market data tools over stdio."""

from __future__ import annotations

import functools
import json
import logging
import sys
from collections.abc import Awaitable, Callable
from typing import Annotated, Any, Literal

import httpx
from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations
from pydantic import Field

from .cache import Cache
from .config import get_settings
from .errors import SourceError
from .financials import build_statement
from .sources.edgar import Edgar
from .sources.fred import Fred
from .sources.yahoo import Yahoo

log = logging.getLogger("stock_data_mcp")

mcp = MCPServer(
    "stock-data",
    instructions=(
        "Market data for equity research. Fundamentals come from SEC EDGAR XBRL filings "
        "(US GAAP filers only), macro series from FRED, prices from Yahoo Finance. "
        "All tools return compact JSON; a response with an 'error' key failed, and its "
        "'hint' says what to try. 'stale': true means the upstream failed and cached data was served."
    ),
)


class Services:
    def __init__(self) -> None:
        s = get_settings()
        self.cache = Cache(s.cache_path)
        self.http = httpx.AsyncClient(
            headers={"User-Agent": s.sec_user_agent, "Accept-Encoding": "gzip, deflate"},
            timeout=httpx.Timeout(30.0, connect=10.0),
            follow_redirects=True,
        )
        self.edgar = Edgar(self.http, self.cache, s.edgar_max_rps)
        self.fred = Fred(self.http, self.cache, s.fred_api_key)
        self.yahoo = Yahoo(self.cache)


_services: Services | None = None


def services() -> Services:
    global _services
    if _services is None:
        _services = Services()
    return _services


def _dump(obj: Any) -> str:
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False, default=str)


def tool_errors(fn: Callable[..., Awaitable[dict]]) -> Callable[..., Awaitable[str]]:
    """Return compact JSON; convert failures into {"error", "hint"} for the model."""

    @functools.wraps(fn)
    async def wrapper(*args: Any, **kwargs: Any) -> str:
        try:
            return _dump(await fn(*args, **kwargs))
        except SourceError as exc:
            out = {"error": str(exc)}
            if exc.hint:
                out["hint"] = exc.hint
            return _dump(out)
        except ValueError as exc:
            return _dump({"error": f"invalid argument: {exc}"})
        except Exception as exc:
            log.exception("tool %s failed", fn.__name__)
            return _dump({"error": f"internal error: {type(exc).__name__}: {exc}"})

    return wrapper


READ_ONLY = ToolAnnotations(readOnlyHint=True, openWorldHint=True)
Ticker = Annotated[str, Field(description="Stock ticker, e.g. AAPL or BRK-B")]


@mcp.tool(annotations=READ_ONLY, structured_output=False)
@tool_errors
async def get_quote(ticker: Ticker) -> dict:
    """Latest quote for a ticker (Yahoo Finance, ~15 min delayed for some exchanges).

    Returns {ticker, price, change, change_pct, prev_close, open, day_high, day_low,
    volume, market_cap, high_52w, low_52w, currency, exchange, fetched_at}.
    Cached for 60s.
    """
    return await services().yahoo.quote(ticker)


@mcp.tool(annotations=READ_ONLY, structured_output=False)
@tool_errors
async def get_price_history(
    ticker: Ticker,
    period: Annotated[
        Literal["1d", "5d", "1mo", "3mo", "6mo", "ytd", "1y", "2y", "5y", "10y", "max"],
        Field(description="Lookback window"),
    ] = "1y",
    interval: Annotated[
        Literal["auto", "1d", "1wk", "1mo"],
        Field(description="Bar size; auto = daily up to 2y, weekly for 5y/10y, monthly for max"),
    ] = "auto",
) -> dict:
    """OHLCV price history (Yahoo Finance), oldest first.

    Returns {ticker, period, interval, columns, count, rows} where each row is
    [date, open, high, low, close, adj_close, volume]. close is the raw close;
    adj_close is adjusted for splits and dividends (use it for returns).
    Capped at the latest 1500 rows ("truncated": true when cut).
    """
    return await services().yahoo.history(ticker, period, interval)


@mcp.tool(annotations=READ_ONLY, structured_output=False)
@tool_errors
async def get_financials(
    ticker: Ticker,
    statement: Annotated[
        Literal["income", "balance", "cashflow"], Field(description="Which financial statement")
    ] = "income",
    years: Annotated[
        int, Field(ge=1, le=20, description="Number of fiscal years (quarterly returns years*4 quarters)")
    ] = 5,
    period: Annotated[
        Literal["annual", "quarterly"], Field(description="Annual (10-K) or quarterly")
    ] = "annual",
) -> dict:
    """Standardized financial statement from SEC XBRL filings (US GAAP filers only).

    Returns columns per fiscal period, oldest first:
    {ticker, cik, company, statement, period, units, periods, period_end,
     items: {line_item: [value per period]}, concepts, computed?, derived?, not_reported?}

    - Money in USD millions; eps_* in USD; shares_* in millions. null = not reported.
    - Period labels use the company's fiscal year, e.g. FY2024, FY2024Q3.
    - concepts: the us-gaap tag(s) each line came from, for auditing.
    - derived: periods computed by subtraction rather than reported directly
      (Q4 = FY - 9M; quarterly cash flow from year-to-date figures).
    - computed: lines calculated from other lines, e.g. free_cash_flow = operating_cash_flow - capex.
    Income lines: revenue, cost_of_revenue, gross_profit, research_development, sga,
    operating_expenses, operating_income, interest_expense, pretax_income, income_tax,
    net_income, eps_basic, eps_diluted, shares_basic, shares_diluted.
    Balance lines: cash, short_term_investments, receivables, inventory, total_current_assets,
    ppe_net, goodwill, intangibles, total_assets, accounts_payable, short_term_debt,
    total_current_liabilities, long_term_debt, total_liabilities, stockholders_equity,
    shares_outstanding.
    Cashflow lines: operating_cash_flow, capex, depreciation_amortization, stock_based_comp,
    investing_cash_flow, financing_cash_flow, dividends_paid, share_repurchases,
    acquisitions, free_cash_flow.
    """
    svc = services()
    cik, name = await svc.edgar.resolve(ticker)
    facts = await svc.edgar.company_facts(cik)
    table = build_statement(facts.value, statement, years=years, quarterly=period == "quarterly")
    out = {"ticker": ticker.upper(), "cik": cik, "company": facts.value.get("name") or name, **table}
    if facts.stale:
        out["stale"] = True
    return out


@mcp.tool(annotations=READ_ONLY, structured_output=False)
@tool_errors
async def get_filings(
    ticker: Ticker,
    form_type: Annotated[
        str | None,
        Field(description="Filter by form, e.g. 10-K, 10-Q, 8-K, DEF 14A, S-1, 4, SC 13G. Omit for all."),
    ] = None,
    limit: Annotated[int, Field(ge=1, le=100, description="Max filings to return")] = 10,
    include_amendments: Annotated[bool, Field(description="Also match amended forms like 10-K/A")] = True,
) -> dict:
    """Recent SEC filings for a company, newest first (from EDGAR submissions).

    Returns {ticker, cik, company, form_type, count, filings: [{form, filed, period,
    accession, url, description?, items?}]}. url points to the primary document;
    items lists 8-K item numbers (e.g. 2.02 = results of operations).
    Covers roughly the last 1000 filings.
    """
    return await services().edgar.filings(ticker, form_type, limit, include_amendments)


@mcp.tool(annotations=READ_ONLY, structured_output=False)
@tool_errors
async def get_macro_series(
    series_id: Annotated[
        str,
        Field(
            description="FRED series ID, e.g. DGS10 (10y Treasury), FEDFUNDS, CPIAUCSL (CPI), "
            "UNRATE, GDPC1 (real GDP), T10Y2Y (10y-2y spread), BAMLH0A0HYM2 (HY spread), VIXCLS"
        ),
    ],
    start: Annotated[str | None, Field(description="Start date YYYY-MM-DD; omit for full history")] = None,
    end: Annotated[str | None, Field(description="End date YYYY-MM-DD")] = None,
    frequency: Annotated[
        Literal["d", "w", "bw", "m", "q", "sa", "a"] | None,
        Field(description="Downsample to this frequency (only lower than native)"),
    ] = None,
    aggregation: Annotated[
        Literal["avg", "sum", "eop"], Field(description="How to aggregate when downsampling")
    ] = "avg",
) -> dict:
    """Macro/economic time series from FRED, oldest first.

    Returns {series_id, title, units, frequency, seasonal_adjustment, last_updated,
    count, observations: [[date, value]]}; value is null where FRED has no data.
    Capped at the latest 2500 observations; use frequency or start to narrow.
    """
    return await services().fred.series(series_id, start, end, frequency, aggregation)


def main() -> None:
    # stdout carries the MCP protocol; logs must go to stderr.
    logging.basicConfig(
        stream=sys.stderr,
        level=get_settings().log_level.upper(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    mcp.run("stdio")


if __name__ == "__main__":
    main()
