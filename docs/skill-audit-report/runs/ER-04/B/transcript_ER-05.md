# Transcript: ER-05 (arm B)

- **Start:** 2026-10-14 07:56:33 UTC (`date -u`)
- **End:** 2026-10-14 08:05:58 UTC (`date -u`)

## Final reply to the user

I've built the Task 2 financial model for AMD: `AMD_Financial_Model_2026-10-14.xlsx` in the run folder. It has 4 historical years (FY2022A–FY2025A) and 5 projected years (FY2026E–FY2030E). Every integrity check passes, including the balance sheet balancing in all nine years. In the base case, FY2026E revenue is USD 49,476 million with a 17.3% GAAP operating margin.

**What's in the workbook**
- **Notes:** sources, the color legend, and data caveats.
- **Revenue Model:** nine sub-product rows across Data Center, Client, Gaming and Embedded, each with segment totals, % of total and YoY growth. A separate block splits revenue across nine countries/regions, grouped into three. Product and geography totals tie.
- **Income Statement:** about 50 lines. It includes amortization of acquired intangibles split between cost of sales and opex, EBITDA, adjusted EBITDA, an approximate non-GAAP operating income and EPS, and basic/diluted EPS.
- **Cash Flow:** the full statement, with FY2025 discontinued operations broken out and AMD-defined free cash flow.
- **Balance Sheet:** about 30 line items, working-capital driver rows (DSO, DIO, DPO and others), a balance check, and memo ratios (net cash, D/E, current ratio, ROIC).
- **Scenarios:** Bull/Base/Bear drivers for each sub-product's growth, cost of sales, R&D, MG&A and capex. One selector cell (`ScenarioSel`) switches the whole model. An output table holds snapshots of all three cases plus a live column.
- **DCF Inputs:** unlevered free cash flow for FY2026E–FY2030E, terminal-year metrics, and the latest market cap / EV bridge, ready for Task 3.
- **Quarterly Hist:** eight quarters (Q3 FY2024–Q2 FY2026) and a FY2026E calibration bridge.
- **Checks:** balance, cash tie-out, revenue ties across tabs, and every historical figure tied back to the reported number.

**How it was built**
- **Historicals:**
  - SEC XBRL data, via the stock-data tool.
  - Full statements from AMD's Q4 earnings releases for FY2023, FY2024 and FY2025.
  - Every reported total for revenue, gross profit, operating income, net income, EPS, cash flow from operations/investing/financing, total assets, current assets/liabilities and equity ties exactly.
- **Free cash flow definition:** I resolved the gap flagged in Task 1. FY2025 operating cash flow of USD 7,709 million includes USD 1,216 million from discontinued operations (the ZT Systems manufacturing business). Continuing operating cash flow is USD 6,493 million; less USD 974 million of capex, that gives AMD's USD 5,519 million free cash flow.
- **FY2026E anchor:** H1 actuals (USD 21,789 million) plus Q3 guidance (about USD 13,000 million) imply Q4 FY2026E of about USD 14,686 million.

**Scenario results (FY2030E)**

| | Revenue (USD M) | GAAP operating margin | Diluted EPS (USD) | Cumulative FCF FY2026E–FY2030E (USD M) |
|---|---|---|---|---|
| Bull | 157,286 | 35.7% | 29.04 | 151,110 |
| Base | 114,511 | 31.4% | 18.69 | 109,248 |
| Bear | 65,406 | 21.0% | 7.29 | 58,930 |

The base case is more conservative than management's long-term targets. It implies a Data Center CAGR of about 40%, against the more than 60% management has targeted.

**Things to know before using it**
- **Estimated splits:** the sub-segment revenue split (EPYC / Instinct / networking, and so on) and the whole geographic split are my estimates. AMD does not disclose the former, and I couldn't retrieve the 10-K's country table. Both are marked in blue as inputs.
- **OpenAI warrant:** the up-to-160-million-share warrant is not in the share count.

Task 3 (valuation) is the next step. Its inputs are on the DCF Inputs tab.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Revenue FY2022 | 23,601 | USD millions | FY2022 (FYE 2022-12-31) | stock-data get_financials (SEC XBRL, 10-K); AMD Q4'23 EX-99.1 (2024-01-30) | H |
| Gross profit FY2022 | 10,603 | USD millions | FY2022 | stock-data get_financials; AMD EX-99.1 (2024-01-30) | H |
| Operating income FY2022 | 1,264 | USD millions | FY2022 | stock-data get_financials; AMD EX-99.1 (2024-01-30) | H |
| Net income FY2022 | 1,320 | USD millions | FY2022 | stock-data get_financials; AMD EX-99.1 (2024-01-30) | H |
| Diluted EPS FY2022 | 0.84 | USD | FY2022 | stock-data get_financials | H |
| Operating cash flow FY2022 | 3,565 | USD millions | FY2022 | stock-data get_financials; AMD EX-99.1 (2024-01-30) | H |
| Capex FY2022 | 450 | USD millions | FY2022 | stock-data get_financials | H |
| Total assets FY2022 | 67,580 | USD millions | 2022-12-31 | stock-data get_financials; AMD EX-99.1 (2024-01-30) | H |
| Stockholders' equity FY2022 | 54,750 | USD millions | 2022-12-31 | stock-data get_financials | H |
| Revenue FY2023 | 22,680 | USD millions | FY2023 (FYE 2023-12-30) | stock-data get_financials; AMD Q4'24 EX-99.1 (ir.amd.com) | H |
| Gross profit FY2023 | 10,460 | USD millions | FY2023 | stock-data get_financials | H |
| Operating income FY2023 | 401 | USD millions | FY2023 | stock-data get_financials | H |
| Net income FY2023 | 854 | USD millions | FY2023 | stock-data get_financials | H |
| Diluted EPS FY2023 | 0.53 | USD | FY2023 | stock-data get_financials | H |
| Operating cash flow FY2023 | 1,667 | USD millions | FY2023 | stock-data get_financials | H |
| Capex FY2023 | 546 | USD millions | FY2023 | stock-data get_financials | H |
| Total assets FY2023 | 67,885 | USD millions | 2023-12-30 | stock-data get_financials | H |
| Stockholders' equity FY2023 | 55,892 | USD millions | 2023-12-30 | stock-data get_financials | H |
| Revenue FY2024 | 25,785 | USD millions | FY2024 (FYE 2024-12-28) | stock-data get_financials (10-K filed 2025-02-05) | H |
| Gross profit FY2024 | 12,725 | USD millions | FY2024 | stock-data get_financials | H |
| Operating income FY2024 | 1,900 | USD millions | FY2024 | stock-data get_financials | H |
| Net income FY2024 | 1,641 | USD millions | FY2024 | stock-data get_financials | H |
| Diluted EPS FY2024 | 1.00 | USD | FY2024 | stock-data get_financials | H |
| Operating cash flow FY2024 | 3,041 | USD millions | FY2024 | stock-data get_financials | H |
| Capex FY2024 | 636 | USD millions | FY2024 | stock-data get_financials | H |
| Total assets FY2024 | 69,226 | USD millions | 2024-12-28 | stock-data get_financials | H |
| Stockholders' equity FY2024 | 57,568 | USD millions | 2024-12-28 | stock-data get_financials | H |
| Revenue FY2025 | 34,639 | USD millions | FY2025 (FYE 2025-12-27) | stock-data get_financials (10-K filed 2026-02-04) | H |
| Gross profit FY2025 | 17,152 | USD millions | FY2025 | stock-data get_financials | H |
| Operating income FY2025 | 3,694 | USD millions | FY2025 | stock-data get_financials | H |
| Net income FY2025 | 4,335 | USD millions | FY2025 | stock-data get_financials | H |
| Diluted EPS FY2025 | 2.65 | USD | FY2025 | stock-data get_financials | H |
| Operating cash flow FY2025 | 7,709 (continuing ops 6,493) | USD millions | FY2025 | stock-data get_financials; AMD Q4'25 earnings release (ir.amd.com, 2026-02-03) | H |
| Capex FY2025 | 974 | USD millions | FY2025 | stock-data get_financials | H |
| Total assets FY2025 | 76,926 | USD millions | 2025-12-27 | stock-data get_financials | H |
| Stockholders' equity FY2025 | 62,999 | USD millions | 2025-12-27 | stock-data get_financials | H |
| Number of historical years | 4 (FY2022A–FY2025A) | years | — | Model | H |
| Number of historical quarters | 8 (Q3 FY2024–Q2 FY2026) | quarters | through 2026-06-27 | Model (Quarterly Hist tab) | H |
| Balance sheet balances in every period | Yes (difference 0 in all 9 years, 4 historical + 5 projected) | yes/no | FY2022A–FY2030E | Model Checks tab (LibreOffice recalculation) | H |
| First projected year revenue (FY2026E, base) | 49,476 | USD millions | FY2026E | Model estimate | M |
| First projected year operating margin (FY2026E, base, GAAP) | 17.3 | % | FY2026E | Model estimate | M |

### 2. Sources used

| Tool / connector / website | Calls (this prompt) |
|---|---|
| stock-data get_financials (balance annual, cashflow annual, cashflow quarterly, balance quarterly) | 4 |
| WebFetch: sec.gov (FY2025 10-K, offset read; no financial tables reached) | 1 |
| WebFetch: ir.amd.com (Q4/FY2025 release; Q4/FY2023 EX-99.1; Q4/FY2024 EX-99.1) | 3 |
| WebSearch (locating FY2024 and FY2023 earnings releases) | 2 |
| Data reused from the ER-04 turn: stock-data get_quote, get_filings, get_financials (income annual and quarterly), Q2 FY2026 10-Q and release | 0 new calls |
| LibreOffice (headless recalculation, run locally) | 4 runs |
| Skill: financial-analysis:xlsx-author | 1 |

### 3. Estimates and gaps

- **Estimated sub-product revenue splits (historical):** EPYC / Instinct / networking-other; desktop / notebook; semi-custom / Radeon; FPGA / embedded x86. AMD does not disclose these. For example, I put Instinct at about USD 5,000 million in FY2024 and USD 6,500 million in FY2025. Segment totals are reported and tie exactly.
- **Geographic split:** all estimated. Shares are blue inputs; I couldn't retrieve the 10-K country table. Confidence L.
- **Q3 and Q4 FY2024 quarterly segment revenue:** from model knowledge. They sum to the reported quarterly totals.
- **Quarterly total debt:** for Q3 FY2025–Q2 FY2026 it is short-term plus long-term from XBRL. Q1 and Q2 FY2025 used the XBRL long-term figure only.
- **Presentation choices:**
  - FY2022 and FY2023 MG&A are shown net of licensing gains (102 and 34) to match the FY2024+ presentation.
  - Related-party receivables and payables, right-of-use assets and equity-method investments are folded into "other" lines.
  - FY2023 balance sheet uses the recast receivables (4,323).
- **Projection defaults (base case):**
  - Sub-product growth: EPYC +40% in FY2026E, decelerating to +10% by FY2030E. Instinct +140%, then +90%, +45%, +25%, +15%.
  - Cost of sales excluding amortization: 45.5% of revenue, falling to 44.0%. R&D 21.5% falling to 15.5%. MG&A 11.5% falling to 8.0%.
  - D&A 2.0% of revenue. Capex 5.0% falling to 3.5%. SBC 4.0% falling to 3.0%.
  - Tax rate 13% in FY2026E, then 15%. Interest at 4.0% of average debt; interest income at 3.5% of beginning cash plus short-term investments.
  - DSO 62 days; DIO 150 falling to 115; DPO 70.
  - Amortization of intangibles USD 2,100 million falling to USD 1,300 million, 45% of it in cost of sales.
  - Buybacks 50% of FCF. Strategic investments USD 3,000 million in FY2026E, reflecting the post-Q2 commitment of up to USD 5.0 billion.
  - Debt, goodwill, short-term investments and deferred taxes held flat. No M&A.
  - Diluted shares 1,660 million in FY2026E, growing 0.5% a year. The OpenAI warrant is excluded.
- **Bull and bear cases:** each driver has its own values on the Scenarios tab. The scenario output table is a static snapshot from full-model recalculation under each case; the Live column updates with the selector.
- **Approximate non-GAAP figures:** EBIT plus amortization plus SBC plus restructuring. This misses inventory and acquisition adjustments: FY2025 approximation is USD 7,586 million against USD 7,768 million reported.
- **Cash basis:** historical cash flow ending cash includes restricted cash (24 in FY2024, 17 in FY2025). Projections roll forward from balance-sheet cash.
- **Defaults chosen:**
  - Five-year projection horizon (FY2026E–FY2030E).
  - Base case selected in the file.
  - File saved in the run folder rather than `./out/`, per the session rules.
  - File delivered after LibreOffice recalculation, so cached values are present.
  - Times New Roman font.

### 4. Freshness

- **Latest market price:** USD 605.53 at 2026-10-14 07:49 UTC (stock-data get_quote, on the DCF Inputs tab).
- **Latest financial reporting period:** Q2 FY2026, quarter ended 2026-06-27 (10-Q filed 2026-08-05). The latest annual period is FY2025 (10-K filed 2026-02-04).

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 7 | `date -u` plus prompt read; read task2 reference; openpyxl/LibreOffice check; scenario recalc (failed, style bug); scenario recalc rerun; final build plus verification; copy to run folder plus `date -u` |
| Skill | 1 | financial-analysis:xlsx-author |
| mcp__remote-devices__stock-data__get_financials | 4 | balance annual; cashflow annual; cashflow quarterly; balance quarterly |
| WebFetch | 4 | FY2025 10-K (offset 100000); Q4/FY2025 release; Q4/FY2023 EX-99.1; Q4/FY2024 EX-99.1 |
| WebSearch | 2 | FY2024 and FY2023 Q4 release URLs |
| Write | 2 | build script (scratchpad); this transcript. The recalc helper script was written through a Bash heredoc. |
| Edit | 1 | build script style fix |
| ToolSearch | 0 | stock-data tools already loaded |

**Files delivered:** /home/claude/results/2026-10-13/runs/ER-04/B/AMD_Financial_Model_2026-10-14.xlsx
