# Stock-Data-MCP

A personal market-data MCP server for stock research in Claude. It runs locally over stdio and exposes five tools:

| Tool | Source | What it returns |
|---|---|---|
| `get_quote(ticker)` | Yahoo Finance (yfinance) | Last price, change, day range, volume, market cap, 52-week range |
| `get_price_history(ticker, period, interval)` | Yahoo Finance | OHLCV rows incl. adjusted close; interval auto-picks daily/weekly/monthly |
| `get_financials(ticker, statement, years, period)` | SEC EDGAR XBRL | Standardized income / balance / cash-flow statement, annual or quarterly |
| `get_filings(ticker, form_type, limit)` | SEC EDGAR | Recent filings with links to the primary document |
| `get_macro_series(series_id, start, end, frequency)` | FRED | Macro time series (rates, CPI, GDP, spreads, ...) |

All tools return compact JSON. Failures come back as `{"error": ..., "hint": ...}` rather than exceptions, and `"stale": true` means the upstream failed and cached data was served.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/lukashmoser/Stock-Data-MCP.git
cd Stock-Data-MCP
uv sync --locked
cp .env.example .env   # then edit it
```

`.env`:

```
SEC_USER_AGENT="Your Name you@example.com"   # required by SEC
FRED_API_KEY=...                              # free: https://fred.stlouisfed.org/docs/api/api_key.html
```

`.env` is read from the repo directory, so it works whatever directory Claude launches the server from.

### Connect to Claude Desktop

Add this to `claude_desktop_config.json` (Settings → Developer → Edit Config), then restart Claude:

```json
{
  "mcpServers": {
    "stock-data": {
      "command": "uv",
      "args": ["run", "--locked", "--no-dev", "--directory", "C:\\path\\to\\Stock-Data-MCP", "stock-data-mcp"]
    }
  }
}
```

If Claude can't find `uv`, use its absolute path as `command` (`where uv` on Windows, `which uv` elsewhere). In JSON, Windows paths need doubled backslashes.

`--locked` refuses to run if `uv.lock` is out of date, so launching never installs anything unreviewed; `--no-dev` leaves out test and Inspector tooling.

## How `get_financials` works

Data comes from EDGAR's `companyfacts` API (XBRL tags from 10-K/10-Q filings). The steps:

- **Concept mapping** (`src/stock_data_mcp/sources/xbrl_map.py`): each line item (e.g. `revenue`) has an ordered list of us-gaap tags. For each period the first tag with a value wins, which handles companies switching tags over time. The response's `concepts` field shows which tags were used. Edit the mapping freely; the cache is keyed on its contents.
- **Periods** are identified by start/end dates, and labels follow the company's fiscal year (`FY2024`, `FY2024Q3`), including 52/53-week calendars.
- **Restatements**: the most recently filed value for a period wins.
- **Quarterly**: reported 3-month values are used when they exist. Otherwise the quarter is derived from year-to-date figures: Q4 = FY − 9M, and quarterly cash flow comes from the YTD numbers in 10-Qs. Derived periods are listed under `derived`. Per-share and share-count lines are never derived by subtraction, so they can be `null` for Q4.
- **Computed lines**: `free_cash_flow = operating_cash_flow − capex`, and `gross_profit = revenue − cost_of_revenue` when gross profit isn't tagged.
- **Units**: money in USD millions, EPS in USD, share counts in millions.
- **Limits**: only US-GAAP filers are supported, so IFRS / 20-F filers return a clear error. Banks and insurers will have sparse lines.

## Caching

The cache is SQLite at `.cache/stock_data.sqlite` (override with `CACHE_PATH`). If a fetch fails, the expired entry is served instead, marked `"stale": true`.

| Data | TTL |
|---|---|
| Quote | 60 s |
| Price history | 12 h (5 min for 1d/5d) |
| Ticker → CIK map | 24 h |
| Filings list | 6 h |
| Company facts | 24 h |
| FRED observations / metadata | 6 h / 7 d |

Delete the file to clear everything; entries expired for more than 30 days are pruned at startup. The cache holds only public data. EDGAR requests are rate-limited to 8/s, under the SEC's 10/s limit.

## Security

The server runs as your user, so it is kept deliberately narrow: it only fetches public market data from fixed hosts and never reads or writes files other than its cache.

**What the code enforces**
- **stdio only.** No network port is opened; `main()` only ever runs the stdio transport.
- **Strict tool arguments.** Tickers, series IDs, form types and dates must match short fixed patterns (also published in the tool schemas). This blocks path or URL tricks and limits how much text a prompt-injected request could smuggle out to FRED, Yahoo or the SEC.
- **Outbound allowlist.** The HTTP client only talks HTTPS to `www.sec.gov`, `data.sec.gov` and `api.stlouisfed.org`, never follows redirects, and caps responses at 150 MB. yfinance uses its own HTTP stack but only builds Yahoo URLs from the validated ticker.
- **Secrets stay out of logs and results.** The FRED key is held as a `SecretStr`, httpx request logging is turned off, and every log line, traceback and tool error is scrubbed of `api_key=...`.
- **Third-party text is sanitized.** Company names, filing descriptions and FRED titles are stripped of control and bidi characters and truncated, and the server tells Claude to treat them as data. No tool fetches or returns filing document bodies; adding one would need its own review, since that text could carry prompt injection.

**What you should do (Windows)**
- Restrict `.env` to your account: `icacls .env /inheritance:r /grant:r "%USERNAME%:F"`.
- Keep the clone outside OneDrive or other synced/shared folders so `.env` isn't uploaded.
- Logs go to `%APPDATA%\Claude\logs\mcp-server-stock-data.log`. Keep `LOG_LEVEL` at `INFO` or higher.
- Only run the MCP Inspector (`mcp dev`) while you're using it; it opens a local web proxy.
- These tools are read-only, so "always allow" in Claude Desktop is reasonable. Take more care when the same chat also has tools that can read private files: an outbound tool like this one is how such data could leak, which is what the argument limits above guard against.

**Updating dependencies.** Dependencies are the largest risk, since any package runs with your permissions. Versions and hashes are pinned in `uv.lock` and major versions are capped in `pyproject.toml`. Upgrade deliberately:

```bash
uv lock --upgrade          # then review the uv.lock diff
uvx pip-audit              # check for known vulnerabilities
uv sync --locked && uv run pytest
```

## Development

```bash
uv run pytest               # offline tests (mocked HTTP + synthetic fixtures)
uv run pytest -m live       # smoke tests against the real APIs (needs .env)
uv run ruff check . && uv run ruff format .
uv run mcp dev src/stock_data_mcp/server.py   # MCP Inspector (dev dependency)
```

Layout:

```
src/stock_data_mcp/
  server.py        MCP tools (MCPServer, the mcp 2.x successor to FastMCP), logging
  validate.py      tool-argument patterns, text sanitizing, secret redaction
  config.py        settings from .env
  cache.py         SQLite TTL cache with stale fallback
  http.py          allowlisted client; GET with retries, size cap, error mapping
  financials.py    XBRL facts -> statement tables (fiscal calendar, Q4 derivation)
  sources/
    edgar.py       ticker->CIK, submissions, companyfacts
    xbrl_map.py    line item -> us-gaap concept candidates
    fred.py        FRED series
    yahoo.py       yfinance quote/history behind a PriceSource protocol
```
