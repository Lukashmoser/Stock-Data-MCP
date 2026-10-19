# FA-04 / Arm A transcript

- Start: Thu Oct 15 02:05:32 UTC 2026
- End: Thu Oct 15 02:12:10 UTC 2026

---

## Final reply to user

# Microsoft (MSFT): DCF valuation informed by comps

**Base-case value: $403.04 per share, against a close of $533.69 on 2026-10-14. That is 24.5% downside.** Bear is $224.47 (-57.9%) and bull is $603.12 (+13.0%).

### Deliverables
- `MSFT_DCF_Model_2026-10-14.xlsx` has five sheets:
  - **DCF:** a case selector, Bear/Base/Bull assumption blocks, a CHOOSE-based column that feeds the selected case into the 10-year projection, the EV-to-equity bridge, a comps cross-check, a scenario summary, and three 5x5 sensitivity tables built from formulas. The tables are WACC x terminal growth, revenue growth shift x EBIT margin shift, and beta x risk-free rate. The centre cell of each table is the base case ($403.04).
  - **WACC:** CAPM cost of capital.
  - **Beta:** the 60 monthly returns and the regression, done with the SLOPE formula.
  - **Scenarios:** recomputes all three cases at once.
  - **Comps:** the peer multiples.
- `MSFT_Comps_2026-10-14.xlsx` is a standalone comps sheet for GOOGL, AMZN, META, AAPL and ORCL, with statistics from max to min.
- Both files recalculate in LibreOffice with no errors (970 and 100 formulas). Inputs are in blue with a source comment on each, and formulas are in black.

### Valuation summary
| | Bear | Base | Bull |
|---|---|---|---|
| Value per share (USD) | 224.47 | 403.04 | 603.12 |
| Upside / (downside) | -57.9% | -24.5% | +13.0% |
| WACC | 11.0% | 10.5% | 10.0% |
| Terminal growth | 2.5% | 3.0% | 3.5% |
| Terminal value as % of EV | 55.2% | 60.9% | 65.6% |

**Base-case equity bridge (USD M):** the present value of FY27–FY36 free cash flow is 1,195,351. Adding the present value of the terminal value (1,860,459) gives EV of 3,055,810. Subtract debt including leases (128,810) and add cash and short-term investments (76,843) to get equity of 3,003,843. Dividing by 7,453M diluted shares gives $403.04.

**WACC is 10.5%.**
- Cost of equity is 10.7%: a risk-free rate of 5.19% (10-year Treasury, 2026-10-14) plus beta of 1.10 (60 monthly returns vs the S&P 500, Oct-2021 to Sep-2026, R² 0.40) times an ERP of 5.0%.
- After-tax cost of debt is 4.5%: 5.6% pre-tax at a 19% tax rate.
- Weights are 96.9% equity and 3.1% debt.

**Base-case operating assumptions:**
- Revenue growth starts at 16% in FY27 and slows to 4.5% by FY36. FY26 growth was +17.8%.
- EBIT margin goes from 46.5% to 48%. FY26 was 46.8%.
- Capex falls from 33% of revenue to 13%. FY26 was 34.9%, the peak of the AI build-out.
- D&A peaks at 14% of revenue and then settles at 12%.

### How the comps informed the model
- **Peer multiples:** the peer median EV/LTM EBITDA is **17.4x** (25th–75th percentile 17.0x–23.9x). The median EV/revenue is 8.3x and the median P/E is 21.1x.
- **DCF vs peers:** the DCF implies **15.8x** LTM EBITDA (13.5x FY27E), a little below the peer median. MSFT itself trades at 20.8x.
- **Gap at the terminal value:** the Gordon terminal value works out to only 8.6x FY36 EBITDA. Using the peer-median 17.4x as an exit multiple instead gives **$633**.
- **Why the gap exists:** most of the shortfall to the market price comes from the 5.19% risk-free rate. Each 25bp change in the risk-free rate moves the value by about $16 per share. At a beta of 1.0 with the risk-free rate 50bp lower, the value is $474.
- **P/E check:** the implied P/E of 22.5x is roughly in line with the peer median of 21.1x. That median is distorted, because GOOGL's and AMZN's earnings include gains on their AI-stake investments.

### Key risks and sensitivities
- **Discount rate:** in the WACC x terminal growth table, the value ranges from $325 to $536.
- **Capex intensity:** the forecast assumes capex falls back as the AI build-out matures. If it stays above 25% of revenue past FY29, free cash flow would fall well short of the base case.
- **Equity stakes left out:** MSFT's holdings in OpenAI and Anthropic are not in the bridge. FY26 included a $4.96bn net-income effect from OpenAI and a $3.2bn gain on Anthropic, so these stakes would add value.
- **Leases:** lease liabilities of about $88.5bn are treated as debt.

Sources consulted: [Microsoft FY26 Q4 release](https://news.microsoft.com/source/2026/07/29/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results-4), [FY26 financial statements](https://microsoft.gcs-web.com/node/35101/html), [U.S. Treasury par yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610), [YCharts 10Y](https://ycharts.com/indicators/10_year_treasury_rate), [Yahoo Finance MSFT history](https://finance.yahoo.com/quote/MSFT/history/), [Yahoo Finance ^GSPC history](https://finance.yahoo.com/quote/%5EGSPC/history/), stockanalysis.com statistics pages (MSFT, GOOGL, AMZN, META, AAPL, ORCL) and financials pages, [Investing.com MSFT](https://www.investing.com/equities/microsoft-corp).

## Comparison Block

### 1. Key figures
| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Current price | 533.69 | USD/share | 2026-10-14 close | stockanalysis.com/stocks/msft/statistics; Yahoo Finance MSFT history (WebFetch) | H |
| Diluted shares | 7,453 | M shares | FY2026 (2026-06-30) diluted weighted avg | Microsoft FY26 Q4 earnings release, 2026-07-29 (microsoft.gcs-web.com/node/35101/html) | H |
| Cash + short-term investments | 76,843 | USD M | 2026-06-30 | FY26 Q4 release, 2026-07-29 (20,935 + 55,908) | H |
| Total debt | 128,810 (incl. leases; bonds only 40,294) | USD M | 2026-06-30 | stockanalysis.com/stocks/msft/statistics; FY26 Q4 release for bond debt | M |
| Revenue FY2024 | 245,122 | USD M | FY ended 2024-06-30 | stockanalysis.com/stocks/msft/financials; model knowledge (10-K filed 2024-07-30) | H |
| Revenue FY2025 | 281,724 | USD M | FY ended 2025-06-30 | FY26 Q4 release, 2026-07-29 (comparative) | H |
| Revenue FY2026 | 331,839 | USD M | FY ended 2026-06-30 | FY26 Q4 release, 2026-07-29 | H |
| Operating income FY2024 | 109,433 | USD M | FY2024 | stockanalysis.com/stocks/msft/financials | H |
| Operating income FY2025 | 128,528 | USD M | FY2025 | FY26 Q4 release, 2026-07-29 | H |
| Operating income FY2026 | 155,237 | USD M | FY2026 | FY26 Q4 release, 2026-07-29 | H |
| Capex FY2024 | 44,477 | USD M | FY2024 | stockanalysis.com/stocks/msft/financials/cash-flow-statement | H |
| Capex FY2025 | 64,551 | USD M | FY2025 | FY26 Q4 release, 2026-07-29 | H |
| Capex FY2026 | 115,948 | USD M | FY2026 | FY26 Q4 release, 2026-07-29 | H |
| Free cash flow FY2024 | 74,071 | USD M | FY2024 (CFO 118,548 - capex) | stockanalysis.com cash-flow statement | H |
| Free cash flow FY2025 | 71,611 | USD M | FY2025 (CFO 136,162 - capex) | FY26 Q4 release, 2026-07-29 | H |
| Free cash flow FY2026 | 66,987 | USD M | FY2026 (CFO 182,935 - capex) | FY26 Q4 release, 2026-07-29 | H |
| Risk-free rate | 5.19% (5.2%) | % | 2026-10-14 | home.treasury.gov daily par yield curve (10 Yr); ycharts.com | H |
| Beta | 1.10 (60 observations) | x | Monthly, 2021-09 to 2026-09 | Calculated from Yahoo Finance MSFT adj. close and ^GSPC monthly history | M |
| Equity risk premium | 5.0% | % | Assumption as of 2026-10-14 | Assumption (model knowledge of practitioner range) | M |
| Cost of debt | 5.6% pre-tax / 4.5% after-tax | % | 2026-10-14 | Rf + 40bp AAA spread (assumption); 19% tax | M |
| WACC | 10.5% (base; bear 11.0%, bull 10.0%) | % | 2026-10-14 | Calculated (WACC sheet) | M |
| Terminal growth | 3.0% (bear 2.5%, bull 3.5%) | % | Perpetuity after FY2036 | Assumption | M |
| Terminal value as % of EV | 60.9% | % | Base case | Calculated (DCF sheet) | H |
| Base value per share | 403.04 | USD/share | Valuation date 2026-10-14 | Calculated (DCF model) | M |
| Bear value per share | 224.47 | USD/share | 2026-10-14 | Calculated (Scenarios sheet) | M |
| Bull value per share | 603.12 | USD/share | 2026-10-14 | Calculated (Scenarios sheet) | M |
| Implied upside % | -24.5% (bear -57.9%, bull +13.0%) | % | vs. 533.69 close 2026-10-14 | Calculated | M |
| DCF-implied EV/EBITDA vs. peer median | 15.8x vs. 17.4x (LTM) | x | FY2026A EBITDA 193,771; peers LTM at 2026-10-14 | Calculated; peer data stockanalysis.com statistics pages | M |

### 2. Sources used
| Tool / source | Calls |
|---|---|
| WebSearch | 4 |
| WebFetch: stockanalysis.com (6 statistics pages, 2 MSFT financials pages, 1 history page) | 9 |
| WebFetch: finance.yahoo.com (MSFT monthly x2, ^GSPC monthly, ^TNX daily) | 4 |
| WebFetch: news.microsoft.com (FY26 Q4 press release) | 1 |
| WebFetch: microsoft.gcs-web.com (FY26 Q4 financial statements) | 1 |
| WebFetch: home.treasury.gov (daily par yield curve) | 1 |
| WebFetch: ycharts.com (10Y Treasury rate) | 1 |
| WebFetch: investing.com (MSFT quote) | 1 |
| Bash (curl attempts to SEC EDGAR, Yahoo API, Stooq, FRED; all blocked by proxy, so no data) | 1 call (4 failed requests) |
| Skills: financial-analysis:dcf, financial-analysis:comps-analysis, financial-analysis:dcf-model | 3 |
| LibreOffice recalc.py (via Bash) | 2 runs |

### 3. Estimates and gaps
- I took recommended defaults with no confirmation gates, as instructed.
- **Equity risk premium** of 5.0% is an assumption and was not verified for Oct-2026.
- **Cost of debt** is the risk-free rate plus a 40bp AAA spread. This is an assumption, because MSFT bond yields were not retrieved. The AAA/Aaa rating comes from model knowledge.
- **Tax rate** is 19.0% normalised. FY26's effective rate was 19.4%.
- **Total debt** of 128,810 includes about 88,516 of lease liabilities (operating and finance), derived as the provider total minus 40,294 of bonds. The lease split was not verified against the 10-K.
- **Diluted shares** use the FY26 weighted average of 7,453M, not the latest quarter-end count. The comps market cap uses 7,430M basic shares.
- **Beta:**
  - It is the raw OLS figure, with no Blume adjustment (the adjusted figure, 1.07, is shown as a memo).
  - MSFT returns include dividends (adjusted close), but S&P 500 returns are price-only.
  - The partial month of Oct-2026 is excluded.
  - Monthly prices came from Yahoo pages through WebFetch's summariser, so they may contain transcription errors. The result, 1.10, matches stockanalysis.com's published 5Y beta of 1.10.
- **FY2024 D&A** (22,287) is from model knowledge; stockanalysis shows a rounded 20,000. FY2024 revenue, operating income, capex and CFO were cross-checked to stockanalysis.com.
- **"D&A"** for FY25 and FY26 is the cash-flow line "depreciation, amortization, and other".
- **Projections:** all assumptions for FY2027E–FY2036E are analyst estimates (Bear/Base/Bull blocks in the model). These cover growth, EBIT margin, D&A %, capex %, NWC at 8% of the change in revenue, scenario WACC adjustments of ±0.5pp, and terminal growth. I did not use consensus estimates.
- **Discounting:** a 10-year projection with the mid-year convention from 2026-07-01. There is no stub-period adjustment for the 3.5 months elapsed, which makes the value slightly conservative.
- **Equity stakes:** MSFT's equity-method and other investments (OpenAI, Anthropic and others) are excluded from the bridge, so the value is understated by their fair value.
- **Peer data:**
  - All peer figures come from stockanalysis.com: LTM revenue, gross profit, EBIT, EBITDA, net income, FCF, debt including leases, cash, and shares.
  - The exact LTM period-end dates were not shown, and the figures were not checked against filings.
  - No historical revenue-growth figures were available for peers, so the growth column was omitted.
  - GOOGL and AMZN net income include large investment gains, which distorts the peer P/E.
- **Peer fiscal years differ** (AAPL Sep, ORCL May, MSFT Jun). The LTM basis was used for all of them.
- **Primary-source access:** SEC EDGAR, FRED and the Yahoo API could not be reached from the sandbox because the proxy blocked them. Price checks used web pages instead. The Investing.com intraday price of 536.99 was not used; the 533.69 close was.

### 4. Freshness
- Latest market price: 2026-10-14 (MSFT close $533.69; peer closes and 10Y yield also 2026-10-14).
- Latest financial reporting period: MSFT FY2026 ended 2026-06-30 (Q4 release dated 2026-07-29). Peers: latest reported quarter LTM as of 2026-10-14 (ORCL last reported 2026-09-10).

---

## Run log

Tool calls:
- Bash: 9 (start time/mkdir; curl access test [blocked]; beta computation; locate recalc.py; build workbooks; rebuild + recalc both files; inspect outputs; end time/listing; plus this transcript written with Write)
- Skill: 3 (financial-analysis:dcf, financial-analysis:comps-analysis, financial-analysis:dcf-model)
- WebSearch: 4 (MSFT price; 10Y yield; MSFT FY26 results; 10Y yield Oct 13/14 2026)
- WebFetch: 18 (news.microsoft.com 1; investing.com 1; microsoft.gcs-web.com 1; stockanalysis.com 9; finance.yahoo.com 4; ycharts.com 1; home.treasury.gov 1)
- Write: 1 (transcript.md)
- ToolSearch: 0 (stock-data tools not loaded or called)

Files delivered (in /home/claude/results/2026-10-13/runs/FA-04/A/):
- MSFT_DCF_Model_2026-10-14.xlsx (DCF, WACC, Beta, Scenarios, Comps sheets; 970 formulas, 0 errors)
- MSFT_Comps_2026-10-14.xlsx (peer comps; 100 formulas, 0 errors)
- transcript.md
- _work/ (build.py, beta.py, prices.json: scratch)
