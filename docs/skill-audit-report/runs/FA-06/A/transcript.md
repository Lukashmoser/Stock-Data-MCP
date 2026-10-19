# Transcript: FA-06 / Arm A

- Start: 2026-10-16 03:19:18 UTC (`date -u`)
- End: 2026-10-16 03:23:37 UTC (`date -u`)

---

## Final reply to user

I built the Zoom take-private LBO in **Zoom_ZM_LBO_Model.xlsx**, with 339 live formulas and 0 errors after recalculation. It has two tabs:
- **Inputs:** every hard-coded figure, with its source.
- **LBO:** Sources and Uses, the operating model, the debt schedule, returns, and the two sensitivity grids.

**Headline:** A 30% premium ($128.06 per share) prices Zoom at a $31.0bn EV, or 15.2x LTM Adj. EBITDA. At that price the deal returns **9.5% IRR and 1.57x MOIC** over 5 years with an exit at the same multiple. That is below a typical 20%+ sponsor hurdle. The reasons:
- **Large equity cheque.** Even after using $6.75bn of Zoom's cash, the sponsor puts in $20.0bn, or 62% of debt plus equity.
- **Slow growth.** Revenue grows about 3-4% a year.
- **SBC has to be replaced.** About half of today's stock-based compensation becomes a cash cost once Zoom is private, worth about 7% of revenue.

**Note on the template:** you asked for the standard template, but its file (`examples/LBO_Model.xlsx`) is missing from the skill package. I built the model myself using the same section layout (Sources & Uses, Operating Model, Debt Schedule, Returns, Sensitivities) and the same colour and format conventions.

**Deal structure**
- **Purchase price:** $128.06 × 298.65m diluted shares = $38,246m equity purchase price. Less $7,250m cash and marketable securities (no existing debt) gives a $30,996m entry EV.
- **Debt:** 6.0x LTM Adj. EBITDA in total, $12,269m.
  - Term Loan B: 4.0x, $8,179m, at SOFR 3.88% + 3.25% = 7.13%.
  - Senior notes: 2.0x, $4,090m, at a 8.77% coupon. That is the 7-year Treasury (5.11%) + the high-yield spread (3.16%) + a 0.50% new-issue concession.
- **Existing cash:** $6,750m of Zoom's cash is used, leaving $500m of minimum operating cash.
- **Fees:** $465m transaction fees (1.5% of EV) and $276m financing fees (2.25% of debt).
- **Sponsor equity:** $19,969m. It is the balancing figure, and Sources minus Uses checks to 0.

**Operating case and debt paydown**
- **Revenue:** grows from $4,993m to $5,959m by Year 5.
- **Adj. EBITDA:** grows from $2,045m to $2,562m, with the margin rising from 41.0% to 43.0%.
- **Free cash flow:** $647m to $1,087m a year after interest, tax and the cash cost of replacing SBC. All of it goes to paying down the term loan.
- **Leverage:** falls from 6.0x to 3.1x by Year 5. Interest cover (cash EBITDA / interest) rises from 1.9x to 3.0x.

**Returns:** Exit EV is $38,840m (15.2x × $2,562m). Less $7,919m of debt plus $500m of cash leaves $31,421m of exit equity. That is **1.57x MOIC and 9.5% IRR**. The equity gain comes from:
- $7.8bn of EBITDA growth.
- $4.35bn of net debt paydown.
- Less $0.74bn of fees.

**IRR sensitivity** (rows: offer premium; columns: exit EV / Adj. EBITDA)

| Premium | 13.2x | 14.2x | 15.2x | 16.2x | 17.2x |
|---|---|---|---|---|---|
| 20% | 9.1% | 11.2% | 13.1% | 14.9% | 16.6% |
| 25% | 7.3% | 9.3% | 11.2% | 13.0% | 14.6% |
| **30%** | 5.7% | 7.6% | **9.5%** | 11.2% | 12.9% |
| 35% | 4.2% | 6.1% | 7.9% | 9.6% | 11.2% |
| 40% | 2.8% | 4.7% | 6.5% | 8.2% | 9.8% |

**MOIC sensitivity**

| Premium | 13.2x | 14.2x | 15.2x | 16.2x | 17.2x |
|---|---|---|---|---|---|
| 20% | 1.55x | 1.70x | 1.85x | 2.00x | 2.15x |
| 25% | 1.42x | 1.56x | 1.70x | 1.84x | 1.98x |
| **30%** | 1.32x | 1.45x | **1.57x** | 1.70x | 1.83x |
| 35% | 1.23x | 1.34x | 1.46x | 1.58x | 1.70x |
| 40% | 1.15x | 1.26x | 1.37x | 1.48x | 1.59x |

The centre cells match the model's own IRR and MOIC. Two things to know when reading the grids:
- **Fixed exit multiples:** the exit multiple columns are fixed numbers around the 15.2x base. They do not reset to each row's own entry multiple.
- **Debt held constant:** debt is sized on EBITDA, so a different premium changes only the sponsor equity and fees.

**Main levers if you want to reach a 20% IRR:**
- A premium of 20% or less combined with an exit at 16x or higher.
- More leverage, about 7x.
- Less of the SBC replaced with cash.
- Faster margin expansion.

Sources: [8-K Ex.99.1, Q2 FY27 (filed 2026-08-25)](https://www.sec.gov/Archives/edgar/data/0001585521/000158552126000119/zm-20260731ex991.htm), [8-K Ex.99.1, Q4 FY26 (filed 2026-02-25)](https://www.sec.gov/Archives/edgar/data/1585521/000158552126000026/zm-20260225ex991.htm), [10-Q Q2 FY27](https://www.sec.gov/Archives/edgar/data/0001585521/000158552126000121/zm-20260731.htm), [stockanalysis.com ZM](https://stockanalysis.com/stocks/zm/), [Yahoo Finance ZM](https://finance.yahoo.com/quote/ZM/), [FRED SOFR](https://fred.stlouisfed.org/series/SOFR), [FRED BAMLH0A0HYM2](https://fred.stlouisfed.org/series/BAMLH0A0HYM2), [FRED DGS7](https://fred.stlouisfed.org/series/DGS7), [FRED DGS5](https://fred.stlouisfed.org/series/DGS5)

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Current price | 98.51 | USD/share | Close 2026-10-15 | https://stockanalysis.com/stocks/zm/ ; https://finance.yahoo.com/quote/ZM/ | H |
| Offer price | 128.06 | USD/share | 2026-10-15 (30% premium) | Calculated in model | H |
| Diluted shares | 298.7 | millions | Basic as of 2026-08-14; dilution from Q2 FY27 | 10-Q Q2 FY27 cover (291.78m basic) + 8-K filed 2026-08-25 (diluted minus basic weighted average shares, 6.87m) | M |
| Equity purchase price | 38,246.1 | USD m | 2026-10-15 | Calculated in model | M |
| Existing cash + short-term investments | 7,249.7 | USD m | 2026-07-31 | 8-K Ex.99.1 filed 2026-08-25 (cash 932.0 + marketable securities 6,317.7) | H |
| Existing debt | 0.0 | USD m | 2026-07-31 | 8-K Ex.99.1 filed 2026-08-25 (no borrowings) | H |
| Entry EV | 30,996.4 | USD m | 2026-10-15 | Calculated in model | M |
| LTM revenue | 4,993.1 | USD m | LTM to 2026-07-31 | 8-K filed 2026-02-25 (FY26) + 8-K filed 2026-08-25 (6M FY27 / 6M FY26) | H |
| LTM EBITDA | 2,044.8 (Adj.); 1,315.6 with SBC expensed | USD m | LTM to 2026-07-31 | Same two 8-Ks. Built as GAAP operating income 1,185.1 + D&A 130.5 = 1,315.6, plus SBC 729.2 added back = 2,044.8. Valuation and leverage use the SBC-added-back figure; 7% of revenue is charged as cash replacement of SBC in the projections | H |
| Entry EV/EBITDA | 15.2 (Adj.); 23.6 with SBC expensed | x | 2026-10-15 | Calculated in model | M |
| SOFR | 3.88% | % | 2026-10-14 | FRED series SOFR | H |
| High-yield spread | 3.16% (ICE BofA US HY OAS) | % | 2026-10-13 | FRED series BAMLH0A0HYM2 | H |
| Total debt raised and leverage multiple | 12,268.8 (TLB 8,179.2 + notes 4,089.6); 6.0x | USD m; x LTM Adj. EBITDA | At close (assumed 2026-10-31) | Model assumption | M |
| Sponsor equity | 19,968.6 | USD m | At close (assumed 2026-10-31) | Calculated in model (balancing figure) | M |
| Base-case IRR | 9.5% | % | 5-year hold to 2031-10-31 | Calculated in model | M |
| Base-case MOIC | 1.57 | x | 5-year hold to 2031-10-31 | Calculated in model | M |

### 2. Sources used

| Tool / source | Calls |
|---|---|
| WebSearch | 4 |
| WebFetch: sec.gov 8-K Ex.99.1 Q2 FY27 (filed 2026-08-25) | 1 |
| WebFetch: sec.gov 8-K Ex.99.1 Q4 FY26 (filed 2026-02-25) | 1 |
| WebFetch: sec.gov 10-Q Q2 FY27 (two reads, one with offset) | 2 |
| WebFetch: stockanalysis.com/stocks/zm | 1 |
| WebFetch: finance.yahoo.com/quote/ZM | 1 |
| WebFetch: FRED SOFR, BAMLH0A0HYM2, DGS7, DGS5 | 4 |
| Skills: financial-analysis:lbo, financial-analysis:lbo-model | 2 |
| Bash (builds with openpyxl, LibreOffice recalc via recalc.py) | 7 |

### 3. Estimates and gaps

**Template**
- The standard template file (`examples/LBO_Model.xlsx`) is missing from the skill package. I built the workbook myself with the standard sections and formatting conventions.

**Share count**
- Diluted shares are 291.78m basic shares (10-Q cover, as of 2026-08-14) plus 6.87m estimated dilution. The dilution is Q2 FY27 diluted minus basic weighted average shares; it is a proxy for the RSU and option count.
- I could not get the actual RSU/option table from the 10-Q.
- Buybacks after 2026-08-14 are not reflected.

**Price**
- The price is the 2026-10-15 close ($98.51). After hours on stockanalysis.com it was $96.96.

**Cash and other assets**
- The balance sheet is as of 2026-07-31; cash burn and buybacks since then are not reflected.
- Restricted cash ($16.6m) is excluded.
- $3.66bn of non-marketable strategic equity investments is excluded from sources and from EV. This is potential upside or a source of funds.

**LTM figures**
- LTM is FY26 + 6M FY27 − 6M FY26.
- Adj. EBITDA adds back SBC but not the employer payroll taxes on SBC, acquisition costs or litigation items, so it is slightly lower than Zoom's own non-GAAP figure.

**Deal assumptions**
- Close on 2026-10-31.
- Minimum cash of $500m.
- Transaction fees of 1.5% of EV and financing fees of 2.25% of debt.
- Financing fees are not amortized for tax purposes.
- No management option pool and no interest income on cash.

**Operating assumptions**
- Revenue growth of 4.0%, 4.0%, 3.5%, 3.5% and 3.0% (FY27 guidance implies about 4.5%).
- Adj. EBITDA margin rising from 41.5% to 43.0%.
- Cash cost of replacing SBC at 7.0% of revenue, about half of the LTM SBC rate of 14.6%.
- D&A at 2.6% of revenue and capex at 1.5% of revenue.
- Net working capital at −20% of revenue, so working capital releases cash as revenue grows.
- Cash tax rate of 23% on pre-tax income.

**Debt assumptions**
- Term Loan B spread of SOFR + 325bp; SOFR held flat at 3.88% with no forward curve.
- Term Loan B amortization of 1% a year, plus 100% of excess cash swept to the term loan.
- Notes coupon of 7-year Treasury (5.11%, 2026-10-13) + HY OAS + 50bp concession = 8.77%. The notes are non-call and still outstanding at exit.
- Leverage of 4.0x term loan plus 2.0x notes is my sizing choice, not a lender quote.

**Returns and sensitivities**
- The exit multiple equals the entry multiple (15.2x Adj. EBITDA). No exit fees.
- IRR uses year-end annual cash flows (no XIRR).
- In the sensitivities, the exit multiple columns are fixed values around the base. Debt is held constant as the premium changes.

### 4. Freshness
- Latest market price: 2026-10-15 close. SOFR as of 2026-10-14. HY OAS and Treasury yield as of 2026-10-13.
- Latest financial reporting period: Q2 FY2027, the quarter ended 2026-07-31 (8-K filed 2026-08-25; 10-Q cover share count as of 2026-08-14).

---

## Run log

| Tool | Calls | Detail |
|---|---|---|
| Bash | 7 | start date + read rules/prompt/run folder; list skill dir / copy template (failed: missing); find template; inspect recalc.py; build+recalc; dump values; rebuild+recalc+end date |
| Skill | 2 | financial-analysis:lbo, financial-analysis:lbo-model |
| WebSearch | 4 | Zoom Q2 FY27 results; ZM stock price Oct 2026; Zoom 10-Q Jul 31 2026; Zoom Q4 FY26 results |
| WebFetch | 10 | sec.gov 8-K Q2 FY27; sec.gov 8-K Q4 FY26; sec.gov 10-Q (×2); stockanalysis.com; finance.yahoo.com; FRED SOFR; FRED BAMLH0A0HYM2; FRED DGS7; FRED DGS5 |
| Write | 2 | _work/build.py; transcript.md |
| ToolSearch | 0 | none |

Files delivered:
- /home/claude/results/2026-10-13/runs/FA-06/A/Zoom_ZM_LBO_Model.xlsx
- /home/claude/results/2026-10-13/runs/FA-06/A/transcript.md
- Build script: /home/claude/results/2026-10-13/runs/FA-06/A/_work/build.py
