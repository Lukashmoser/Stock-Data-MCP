# followup_B: weekly-watchlist-review test run (AAPL, NVDA, META)

Run date: 2026-10-18 (Sunday). As-of = today (the user gave no date), latest close = Fri 2026-10-16.
Outputs: `followup_B/review.md` (final report). Scratch: `_work/watchlist_data.json` (raw tool results, verbatim), `_work/review.md`.

## 1. Output the skill produced (script output unedited, plus the 3 bullets)

# Weekly watchlist review — week ending 2026-10-18
Prices as of close 2026-10-16 (Yahoo Finance via get_quote/get_price_history); filings from SEC EDGAR via get_filings.

| Ticker | Last price (USD) | 1W % | 1M % | 52w position | Latest SEC filing | 8-K last 7d |
|---|---|---|---|---|---|---|
| AAPL | 343.46 | +2.0% | +3.3% | 95.5% (243.42–348.15) | 8-K/A 2026-09-01 | — |
| NVDA | 214.13 | -6.6% | +0.1% | 63.0% (164.27–243.37) | 8-K 2026-09-03 | — |
| META | 709.33 | -1.3% | +5.4% | 72.8% (520.26–779.82) | n/a | — |

Notes: 1W/1M use adjusted closes vs the last close on/before 7 days / 1 calendar month earlier. 52w position: 0% = 52-week low, 100% = high. 8-K window: 2026-10-12 to 2026-10-18. Latest SEC filing excludes insider-ownership forms (3/4/5/144/13D/13G); newest filing of any form: AAPL 144 2026-10-16, NVDA 4/A 2026-10-13.

## Summary
- NVDA was the worst 1W mover at -6.6% and AAPL the best at +2.0%, with META -1.3% (median -1.3%), so the watchlist was net lower on the week ending 2026-10-16.
- AAPL sits at 95.5% of its 52-week range, close to its 348.15 high, while NVDA (63.0%) and META (72.8%) are mid-to-upper range and no name is near its 52-week low.
- No 8-K or 8-K/A was filed by any of the three names in 2026-10-12 to 2026-10-18; based on last quarter's late-July earnings 8-Ks (item 2.02) for AAPL and META, their next quarterly results are likely due in late October.

## 2. Deviations / workarounds

- **Tool names and parameters:** none needed. The skill's `compatibility` line correctly maps to `mcp__remote-devices__stock-data__*` (loaded with one ToolSearch call). All parameters (`period="3mo"`, `interval="1d"`, `limit=40`, `form_type="8-K"`, `limit=5`) matched the tool schemas. Every call succeeded on the first try, so no retries and no `{"error":...}` entries were needed.
- **Script:** ran without errors (`python3 build_review.py watchlist_data.json --out review.md --json`). I used `python3` because the skill says `python`. Paths were adjusted to the skill's absolute location and my `_work/` folder.
- **Missing data / silent gap (META "Latest SEC filing" = n/a):** META's 40 most recent filings (2026-08-12 to 2026-10-14) are all Form 4 or Form 144. The `limit=40` all-forms call never reaches a non-ownership filing, so the script prints `n/a`. The cause is a design gap in the skill, not a tool failure, and three things go wrong:
  - It does **not** appear on a "Data issues" line, because no error occurred.
  - META is **left out** of the "newest filing of any form" footnote, because that note is only written when `latest_filing` is non-null.
  - The script does **not** fall back to the `filings_8k` result it already has. That result shows META 8-K 2026-07-29 (2.02, 9.01), so the cell should be at least `8-K 2026-07-29`; the true answer is probably the Q2 10-Q filed around 2026-07-30. That is not verified, because the skill's 4-call budget rules out another fetch.
  - I did not hand-edit the table. The skill says to use the script's output, and the test asked whether the table is correct without edits.
- **As-of date:** the skill defaults as-of to "today". Today is Sunday 2026-10-18, so the header reads "week ending 2026-10-18" while prices are from Friday 2026-10-16. The skill expects this and the close date is reported correctly. The 8-K window runs 10-12 to 10-18.
- **Input JSON:** I pasted the tool results verbatim as instructed, which makes about 60 KB of hand-written JSON. That is a lot of output tokens; a helper that writes each tool result to disk would be cheaper, but the skill gives no such mechanism.
- **Bullet 3, "next notable item":** this comes from the prior-quarter 8-K dates (pattern-based). I made no extra calls to confirm the earnings dates.

## 3. Was the table correct without edits?

**No.** Every numeric column is correct; I checked each one by hand against the raw data:
- AAPL 1W: 343.46 / 336.64 = +2.0%. AAPL 1M: vs 09-16 close of 332.41 = +3.3%.
- NVDA 1W: 214.13 / 229.28 = -6.6%. NVDA 1M: vs 213.90 = +0.1%.
- META 1W: 709.33 / 718.67 = -1.3%. META 1M: vs 672.78 = +5.4%.
- 52w positions: AAPL (343.46 − 243.42) / 104.73 = 95.5%, and the same check works for the others.
- The 8-K flags are correct: none in the window.
- AAPL's and NVDA's "Latest SEC filing" cells match the definition.

However, **META's "Latest SEC filing" is wrong (`n/a`)**. Its latest non-ownership filing exists (at least 8-K 2026-07-29), but it is beyond the 40-filing window, and the report hides this gap instead of flagging it. Large caps with heavy insider filing will hit this regularly. Possible fixes:
- Raise `limit` (up to 100).
- Make a second filtered call (e.g. 10-Q/10-K).
- Have the script fall back to the newest entry in `filings_8k`, and list the gap under Data issues.

## 4. Tool-call log

| Tool | Count | Notes |
|---|---|---|
| Bash | 4 | read SKILL.md + mkdir; read build_review.py; run script; append summary/copy |
| ToolSearch | 1 | loaded get_quote, get_price_history, get_filings |
| mcp__remote-devices__stock-data__get_quote | 3 | AAPL, NVDA, META; all OK |
| mcp__remote-devices__stock-data__get_price_history | 3 | period=3mo, interval=1d; all OK |
| mcp__remote-devices__stock-data__get_filings | 6 | 3 × limit=40 all forms; 3 × form_type=8-K limit=5; all OK |
| Write | 2 | _work/watchlist_data.json, result.md |
| **Total** | **19** | 12 stock-data calls = exactly the skill's 4-per-ticker budget; 0 retries, 0 errors |
