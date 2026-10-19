# Transcript FA-12 / arm B

- Start: Fri Oct 16 03:35:09 UTC 2026
- End: Fri Oct 16 03:36:16 UTC 2026

## Final reply

I built the workbook at `/home/claude/results/2026-10-13/runs/FA-12/B/out/MSFT_10Y_correlation.xlsx` (relative to the run folder: `out/MSFT_10Y_correlation.xlsx`).

**What's in it**
- **Inputs:** 61 month-ends from 2021-09-30 to 2026-09-30. Each row has the MSFT adjusted close (USD per share) and the 10-year Treasury yield (%). All input values are in blue. Row 5 gives the source of each column:
  - Date column: calendar month-ends, which I constructed.
  - MSFT column: Yahoo Finance monthly bars, adjusted for splits and dividends, pulled with stock-data `get_price_history`.
  - Yield column: FRED series DGS10, taking the last value of each month, pulled with stock-data `get_macro_series` (FRED last updated 2026-10-13).
- **Calc:** every cell is a live formula (366 of 366).
  - Columns A to C link to Inputs (green).
  - MSFT monthly return = `B/B_prior - 1`.
  - Change in the 10-year yield is in percentage points.
  - The 12-month rolling correlation uses `CORREL` over the last 12 months of pairs.
  - The full-period correlation is in `Calc!C3`. It uses all 60 monthly pairs.
  - Cells where a value can't be calculated yet (the first row, and the first 11 rolling-correlation rows) show `=NA()`.
- **Summary:** a table of key figures driven by formulas, plus two charts:
  - a line chart of the 12-month rolling correlation, with the axis fixed at -1 to 1;
  - a scatter chart of MSFT monthly return against the monthly change in yield.
- **Checks:** five TRUE/FALSE tests (row counts, blanks, positive prices, dates in order, correlation bounds). All of them are TRUE.
- Named ranges `FullPeriodCorr` and `LatestRollingCorr` point to the two headline correlations. The file is set to recalculate fully when opened. I recalculated a copy in LibreOffice to check the values, and there were no formula errors apart from the intended #N/A cells.

**Results**
- Over the full period, the correlation between MSFT monthly returns and the monthly change in the 10-year yield is **-0.257**: mildly negative, so MSFT tended to do worse in months when yields rose.
- The 12-month rolling correlation has moved a lot, from a low of -0.882 to a high of +0.513.
- The latest reading (12 months to 2026-09-30) is **+0.330**.

## Comparison Block

### 1. Key figures
| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| First month in data | 2021-09-30 | date | 2021-09 | stock-data get_price_history / get_macro_series | H |
| Last month in data | 2026-09-30 | date | 2026-09 | stock-data get_price_history / get_macro_series | H |
| Number of monthly rows | 61 (60 return/yield-change observations) | rows | 2021-09-30 to 2026-09-30 | Workbook Inputs tab | H |
| First MSFT adjusted close | 270.57 | USD per share | 2021-09-30 | stock-data get_price_history (Yahoo Finance, 1mo, adj_close) | H |
| Last MSFT adjusted close | 512.90 | USD per share | 2026-09-30 | stock-data get_price_history (Yahoo Finance, 1mo, adj_close) | H |
| First 10-year yield | 1.52 | % | 2021-09-30 | stock-data get_macro_series (FRED DGS10, monthly end-of-period) | H |
| Last 10-year yield | 5.29 | % | 2026-09-30 | stock-data get_macro_series (FRED DGS10, monthly end-of-period) | M |
| Full-period correlation | -0.257 (-25.7%) | correlation coefficient | 60 months, 2021-10 to 2026-09 | Workbook Calc!C3 (calculated) | H |
| Latest 12-month rolling correlation | 0.330 (33.0%) | correlation coefficient | 12 months to 2026-09-30 | Workbook Calc!F66 (calculated) | H |
| Every Calc cell is a formula | Yes (366/366) | yes/no | n/a | openpyxl scan of the workbook | H |
| Any input values estimated or interpolated | No | yes/no | n/a | Inputs tab | H |

### 2. Sources used
- stock-data `get_price_history` (Yahoo Finance): 1 call (MSFT, 10y, 1mo)
- stock-data `get_macro_series` (FRED DGS10): 1 call (monthly, end-of-period, start 2021-08-15)
- Skill `financial-analysis:xlsx-author`: loaded once
- ToolSearch: 1 call
- Python/openpyxl and LibreOffice (local, for building and recalculating the workbook): no external data

### 3. Estimates and gaps
- **Window:** "Last 5 years" means 61 month-ends from 2021-09-30 to 2026-09-30, which gives 60 monthly changes. I left out October 2026 because the month isn't finished (data runs to 2026-10-15).
- **Dates:** each row is labelled with the calendar month-end. The values themselves are from the last trading day of the month (the Yahoo monthly bar close, and FRED's last value in the month). For months ending on a weekend or holiday, the actual observation date is a day or two earlier.
- **Adjusted prices:** these are Yahoo's split- and dividend-adjusted closes as of retrieval (2026-10-15). They will shift slightly as future dividends are paid, which affects the price levels but barely changes the returns.
- **Yield change:** measured in percentage points (a simple difference), not as a percentage change.
- **Rolling window:** the trailing 12 monthly pairs. The first value is at 2022-09-30.
- **Pearson correlation:** calculated with Excel's `CORREL` on simple (not log) returns.
- **September 2026 yield:** the 10-year yield of 5.29% on 2026-09-30 is a 54-basis-point jump from August. I took it from FRED as reported and couldn't check it independently, so that row's confidence is M.
- **Nothing was interpolated or estimated:** neither series had gaps in the window.
- **Output location:** the skill says to write to `./out/`, so I saved the file in `out/` inside the run folder.
- **Cached values:** the delivered file comes straight from openpyxl, so it has formulas but no stored results until it's opened. Excel recalculates when the file opens, and the values above come from a LibreOffice recalculation of a copy.

### 4. Freshness
- Latest market price used: MSFT adjusted close on 2026-09-30 (512.90 USD); the 10-year yield on 2026-09-30 (5.29%). The FRED series was last updated 2026-10-13.
- Latest financial reporting period used: N/A (no company financials used).

## Run log
| Tool | Calls | Notes |
|---|---|---|
| Bash | 6 | read rules/prompt; date -u (x2); environment check; build + LibreOffice recalc + verification; |
| Skill | 1 | financial-analysis:xlsx-author |
| ToolSearch | 1 | "select:mcp__remote-devices__stock-data__get_price_history,mcp__remote-devices__stock-data__get_macro_series" |
| mcp__remote-devices__stock-data__get_price_history | 1 | MSFT, 10y, 1mo |
| mcp__remote-devices__stock-data__get_macro_series | 1 | DGS10, m, eop |
| Write | 2 | _work/build.py, transcript.md |

Files delivered:
- /home/claude/results/2026-10-13/runs/FA-12/B/out/MSFT_10Y_correlation.xlsx
- /home/claude/results/2026-10-13/runs/FA-12/B/transcript.md
- Build script: /home/claude/results/2026-10-13/runs/FA-12/B/_work/build.py (recalculated check copy in _work/recalc/)
