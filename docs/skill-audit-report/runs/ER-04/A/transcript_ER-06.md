# Transcript: ER-06 (Arm A)

- **Start:** Wed Oct 14 08:09:47 UTC 2026
- **End:** Wed Oct 14 08:18:30 UTC 2026

## User message

Now run Task 3 (valuation) for AMD using the Task 2 model. Use DCF plus trading comps against NVDA, AVGO, INTC and QCOM, and arrive at a price target and rating. (Full text: prompts/ER-06.txt)

## Final reply to user

My rating on AMD is **SELL**, with a 12-month price target of **USD 265**. That is 56.2% below the 2026-10-13 close of USD 605.53, and well below the consensus target of USD 636.21.

**Deliverables:**
- `/home/claude/results/2026-10-13/runs/ER-04/A/AMD_Valuation_Analysis_2026-10-14.md`: the written analysis, about 3,000 words.
- `/home/claude/results/2026-10-13/runs/ER-04/A/AMD_Financial_Model_2026-10-14.xlsx`: the Task 2 model with four new tabs (DCF, Sensitivity, Comps, Valuation Summary). LibreOffice recalculated all 1,772 formulas with no errors.

**How the target is built (50% DCF, 50% comps):**
- **DCF: USD 168.73 per share.**
  - Two stages: our model's base case for FY2026E–FY2030E, then a fade through FY2035E to a 30% free-cash-flow margin, with 3.0% terminal growth.
  - The discount rate (WACC) is 14.95%. It uses a 5.21% 10-year Treasury yield, a beta of 1.95 and a 5.0% equity risk premium.
  - The terminal value is 47% of enterprise value.
- **Trading comps: USD 358.03 per share.**
  - The peer median is 9.2x EV/next-twelve-months revenue: NVDA 10.0x, AVGO 11.1x, INTC 8.3x, QCOM 4.4x.
  - I applied it to AMD's next-twelve-months revenue of USD 63,658m from our model.
  - AMD itself trades at 15.6x.
- **Weighted result:** USD 263.38, rounded to USD 265.

**Why SELL:**
- The current price implies results beyond our bull case. Even the bull-case DCF is only USD 235.57 per share.
- The bear-case DCF is USD 96.43.
- Lowering the WACC to 8% still gives only USD 448.90.
- AMD trades at roughly a 70% premium to NVIDIA on next-twelve-months revenue, while its EBITDA margin is about a third of NVIDIA's.
- Stock-based pay and the OpenAI warrant (up to 160m shares) dilute shareholders further.

**What would make me wrong:**
- the MI450/Helios AI rack ramp coming in faster than our bull case;
- the AI peer group being re-rated to higher multiples;
- interest rates falling.

**Caveats:**
- The DCF result is very sensitive to the discount rate.
- I estimated the peers' next-fiscal-year revenue myself because consensus figures were behind a paywall.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Current price (AMD) | 605.53 | USD per share | 2026-10-13 close | https://stockanalysis.com/stocks/amd/statistics/ ; https://stockevents.app/en/stock/AMD | H |
| Diluted shares | 1,659 | millions | Q2 FY2026 weighted average (quarter ended 2026-06-27) | 10-Q Q2 FY2026 (filed 2026-08-05), XBRL R2 | H |
| Net cash/(debt) | 9,885 | USD m | 2026-06-27 (cash + STI 13,111 − debt 3,226) | 10-Q Q2 FY2026 (filed 2026-08-05) | H |
| Risk-free rate and source date | 5.21 | % | 2026-10-13 | US Treasury Daily Par Yield Curve, 10 Yr (home.treasury.gov TextView, Oct-2026) | H |
| Beta and how derived | 1.95 (average of Blume-adjusted AMD 5Y beta 1.97 [0.67×2.45+0.33] and peer median raw beta 1.94) | x | Betas as of 2026-10-14 | stockanalysis.com statistics pages (AMD, NVDA, AVGO, INTC, QCOM) | M |
| Equity risk premium | 5.0 | % | Assumption | Analyst assumption (model knowledge of the typical 4.5–5.5% range) | M |
| WACC | 15.0 (14.95) | % | 2026-10-13 | Model DCF tab (CAPM Ke 14.98%; Kd after-tax 5.28%; E/V 99.7%) | M |
| Terminal growth | 3.0 | % | Applied after FY2035E | Assumption | M |
| DCF value per share | 168.73 | USD | Valuation date 2026-10-13 | Model DCF tab | M |
| NVDA market cap | 5,520,000 | USD m | 2026-10-13 close | https://stockanalysis.com/stocks/nvda/statistics/ | H |
| NVDA LTM P/E | 28.9 | x | LTM to latest report; price 2026-10-13 | https://stockanalysis.com/stocks/nvda/statistics/ | H |
| AVGO market cap | 1,710,000 | USD m | 2026-10-13 close | https://stockanalysis.com/stocks/avgo/statistics/ | H |
| AVGO LTM P/E | 45.6 | x | LTM to FQ3 FY2026 (reported 2026-09-02); price 2026-10-13 | https://stockanalysis.com/stocks/avgo/statistics/ | H |
| INTC market cap | 540,220 | USD m | 2026-10-13 close | https://stockanalysis.com/stocks/intc/statistics/ | H |
| INTC LTM P/E | N/A (n/m: LTM net loss of 11,290; EPS −2.30) | x | LTM; price 2026-10-13 | https://stockanalysis.com/stocks/intc/statistics/ | H |
| QCOM market cap | 188,860 | USD m | 2026-10-13 close | https://stockanalysis.com/stocks/qcom/statistics/ | H |
| QCOM LTM P/E | 20.6 | x | LTM; price 2026-10-13 | https://stockanalysis.com/stocks/qcom/statistics/ | H |
| Peer median EV/NTM revenue | 9.2 | x | 2026-10-13 | Model Comps tab (EV per stockanalysis.com; NTM revenue partly estimated) | M |
| Comps-implied value per share | 358.03 | USD | 2026-10-13 | Model Comps tab (9.2x × AMD NTM revenue 63,658 + net cash 9,885, ÷ 1,659m) | M |
| Price target | 265.00 | USD | 12-month, set 2026-10-14 | Model Valuation Summary (50% DCF + 50% comps = 263.38, rounded to nearest 5) | M |
| Implied upside % | −56.2 | % | vs. 2026-10-13 close | Model Valuation Summary | M |
| Rating | SELL | – | 2026-10-14 | Rating rule: below −15% = SELL | M |

### 2. Sources used

| Tool / connector / website | Calls |
|---|---|
| WebFetch (total) | 15 (1 failed: cnbc.com) |
| of which stockanalysis.com (statistics x5, forecast x5) | 10 |
| of which home.treasury.gov (daily par yield curve) | 1 |
| of which stockevents.app (NVDA) | 1 |
| of which spglobal.com (Nvidia outlook note, 2026-09-04) | 1 |
| of which app.sentisense.ai (Broadcom AI revenue target, 2026-09-08) | 1 |
| of which cnbc.com (failed) | 1 |
| WebSearch | 3 |
| Bash (incl. valuation build, LibreOffice recalc x5 via xlsx skill script, scenario runs) | 8 |
| Write | 3 |
| Task 2 model (AMD_Financial_Model_2026-10-14.xlsx) and Task 1 document | inputs, already in session |

### 3. Estimates and gaps

- **Peer next-fiscal-year revenue** (consensus was paywalled) is my estimate:
  - NVDA FY2028 = FY2027 consensus 411,650 × 1.50. Management's outlook implies about +70% (S&P Global, 2026-09-04); I applied a haircut.
  - AVGO FY2027 = 157,000 (AI semiconductor target of about 115,000 plus about 42,000 non-AI).
  - INTC FY2027 = FY2026 consensus × 1.08.
  - QCOM FY2027 = FY2026 consensus × 1.04.
- **NTM weighting:** NVDA 1/3 FY27 + 2/3 FY28; AVGO = FY27; INTC 0.2 × FY26 + 0.8 × FY27; QCOM = FY27; AMD 0.25 × FY26E + 0.75 × FY27E (model base case, not consensus; consensus FY2026 revenue is 50,950).
- **Discount-rate inputs:**
  - The equity risk premium of 5.0% is an assumption.
  - The credit spread of 100 bp is an assumption.
  - The tax rate in WACC is 15%, the model's long-run effective rate.
  - Beta methodology: the average of the Blume-adjusted AMD beta and the peer median raw beta. Raw betas are from stockanalysis.com.
  - Debt is at book value of 3,226. Leases are excluded; stockanalysis shows 4,280 including other items.
- **DCF structure:**
  - Two stages.
  - Stage-2 revenue growth of 12% / 10% / 8% / 6% / 4.5% is an assumption.
  - The terminal UFCF margin of 30% is an assumption.
  - Terminal growth is 3.0%.
  - Mid-year convention, with a 20% FY2026 stub (about 74 days to the 2026-12-26 fiscal year-end).
  - SBC is treated as a cash cost.
  - No 12-month roll-forward of the price target.
- **Shares and equity bridge:**
  - Diluted shares are the Q2 FY2026 weighted average (1,659m).
  - The OpenAI warrant is excluded from the base value. Including it gives 153.94 per share.
  - Net cash is as of 2026-06-27, not updated for Q3 FY2026 cash flow.
- **Scenario values:** the Bear and Bull DCF values (96.43 / 235.57) are static values captured by flipping `Scenarios!C4` and recalculating. They are stored as blue inputs with cell comments.
- **AMD comps inputs:**
  - LTM EBITDA (9,560) and forward P/E (54.53) come from stockanalysis.com.
  - LTM revenue of 41,305 uses a derived Q3 FY2025 figure (9,246 = FY2025 less H1 less Q4).
- **Peer LTM P/E:** the reported stockanalysis figures (28.9 / 45.6 / 20.6) differ slightly from the workbook's own market cap ÷ LTM net income calculation (28.6 / 44.7 / 20.4).
- **Weights and rating rule:** DCF 50% / comps 50%. BUY above +15%, SELL below −15%.
- **Not applied:** precedent transactions.
- **Q3 FY2026 earnings date:** not confirmed.
- **Freshness check:** the stockevents NVDA quote was shown as "19:59 Today". I relied on the stockanalysis close of 2026-10-13 for all peers.

### 4. Freshness

- Latest market price: 2026-10-13 close, for AMD, NVDA, AVGO, INTC and QCOM. Treasury yield also 2026-10-13.
- Latest financial reporting period: AMD Q2 FY2026, quarter ended 2026-06-27 (10-Q filed 2026-08-05). Peer LTM data runs to each company's latest report (e.g. AVGO's report of 2026-09-02).

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 8 | date + read prompt; read task3 reference; read row map; list DCF Inputs rows; build valuation tabs + recalc + inspect; bull/bear scenario runs (3 recalcs); insert scenario values + recalc + verify; date/ls/wc |
| WebFetch | 15 | stockanalysis statistics (AMD, NVDA, AVGO, INTC, QCOM); stockanalysis forecast (AMD, NVDA, AVGO, INTC, QCOM); treasury.gov; stockevents NVDA; S&P Global; Sentisense; cnbc (failed) |
| WebSearch | 3 | 10-year Treasury; NVDA FY2028 consensus; AVGO FY2027 consensus |
| Write | 3 | valuation build script (scratchpad); valuation analysis .md; this transcript |
| Skill | 0 | (xlsx skill already loaded in ER-05; its recalc script reused) |
| ToolSearch | 0 | none |

**Files delivered:**
- /home/claude/results/2026-10-13/runs/ER-04/A/AMD_Valuation_Analysis_2026-10-14.md
- /home/claude/results/2026-10-13/runs/ER-04/A/AMD_Financial_Model_2026-10-14.xlsx (updated with DCF, Sensitivity, Comps, Valuation Summary tabs)
- /home/claude/results/2026-10-13/runs/ER-04/A/transcript_ER-06.md
