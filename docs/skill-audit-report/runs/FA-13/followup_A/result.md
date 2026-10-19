# followup_A: weekly-watchlist-review test run (AAPL, NVDA, META)

The run date was 2026-10-18 (a Sunday), which the skill uses as the as-of date. Prices are the Friday 2026-10-16 close.

## 1. Skill output (table and 3 bullets)

## Weekly watchlist review - 2026-10-18

| Ticker | Last price (USD) | Price date | 1W % | 1M % | 52-wk position | 52-wk low-high (USD) | Latest SEC filing | 8-K last 7d | Status |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 343.46 | 2026-10-16 | +2.0% | +3.3% | 95.5% | 243.42-348.15 | 144 (2026-10-16) | - | OK |
| NVDA | 214.13 | 2026-10-16 | -6.6% | +0.1% | 63.0% | 164.27-243.37 | 4/A (2026-10-13) | - | OK |
| META | 709.33 | 2026-10-16 | -1.3% | +5.3% | 72.8% | 520.26-779.82 | 4 (2026-10-14) | - | OK |

- **Tape:** equal-weight 1W average -2.0% across the 3 names; best AAPL +2.0%, worst NVDA -6.6% (META -1.3%, including -3.3% on Friday alone). Cause not checked.
- **Positioning:** AAPL sits at 95.5% of its 52-wk range, about 1.3% below the 52-wk high of 348.15 set on 2026-10-13. NVDA (63.0%, about 12% below its high) and META (72.8%, about 9% below its 2026-09-24 high of 779.82) are mid-range. None is near a 52-wk low. 1M moves are modest: META +5.3%, AAPL +3.3%, NVDA +0.1%.
- **Filings/events:** none of the three filed an 8-K in the last 7 days (2026-10-11 to 2026-10-18). The latest filings are all insider forms: AAPL Form 144 (10-16), NVDA Form 4/A (10-13) and META Form 4 (10-14). NVDA's most recent 8-K (2026-09-03, Item 8.01) falls outside the window. No tickers had data errors.

Footnote: Sources: stock-data MCP (Yahoo Finance for quote and price history, SEC EDGAR for filings). Prices are the 2026-10-16 close, using raw closes. The definitions match SKILL.md step 4.

## 2. Deviations and workarounds

1. **The price-history output shape isn't supported, and the failure is silent (the main issue).** `get_price_history` returns `{ticker, period, interval, columns:[...], count, rows:[[date, open, high, low, close, adj_close, volume], ...]}`.
   - `build_review.py`'s `unwrap()` doesn't list `rows` among its wrapper keys. It therefore falls into the "columnar dict" branch, which treats the `columns` and `rows` lists as two columns, and every parsed bar has no date.
   - Pasting the raw output as SKILL.md step 3 says ("Paste raw tool output") produced a table with **no error raised**. Every name showed `PARTIAL`, with 1W, 1M and 52-wk all `n/a` and the note "no usable price data". This is reproduced in `_work/review_raw.md`.
   - Workaround: I followed references/data_sources.md ("reshape it to `[{"date":..,"close":..}]` ... rather than editing the script"). `_work/assemble.py` maps rows to `{date, high, low, close}`.
   - Fix for the skill: add `rows` plus `columns` handling to `unwrap()`, or document this tool's shape.
2. **The period parameter isn't spelled out.** SKILL.md says "daily, >= 13 months back", but the tool takes enums: `period` (1y, 2y, ...) and `interval` (`1d`, `auto`, ...). 1y would be short of 13 months, so I used `period="2y", interval="1d"` (501 rows). Choosing it was easy, but the skill could name it.
3. **Raw vs adjusted close.** The tool returns both `close` and `adj_close`, and its own docstring says "use adj_close for returns". The script picks `close` first. I kept raw close, which is consistent with the raw quote price and the raw daily highs/lows.
   - AAPL and NVDA are unaffected in the 1W and 1M windows, because close equals adj_close from 2026-08-10 and 2026-09-10 respectively.
   - META's 1M reference close differs by 0.08% (673.31 raw vs 672.78 adjusted), so the rounded figure doesn't change.
   - The skill doesn't say which series to choose for this tool.
4. **Quote date key isn't recognised.** `get_quote` returns `fetched_at`, which isn't in `QUOTE_DATE_KEYS`. The script fell back to the last bar date (2026-10-16), which is correct. If history had been missing, the price date would have been n/a and no stale-price check would have run.
5. **Getting data into the input file means retyping it.** The tool output can't be piped to disk, so building `watchlist_input.json` meant writing the tool output out by hand.
   - I trimmed the history to rows from 2025-10-01 onward, which still covers 52 weeks plus the 1M lookback; the script reported no partial-range note.
   - I copied only the needed filing fields (form, filed, period, items) and dropped url and accession.
   - This is laborious (about 790 rows) and a place where transcription errors could creep in. All key reference values were cross-checked; see section 3.
6. **The filings call needed no parameter changes.** `get_filings(ticker, limit=20)` worked, and the `filed` key is in `FILED_KEYS`. The 8-K detail step (item numbers) wasn't needed because no 8-K fell in the window. `get_filings` already returns `items`, so no separate detail call exists or is needed.
7. **Minor issues:**
   - The script's heading is `### Weekly watchlist review - as of <date>`, while SKILL.md wants `Weekly watchlist review - <as-of>`; I used the SKILL.md form.
   - The "Latest SEC filing, any form" definition puts Form 144 and Form 4 insider filings in that column for all three names. That is correct per the definition but not very informative.
   - Tool naming matched SKILL.md (`mcp__remote-devices__stock-data__*`, loaded with ToolSearch `+stock-data`). No fallbacks were needed and no script errors occurred.

## 3. Was the table correct without edits?

**No, if "without edits" means following step 3 literally (raw paste).** That produced a wrong, degraded table: all three names PARTIAL with n/a for every price metric, and no error to tell the user something was wrong.

**Yes, after the reshape that data_sources.md prescribes, with no hand edits to the output.** I checked the reshaped table against the tool data:

| Ticker | 1W check | 1M check | 52-wk low and high |
|---|---|---|---|
| AAPL | 343.46 / 336.64 (10-09) = +2.03% | / 332.41 (09-16) = +3.32% | Match the quote's `low_52w`/`high_52w` (243.42 / 348.15) |
| NVDA | / 229.28 = -6.61% | / 213.90 = +0.11% | Match the quote (164.27 / 243.37) |
| META | / 718.67 = -1.30% | / 673.31 = +5.35% | Match the quote (520.26 / 779.82) |

The 8-K window is correct: NVDA's 2026-09-03 8-K is outside it, and there are no others.

## 4. Tool-call log

| Tool | Count | Purpose |
|---|---|---|
| Bash | 3 | List skill and read SKILL.md; read the reference doc and script, then mkdir; run assemble.py and build_review.py (raw and shaped) and print the computed rows |
| ToolSearch | 1 | `+stock-data` to load the schemas |
| mcp__remote-devices__stock-data__get_quote | 3 | AAPL, NVDA, META |
| mcp__remote-devices__stock-data__get_filings | 3 | limit=20 each |
| mcp__remote-devices__stock-data__get_price_history | 3 | period=2y, interval=1d |
| Write | 8 | 3 raw history files, raw quotes and filings, assemble.py, the review deliverable, result.md (this file) |
| Read / Edit | 0 | |

- Tool errors and retries: 0.
- Total: 21 calls, plus 1 SubagentHandback.

## Files (all under /home/claude/results/2026-10-13/runs/FA-13/followup_A/)

- Deliverable: `weekly_watchlist_review_2026-10-18.md`
- This report: `result.md`
- Final script output: `_work/watchlist_input.json`, `_work/review.json`, `_work/review.md`
- Raw-paste failure reproduction: `_work/watchlist_input_raw.json`, `_work/review_raw.md`, `_work/review_raw.json`
- Saved tool output and the reshaping script: `_work/raw_{AAPL,NVDA,META}_history.json`, `_work/raw_quotes_filings.json`, `_work/assemble.py`
