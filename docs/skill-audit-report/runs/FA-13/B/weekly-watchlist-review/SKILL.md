---
name: weekly-watchlist-review
description: Weekly (Monday) watchlist review for a list of stock tickers. For each ticker it shows last price, 1-week and 1-month % change, where the price sits in its 52-week range, the latest SEC filing (form + date), and a flag for any 8-K filed in the last 7 days, then a 3-bullet summary. Use this skill whenever the user wants a weekly or Monday check-in on a watchlist, portfolio or basket of tickers, asks "how did my names do this week", wants a quick price + filings scan across several stocks, or asks to set up a recurring watchlist report, even if they don't say "watchlist review".
compatibility: Needs the stock-data tools get_quote, get_price_history and get_filings (exposed in this environment as mcp__remote-devices__stock-data__*; load them with ToolSearch if deferred). Python 3 for scripts/build_review.py.
---

# Weekly watchlist review

Produces one compact table plus a 3-bullet summary for a watchlist of US-listed tickers.
It is meant to run every Monday, so the numbers describe the week that just ended.

## Inputs

- **Watchlist**: tickers from the user's message, an attached file (CSV/TXT/XLSX, one ticker per row
  or a `ticker` column), or a previously saved list. Upper-case them, strip `$`, de-duplicate, keep the
  user's order. Use Yahoo-style share classes (`BRK-B`, not `BRK.B`).
- **As-of date**: today, unless the user gives one. On a Monday the latest close is the prior Friday
  (or Thursday after a holiday) — that is expected; report the actual close date, never pretend it is
  Monday's close.

## Data tools (use these, in this order, per ticker)

| Need | Tool | Call |
|---|---|---|
| Last price, 52-week high/low | `get_quote` | `ticker` |
| 1W / 1M returns, fallback 52w range | `get_price_history` | `ticker`, `period="3mo"`, `interval="1d"` (use `period="1y"` only if the quote lacks `high_52w`/`low_52w`) |
| Latest SEC filing | `get_filings` | `ticker`, `limit=40` (all forms) |
| 8-K check | `get_filings` | `ticker`, `form_type="8-K"`, `limit=5` (amendments included by default) |

Call the tools for all tickers in parallel where the client allows it. Four calls per ticker is the
budget; don't fetch anything else unless the user asks.

If these tools are not available, say so plainly and stop rather than estimating prices from memory —
a watchlist report with recalled numbers is worse than none.

## Handling a ticker that errors

Tools return `{"error": ..., "hint": ...}` for bad or delisted tickers, ETFs/foreign names that have no
SEC filer record, or upstream hiccups. Don't drop the ticker and don't let it stop the run:

1. Retry a failed call once (transient Yahoo errors are common).
2. If it still fails, keep the ticker's row and write `n/a` in the affected cells. Filings failing but
   prices working (typical for ETFs, ADRs filing 6-K/20-F under a different name, or non-US listings) is
   normal — show prices and mark filings `n/a (no SEC record)`.
3. List every error under a **Data issues** line below the table: ticker, which tool, the error text.
4. If every ticker fails, report that and stop — don't produce an empty table.

## Computing the columns

Save the raw tool results to a JSON file and run the bundled script; it does the date arithmetic and
filing filters identically every week and handles missing pieces:

```bash
python scripts/build_review.py watchlist_data.json --out review.md
```

Input format (one entry per ticker; paste each tool's JSON result verbatim, or an `{"error": ...}`
object if it failed):

```json
{
  "as_of": "2026-10-19",
  "tickers": {
    "AAPL": {"quote": {...}, "history": {...}, "filings": {...}, "filings_8k": {...}},
    "ZZZZ": {"quote": {"error": "..."}, "history": {"error": "..."}, "filings": {"error": "..."}, "filings_8k": {"error": "..."}}
  }
}
```

Definitions the script uses (state them in a footnote of the report):

- **Last price**: `get_quote.price` (USD per share). Close date = last row of the price history.
- **1W % / 1M %**: latest `adj_close` vs the last `adj_close` on or before (close date − 7 calendar days)
  and (close date − 1 calendar month). Adjusted closes so dividends/splits don't distort returns.
  One decimal place.
- **52-week position**: `(price − low_52w) / (high_52w − low_52w) × 100`, 0% = at the low, 100% = at the
  high, shown with the range (e.g. `94.1% (243.42–348.15)`). Falls back to 1y history min/max.
- **Latest SEC filing**: newest filing whose form is *not* an insider-ownership form (3, 4, 5, 144 and
  their amendments, SC 13D/13G, SCHEDULE 13D/13G). Large caps file Form 4s almost daily, so the literal
  newest filing is nearly always a Form 4 and tells the reader nothing; the script also notes the
  newest filing of any form in a footnote so nothing is hidden. If the user wants the literal newest
  filing, pass `--all-forms`.
- **8-K flag**: `YES` if any 8-K or 8-K/A was filed within the 7 calendar days ending on the as-of date
  (inclusive), with item numbers (e.g. `YES 2.02, 9.01`); otherwise `—`.

If you can't run Python, apply the same definitions by hand.

## Output format

```
# Weekly watchlist review — week ending YYYY-MM-DD
Prices as of close YYYY-MM-DD (Yahoo Finance via get_quote/get_price_history); filings from SEC EDGAR via get_filings.

| Ticker | Last price (USD) | 1W % | 1M % | 52w position | Latest SEC filing | 8-K last 7d |
|---|---|---|---|---|---|---|
| AAPL | 342.00 | +0.5% | +3.2% | 94.1% (243.42–348.15) | 8-K/A 2026-09-01 | — |

Data issues: ZZZZQ — get_quote: Yahoo Finance error ...; get_filings: not found in SEC company list.

## Summary
- ...
- ...
- ...
```

**The 3 bullets** — exactly three, each one sentence, each grounded in the table:
1. Performance: the best and worst 1W movers (with numbers) and the median or overall direction.
2. Positioning: names near 52-week highs (≥90%) or lows (≤10%), or note none are at extremes.
3. Filings/events: any 8-K flags with what the items mean (2.02 earnings, 5.02 officer/director change,
   1.01 material agreement, 7.01/8.01 Reg FD/other, 9.01 exhibits); if none, say so and mention the
   next notable item if obvious (e.g. a 10-Q due). Mention data issues here only if a ticker failed.

Keep bullets factual; don't add price targets or buy/sell advice — this is a monitoring report.

## Running it every Monday

The skill does the review whenever it is invoked. If the user wants it automatic, offer to create a
scheduled task (e.g. Mondays ~07:45 in their time zone) whose prompt contains the full ticker list
and says "Run the weekly-watchlist-review skill on: ...". Confirm the time zone before creating it.
