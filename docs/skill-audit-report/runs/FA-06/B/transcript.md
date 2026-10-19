# FA-06 / Arm B transcript

- Start: 2026-10-16 03:19:20 UTC
- End: 2026-10-16 03:23:00 UTC

---

## Final reply to user

I built the Zoom (ZM) take-private LBO as a formula-driven Excel model: **ZM_LBO_Model.xlsx**. It has six tabs: Inputs, Sources & Uses, Operating Model, Debt Schedule, Returns, and sensitivities on the Returns tab.

**Headline: at a 30% premium with exit at the entry multiple, the base case returns a 9.0% IRR and 1.54x MOIC over 5 years.** That is well below a typical sponsor hurdle of about 20%.

The problem is the price. A $128.06 offer means paying about 23.6x LTM EBITDA (operating income plus D&A, with stock-based pay treated as a cost). At that multiple only about 6.0x of debt fits, so the sponsor has to put up about $24.4bn of equity, roughly 62.5% of sources.

### Transaction summary (USD m unless stated)

**Purchase price**
- Offer price is $128.06 per share: $98.51 close on 2026-10-15 plus a 30% premium.
- Diluted shares are 298.65m. That is 291.78m basic shares plus an estimated 6.87m from the treasury-stock method.
- Equity purchase price is $38,246.1m.
- Less cash and short-term investments of $7,249.7m. Zoom has no debt.
- Entry EV is $30,996.4m.
- That equals 23.6x LTM EBITDA of $1,315.6m, or 15.2x adjusted EBITDA of $2,044.8m with stock-based pay added back. It is 6.2x LTM revenue.

**Sources**

| Source | USD m | Basis |
|---|---|---|
| Term Loan B | 5,262.2 | 4.0x EBITDA; SOFR 3.88% + 325bp = 7.13% |
| Senior notes | 2,631.1 | 2.0x EBITDA; 7Y Treasury 5.09% + HY spread 3.25% = 8.34% |
| Existing cash | 6,749.7 | Cash on hand less a $500m minimum operating balance |
| Sponsor equity | 24,420.3 | Balancing figure |
| **Total** | **39,063.4** | |

**Uses**

| Use | USD m |
|---|---|
| Equity purchase | 38,246.1 |
| Advisory fees (2.0% of EV) | 619.9 |
| Financing fees (2.5% of debt) | 197.3 |
| **Total** | **39,063.4** |

The sources-minus-uses check is 0.

**Leverage**
- Total debt is $7,893.3m: 6.0x EBITDA, or 3.9x adjusted EBITDA.
- Leverage falls to 2.3x by Year 5.
- 75.1% of the Term Loan is repaid from cash sweeps.
- EBITDA covers interest 2.3x in Year 1, rising to 4.5x in Year 5.

**Operations**
- Revenue grows 4.5% / 4.5% / 4.0% / 4.0% / 3.5%. The latest quarter grew 4.9% year on year.
- EBITDA margin rises 50bp a year, from 26.5% to 28.5%.
- Free cash flow for debt paydown grows from $582m in Year 1 to $1,009m in Year 5.

**Exit (Year 5)**
- EBITDA of $1,739.6m at 23.6x gives an EV of $40,987.8m.
- Less $3,941.8m of debt, plus $500m of cash, leaves exit equity of $37,546.0m.
- Against $24,420.3m invested, that is **MOIC 1.54x, IRR 9.0%**.

### Sensitivity: IRR (rows = entry premium, columns = exit EV/EBITDA)

| Premium \ Exit | 21.6x | 22.6x | 23.6x | 24.6x | 25.6x |
|---|---|---|---|---|---|
| 20% | 9.7% | 10.8% | 11.9% | 12.9% | 13.9% |
| 25% | 8.3% | 9.3% | 10.4% | 11.4% | 12.3% |
| **30%** | 6.9% | 7.9% | **9.0%** | 10.0% | 10.9% |
| 35% | 5.6% | 6.7% | 7.7% | 8.7% | 9.6% |
| 40% | 4.4% | 5.5% | 6.5% | 7.5% | 8.4% |

### Sensitivity: MOIC

| Premium \ Exit | 21.6x | 22.6x | 23.6x | 24.6x | 25.6x |
|---|---|---|---|---|---|
| 20% | 1.59x | 1.67x | 1.75x | 1.83x | 1.92x |
| 25% | 1.49x | 1.56x | 1.64x | 1.71x | 1.79x |
| **30%** | 1.40x | 1.47x | **1.54x** | 1.61x | 1.68x |
| 35% | 1.31x | 1.38x | 1.45x | 1.52x | 1.58x |
| 40% | 1.24x | 1.31x | 1.37x | 1.43x | 1.50x |

The center cell of each table matches the model's own output, and the check cell is 0.

**What this means:**
- **The deal does not work at today's price.** Even at a 20% premium with exit 2x above entry, the IRR is only 13.9%.
- **Low growth is the main cause.** Value creation relies almost entirely on paying down debt and about 2 points of margin gain.
- **Including Zoom's ~$3.8bn of strategic investments would help, but not enough.** These include a $3.13bn preferred stake in Anthropic and are excluded from the model (left out of EV, with no exit value). Counting them would lift the base MOIC to roughly 1.69x.
- **Cash flow is front-loaded in the model's favor only if stock-based pay is not a real cost.** If it were treated as non-cash, early-year free cash flow would be about $560m a year higher. I treated it as a real cost on the view that it is replaced with cash pay after a take-private.

**About the model:**
- It recalculates in LibreOffice with zero errors across 363 formulas.
- Interest is calculated on beginning balances, so there are no circular references.
- The skill's bundled standard template (`examples/LBO_Model.xlsx`) was missing from the plugin. I rebuilt its standard layout (Sources & Uses, Operating Model, Debt Schedule, Returns, Sensitivity) with the skill's color and formatting conventions.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Current price | 98.51 | USD/share | 2026-10-15 close (fetched 2026-10-16 03:19 UTC) | stock-data get_quote (Yahoo Finance) | H |
| Offer price | 128.06 | USD/share | 2026-10-15 | Model: 98.51 x 1.30 | H |
| Diluted shares | 298.65 | m shares | Basic as of 2026-08-14; dilution from FY27Q2 (to 2026-07-31) | 10-Q filed 2026-08-26 cover (291.78m basic) + stock-data get_financials (diluted - basic weighted, 6.87m) | M |
| Equity purchase price | 38,246.1 | USD m | 2026-10-15 | Model | M |
| Existing cash + short-term investments | 7,249.7 (931.99 cash + 6,317.73 marketable securities) | USD m | 2026-07-31 | stock-data get_financials (balance); 10-Q filed 2026-08-26 | H |
| Existing debt | 0.0 | USD m | 2026-07-31 | 10-Q filed 2026-08-26 (no borrowings on balance sheet); stock-data get_financials | H |
| Entry EV | 30,996.4 | USD m | 2026-10-15 | Model | M |
| LTM revenue | 4,993.1 | USD m | LTM to 2026-07-31 (FY26Q3-FY27Q2) | stock-data get_financials (SEC XBRL) | H |
| LTM EBITDA | 1,315.6 = operating income 1,185.1 + D&A 130.5; SBC (729.2) treated as an expense and not added back. Memo: Adj. EBITDA with SBC added back = 2,044.8 | USD m | LTM to 2026-07-31 | stock-data get_financials (income + cashflow) | H |
| Entry EV/EBITDA | 23.6 (15.2 on SBC-adjusted EBITDA) | x | 2026-10-15 / LTM 2026-07-31 | Model | M |
| SOFR | 3.88 | % | 2026-10-14 | stock-data get_macro_series (FRED SOFR) | H |
| High-yield spread | 3.25 (ICE BofA US HY OAS) | % | 2026-10-14 | stock-data get_macro_series (FRED BAMLH0A0HYM2) | H |
| Total debt raised and leverage multiple | 7,893.3; 6.0x LTM EBITDA (3.9x Adj. EBITDA) | USD m; x | At close | Model (TLB 5,262.2 at 7.13%; notes 2,631.1 at 8.34%) | M |
| Sponsor equity | 24,420.3 (62.5% of sources) | USD m | At close | Model | M |
| Base-case IRR | 9.0 | % | 5-year hold | Model | M |
| Base-case MOIC | 1.54 | x | 5-year hold | Model | M |

### 2. Sources used

| Tool / connector / website | Calls |
|---|---|
| stock-data get_quote (ZM) | 1 |
| stock-data get_financials (income quarterly, cashflow quarterly, balance quarterly) | 3 |
| stock-data get_macro_series (SOFR, BAMLH0A0HYM2, DGS7) | 3 |
| stock-data get_filings (ZM 10-Q) | 1 |
| WebFetch: sec.gov ZM 10-Q for 2026-07-31 (filed 2026-08-26) | 3 |
| curl to sec.gov (blocked by the proxy, no data) | 1 |
| Skills: financial-analysis:lbo, financial-analysis:lbo-model | 2 |

### 3. Estimates and gaps

**Data I estimated or could not verify**
- **Template:** the standard template the skill points to (`examples/LBO_Model.xlsx`) was not in the plugin directory. I rebuilt its standard section structure from the skill's description.
- **Dilution:** I could not read the option/RSU/PSU counts; the 10-Q equity note was beyond what the fetch returned and direct SEC access was blocked. Dilution is estimated at 6.87m shares, the FY27Q2 weighted diluted shares minus basic shares. It is held constant across premiums, which slightly understates dilution at a higher offer price.
- **Basic shares** (291.78m) are as of 2026-08-14. They do not reflect buybacks since then, though the market cap in the quote implies about the same count.
- **Stock-based pay (SBC):** treated as an operating cost both when sizing debt and in cash flow, assuming it is replaced by cash pay after the take-private. Lenders and sponsors often add SBC back, which would support more debt and a higher IRR.
- **Strategic investments** (~$3,785.9m, including the $3,134.5m Anthropic preferred stake) are not counted as cash and get no value at exit. This is conservative.
- **Operating leases** are not treated as debt (small). Deferred revenue is not treated as debt-like.
- **Q4 figures:** FY26Q4 quarterly figures and some quarterly cash-flow lines are derived as full year minus nine months (flagged by the data tool).

**Defaults I chose**
- **Close and periods:** close is assumed on the price date. Projection years run as 12-month periods from the LTM base, not on Zoom's fiscal calendar.
- **Fees and cash:** minimum operating cash is $500m; advisory fees are 2.0% of EV; financing fees are 2.5% of debt. Fees are expensed and not amortized, and there is no tax benefit from them.
- **Debt sizing:** a Term Loan B of 4.0x EBITDA and senior notes of 2.0x EBITDA, for 6.0x total.
- **Term Loan terms:** SOFR (3.88%, 2026-10-14) plus a 325bp spread (assumed), floating but held flat. 1% annual amortization and a 100% excess cash sweep.
- **Notes coupon:** 7Y Treasury (5.09%, 2026-10-14) plus the HY OAS (3.25%), giving 8.34%. Bullet repayment with no call or refinancing.
- **Interest:** charged on beginning balances; no interest income on cash.
- **Tax:** 23% cash tax rate, with no NOLs or interest-deductibility cap (163(j)).
- **Operating forecast:**
  - Revenue growth of 4.5/4.5/4.0/4.0/3.5% (the latest quarter grew 4.9% year on year).
  - EBITDA margin from 26.5% to 28.5% (LTM was 26.3%).
  - D&A at 2.6% of revenue and capex at 1.5% of revenue.
  - Working capital releases cash equal to 10% of each year's revenue increase, from deferred revenue.
- **Exit and returns:** exit EV/EBITDA equals entry EV/EBITDA (23.6x), with no dividends during the hold and no management incentive pool or other dilution.
- **Sensitivities:**
  - Premium is tested at 20-40% in 5% steps; exit multiple at entry ±2.0x in 1.0x steps.
  - Debt size and the paydown schedule are held fixed across premiums, since debt is sized on EBITDA rather than price.
  - IRR in the tables uses a closed-form equivalent: one cash outflow and one inflow over 5 years.

### 4. Freshness
- Latest market price: 2026-10-15 close ($98.51). SOFR, HY OAS and the 7Y Treasury are as of 2026-10-14.
- Latest financial reporting period: FY2027 Q2, quarter ended 2026-07-31 (10-Q filed 2026-08-26). LTM = 2025-08-01 to 2026-07-31.

---

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 9 | Read rules, prompt and run folder; date start; list skill files and copy template (template missing); check tools; curl to SEC (blocked); inspect recalc script; build and recalculate; dump values; date end |
| Skill | 2 | financial-analysis:lbo, financial-analysis:lbo-model |
| ToolSearch | 1 | `select:mcp__remote-devices__stock-data__get_quote,get_financials,get_macro_series,get_filings,get_price_history` |
| mcp__remote-devices__stock-data__get_quote | 1 | ZM |
| mcp__remote-devices__stock-data__get_financials | 3 | Income, cashflow and balance, quarterly |
| mcp__remote-devices__stock-data__get_macro_series | 3 | SOFR, BAMLH0A0HYM2, DGS7 |
| mcp__remote-devices__stock-data__get_filings | 1 | ZM 10-Q |
| WebFetch | 3 | ZM 10-Q (2026-07-31) on sec.gov |
| Write | 2 | _work/build.py, transcript.md |

The Bash count above includes the curl attempt (made inside one Bash call) and the LibreOffice recalc via `/mnt/skills/public/xlsx/scripts/recalc.py` (success, 0 errors, 363 formulas).

**Files delivered**
- /home/claude/results/2026-10-13/runs/FA-06/B/ZM_LBO_Model.xlsx
- /home/claude/results/2026-10-13/runs/FA-06/B/transcript.md
- Build script (scratch): /home/claude/results/2026-10-13/runs/FA-06/B/_work/build.py
