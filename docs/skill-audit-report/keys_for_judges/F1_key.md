# F1 answer key: MSFT_model.xlsx planted errors

Fixture: `/home/claude/results/2026-10-13/fixtures/MSFT_model.xlsx`
Sheets: Assumptions, IS, BS, Schedules, CFS, Valuation. Columns B-E = FY2023A-FY2026A, F-J = FY2027E-FY2031E.
Workbook recalculated with LibreOffice (433 formulas, 0 formula errors); cached values are present.

## Planted errors

| ID | Sheet | Cell | What's wrong | Correct value / formula |
|----|-------|------|--------------|-------------------------|
| D1 | IS | D6 | FY2025 revenue hardcode is 304,262, which is 8% above reported (281,724 x 1.08 = 304,261.92, rounded). Inflates FY2025 gross profit, operating income and net income (NI shows 124,370 vs reported 101,832) and FY2025/FY2026 growth memo. | 281,724 |
| D2 | Valuation | B5 | Diluted shares = 7,472 (FY2023 weighted-average diluted count) instead of the latest. Market cap shows 4,060,658 instead of 4,050,333; EV 4,014,802 instead of 4,013,784. | 7,453 (FY2026 weighted-average diluted shares, 10-K) |
| D3 | BS | E6 | FY2026 cash = 30,242 (the FY2025 value) instead of reported 20,935. Does not break the check: historical "Other current assets" (BS!E10) is a residual of reported total current assets, so it absorbs the 9,307 difference; the CFS FY2026 FX/other residual (CFS!E24) absorbs it too. Opening cash for projections is overstated by 9,307 every year (e.g., FY2027 cash 50,135 vs 40,828) and FY2026 net debt / EV are off. | 20,935 |
| M1 | BS | G11 | FY2028 total current assets `=SUM(G6:G7,G9:G10)` skips accounts receivable (row 8). Result 188,514 vs 294,593; total assets understated by 106,078, so the Checks row shows -106,078 in FY2028 only. | `=SUM(G6:G10)` (= 294,592.6) |
| M2 | IS | H6 | FY2029 revenue is a typed constant 491,596.24977 (equal to the formula result) instead of a formula, so it no longer responds to FY2027-FY2029 growth assumptions or to FY2028 revenue. | `=G6*(1+Assumptions!H6)` |
| M3 | BS | I28 | FY2030 retained earnings & other equity `=H28+IS!H16+CFS!I8+CFS!I19+CFS!I20` adds prior-year (FY2029) net income instead of FY2030. Equity understated by 22,899 (213,244 - 190,345); Checks row (BS row 32, formula intact) shows 22,899 in FY2030 and FY2031. | `=H28+IS!I16+CFS!I8+CFS!I19+CFS!I20` (= 998,840.9) |
| M4 | Schedules | J9 | FY2031 D&A `=J8` references the capex row instead of beginning PP&E x D&A rate. Shows 152,788 vs 91,206; FY2031 PP&E and CFS D&A add-back wrong (no balance break, since both sides move together). | `=J7*Assumptions!J18` (= 91,206.2) |

## Checks row after planting (BS row 32, FY2023A-FY2031E)

0, 0, 0, 0, 0, -106,078.473 (FY2028, from M1), 0, 22,899.499 (FY2030, from M3), 22,899.499 (FY2031, M3 carried forward).
In the clean pre-plant model every year was 0.

## Historical data used (stock-data get_financials, MSFT, SEC XBRL, USD mm)

| Item | FY2023 | FY2024 | FY2025 | FY2026 |
|------|-------:|-------:|-------:|-------:|
| Revenue | 211,915 | 245,122 | 281,724 | 331,839 |
| Cost of revenue | 65,863 | 74,114 | 87,831 | 106,374 |
| R&D | 27,195 | 29,510 | 32,488 | 35,562 |
| Total operating expenses | 57,529 | 61,575 | 65,365 | 70,228 |
| Operating income | 88,523 | 109,433 | 128,528 | 155,237 |
| Interest expense | 1,968 | 2,935 | 2,385 | 3,051 |
| Pretax income | 89,311 | 107,787 | 123,627 | 165,934 |
| Income tax | 16,950 | 19,651 | 21,795 | 32,185 |
| Net income | 72,361 | 88,136 | 101,832 | 133,749 |
| Diluted shares (mm) | 7,472 | 7,469 | 7,465 | 7,453 |
| Cash | 34,704 | 18,315 | 30,242 | 20,935 |
| Short-term investments | 76,558 | 57,228 | 64,323 | 55,908 |
| Receivables | 48,688 | 56,924 | 69,905 | 80,876 |
| Inventory | 2,500 | 1,246 | 938 | 1,397 |
| Total current assets | 184,257 | 159,734 | 191,131 | 207,710 |
| PP&E, net | 95,641 | 135,591 | 204,966 | 313,076 |
| Goodwill | 67,886 | 119,220 | 119,509 | 119,651 |
| Intangibles | 9,366 | 27,597 | 22,604 | 18,609 |
| Total assets | 411,976 | 512,163 | 619,003 | 758,376 |
| Accounts payable | 18,095 | 21,996 | 27,724 | 42,416 |
| Current portion of LT debt | 5,247 | 2,249 | 2,999 | 9,227 |
| Total current liabilities | 104,149 | 125,286 | 141,218 | 168,825 |
| Long-term debt | 41,990 | 42,688 | 40,152 | 31,067 |
| Total liabilities | 205,753 | 243,686 | 275,524 | 315,989 |
| Stockholders' equity | 206,223 | 268,477 | 343,479 | 442,387 |
| Operating cash flow | 87,582 | 118,548 | 136,162 | 182,935 |
| Capex | 28,107 | 44,477 | 64,551 | 115,948 |
| Stock-based comp | 9,611 | 10,734 | 11,974 | 12,405 |
| Investing cash flow | -22,680 | -96,970 | -72,599 | -139,500 |
| Financing cash flow | -43,935 | -37,757 | -51,699 | -52,546 |
| Dividends paid | 19,800 | 21,771 | 24,082 | 26,445 |
| Share repurchases | 22,245 | 17,254 | 18,420 | 22,271 |

FY2022 cash (FY2023 beginning cash): 13,931. Share price: 543.45 (get_quote, fetched 2026-10-14 03:54 UTC).

## Defaults / modelling choices (not errors)

- "Latest" diluted shares = FY2026 weighted-average diluted shares from the 10-K (7,453), entered as a hardcode in the valuation block; the FY2026 period-end shares outstanding (7,427) was not used.
- SG&A (IS row 10) = total operating expenses less R&D; other income, net (row 13) = pretax less operating income plus interest expense (derived hardcodes, blue).
- D&A is not reported by the data source: historical D&A left blank; projected D&A = beginning PP&E x 15% on Schedules, used for PP&E and the CFS add-back; D&A is treated as embedded in cost of revenue / opex on the IS (so D&A changes do not move net income).
- Historical "other" lines (other current assets, other LT assets, other current/LT liabilities, other operating/investing/financing, FX & other) are formulas: reported totals less reported components. Historical totals are blue inputs; projected totals are SUM formulas.
- Equity is a single line ("Retained earnings & other equity", BS row 28) because the source reports only total equity; projected roll-forward = prior + NI + SBC + dividends (negative) + buybacks (negative).
- Projection assumptions (Assumptions tab): growth 15/14/13/12/11%, COGS 32%, R&D 10.5%, SG&A 10%, interest 5% on beginning debt, other income 3,000/yr, tax 19%, DSO 89, DIO 5, DPO 145, SBC 3.7%, capex 33/31/29/27/25% of revenue, D&A 15% of beginning PP&E, payout 20%, buybacks 22,000/yr, net debt repayment 5,000/yr; STI, other current assets, goodwill, intangibles, other LT items and current debt held flat.
- Valuation net debt uses FY2026 balance sheet (debt less cash and short-term investments); EV/Revenue shown on FY2026A and FY2027E revenue.
- Side effects of D1 visible internally: FY2025 revenue growth memo 24.1% and FY2026 9.1% (vs 14.9%/17.8% correct). D3 also changes the FY2026 historical residuals BS!E10 and CFS!E24.
