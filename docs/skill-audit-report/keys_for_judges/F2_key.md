# F2 answer key: quarterly_export.csv

Fixture: `/home/claude/results/2026-10-13/fixtures/quarterly_export.csv`
Source: stock-data MCP `get_financials` (income statement, quarterly; SEC XBRL), pulled 2026-10-13. USD millions.

## Shape
- Header: `ticker,period_end,fiscal_label,metric,value,notes` (the spec's five columns plus the required `notes` column).
- 100 data rows (lines 2-101; the header is line 1). The clean dataset is 96 rows: 4 tickers x 8 quarters x 3 metrics. The extra 4 are 3 exact duplicates and 1 near-duplicate.
- Line endings are CRLF (written by Python's csv module). Rows are ordered by ticker (GOOGL, AMZN, META, MSFT), then period, then metric (revenue, operating_income, net_income). Each duplicate sits directly below its original.
- Row numbers below are **file line numbers** (header = line 1). Data-row index = line - 1.

## Quarters covered (last 8 reported as of 2026-10-13)
- GOOGL, AMZN, META: FY2024Q3-FY2026Q2 (fiscal = calendar year), period_end 2024-09-30 to 2026-06-30.
- MSFT: FY2025Q1-FY2026Q4 (June fiscal year), same period_end dates 2024-09-30 to 2026-06-30. `fiscal_label` uses Microsoft's own fiscal labels.
- Q4 values (calendar Q4 for GOOGL/AMZN/META, FY Q4 = June quarter for MSFT) were **derived by the tool** as annual minus Q1-Q3; they were not reported as standalone quarters in XBRL. No EPS or share data is used in this fixture.

## Perturbations

### 1. Mixed date formats (all rows)
`period_end` uses one of three formats chosen at random per row: ISO `2026-06-30` (30 rows), US `06/30/2026` (38 rows), `30-Jun-26` (32 rows). The underlying date is always correct.

### 2. Ticker casing and whitespace (all rows)
Random variants per row, e.g. `GOOGL`, ` googl`, `Googl `, `googl`, `GOOGL `; `amzn`, ` Amzn`, `AMZN `, `amzn `; `Meta `, `meta`, ` META`, `meta `; `msft `, ` Msft`, `MSFT `, `msft`. All should normalize to GOOGL/AMZN/META/MSFT.

### 3. Values as text with `$` and thousands separators
32 of 100 rows (about a third) are written like `"$88,268"` (quoted because of the comma). The rest are plain numbers. The near-duplicate is `31652.6`, the only decimal value.

### 4. Duplicates
| Type | Lines | Key | Values |
|---|---|---|---|
| Exact duplicate | 6 & 7 | GOOGL FY2024Q4 operating_income | 30972 / 30972 (identical rows, including notes) |
| Exact duplicate | 47 & 48 | AMZN FY2026Q1 net_income | 30255 / 30255 |
| Exact duplicate | 83 & 84 | MSFT FY2025Q3 revenue | 70066 / 70066 |
| Near-duplicate | 80 & 81 | MSFT FY2025Q2 (period_end 2024-12-31) operating_income | line 80 `31653` (correct, date `31-Dec-24`, ticker `msft`); line 81 `31652.6` (date `12/31/2024`, ticker `MSFT`). These differ only by rounding; keep one and use 31,653. |

### 5. `notes` column
Notes are random and carry no information: blanks, numbers (`1`, `2`, `3`, `0.5`, `12.5`) and text (`10-Q`, `10-K`, `XBRL`, `n/a`, `prelim`, `see filing`, `ok`, `FY`). They are not correlated with any perturbation. One `prelim` note that happened to land on a perturbed row (line 39) was changed to `10-Q`.

### 6. META in thousands instead of millions (2 quarters, all 3 metrics each)
| Line | Quarter | Metric | Written | Correct (USD mm) |
|---|---|---|---|---|
| 55 | META FY2024Q4 (2024-12-31) | revenue | $48,385,000 | 48,385 |
| 56 | META FY2024Q4 | operating_income | $23,364,000 | 23,364 |
| 57 | META FY2024Q4 | net_income | $20,838,000 | 20,838 |
| 64 | META FY2025Q3 (2025-09-30) | revenue | $51,242,000 | 51,242 |
| 65 | META FY2025Q3 | operating_income | 20535000 | 20,535 |
| 66 | META FY2025Q3 | net_income | 2709000 | 2,709 |

Trap: META FY2025Q3 net income really is only $2,709mm (about $18.95bn of income tax expense that quarter, a one-time charge). The x1000 is the perturbation; the low level is real. Don't "fix" it to a value near operating income.

### 7. Wrong but plausible values (+/-12%, different tickers)
| Line | Key | Written | Correct | Error |
|---|---|---|---|---|
| 11 | GOOGL FY2025Q1 (2025-03-31) net_income | 30395 | 34,540 | -12.0% |
| 39 | AMZN FY2025Q3 (2025-09-30) revenue | $201,789 | 180,169 | +12.0% |

## Clean reference data (USD millions)
| ticker | fiscal_label | period_end | revenue | operating_income | net_income |
|---|---|---|---:|---:|---:|
| GOOGL | FY2024Q3 | 2024-09-30 | 88,268 | 28,521 | 26,301 |
| GOOGL | FY2024Q4 | 2024-12-31 | 96,469 | 30,972 | 26,536 |
| GOOGL | FY2025Q1 | 2025-03-31 | 90,234 | 30,606 | 34,540 |
| GOOGL | FY2025Q2 | 2025-06-30 | 96,428 | 31,271 | 28,196 |
| GOOGL | FY2025Q3 | 2025-09-30 | 102,346 | 31,228 | 34,979 |
| GOOGL | FY2025Q4 | 2025-12-31 | 113,829 | 35,934 | 34,455 |
| GOOGL | FY2026Q1 | 2026-03-31 | 109,896 | 39,696 | 62,578 |
| GOOGL | FY2026Q2 | 2026-06-30 | 119,796 | 40,770 | 112,193 |
| AMZN | FY2024Q3 | 2024-09-30 | 158,877 | 17,411 | 15,328 |
| AMZN | FY2024Q4 | 2024-12-31 | 187,792 | 21,203 | 20,004 |
| AMZN | FY2025Q1 | 2025-03-31 | 155,667 | 18,405 | 17,127 |
| AMZN | FY2025Q2 | 2025-06-30 | 167,702 | 19,171 | 18,164 |
| AMZN | FY2025Q3 | 2025-09-30 | 180,169 | 17,422 | 21,187 |
| AMZN | FY2025Q4 | 2025-12-31 | 213,386 | 24,977 | 21,192 |
| AMZN | FY2026Q1 | 2026-03-31 | 181,519 | 23,852 | 30,255 |
| AMZN | FY2026Q2 | 2026-06-30 | 200,606 | 27,461 | 62,647 |
| META | FY2024Q3 | 2024-09-30 | 40,589 | 17,350 | 15,688 |
| META | FY2024Q4 | 2024-12-31 | 48,385 | 23,364 | 20,838 |
| META | FY2025Q1 | 2025-03-31 | 42,314 | 17,555 | 16,644 |
| META | FY2025Q2 | 2025-06-30 | 47,516 | 20,441 | 18,337 |
| META | FY2025Q3 | 2025-09-30 | 51,242 | 20,535 | 2,709 |
| META | FY2025Q4 | 2025-12-31 | 59,893 | 24,745 | 22,768 |
| META | FY2026Q1 | 2026-03-31 | 56,311 | 22,872 | 26,773 |
| META | FY2026Q2 | 2026-06-30 | 60,801 | 18,775 | 15,848 |
| MSFT | FY2025Q1 | 2024-09-30 | 65,585 | 30,552 | 24,667 |
| MSFT | FY2025Q2 | 2024-12-31 | 69,632 | 31,653 | 24,108 |
| MSFT | FY2025Q3 | 2025-03-31 | 70,066 | 32,000 | 25,824 |
| MSFT | FY2025Q4 | 2025-06-30 | 76,441 | 34,323 | 27,233 |
| MSFT | FY2026Q1 | 2025-09-30 | 77,673 | 37,961 | 27,747 |
| MSFT | FY2026Q2 | 2025-12-31 | 81,273 | 38,275 | 38,458 |
| MSFT | FY2026Q3 | 2026-03-31 | 82,886 | 38,398 | 31,778 |
| MSFT | FY2026Q4 | 2026-06-30 | 90,007 | 40,603 | 35,766 |

## Defaults / notes
- The "last 8 reported quarters" are taken as of 2026-10-13. Calendar Q3 2026 results were not yet reported, so the latest quarter is the one ending 2026-06-30 for all four tickers.
- The near-duplicate is placed right after its original but uses a different date format and ticker casing, so it is the same key with a different surface form.
- Generated with Python `random.seed(20261013)`.
