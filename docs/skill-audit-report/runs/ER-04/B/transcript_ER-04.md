# Transcript: ER-04 (arm B)

- **Start:** 2026-10-14 07:49:13 UTC (`date -u`)
- **End:** 2026-10-14 07:55:50 UTC (`date -u`)

## Final reply to the user

I've completed Task 1 (company research) for AMD. The deliverable is a research document of about 8,100 words, including tables: `AMD_Research_Document_2026-10-14.md` in the run folder.

It covers all nine required sections:
1. Company overview
2. History, from 1969 to the 2026 Helios launch
3. Management: bios of Lisa Su, Jean Hu, Mark Papermaster and Forrest Norrod, plus governance
4. Products
5. Customers and go-to-market
6. Industry overview
7. Competitive landscape: 10 competitors, with a share snapshot
8. Market opportunity: TAM, SAM and penetration
9. Risk assessment: 16 risks across all four categories

A data-sources list closes the document.

**What the research shows**
- **Growth is accelerating:**
  - Revenue went from USD 22,680 million (FY2023, -3.9%) to USD 25,785 million (FY2024, +13.7%) to USD 34,639 million (FY2025, +34.3%).
  - Q2 FY2026 revenue was a record USD 11,536 million, up 50.1% YoY.
  - Data Center revenue was USD 6,718 million, up 107.3% YoY and 58% of total revenue.
  - Q3 FY2026 guidance is about USD 13,000 million.
- **GAAP profit looks weaker than the business because of acquisition amortization.** FY2025 GAAP operating margin was 10.7%, against about 22.4% non-GAAP; intangibles are still USD 15,635 million.
- **Free cash flow and the balance sheet are strong.** FY2025 free cash flow was USD 5,519 million on AMD's definition. Net cash is about USD 9,885 million: USD 13,111 million of cash and short-term investments against USD 3,226 million of debt.
- **The thesis rests on AI accelerators.** The MI450/Helios ramp starts in the second half of 2026 and is anchored by OpenAI (6 GW) and Anthropic (up to 2 GW). It is tracked against the November 2025 targets: revenue CAGR above 35%, Data Center CAGR above 60%, and non-GAAP EPS above USD 20.
- **Valuation is demanding.** At USD 605.53 the market cap is about USD 988,513 million, roughly 28.5x FY2025 revenue.
- **The biggest risks:**
  - Execution on rack-scale AI products
  - Customer concentration
  - Nvidia's scale and the CUDA software lead
  - Custom chips designed by the hyperscalers themselves
  - Export controls
  - Dilution from the OpenAI warrant
  - Swings in AI capex

**Gaps to check before Task 5:**
- **Executive bios, market shares and much of the history come from memory.** The proxy's executive and ownership sections didn't render, so these items are marked "(MK)" in the document and need checking against the 2026 proxy.
- **Two free cash flow figures disagree.** XBRL operating cash flow minus capex gives USD 6,735 million; AMD's own definition gives USD 5,519 million. I used AMD's figure and flagged the gap.

As the skill specifies, I ran Task 1 only. Task 2 (financial model) is the logical next step.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Latest 10-K filing date and fiscal year | 2026-02-04; FY2025 (FYE 2025-12-27) | date / FY | 2026-02-04 | stock-data get_filings (Form 10-K, filed 2026-02-04; 10-K/A same day) | H |
| Latest 10-Q filing date and quarter | 2026-08-05; Q2 FY2026 (quarter ended 2026-06-27) | date / quarter | 2026-08-05 | stock-data get_filings (Form 10-Q, filed 2026-08-05) | H |
| Revenue FY2023 | 22,680 | USD millions | FY2023 (FYE 2023-12-30) | stock-data get_financials (XBRL, 10-K) | H |
| Revenue FY2024 | 25,785 | USD millions | FY2024 (FYE 2024-12-28) | stock-data get_financials (XBRL, 10-K) | H |
| Revenue FY2025 | 34,639 | USD millions | FY2025 (FYE 2025-12-27) | stock-data get_financials (XBRL, 10-K filed 2026-02-04) | H |
| Revenue growth FY2023 | -3.9 | % | FY2023 vs FY2022 (23,601) | Computed from stock-data get_financials | H |
| Revenue growth FY2024 | 13.7 | % | FY2024 vs FY2023 | Computed from stock-data get_financials | H |
| Revenue growth FY2025 | 34.3 | % | FY2025 vs FY2024 | Computed from stock-data get_financials | H |
| Latest-quarter revenue | 11,536 | USD millions | Q2 FY2026 (ended 2026-06-27) | 10-Q filed 2026-08-05 (via stock-data get_financials and WebFetch) | H |
| Latest-quarter revenue YoY growth | 50.1 | % | Q2 FY2026 vs Q2 FY2025 (7,685) | Computed; AMD press release 2026-08-05 states 50% | H |
| Latest-quarter Data Center segment revenue | 6,718 | USD millions | Q2 FY2026 | 10-Q filed 2026-08-05 (WebFetch of sec.gov) | H |
| GAAP operating margin, last fiscal year | 10.7 | % | FY2025 (3,694 / 34,639) | Computed from stock-data get_financials (10-K filed 2026-02-04) | H |
| Free cash flow, last fiscal year | 5,519 | USD millions | FY2025 | AMD Q4/FY2025 press release (ir.amd.com, 2026-02-03), company definition; XBRL OCF 7,709 less capex 974 = 6,735 | M |
| Stock-based compensation, last fiscal year | 1,638 | USD millions | FY2025 | stock-data get_financials (XBRL, 10-K filed 2026-02-04) | H |
| Current price | 605.53 | USD per share | 2026-10-14 07:49 UTC | stock-data get_quote (Yahoo Finance) | H |
| Market cap | 988,513 | USD millions | 2026-10-14 | stock-data get_quote | H |
| Cash + short-term investments | 13,111 (5,086 + 8,025) | USD millions | 2026-06-27 | 10-Q filed 2026-08-05 (stock-data get_financials, WebFetch) | H |
| Total debt | 3,226 (carrying: 875 current + 2,351 long-term; principal 3,250) | USD millions | 2026-06-27 | 10-Q filed 2026-08-05 | H |

### 2. Sources used

| Tool / connector / website | Calls |
|---|---|
| stock-data get_quote | 1 |
| stock-data get_filings | 2 |
| stock-data get_financials | 4 |
| WebFetch: sec.gov (10-Q x2, 10-K x1, DEF 14A x2) | 5 |
| WebFetch: ir.amd.com (Q2 2026 PR, Q4/FY2025 PR, Analyst Day PR, Analyst Day page) | 4 |
| WebSearch | 6 |
| Bash curl to sec.gov (blocked by proxy, 403) | 1 |
| Skills: equity-research:initiate, equity-research:initiating-coverage | 2 |

### 3. Estimates and gaps

- **Free cash flow:** I used AMD's reported FY2025 figure, USD 5,519 million. Plain XBRL OCF less capex gives USD 6,735 million. The likely cause is that XBRL OCF includes discontinued operations (the ZT manufacturing business); this is not verified.
- **Q2 FY2026 YoY growth:** computed by me from reported figures. Data Center growth (+107.3%) is computed from 6,718 vs 3,240.
- **Total debt:** shown at carrying value (USD 3,226 million). Principal is USD 3,250 million. Leases and the USD 4.1 billion of lease guarantees are excluded.
- **Market cap:** taken from the quote tool (Yahoo). It is consistent with 1,632 million shares x USD 605.53.
- **FY2023 and FY2024 segment splits:** not retrieved. Only FY2025 and Q2 FY2026 segment data are used.
- **Items from model knowledge, marked (MK) and not verified:**
  - Executive biographies and titles: the officer section of the 2026 DEF 14A did not render. Titles may have changed in 2026.
  - Insider ownership and largest holders.
  - Market shares (Mercury Research, JPR).
  - TAM sizes beyond the USD 1 trillion headline.
  - Historical deal values: Xilinx about USD 49 billion, ZT about USD 4.9 billion, ATI about USD 5.4 billion, Pensando, Silo AI.
  - OpenAI warrant terms (160 million shares).
  - The USD 500 billion AI TAM figure.
  - Hyperscaler capex estimates.
- **Nvidia Q2 FY2027 revenue (USD 96.2 billion):** taken from press coverage and a search snippet. The primary 8-K was not read. Confidence M.
- **TAM table, SAM, penetration and Data Center 3-5 year range:** my own estimates.
- **Defaults chosen:**
  - Ran Task 1 only, as instructed.
  - Delivered markdown, per the skill. The skill's Times New Roman default does not apply to .md.
  - File dated 2026-10-14.
  - Included 16 risks rather than 8-12, to give depth across all categories.
  - The word count of about 8,075 includes tables, so prose is within the 6-8K target.
- **Gap:** I could not download EDGAR files directly because the proxy returned 403, so I relied on WebFetch summaries. Q2 FY2026 MD&A text was not retrieved in full.

### 4. Freshness

- **Latest market price:** 2026-10-14, 07:49 UTC (USD 605.53).
- **Latest financial reporting period:** Q2 FY2026, quarter ended 2026-06-27 (10-Q filed 2026-08-05). Q3 FY2026 guidance was issued 2026-08-05.

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 6 | rules/listing; `date -u` plus prompt read; read task1 reference; curl to EDGAR (403); sed fix plus word count; `date -u` end |
| Skill | 2 | equity-research:initiate; equity-research:initiating-coverage |
| ToolSearch | 1 | "select:mcp__remote-devices__stock-data__get_quote,...get_filings,...get_financials,...get_price_history" |
| mcp__remote-devices__stock-data__get_quote | 1 | AMD |
| mcp__remote-devices__stock-data__get_filings | 2 | 10-K, 10-Q |
| mcp__remote-devices__stock-data__get_financials | 4 | income annual, cashflow annual, income quarterly, balance quarterly |
| WebFetch | 9 | 10-Q x2, Q2 PR, 10-K, DEF 14A x2, Analyst Day page, Analyst Day PR, Q4 FY2025 PR |
| WebSearch | 6 | Q2 2026 results; executives; Analyst Day targets; Q4 FY2025 results; Nvidia Q2 FY2027; OpenAI warrant |
| Write | 2 | research document; this transcript |

**Files delivered:** /home/claude/results/2026-10-13/runs/ER-04/B/AMD_Research_Document_2026-10-14.md
