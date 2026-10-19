# Transcript: ER-06 (arm B)

- **Start:** 2026-10-14 08:06:51 UTC (`date -u`)
- **End:** 2026-10-14 08:13:55 UTC (`date -u`)

## Final reply to the user

I'm initiating AMD at **SELL with a 12-month price target of USD 285**, 52.9% below the 2026-10-14 price of USD 605.53. The target is an equal blend of a DCF on the Task 2 base case (USD 175.91) and trading comps against NVDA, AVGO, INTC and QCOM (USD 390.80).

**Deliverables**
- `AMD_Valuation_Analysis_2026-10-14.md`: the written valuation, covering the DCF, sensitivities, scenario values, the comps table with its statistical summary, the football field, sanity checks, catalysts and risks.
- `AMD_Financial_Model_2026-10-14.xlsx`: I added four live tabs to the Task 2 model, and the model's Checks tab still passes.
  - **DCF:** cost of capital build, the base DCF, and bull/base/bear scenario DCFs.
  - **Sensitivity:** WACC x terminal growth, WACC x cash-flow margin, beta x equity risk premium, and the comps multiple ladder.
  - **Comps:** the peer table with max / 75th / median / 25th / min.
  - **Valuation Summary:** the target, rating logic and football field.

**DCF: USD 175.91 per share**
- **Discount rate:** WACC is 13.2%. It is built from:
  - the 10-year Treasury yield of 5.24% (FRED, 2026-10-09);
  - a 5.0% equity risk premium;
  - a beta of 1.59. This is the median of the four peers' betas, adjusted for debt, from 5 years of monthly returns against the S&P 500, then re-adjusted to AMD's 0.3% debt/equity. AMD's own adjusted beta of 2.02 is shown as a sensitivity.
- **Terminal growth:** 3.0%.
- **Structure:** explicit cash flows from H2 FY2026E to FY2030E, then a five-year period in which growth fades toward the terminal rate. The terminal value is 47.7% of enterprise value.
- **Range:**
  - WACC ±1 point and growth ±0.5 points: USD 156–202.
  - Whole sensitivity grid: USD 130–280.
  - Scenarios: bear USD 70.93, bull USD 280.02, probability-weighted USD 175.69.

**Comps: USD 390.80 per share**
- **Peer median:** 9.9x enterprise value to next-twelve-months revenue, against AMD's 15.2x, a 53.2% premium.
- **Range:** USD 297.67–465.12, using the peer 25th–75th percentile.
- **No premium applied:** AMD grows faster than the median, but it has much lower margins than NVDA and AVGO, which trade at only 11.4x and 13.4x despite similar growth.

**Why SELL:** the business is strong, but at the current price the market is paying for more than our bull case. That bull case is roughly management's long-term targets, with revenue growing about 35% a year to FY2030E. To justify USD 605.53, AMD would need above-bull growth well beyond 2030, margins close to Nvidia's, or a cost of capital well below 10%.

**What would make me wrong:**
- Data Center growth above 60%, as management targets.
- More gigawatt-scale AI customer wins.
- Lower interest rates: each 1-point drop in WACC adds about USD 20–30 per share.
- Continued sector re-rating and momentum.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Current price | 605.53 | USD per share | 2026-10-14 08:07 UTC | stock-data get_quote | H |
| Diluted shares | 1,659 | millions | Q2 FY2026 (quarter ended 2026-06-27) | AMD Form 10-Q filed 2026-08-05 (via stock-data get_financials) | H |
| Net cash/(debt) | 9,885 (5,086 cash + 8,025 ST investments - 3,226 debt) | USD millions | 2026-06-27 | AMD Form 10-Q filed 2026-08-05 | H |
| Risk-free rate and its source date | 5.24 (10-year UST) | % | 2026-10-09 (FRED last observation) | stock-data get_macro_series (FRED DGS10) | H |
| Beta and how it was derived | 1.59: peer median unlevered beta (1.588) relevered at AMD D/E of 0.3% (15% tax). Peer betas from 5y monthly returns vs S&P 500 (59 months to 2026-09), Blume-adjusted. AMD's own raw 2.52 / Blume 2.02 shown as a sensitivity only | x | 2021-11 to 2026-09 | stock-data get_price_history (AMD, NVDA, AVGO, INTC, QCOM, ^GSPC); computed | M |
| Equity risk premium | 5.0 | % | as of 2026-10-14 | Assumption (model knowledge of long-run US ERP) | M |
| WACC | 13.2 (13.18) | % | 2026-10-14 | Computed: Ke 13.2%, after-tax Kd 5.0%, E/V 99.7% | M |
| Terminal growth | 3.0 | % | from FY2036E | Assumption | M |
| DCF value per share | 175.91 | USD | Valuation date 2026-10-14 | Model DCF tab (two-stage, Task 2 base case) | M |
| NVDA market cap | 5,518,073 | USD millions | 2026-10-14 | stock-data get_quote | H |
| NVDA LTM P/E | 28.6 | x | LTM to 2026-07-26 (NI 192,879) | stock-data get_quote + get_financials (SEC XBRL) | H |
| AVGO market cap | 1,705,666 | USD millions | 2026-10-14 | stock-data get_quote | H |
| AVGO LTM P/E | 44.6 | x | LTM to 2026-08-02 (NI 38,265) | stock-data get_quote + get_financials (SEC XBRL) | H |
| INTC market cap | 540,218 | USD millions | 2026-10-14 | stock-data get_quote | H |
| INTC LTM P/E | N/A (n.m.: LTM net loss of 11,289) | x | LTM to 2026-06-27 | stock-data get_financials (SEC XBRL) | H |
| QCOM market cap | 188,858 | USD millions | 2026-10-14 | stock-data get_quote | H |
| QCOM LTM P/E | 20.4 | x | LTM to 2026-06-28 (NI 9,259, includes large tax items) | stock-data get_quote + get_financials (SEC XBRL) | M |
| Peer median EV/NTM revenue | 9.9 (9.94) | x | 2026-10-14 | Computed. Peer NTM revenue estimated by me (NVDA 11.4x, AVGO 13.4x, INTC 8.5x, QCOM 4.6x) | L |
| Comps-implied value per share | 390.80 (range 297.67-465.12) | USD | 2026-10-14 | Model Comps tab: median multiple x AMD NTM revenue 64,207 + net cash | L |
| Price target | 285 | USD | 12-month, set 2026-10-14 | Model Valuation Summary: 50% DCF + 50% comps = 283.35, rounded to USD 5 | M |
| Implied upside % | -52.9 | % | vs 605.53 on 2026-10-14 | Computed | M |
| Rating | SELL (Underperform) | — | 2026-10-14 | Rule: BUY > +15%, SELL < -10%, otherwise HOLD | M |

### 2. Sources used

| Tool / connector / website | Calls (this prompt) |
|---|---|
| stock-data get_quote (AMD, NVDA, AVGO, INTC, QCOM) | 5 |
| stock-data get_financials (quarterly income x4 peers; quarterly balance x4 peers) | 8 |
| stock-data get_price_history (AMD, ^GSPC, NVDA, AVGO, INTC, QCOM; 5y monthly) | 6 |
| stock-data get_macro_series (FRED DGS10) | 1 |
| ToolSearch (load get_macro_series) | 1 |
| LibreOffice headless recalculation (local) | 1 |
| Reused from earlier turns, no new calls: AMD 10-Q data, Task 2 model and scenario snapshots, and the webull.com search-result title for NVDA Q3 FY2027 guidance (WebSearch in ER-04) | 0 |

### 3. Estimates and gaps

- **Peer NTM revenue:** estimated by me, because no consensus feed was available.
  - NVDA 486,660: Q3 FY2027 guidance of about 108,000 (from a search-result title, not verified in the primary release), then +8% a quarter.
  - AVGO 130,200: latest quarter x4 x1.10.
  - INTC 65,800: latest quarter x4 x1.02.
  - QCOM 42,747: LTM x0.97.
  - The peer median EV/NTM revenue and the comps value are therefore Low confidence.
- **AMD NTM revenue:** 64,207, calculated as 25% x FY2026E + 75% x FY2027E from my Task 2 base case, not consensus.
- **NVDA cash:** excludes marketable securities, which have been untagged in XBRL since FY2026Q4. This overstates NVDA's EV by up to about USD 50 billion, under 1% of EV, so its multiple is barely affected.
- **QCOM debt:** the latest quarter's long-term debt is untagged, so I used the last tagged total of USD 14,811 million.
- **Assumptions:**
  - Equity risk premium 5.0%.
  - Pre-tax cost of debt = risk-free rate + 0.6% = 5.84%.
  - Tax rate 15% for levering and the debt tax shield.
  - Terminal growth 3.0%.
  - Fade period: growth declines in a straight line from 11.5% to 3.0% over FY2031E-FY2035E, with UFCF margin held at 25.6%.
  - Mid-period discounting from 2026-10-14. Only the H2 FY2026E cash flow is included, because the balance sheet is dated 2026-06-27.
  - SBC treated as a cash-equivalent cost and not added back.
- **Beta choice:** I used the peer-median unlevered beta rather than AMD's own regression beta (2.02 adjusted), which the 2026 rally inflates. Using AMD's beta would cut the DCF to about USD 145.
- **Market cap in the model:** price x 1,632 million basic shares = 988,225, against 988,513 from the quote tool.
- **Weights and bands:** DCF 50% / comps 50%. Precedent transactions not applied. Rating bands are BUY > +15%, SELL < -10%. Scenario probabilities are 25/50/25. The price target is rounded to USD 5.
- **Not in per-share value:** the OpenAI warrant (up to 160 million shares, from model knowledge), the Sanmina earn-out receivable (348) and the off-balance-sheet lease guarantees (4.1 billion).
- **QCOM LTM net income** includes large one-off tax items (Q4 FY2025 -6,088 provision; Q2 FY2026 +5,138 benefit), so its P/E is distorted.
- **Historical multiple range** cited in the sanity check (about 6-12x NTM sales) is from model knowledge and not verified.
- **Scenario DCFs** use static snapshots of the Task 2 bull and bear cash flows.

### 4. Freshness

- **Latest market price:** 2026-10-14, 08:07 UTC (AMD USD 605.53; peers fetched 08:07 UTC). The risk-free rate is from 2026-10-09, the latest FRED observation.
- **Latest financial reporting period:**
  - AMD: Q2 FY2026, ended 2026-06-27 (10-Q filed 2026-08-05).
  - NVDA: Q2 FY2027, ended 2026-07-26.
  - AVGO: Q3 FY2026, ended 2026-08-02.
  - INTC: Q2 FY2026, ended 2026-06-27.
  - QCOM: Q3 FY2026, ended 2026-06-28.

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 9 | `date -u` plus prompt read; read task3 reference; AMD beta plus scenario UFCF; peer betas; scenario series plus first add-tabs attempt (missing dir); add tabs plus LibreOffice recalc plus DCF inspection; comps/sensitivity/summary inspection; copy to run folder; `date -u` end |
| ToolSearch | 1 | "select:mcp__remote-devices__stock-data__get_macro_series" |
| mcp__remote-devices__stock-data__get_macro_series | 1 | DGS10 from 2026-09-15 |
| mcp__remote-devices__stock-data__get_quote | 5 | AMD, NVDA, AVGO, INTC, QCOM |
| mcp__remote-devices__stock-data__get_financials | 8 | quarterly income and balance for NVDA, AVGO, INTC, QCOM |
| mcp__remote-devices__stock-data__get_price_history | 6 | AMD, ^GSPC, NVDA, AVGO, INTC, QCOM (5y, 1mo) |
| Write | 3 | add_valuation.py (scratchpad); valuation analysis .md; this transcript |
| Edit | 1 | valuation .md sanity-check wording |
| Skill | 0 | initiating-coverage already loaded in ER-04 |

**Files delivered:**
- /home/claude/results/2026-10-13/runs/ER-04/B/AMD_Valuation_Analysis_2026-10-14.md
- /home/claude/results/2026-10-13/runs/ER-04/B/AMD_Financial_Model_2026-10-14.xlsx (DCF, Sensitivity, Comps and Valuation Summary tabs added)
