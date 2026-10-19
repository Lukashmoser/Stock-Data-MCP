# Transcript: FA-04 / arm B

- Start (UTC): Thu Oct 15 02:05:34 UTC 2026
- End (UTC): Thu Oct 15 02:12:15 UTC 2026

---

## Final reply to user

**MSFT DCF valuation (comps-informed), as of 2026-10-14**

Deliverables (run folder):
- `MSFT_DCF_Model_2026-10-14.xlsx`: sheets DCF (case selector, Bear/Base/Bull blocks, 10-year FCF build, terminal value, valuation summary, side-by-side scenario summary, three 5x5 sensitivity tables), WACC, Beta (60 monthly returns with live `SLOPE`), and Comps (linked into the DCF).
- `MSFT_Comps_2026-10-14.xlsx`: a standalone peer trading comps workbook.

Every derived cell is a live formula. Hard-coded inputs are blue and each one has a source comment. I recalculated both files in LibreOffice: 829 + 122 formulas, 0 errors. The centre cell of each sensitivity table matches the model value exactly (check cells = 0).

### Valuation summary
| | Bear | **Base** | Bull |
|---|---|---|---|
| Value per share (USD) | 217.56 | **369.06** | 553.45 |
| Upside vs 533.69 | -59.2% | **-30.8%** | +3.7% |
| WACC / terminal g | 11.2% / 2.5% | 10.7% / 3.0% | 10.2% / 3.5% |
| EV (USD M) | 1,584,897 | 2,714,067 | 4,088,287 |
| TV % of EV | 53.8% | 59.2% | 63.9% |
| Implied EV / FY2026A EBITDA | 8.2x | 14.0x | 21.0x |

**Comps (LTM, peers GOOGL, AMZN, META, AAPL, ORCL):**
- EV/EBITDA median is 17.1x, with a range of 14.3x to 29.9x.
- EV/EBIT median is 27.8x and EV/Revenue median is 8.2x.
- Peer median LTM revenue growth is 20.1% and median EBITDA margin is 38.7%.
- MSFT trades at 20.2x LTM EBITDA, an 18% premium to the peer median.

**Cross-check:**
- The base DCF implies 14.0x FY2026A EBITDA, an 18% discount to the peer median. The market's 20.3x is roughly the bull case.
- If the terminal value uses the peer-median 17.1x exit multiple instead of 3.0% perpetuity growth, the value is about USD 616 per share.
- The perpetuity method implies only an 8.0x terminal EBITDA multiple in FY2036. That is the core of the gap.

**WACC x terminal growth (base case, USD per share):**

| WACC \ g | 2.0% | 2.5% | 3.0% | 3.5% | 4.0% |
|---|---|---|---|---|---|
| 9.7% | 393.86 | 411.33 | 431.42 | 454.77 | 482.25 |
| 10.2% | 366.47 | 381.21 | 398.02 | 417.34 | 439.81 |
| **10.7%** | 342.33 | 354.87 | **369.06** | 385.23 | 403.83 |
| 11.2% | 320.90 | 331.66 | 343.74 | 357.39 | 372.95 |
| 11.7% | 301.77 | 311.05 | 321.41 | 333.04 | 346.18 |

There are two more tables in the model: revenue-growth shift x EBIT-margin shift (USD 248 to 543) and beta x risk-free rate (USD 302 to 469).

**What drives the result:**
1. **Cost of capital.** The 10-year Treasury is at 5.21% and the 5-year monthly beta is 1.10, so the cost of equity is 10.7%. That is about 2 to 3 points above the 7.5 to 8.5% WACC a market price of USD 534 typically implies for MSFT. Each 50bp of WACC moves the value by about USD 25 to 30 per share.
2. **AI capex.** FY2026 cash capex was USD 115.9B, or 34.9% of revenue, and reported FCF fell to USD 67.0B. The base case keeps capex at 36% of revenue in FY2027 and assumes it normalises to about 15.5% by FY2036. A slower normalisation is the main downside risk. A faster one, plus the useful-life extension, is the upside.
3. **Growth duration.** The base case has revenue growth of 16% fading to 5% over 10 years. A +2pp/yr growth shift adds about USD 58 per share.

**Bottom line:** under the inputs you specified (spot 10-year Treasury and raw 5-year beta), MSFT looks fully valued to expensive. The base case is about 31% below the current price, and only the bull case clears it. The comps cross-check is more favourable at about USD 616. So the conclusion depends heavily on whether today's 5.2% risk-free rate persists.

## Comparison Block

### 1. Key figures
| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Current price | 533.69 | USD | 2026-10-14 close | stock-data get_quote (Yahoo) | H |
| Diluted shares | 7,453 | millions | FY2026 (2026-06-30) weighted avg diluted | stock-data get_financials (10-K filed 2026-07-29) | H |
| Cash + short-term investments | 76,843 | USD M | 2026-06-30 | stock-data get_financials (10-K filed 2026-07-29) | H |
| Total debt | 40,294 | USD M | 2026-06-30 (excl. leases) | stock-data get_financials (10-K filed 2026-07-29) | H |
| Revenue FY2024 | 245,122 | USD M | FY2024 (2024-06-30) | stock-data get_financials (SEC XBRL, 10-K) | H |
| Revenue FY2025 | 281,724 | USD M | FY2025 (2025-06-30) | stock-data get_financials (10-K filed 2025-07-30) | H |
| Revenue FY2026 | 331,839 | USD M | FY2026 (2026-06-30) | stock-data get_financials (10-K filed 2026-07-29) | H |
| Operating income FY2024 | 109,433 | USD M | FY2024 | stock-data get_financials | H |
| Operating income FY2025 | 128,528 | USD M | FY2025 | stock-data get_financials | H |
| Operating income FY2026 | 155,237 | USD M | FY2026 | stock-data get_financials | H |
| Capex FY2024 | 44,477 | USD M | FY2024 | stock-data get_financials | H |
| Capex FY2025 | 64,551 | USD M | FY2025 | stock-data get_financials | H |
| Capex FY2026 | 115,948 | USD M | FY2026 | stock-data get_financials | H |
| Free cash flow FY2024 (OCF - capex) | 74,071 | USD M | FY2024 | stock-data get_financials | H |
| Free cash flow FY2025 (OCF - capex) | 71,611 | USD M | FY2025 | stock-data get_financials | H |
| Free cash flow FY2026 (OCF - capex) | 66,987 | USD M | FY2026 | stock-data get_financials | H |
| Risk-free rate | 5.2% (5.21%) | % | 2026-10-13 | stock-data get_macro_series (FRED DGS10) | H |
| Beta | 1.10 (60 monthly obs; R² 0.40) | x | 2021-09 to 2026-09 month-ends | Calculated from stock-data get_price_history (MSFT, ^GSPC) | H |
| Equity risk premium | 5.0 | % | 2026-10-14 | Assumption (skill default; model knowledge) | M |
| Cost of debt | 5.8 pre-tax / 4.7 after-tax | % | 2026-10-13 | 10-year Treasury + 60bp AAA spread (model knowledge) | M |
| WACC | 10.7 | % | 2026-10-14 | Calculated (WACC sheet) | M |
| Terminal growth | 3.0 | % | after FY2036 | Assumption | M |
| Terminal value as % of EV | 59.2 | % | base case | Calculated (DCF sheet) | M |
| Base value per share | 369.06 | USD | 2026-10-14 | Calculated (DCF model) | M |
| Bear value per share | 217.56 | USD | 2026-10-14 | Calculated (DCF model) | M |
| Bull value per share | 553.45 | USD | 2026-10-14 | Calculated (DCF model) | M |
| Implied upside % (base) | -30.8 | % | vs 533.69 on 2026-10-14 | Calculated | M |
| DCF-implied EV/EBITDA vs peer median | 14.0x vs 17.1x | x | FY2026A EBITDA vs peer LTM | Calculated (DCF + Comps sheets) | M |

### 2. Sources used
- Skill: financial-analysis:dcf (1), financial-analysis:comps-analysis (1), financial-analysis:dcf-model (1)
- ToolSearch: 1
- stock-data get_quote: 6 (MSFT, GOOGL, AMZN, META, AAPL, ORCL)
- stock-data get_financials: 18 (MSFT annual income/cashflow/balance; 5 peers × quarterly income/cashflow/balance)
- stock-data get_price_history: 4 (MSFT and ^GSPC, 5-year and 10-year monthly)
- stock-data get_macro_series: 1 (FRED DGS10)
- stock-data get_filings: 2 (MSFT 10-K, 10-Q)
- WebSearch: 3
- WebFetch: 7:
  - [MSFT 10-K FY2026](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm) ×2 (only the cover page could be read)
  - [stockanalysis.com MSFT cash flow](https://stockanalysis.com/stocks/msft/financials/cash-flow-statement/)
  - [TIKR article (2026-09-29)](https://www.tikr.com/blog/did-microsoft-really-cut-its-capex-heres-the-accounting-move-behind-the-headline)
  - [Oracle 8-K ex99.1 FY2026](https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm)
  - [Oracle 10-Q 2026-08-31](https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm)
  - [Alphabet 10-Q 2026-06-30](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm)
- Bash: 9 (one curl to the SEC XBRL API was blocked by the proxy with a 403)

### 3. Estimates and gaps
- **MSFT D&A.** The stock-data tool does not report it.
  - FY2026 is about 39,000, from stockanalysis.com and TIKR. It is rounded and I could not check it against the 10-K. (M/L)
  - FY2025 (34,153) and FY2024 (22,287) are from model knowledge. stockanalysis showed 28,000 / 20,000, which conflicts. (L/M)
  - D&A feeds FY2026 EBITDA (194,237) and the EV/EBITDA comparisons.
- **GOOGL LTM D&A of 25,086 is an estimate.** H1-2026 is 13,586 from the 10-Q. H2-2025 is my estimate of 11,500.
- **ORCL LTM D&A of 10,881 is derived.** It is FY2026 (9,294, from the 8-K) plus Q1 FY2027 (3,358) minus Q1 FY2026 (1,771), both quarters from the 10-Q. ORCL gross profit is not reported, so it shows as n/a.
- **Peer figures:**
  - Peer share counts are implied from quote market cap divided by price.
  - Peer cash covers only cash plus current marketable securities.
  - Peer debt excludes leases.
  - P/E for GOOGL and AMZN is distorted by investment gains, and META's by a one-off tax charge. I used EV/EBITDA as the primary peer multiple.
- **Debt definition.** MSFT total debt excludes finance and operating lease liabilities (finance leases are material). I applied this consistently to WACC weights and the equity bridge.
- **Cost of debt.** I used the 10-year Treasury plus an assumed 60bp AAA spread. I did not use interest expense divided by average debt (7.3%), because that figure is inflated by lease interest. WACC uses gross debt weights.
- **ERP** is 5.0% by default. Damodaran's implied ERP of about 4.0 to 4.5% would raise the value.
- **Beta** is raw, not Blume-adjusted (the adjusted figure would be 1.07). It uses 60 completed months; the partial October 2026 month is excluded. Returns are MSFT adjusted close against S&P 500 price returns (dividends excluded from the index).
- **Model structure:**
  - The projection runs 10 years (FY2027 to FY2036) rather than 5, because MSFT is still growing in the mid-teens.
  - It uses the mid-year convention from 2026-07-01 and ignores the ~3.5 months already elapsed. The terminal value is discounted at period 9.5.
  - The tax rate is 19.0% (FY2026 effective rate 19.4%).
  - The change in working capital is 5% of incremental revenue.
- **Scenario assumptions** (growth, EBIT margin, D&A and capex paths, and WACC of base ±0.5pp) are my own judgement. They do not use consensus estimates, which I could not access.
- **No SBC adjustment.** I did not deduct stock-based compensation (12,405 in FY2026) from FCF.
- **Recalculation tooling.** The skill's `recalc.py` was not available, so I recalculated with a LibreOffice headless equivalent.

### 4. Freshness
- Latest market price: 2026-10-14 close (quotes fetched 2026-10-15 02:05 to 02:06 UTC). The 10-year Treasury is as of 2026-10-13.
- Latest financial reporting period:
  - MSFT: FY2026 (ended 2026-06-30), from the 10-K filed 2026-07-29.
  - Peers: LTM to 2026-06-30 (GOOGL, AMZN, META), 2026-06-27 (AAPL) and 2026-08-31 (ORCL).

---

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 9 | read rules/prompt; date start + mkdir; SEC XBRL curl (blocked, 403); beta calc; locate recalc.py; build workbooks; rebuild + LibreOffice recalc; inspect outputs; date end |
| Skill | 3 | financial-analysis:dcf, financial-analysis:comps-analysis, financial-analysis:dcf-model |
| ToolSearch | 1 | "select:mcp__remote-devices__stock-data__get_quote,get_financials,get_price_history,get_macro_series,get_filings" |
| mcp__remote-devices__stock-data__get_quote | 6 | MSFT, GOOGL, AMZN, META, AAPL, ORCL |
| mcp__remote-devices__stock-data__get_financials | 18 | MSFT annual ×3; peers quarterly income/cashflow/balance ×15 |
| mcp__remote-devices__stock-data__get_price_history | 4 | MSFT and ^GSPC, 5y and 10y monthly |
| mcp__remote-devices__stock-data__get_macro_series | 1 | DGS10 |
| mcp__remote-devices__stock-data__get_filings | 2 | MSFT 10-K, 10-Q |
| WebSearch | 3 | MSFT D&A FY2026; Oracle debt Q1 FY2027; Alphabet depreciation Q2 2026 |
| WebFetch | 7 | MSFT 10-K ×2, stockanalysis, TIKR, ORCL 8-K, ORCL 10-Q, GOOGL 10-Q |
| Write | 1 | transcript.md |

Files delivered (in /home/claude/results/2026-10-13/runs/FA-04/B/):
- MSFT_DCF_Model_2026-10-14.xlsx
- MSFT_Comps_2026-10-14.xlsx
- transcript.md
- _work/ (build.py, beta.py, recalc.py, beta_data.json, recalc_out/, lo_profile/): scratch files
