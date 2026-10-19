# F3 key: MSFT_snapshot.pptx

Deck: `/home/claude/results/2026-10-13/fixtures/MSFT_snapshot.pptx` (6 slides, 16:9, built with pptxgenjs; slide 3 has a native clustered column chart with embedded data).
Point in time: end of Microsoft FY2025 (June 30, 2025). The deck has no planted errors. Every figure should match the sources below.

## Sources (all from the stock-data MCP tools, pulled 2026-10-13)
- `get_financials MSFT income annual`: FY2021–FY2025 revenue, operating income, diluted EPS
- `get_financials MSFT cashflow annual`: FY2024–FY2025 operating cash flow, capex (PaymentsToAcquirePropertyPlantAndEquipment), free cash flow (computed by the tool as OCF − capex)
- `get_financials MSFT balance annual`: FY2025 cash, short-term investments, current and long-term debt, shares outstanding (CommonStockSharesOutstanding = 7,434M)
- `get_price_history MSFT 2y 1d`: close on 2025-06-30 = $497.41 (raw close; adj_close 492.54 not used)

Raw inputs ($M): Revenue FY21 168,088 / FY22 198,270 / FY23 211,915 / FY24 245,122 / FY25 281,724. Operating income FY21 69,916 / FY22 83,383 / FY23 88,523 / FY24 109,433 / FY25 128,528. FY25 OCF 136,162; capex 64,551; FCF 71,611. FY24 capex 44,477; FCF 74,071. Debt: current 2,999 + long-term 40,152 = 43,151. Cash 30,242 + ST investments 64,323 = 94,565. Diluted EPS FY25 $13.64.

## Defaults and assumptions
- Market cap = $497.41 × 7,434M shares = $3,697,746M (shares outstanding from FY2025 10-K balance data, not diluted weighted shares of 7,465M).
- EV = market cap + total debt (no leases) − cash − short-term investments = $3,646,332M.
- FCF = OCF − capex (PP&E additions only; finance leases not deducted).
- P/E = price ÷ FY2025 diluted EPS. Using market cap ÷ net income ($101,832M) gives 36.3x instead of 36.5x. Both are reasonable; the deck uses price/EPS.
- Number formats are deliberately mixed: $B on slides 2–4, $M with commas on slide 5, unitless one-decimal values on the chart (in $B).

## Every number in the deck

| Slide | Exact text | Metric | Period |
|---|---|---|---|
| 1 | Fiscal year ended June 30, 2025 | Fiscal year-end date | FY2025 |
| 1 | Data as of 2025-06-30 | As-of date | 2025-06-30 |
| 2 | Key stats: FY2025 at a glance | Fiscal year label | FY2025 |
| 2 | $497.41 | Share price (close) | 2025-06-30 |
| 2 | Close, 2025-06-30 | Price date | 2025-06-30 |
| 2 | $3.70T | Market cap (497.41 × 7,434M = $3,697.7B) | 2025-06-30 |
| 2 | 7,434M shares outstanding | Common shares outstanding | FY2025 year-end |
| 2 | $281.7B | Revenue | FY2025 |
| 2 | Fiscal year to 6/30/25 | Period end | FY2025 |
| 2 | 14.9% | Revenue growth YoY (281,724 / 245,122 − 1 = 14.93%) | FY2025 vs FY2024 |
| 2 | vs. FY2024 $245.1B | Revenue | FY2024 |
| 2 | 45.6% | Operating margin (128,528 / 281,724 = 45.62%) | FY2025 |
| 2 | Op. income $128.5B | Operating income | FY2025 |
| 2 | $71.6B | Free cash flow (136,162 − 64,551 = 71,611) | FY2025 |
| 2 | $13.64 | Diluted EPS | FY2025 |
| 2 | FY2025 GAAP | Period label | FY2025 |
| 3 | FY2021–FY2025 (title) | Period range | FY2021–FY2025 |
| 3 | Chart: 168.1 / 198.3 / 211.9 / 245.1 / 281.7 | Revenue, $B | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 |
| 3 | Chart: 69.9 / 83.4 / 88.5 / 109.4 / 128.5 | Operating income, $B | FY2021–FY2025 |
| 3 | Axis: 0.0, 80.0, 160.0, 240.0, 320.0 | Value-axis gridlines ($ billions) | n/a |
| 3 | 13.8% | Revenue CAGR ((281,724 / 168,088)^(1/4) − 1 = 13.78%) | FY2021–FY2025 |
| 3 | 16.4% | Operating income CAGR ((128,528 / 69,916)^(1/4) − 1 = 16.44%) | FY2021–FY2025 |
| 3 | 45.6% | Operating margin | FY2025 |
| 3 | (FY2021: 41.6%) | Operating margin (69,916 / 168,088 = 41.59%) | FY2021 |
| 4 | 14.9% (badge and text) | Revenue growth YoY | FY2025 |
| 4 | $281.7B | Revenue | FY2025 |
| 4 | $245.1B | Revenue | FY2024 |
| 4 | 25.4% (badge and text) | FCF margin (71,611 / 281,724 = 25.42%) | FY2025 |
| 4 | $71.6B | Free cash flow | FY2025 |
| 4 | 30.2% | FCF margin (74,071 / 245,122 = 30.22%) | FY2024 |
| 4 | 45.1% | Capex growth YoY (64,551 / 44,477 − 1 = 45.13%) | FY2025 vs FY2024 |
| 4 | $64.6B (badge and text) | Capex | FY2025 |
| 4 | 22.9% of revenue | Capex / revenue (64,551 / 281,724 = 22.91%) | FY2025 |
| 5 | $497.41 (table and P/E card) | Share price | 2025-06-30 close |
| 5 | Share price (6/30/25 close) | Price date | 2025-06-30 |
| 5 | 7,434 | Shares outstanding (M) | FY2025 year-end |
| 5 | $3,697,746M | Market cap | 2025-06-30 |
| 5 | $43,151M | Total debt (2,999 + 40,152) | 2025-06-30 |
| 5 | ($94,565M) | Cash + short-term investments (30,242 + 64,323) | 2025-06-30 |
| 5 | $3,646,332M (table, EV/Revenue card, EV/FCF card) | Enterprise value | 2025-06-30 |
| 5 | $281,724M (table and EV/Revenue card) | Revenue | FY2025 |
| 5 | $71,611M (table and EV/FCF card) | Free cash flow | FY2025 |
| 5 | $13.64 (table and P/E card) | Diluted EPS | FY2025 |
| 5 | 36.5x | P/E (497.41 / 13.64 = 36.47x) | FY2025 |
| 5 | 12.9x | EV / Revenue (3,646,332 / 281,724 = 12.94x) | FY2025 |
| 5 | 50.9x | EV / FCF (3,646,332 / 71,611 = 50.92x) | FY2025 |
| 6 | June 30, 2025; FY2021–FY2024 | Filing periods | FY2021–FY2025 |
| 6 | June 30, 2025 ($497.41) | Closing price | 2025-06-30 |
| 6 | 7,434M | Shares outstanding | FY2025 year-end |
| 6 | $2,999M / $40,152M | Current / long-term debt | 2025-06-30 |
| 6 | $30,242M / $64,323M | Cash & equivalents / short-term investments | 2025-06-30 |
| 6 | $136,162M / $64,551M | Operating cash flow / PP&E additions | FY2025 |
| 6 | October 13, 2026 | Date compiled | n/a |
| 6 | Notes numbered 1–7 | List numbering (not data) | n/a |
| 2–6 | Footer "FY2025" and slide numbers 2–6 | Labels (not data) | n/a |

Cross-format equivalences (all consistent): $281.7B = $281,724M = 281.7 on the chart; $71.6B = $71,611M; $3.70T = $3,697,746M; op. income $128.5B = 128.5 on the chart.
