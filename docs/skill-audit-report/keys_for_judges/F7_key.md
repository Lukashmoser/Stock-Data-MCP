# F7 answer key: MSFT_quarterly_model.xlsx

Fixture: `/home/claude/results/2026-10-13/fixtures/MSFT_quarterly_model.xlsx`
Source: stock-data MCP `get_financials` (MSFT income statement, quarterly and annual; SEC XBRL) and `get_filings`, pulled 2026-10-13.

## Most recently reported quarter: FY2026Q4 (quarter ended 2026-06-30)
In the model this quarter is still an **estimate** (column J, marked "E").

| Line item | Reported actual | Model estimate (col J) | Actual vs. estimate |
|---|---:|---:|---:|
| Revenue ($mm) | **90,007** | 85,614 | +4,393 (+5.1%) |
| Gross profit ($mm) | **60,482** | 58,496 | +1,986 (+3.4%) |
| Operating income ($mm) | **40,603** | 39,305 | +1,298 (+3.3%) |
| Net income ($mm) | **35,766** | 32,230 | +3,536 (+11.0%) |
| Diluted EPS ($) | **4.80** (computed; see note) | 4.34 | +0.46 |
| Diluted shares (mm) | **7,453** (FY2026 annual weighted-average diluted; see note) | 7,423 | +30 |

Other derived actuals for FY2026Q4: cost of revenue 29,525; operating expenses 19,879; pretax income 44,047; income tax 8,281 (effective rate 18.8%); other income, net +3,444 (pretax minus operating income). Actual gross margin was 67.2% against a modeled 68.3%. Actual YoY revenue growth was 17.7% against a modeled 12.0%.

**Filing:** FY2026Q4 is the fiscal fourth quarter, so it was filed in the **10-K for FY2026 (period 2026-06-30), filed 2026-07-29**. Accession 0001193125-26-323660, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm. There is no 10-Q for this quarter.

**Q4 derivation note:** XBRL has no standalone fiscal-Q4 figures. The tool derives Q4 as FY2026 annual minus Q1-Q3 (e.g. revenue 331,839 - 77,673 - 81,273 - 82,886 = 90,007). It returns null EPS and null shares for Q4. Per instructions:
- Diluted shares = FY2026 annual weighted-average diluted shares, **7,453mm**.
- Diluted EPS = 35,766 / 7,453 = **$4.799, which rounds to $4.80**.
- Alternative: the implied Q4 share count is 4 x 7,453 - (7,466 + 7,460 + 7,445) = 7,441mm. That gives EPS of $4.807, which rounds to **$4.81**. Treat $4.80-$4.81 as acceptable. A Q4 EPS taken as annual EPS minus Q1-Q3 EPS gives 17.95 - 3.72 - 5.16 - 4.27 = $4.80.

## Model structure
- Tabs: `Quarterly IS`, `Annual Summary`, `Valuation`, `Assumptions`.
- **Actuals (A), 8 quarters:** FY2024Q4, FY2025Q1-Q4, FY2026Q1-Q3 (columns B-I, period ends 2024-06-30 to 2026-03-31).
- **Estimates (E), 5 quarters:** FY2026Q4, FY2027Q1-Q4 (columns J-N). Estimate columns are shaded grey.
- Labels follow Microsoft's fiscal year (FY ends June 30).
- 198 live formulas, recalculated with LibreOffice, 0 errors. Cached values are present.
- Actual inputs (blue) are revenue, cost of revenue, operating expenses, other income, income tax and diluted shares. Gross profit, operating income, pretax income, net income, margins, tax rate and EPS are formulas.

## Estimate rules as implemented (levers on the Assumptions tab)
- Revenue = same quarter last year x (1 + 12%).
- Gross margin = average of the 4 preceding quarters' GM. This is rolling, so later estimate quarters average in earlier estimates. GP = revenue x GM; COGS = revenue - GP.
- Operating expenses = same quarter last year x (1 + 6%).
- Tax rate = 18.0% of pretax income.
- Diluted shares = prior quarter x (1 - 0.3%). The first estimate quarter is based on the latest actual, FY2026Q3's 7,445mm.
- **Default (not in spec):** other income (expense), net = 0 in estimate quarters, so pretax = operating income. Historical other income is volatile; FY2026Q2 was +9,971.

## Key model outputs
| Quarter | Revenue | GM % | Opex | Op. income | Net income | Shares | EPS |
|---|---:|---:|---:|---:|---:|---:|---:|
| FY2026Q4E | 85,614 | 68.32% | 19,190 | 39,305 | 32,230 | 7,422.7 | 4.34 |
| FY2027Q1E | 86,994 | 68.26% | 16,609 | 42,773 | 35,074 | 7,400.4 | 4.74 |
| FY2027Q2E | 91,026 | 68.06% | 18,041 | 43,914 | 36,009 | 7,378.2 | 4.88 |
| FY2027Q3E | 92,832 | 68.07% | 18,720 | 44,472 | 36,467 | 7,356.1 | 4.96 |
| FY2027Q4E | 95,888 | 68.18% | 20,342 | 45,034 | 36,928 | 7,334.0 | 5.04 |

**Annual Summary:**
- FY2025A: revenue 281,724, net income 101,832, EPS 13.64. Ties to the 10-K.
- FY2026E (3A + 1E): revenue 327,446, net income 130,213, EPS 17.48. The reported FY2026 figures were revenue 331,839, net income 133,749, EPS 17.95.
- FY2027E: revenue 366,739, net income 144,478, EPS 19.61.
- Annual EPS = net income / average of quarterly diluted shares.

**Valuation:**
- NTM = FY2026Q4E-FY2027Q3E, the 4 quarters after the last actual, as of a model dated before the print.
- NTM EPS = $18.92. Target price = $18.92 x 30 = **$567.58**.

## Defaults and caveats
- The quarterly actual share counts for FY2024Q4 and FY2025Q4 are also null from the tool, so the model uses the FY2024 (7,469) and FY2025 (7,465) annual diluted shares. Cell comments in the workbook say so.
- Actual operating expenses = gross profit - operating income. The tool's OperatingExpenses tag is null before FY2025Q1; where it exists, it ties to GP - OI.
