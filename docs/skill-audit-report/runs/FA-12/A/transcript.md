# Transcript FA-12 / Arm A

- Start: Fri Oct 16 03:35:07 UTC 2026
- End: Fri Oct 16 03:38:34 UTC 2026

## Final reply to user

I built the workbook: `/home/claude/results/2026-10-13/runs/FA-12/A/out/MSFT_vs_10Y_correlation.xlsx` (relative: `out/MSFT_vs_10Y_correlation.xlsx`).

It has four tabs:
- **Summary**: the headline figures, all linked by formula. It has two charts. The first is a line chart of the 12-month rolling correlation, with a dashed line for the full-period correlation. The second is a scatter of monthly MSFT return against the monthly change in yield.
- **Inputs**: 61 month-ends from 2021-09-30 to 2026-09-30. The inputs are in blue: MSFT adjusted close from Yahoo Finance and the 10-year Treasury yield from the U.S. Treasury Daily Par Yield Curve. Each column has a row under its header saying where the data came from.
- **Calc**: every cell is a live formula. It covers the links to Inputs, the monthly return (`=B/B_prev-1`), the change in yield in percentage points, and the 12-month rolling `CORREL` (49 windows). It also has the full-period `CORREL` and some extra statistics: standard deviations, the slope of return against yield change, and the minimum and maximum of the rolling correlation.
- **Checks**: six TRUE/FALSE checks covering row counts, blanks, date order and that correlations fall within [-1, 1]. All six pass.

I recalculated the workbook in LibreOffice and it shows no formula errors. The workbook is set to recalculate fully when opened.

**Results:**
- Over the full period, MSFT returns moved weakly against yield changes: the correlation is -0.257.
- Each +1 percentage point (pp) rise in the 10-year yield went with about a -7.2% MSFT return in the same month.
- The 12-month rolling correlation varied a lot, from -0.882 to +0.513. In the latest window (2025-10 to 2026-09) it was +0.330.

## Comparison Block

### 1. Key figures
| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| First month in data | 2021-09-30 | date | 2021-09 | Yahoo Finance MSFT history page; home.treasury.gov 2021 yield file (WebFetch) | H |
| Last month in data | 2026-09-30 | date | 2026-09 | Yahoo Finance MSFT history page; home.treasury.gov 2026 yield file (WebFetch) | H |
| Number of monthly rows | 61 (60 returns) | count | 2021-09-30 to 2026-09-30 | Workbook (Inputs/Calc) | H |
| First MSFT adjusted close | 270.57 | USD per share | 2021-09-30 | https://finance.yahoo.com/quote/MSFT/history/?frequency=1mo (WebFetch) | M |
| Last MSFT adjusted close | 512.90 | USD per share | 2026-09-30 | https://finance.yahoo.com/quote/MSFT/history/?frequency=1mo (WebFetch) | M |
| First 10-year yield | 1.5 (1.52) | % | 2021-09-30 | https://home.treasury.gov daily-treasury-rates.csv/2021 (WebFetch) | H |
| Last 10-year yield | 5.3 (5.29) | % | 2026-09-30 | https://home.treasury.gov daily-treasury-rates.csv/2026 (WebFetch) | M |
| Full-period correlation | -0.257 | correlation coefficient | 2021-10 to 2026-09 (60 months) | Workbook formula `CORREL` (checked in Python and LibreOffice) | M |
| Latest 12-month rolling correlation | 0.330 | correlation coefficient | 2025-10 to 2026-09 | Workbook formula `CORREL` (checked in Python and LibreOffice) | M |
| Every Calc cell a formula (yes/no) | Yes. Every data cell is a formula; the only non-formula cells are the text headers and labels | yes/no | N/A | Checked with openpyxl | H |
| Any inputs estimated or interpolated (yes/no, which) | No | yes/no | N/A | N/A | H |

### 2. Sources used
- WebFetch: 18 calls in total
  - home.treasury.gov Daily Par Yield Curve CSVs: 9 calls. All the yield data came from these. There was one call per year for 2021 to 2026. I re-fetched 2024 and 2025 because the first reads picked the first day of each month instead of the last. A second 2026 read cross-checked the month-end values.
  - finance.yahoo.com MSFT monthly history page: 2 calls. All the price data came from these. The first had the wrong date range; the second was correct.
  - query1.finance.yahoo.com chart API: 1 call, blocked by robots.txt
  - fred.stlouisfed.org: 5 calls (fredgraph.csv ×2, GS10.txt, DGS10.txt ×2). None of these were used. The CSVs came back as binary, GS10 is a monthly average rather than month-end, and the DGS10 text was cut off at 1968.
  - stooq.com: 1 call, blocked by robots.txt
- WebSearch: 1 call, MSFT monthly price history. No results were used.
- Bash curl to FRED, Yahoo, Stooq, Treasury, Nasdaq and Alpha Vantage: all blocked by the egress proxy (403).
- LibreOffice (local): recalculated a copy of the workbook to check the formulas.

### 3. Estimates and gaps
- **Window:** "last 5 years" means the 60 completed months from 2021-10 to 2026-09, with 2021-09-30 as the base month for the first return. October 2026 is a partial month and is left out.
- **Yield series:** I used the Treasury 10-year par yield on the last trading day of each month. This should match FRED DGS10 at month-end. I did not use FRED GS10, which is a monthly average.
- **Correlation measure:** Pearson correlation of simple monthly returns with the change in yield in percentage points. The rolling window is the trailing 12 months, so the first value is at 2022-09-30.
- **Unchecked Yahoo figures:** the adjusted closes are Yahoo's split- and dividend-adjusted values as of 2026-10-15. They will move a little as new dividends are paid. I could not compare them with a second price source because other sites were blocked. The adjusted close is a proxy for total return.
- **Values read by a summarising model:** I could not download the raw files, so all the inputs were extracted by WebFetch's summarising model. Two things support the extraction:
  - The two Yahoo pulls matched exactly where they overlapped.
  - The two 2026 Treasury pulls matched.
  - The 2021 to 2025 yields fit the published history I know of.

  Even so, I did not check the 2026 values against a second source (confidence M).
- **Dates:** the Inputs dates are the Treasury month-end trading days. Yahoo labels its monthly bars with the first of the month, and I matched them by month.
- **Not recalculated in the delivered file:** openpyxl stores no computed values, so the file is set to recalculate fully on open. I checked the figures in a separate LibreOffice-recalculated copy.
- **Data access:** the stock-data tools were turned off for this run.

### 4. Freshness
- **Latest market price used:** MSFT adjusted close on 2026-09-30, and the 10-year yield on 2026-09-30. The latest available values were 533.69 for MSFT (partial October bar) and 5.19% for the yield on 2026-10-14; neither was used.
- **Latest financial reporting period used:** N/A, since no company financials were used.

## Run log
- Bash: 8 calls
  - Read the rules, prompt and run folder: 1
  - Start time and creating _work: 1
  - curl data attempts: 1
  - Proxy status and host tests: 1
  - Tool and version check: 1
  - Build, LibreOffice recalculation and checks: 2
  - Final rebuild and end time: 1
- Skill: 1 (financial-analysis:xlsx-author)
- WebFetch: 18 calls (Treasury 9, Yahoo 3, FRED 5, Stooq 1)
- WebSearch: 1
- Write: 2 (_work/build.py, transcript.md), plus 1 more Bash call to fix this transcript
- Read: 1 (rendered PNG of the Summary page, to check the chart)
- ToolSearch: 0. Stock-data tools: not used.
- Delivered files:
  - /home/claude/results/2026-10-13/runs/FA-12/A/out/MSFT_vs_10Y_correlation.xlsx
  - /home/claude/results/2026-10-13/runs/FA-12/A/transcript.md
  - Build script: /home/claude/results/2026-10-13/runs/FA-12/A/_work/build.py
