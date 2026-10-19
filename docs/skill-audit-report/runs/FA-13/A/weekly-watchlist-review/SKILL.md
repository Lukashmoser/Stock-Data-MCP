---
name: weekly-watchlist-review
description: Weekly (Monday) review of a stock watchlist. Produces one table per run with last price, 1-week and 1-month % change, position in the 52-week range, latest SEC filing (form + date), and a flag for any 8-K filed in the last 7 days, followed by a 3-bullet summary. Use when the user asks for a weekly/Monday watchlist review, watchlist check-in, "how did my watchlist do this week", or runs this as a scheduled Monday task on a list of tickers.
---

# Weekly Watchlist Review

Turn a list of tickers into a dated review table plus a 3-bullet summary. Fetch data with the
environment's market-data tools, then let `scripts/build_review.py` do every calculation so
numbers are deterministic and one bad ticker never breaks the run.

## Workflow

### 1. Get the watchlist and the as-of date
- Tickers: from the user's message, an attached file (txt/csv, one ticker per line or a
  `ticker` column), or a saved watchlist file the user names. Uppercase, de-duplicate, keep order.
- If no watchlist is given and none can be found, ask once; in an unattended scheduled run,
  stop and report that no watchlist was supplied.
- As-of date: today. On a Monday run, prices will be Friday's close; that is expected.

### 2. Fetch data per ticker (stock-data tools first)
Use the `stock-data` MCP tools (named `mcp__remote-devices__stock-data__*` in a cloud session
linked to the user's computer; load them with ToolSearch `+stock-data` if deferred):

| Need | Tool | Request |
|---|---|---|
| Last price | `get_quote` | ticker |
| Daily closes / highs / lows | `get_price_history` | ticker, daily, >= 13 months back (covers 52 wks + 1M lookback) |
| SEC filings | `get_filings` | ticker, most recent ~20 filings (or last 90 days) |

- Fetch tickers in parallel where possible. Wrap each ticker independently: if a call errors,
  times out, or returns empty, record `"error": "<message>"` for that ticker and continue.
  Retry a failed call once at most.
- If the stock-data tools are not available, use the fallbacks in
  `references/data_sources.md` (SEC EDGAR via WebFetch for filings; web price pages for prices)
  and say which fallback was used.

### 3. Assemble the input file
Write `watchlist_input.json` (in a work folder, not the deliverable folder):
```json
{"as_of": "YYYY-MM-DD",
 "tickers": {"AAPL": {"quote": {...}, "history": [...], "filings": [...]},
             "XYZ":  {"error": "get_quote: unknown symbol"}}}
```
Paste raw tool output into `quote` / `history` / `filings`. The script accepts common key names
and wrapper shapes (lists, `{"data": [...]}`, columnar `{"date": [...], "close": [...]}`); see
`references/data_sources.md` if a tool's shape is not recognised.

### 4. Compute
```bash
python3 scripts/build_review.py watchlist_input.json --json review.json --md review.md
```
Definitions the script applies (state them in the footnote, do not re-derive by hand):
- Last price: quote price; falls back to the latest daily close.
- 1W %: last vs close on/before (price date - 7 days). 1M %: vs close on/before same day
  last month.
- 52-wk position: (last - 52wk low) / (52wk high - 52wk low), 0% = at low, 100% = at high, using
  daily highs/lows when present, else closes.
- Latest SEC filing: most recent filing date on/before as-of, any form.
- 8-K flag: any form starting `8-K` (incl. `8-K/A`) filed in [as-of - 7 days, as-of].
- Status: OK / PARTIAL (some fields missing) / ERROR (no price and no filings). Errors and stale
  prices (> 5 days old) are listed under "Data notes".

### 5. Write the reply
1. Heading `Weekly watchlist review - <as-of>`.
2. The table from `review.md` (keep its columns and order; percentages to 1 dp, prices in USD).
3. Exactly 3 bullets, built from the `facts` list in `review.json` plus the table:
   - Bullet 1 - the week's tape: average 1W move, best and worst names.
   - Bullet 2 - positioning: names near 52-wk highs/lows or with big 1M moves.
   - Bullet 3 - filings/events: every 8-K flagged (open the 8-K item numbers via `get_filings`
     detail or EDGAR if available, else just name the date), plus any tickers with data errors.
   Never invent catalysts or causes not supported by fetched data; say "cause not checked"
   rather than guess.
4. One footnote line: data sources used, price date, and definitions above in short form.

### 6. Scheduling (optional)
If the user wants it automatic, offer a weekly scheduled task (Monday morning, user's time zone)
whose prompt names this skill and the watchlist location. Do not create it without their say-so.
