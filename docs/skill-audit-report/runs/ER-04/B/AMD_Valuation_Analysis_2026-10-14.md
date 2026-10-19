# AMD: Valuation Analysis, Price Target and Rating

**Advanced Micro Devices, Inc. (NASDAQ: AMD)** | Initiating Coverage, Task 3 | 2026-10-14

| | |
|---|---|
| **Rating** | **SELL** (Underperform) |
| **12-month price target** | **USD 285** |
| **Current price** | USD 605.53 (2026-10-14, stock-data get_quote) |
| **Implied downside** | **-52.9%** |
| **Market cap / EV** | USD 988,225 million / USD 978,340 million (1,632 million basic shares; net cash USD 9,885 million) |
| **Method** | 50% DCF (USD 175.91) + 50% trading comps, peer-median EV/NTM revenue (USD 390.80) |

Conventions: USD millions unless stated; per-share values in USD; percentages to one decimal place. All calculations are live in `AMD_Financial_Model_2026-10-14.xlsx`, on the tabs **DCF**, **Sensitivity**, **Comps** and **Valuation Summary**, which were added to the Task 2 model.

---

## 1. Executive summary

AMD is executing very well. Revenue grew 50.1% YoY in Q2 FY2026, Data Center revenue grew 107.3%, and gigawatt-scale MI450/Helios commitments from OpenAI and Anthropic underpin 2027. The issue is valuation, not the business.

At USD 605.53, AMD trades at:
- **15.2x** EV/NTM revenue, a 53.2% premium to the median of the four peers (9.9x);
- about **55x** FY2027E approximate non-GAAP EPS (USD 10.98);
- **153.6x** LTM GAAP earnings.

Our base case already assumes:
- revenue up 42.8% in FY2026E and 39.7% in FY2027E;
- Data Center revenue reaching USD 90.6 billion by FY2030E;
- GAAP operating margin rising from 10.7% (FY2025) to 31.4% (FY2030E).

On those assumptions the DCF is worth USD 175.91 per share. Even our bull case is worth only USD 280.02: it has 35.3% revenue CAGR to FY2030E, about 35.7% operating margin, and is roughly in line with management's November 2025 targets. No WACC/terminal-growth pair in our grid (WACC 10.2%-16.2%, g 2.0%-4.0%) reaches the current price.

Trading comps give USD 297.67-465.12 (peer 25th-75th percentile). Blending the two methods 50/50 gives **USD 283.35**, which we round to a **USD 285 target**. The -52.9% implied return is well below our -10% SELL threshold.

Investors should be clear about the nature of the call. The market is capitalizing AMD as a company that grows at above 35% for well beyond five years and reaches margins close to those of Nvidia and Broadcom. That outcome is possible. But it is not the base case, and it is not supported by the current mix: GAAP operating margin of 15.7% over the last twelve months.

---

## 2. DCF analysis

### 2.1 Cost of capital

| Input | Value | Basis |
|---|---|---|
| Risk-free rate | 5.2% (5.24%) | FRED DGS10, 10-year UST, 2026-10-09 close (stock-data get_macro_series) |
| Equity risk premium | 5.0% | Assumed, long-run US ERP |
| Beta (applied) | 1.59 | Peer median unlevered beta (1.588), relevered at AMD's market D/E of 0.3% |
| Beta derivation | 5-year monthly returns vs S&P 500 (59 months to 2026-09), Blume-adjusted (0.67 x raw + 0.33), unlevered at a 15% tax rate | NVDA 1.82, AVGO 1.33, INTC 1.91, QCOM 1.50 (levered Blume) |
| Memo: AMD's own beta | Raw 2.52, Blume 2.02 | Not used: inflated by the 2026 rally (stock +200% since March) |
| Cost of equity | 13.2% | CAPM |
| Pre-tax / after-tax cost of debt | 5.8% / 5.0% | Rf + 0.6% A-rated spread (assumed), 15% tax |
| Weights (E / D) | 99.7% / 0.3% | Market cap USD 988,225 million; debt USD 3,226 million |
| **WACC** | **13.2%** (13.18%) | |
| **Terminal growth** | **3.0%** | Nominal; below the 5.2% risk-free rate and long-run nominal GDP |

### 2.2 Cash flows and structure

- **Explicit period (H2 FY2026E-FY2030E):** unlevered FCF from the Task 2 base case.
  - Calculation: NOPAT on GAAP EBIT, plus D&A and acquired-intangible amortization, less capex and the increase in NWC.
  - SBC is treated as a real cost and not added back.
  - Only 50% of FY2026E is included, because the balance sheet is dated 2026-06-27.
- **Fade period (FY2031E-FY2035E):** revenue growth fades in a straight line from FY2030E's 11.5% toward the 3.0% terminal rate. UFCF margin is held at the FY2030E level (25.6%).
- **Terminal value:** Gordon growth on FY2036E UFCF, discounted from the end of FY2035E. All other cash flows use mid-period discounting from the 2026-10-14 valuation date.

| USD millions | H2 FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E | FY34E | FY35E |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue (full year) | 49,476 | 69,117 | 87,417 | 102,679 | 114,511 | 126,081 | 137,028 | 146,979 | 155,565 | 162,442 |
| Growth | 42.8% | 39.7% | 26.5% | 17.5% | 11.5% | 10.1% | 8.7% | 7.3% | 5.8% | 4.4% |
| UFCF (full year) | 7,566 | 12,188 | 18,862 | 24,814 | 29,285 | 32,244 | 35,044 | 37,588 | 39,784 | 41,543 |
| UFCF margin | 15.3% | 17.6% | 21.6% | 24.2% | 25.6% | 25.6% | 25.6% | 25.6% | 25.6% | 25.6% |
| Cash flow discounted | 3,783 | 12,188 | 18,862 | 24,814 | 29,285 | 32,244 | 35,044 | 37,588 | 39,784 | 41,543 |
| Discount factor | 1.000 | 0.915 | 0.809 | 0.715 | 0.631 | 0.558 | 0.493 | 0.436 | 0.385 | 0.340 |
| PV | 3,783 | 11,156 | 15,251 | 17,730 | 18,490 | 17,990 | 17,272 | 16,371 | 15,311 | 14,128 |

### 2.3 Enterprise to equity bridge

| Item | USD millions |
|---|---|
| PV, explicit period | 66,411 |
| PV, fade period | 81,072 |
| Terminal value (end-FY2035E) | 420,529 (9.8x FY2036E UFCF) |
| PV of terminal value | 134,462 (47.7% of EV) |
| **Enterprise value** | **281,945** |
| Plus net cash (5,086 cash + 8,025 ST investments - 3,226 debt) | 9,885 |
| **Equity value** | **291,830** |
| Diluted shares (Q2 FY2026) | 1,659 million |
| **DCF value per share** | **USD 175.91** (-70.9%) |

Terminal value is 47.7% of EV, comfortably below the 60%-70% warning level. The 10-year horizon captures most of the value explicitly.

### 2.4 Sensitivity (USD per share)

**Table 1: WACC vs terminal growth**

| WACC \ g | 2.0% | 2.5% | 3.0% | 3.5% | 4.0% |
|---|---|---|---|---|---|
| 10.2% | 234.87 | 243.87 | 254.13 | 265.93 | 279.63 |
| 11.2% | 207.54 | 214.13 | 221.53 | 229.89 | 239.41 |
| 12.2% | 185.73 | 190.68 | 196.17 | 202.29 | 209.16 |
| **13.2%** | 167.94 | 171.74 | **175.91** | 180.51 | 185.61 |
| 14.2% | 153.17 | 156.14 | 159.37 | 162.90 | 166.78 |
| 15.2% | 140.73 | 143.08 | 145.62 | 148.38 | 151.39 |
| 16.2% | 130.12 | 132.01 | 134.03 | 136.22 | 138.59 |

**Table 2: WACC vs fade-period and terminal UFCF margin (base 25.6%)**

| WACC \ margin | 18% | 22% | 26% | 30% | 34% |
|---|---|---|---|---|---|
| 10.2% | 193.24 | 225.40 | 257.56 | 289.71 | 321.87 |
| 13.2% | 137.43 | 157.75 | 178.07 | 198.39 | 218.71 |
| 16.2% | 107.28 | 121.41 | 135.54 | 149.67 | 163.80 |

**Table 3: Beta vs ERP.** The range is USD 113.86 (beta 2.2, ERP 6.0%) to USD 259.90 (beta 1.2, ERP 4.0%). Using AMD's own Blume beta of 2.0 gives USD 145.23.

### 2.5 Scenario DCFs (same WACC, fade and terminal growth)

| Scenario | Probability | FY2030E revenue | FY2030E UFCF | Value / share | vs price |
|---|---|---|---|---|---|
| Bear | 25% | 65,406 | 11,780 | 70.93 | -88.3% |
| Base | 50% | 114,511 | 29,285 | 175.91 | -70.9% |
| Bull | 25% | 157,286 | 44,813 | 280.02 | -53.8% |
| **Probability-weighted** | | | | **175.69** | -71.0% |

---

## 3. Comparable companies analysis

The peer set (NVDA, AVGO, INTC, QCOM) was specified by the user:
- **NVDA:** the direct AI accelerator competitor.
- **AVGO:** the custom-ASIC and networking alternative for hyperscaler AI budgets.
- **INTC:** the x86 CPU rival.
- **QCOM:** an Arm PC entrant and large-cap fabless peer.

Data sources:
- Prices and market caps: stock-data get_quote, 2026-10-14.
- LTM financials and balance sheets: SEC XBRL, latest reported quarter, via stock-data get_financials.
- NTM revenue: our estimates, because no consensus feed was available. See section 7.

| Company | Mkt cap | EV | LTM rev | NTM rev (est.) | EV/LTM rev | **EV/NTM rev** | EV/LTM EBIT | P/E LTM | NTM growth | LTM op. margin |
|---|---|---|---|---|---|---|---|---|---|---|
| NVIDIA (NVDA) | 5,518,073 | 5,528,996 | 302,969 | 486,660 | 18.2x | **11.4x** | 28.0x | 28.6x | 60.6% | 65.2% |
| Broadcom (AVGO) | 1,705,666 | 1,741,110 | 89,104 | 130,200 | 19.5x | **13.4x** | 40.7x | 44.6x | 46.1% | 48.0% |
| Intel (INTC) | 540,218 | 561,028 | 57,032 | 65,800 | 9.8x | **8.5x** | n.m. | n.m. | 15.4% | -0.1% |
| Qualcomm (QCOM) | 188,858 | 195,365 | 44,069 | 42,747 | 4.4x | **4.6x** | 19.1x | 20.4x | -3.0% | 23.2% |
| **Maximum** | 5,518,073 | | | | 19.5x | 13.4x | 40.7x | 44.6x | 60.6% | 65.2% |
| **75th percentile** | 2,658,767 | | | | 18.6x | 11.9x | 34.3x | 36.6x | 49.7% | 52.3% |
| **Median** | 1,122,942 | | | | 14.0x | **9.9x** | 28.0x | 28.6x | 30.7% | 35.6% |
| **25th percentile** | 452,378 | | | | 8.5x | 7.5x | 23.6x | 24.5x | 10.8% | 17.4% |
| **Minimum** | 188,858 | | | | 4.4x | 4.6x | 19.1x | 20.4x | -3.0% | -0.1% |
| **AMD** | 988,225 | 978,340 | 41,305 | 64,207 | 23.7x | **15.2x** | 150.8x | 153.6x | 55.4% | 15.7% |

**Which multiple and why.** EV/NTM revenue is the primary multiple. AMD's GAAP earnings are depressed by about USD 2.1 billion a year of acquisition amortization, and Intel's LTM earnings are negative, which makes P/E and EV/EBIT unusable across the set.

**No premium or discount to the median.** AMD's NTM growth (55.4%) is above the peer median, but its LTM GAAP operating margin (15.7%) is a fraction of NVDA's (65.2%) and AVGO's (48.0%). Those two companies, which have similar growth, trade at only 11.4x and 13.4x NTM revenue. Revenue at AMD is worth less per dollar than at those peers.

| Comps-implied value | Multiple | Implied EV | Equity value | Per share | vs price |
|---|---|---|---|---|---|
| 25th percentile | 7.5x | 483,943 | 493,828 | 297.67 | -50.8% |
| **Median** | **9.9x** | **638,451** | **648,336** | **390.80** | **-35.5%** |
| 75th percentile | 11.9x | 761,747 | 771,632 | 465.12 | -23.2% |

Only a multiple of about 15.2x NTM revenue justifies the current price, above every peer including Broadcom.

**Precedent transactions:** not applied. AMD is a USD 1 trillion acquirer, not a plausible target.

---

## 4. Valuation summary and football field

| Method | Low | Base | High | Weight | Weighted |
|---|---|---|---|---|---|
| DCF, base case (WACC +/-1pp, g -/+0.5pp) | 156.14 | 175.91 | 202.29 | 50% | 87.95 |
| Trading comps, EV/NTM revenue (25th / median / 75th) | 297.67 | 390.80 | 465.12 | 50% | 195.40 |
| **Weighted value** | 226.90 | **283.35** | 333.70 | 100% | |
| **Price target (rounded to USD 5)** | | **285.00** | | | |

```
USD/share     0        100       200       300       400       500       600       700
DCF base      |          [==156-202==]
DCF grid      |        [=====130-280=======]
DCF scen.     |  [=======71-280================]
Comps         |                          [===298-465===]
52-wk range   |                 [================188-659=============================]
Target 285    |                             X
Price 605.53  |                                                              |
```

**Weighting rationale.** The DCF captures the long-duration cash-flow math and comps capture where the market prices AI-semiconductor revenue today, so we weight them equally. We give the DCF no more than 50% because AMD's growth runway is unusually uncertain in both directions.

---

## 5. Sanity checks

1. **Historical multiple.** AMD's 52-week low was USD 188.22. Our target sits at about 7.2x EV/NTM revenue, within the stock's 2024-2025 trading range (MK: roughly 6-12x NTM sales), while the current 15.2x is a cycle high.
2. **Peers.** At USD 285 AMD trades at about 26x FY2027E approximate non-GAAP EPS. That is roughly in line with NVDA at 28.6x LTM GAAP earnings, even though NVDA earns about four times AMD's operating margin.
3. **Implied expectations.** Base-case cash flows reach at most USD 279.63 anywhere in the grid (WACC down to 10.2%, g up to 4.0%). The bull scenario is worth USD 280.02 at the base WACC. The current price therefore implies a combination this model does not reach: above-bull growth sustained past FY2030E and NVDA-like margins, and/or a cost of capital well below 10%.
4. **WACC reasonableness.** 13.2% sits in the 10%-14% range for high-growth technology. It is elevated mainly because the risk-free rate is 5.2%. Every 1pp lower WACC adds about USD 20-30 per share.
5. **Terminal value.** 47.7% of EV, below the 60%-70% threshold.
6. **Implied return.** -52.9% over 12 months, consistent with a SELL rating.

---

## 6. Recommendation, catalysts and risks

**Rating: SELL. 12-month price target: USD 285 (-52.9%).**

### Catalysts (events that could close the valuation gap)

1. **Q3 FY2026 results (early November 2026).** Guidance is about USD 13,000 million. Any shortfall, or a Q4 guide below about USD 14,700 million, would challenge the trajectory the market is pricing.
2. **MI450/Helios deployment milestones (H2 2026-2027).** The pace of OpenAI's first gigawatt and Anthropic's ramp, and evidence of rack-level gross margin dilution.
3. **Nvidia Vera Rubin ramp (2026-2027).** A competitive response on price and performance per dollar.
4. **Gross-margin trajectory.** Non-GAAP gross margin of about 56% is guided for Q3 FY2026. Rack-scale pass-through content is the key watch item.
5. **Dilution events.** OpenAI warrant vesting (up to 160 million shares, about 9.8%) and the resumption or pause of buybacks.

### Risks to a SELL rating (upside risks)

1. **Faster AI share gains (high impact).** If AMD reaches the more than 60% Data Center CAGR targeted at the Analyst Day, revenue could exceed our bull case and the stock could stay at a premium.
2. **Additional gigawatt-scale customer wins.** More frontier-lab or sovereign commitments would lift visibility.
3. **Lower rates.** Each 1pp fall in WACC adds about USD 20-30 per share to the DCF.
4. **Persistent sector multiple expansion.** AI-semiconductor multiples may stay elevated for longer than fundamentals suggest; momentum is strong (stock +200% since March 2026).
5. **Margin upside.** Software (ROCm) and mix could lift UFCF margins toward 30%-34%, adding about USD 20-40 per share.

---

## 7. Assumptions and data caveats

- **Peer NTM revenue is our estimate** (no consensus data):
  - NVDA: Q3 FY2027 guidance of about USD 108,000 million (press coverage), then +8% a quarter.
  - AVGO: latest quarter x4 x1.10.
  - INTC: latest quarter x4 x1.02.
  - QCOM: LTM x0.97.
- **Peer balance-sheet gaps:** NVDA cash excludes marketable securities, which are untagged in recent XBRL, so its EV is overstated by up to about USD 50 billion, under 1% of EV. QCOM debt uses the last tagged total of USD 14,811 million.
- **AMD NTM revenue** = 25% x FY2026E + 75% x FY2027E (base case) = USD 64,207 million.
- **Market cap** in the model = price x 1,632 million basic shares = USD 988,225 million. The quote tool shows USD 988,513 million.
- **Excluded from per-share value:** the OpenAI warrant (dilutive) and the Sanmina earn-out receivable of USD 348 million.

---

## Sources

- stock-data get_quote: AMD, NVDA, AVGO, INTC, QCOM, 2026-10-14.
- stock-data get_financials: SEC XBRL quarterly income statements and balance sheets for the peers, latest quarters ended 2026-06-27 to 2026-08-02.
- stock-data get_price_history: 5-year monthly prices for AMD, peers and ^GSPC.
- stock-data get_macro_series: FRED DGS10, last observation 2026-10-09 (5.24%).
- AMD Form 10-Q, filed 2026-08-05: cash, ST investments, debt, diluted shares.
- Task 2 model: `AMD_Financial_Model_2026-10-14.xlsx`.
- NVDA Q3 FY2027 guidance (about USD 108 billion): https://www.webull.com/blog/304-Nvidia-Q2-FY2027-Earnings-Beats-Revenue-EPS-Estimates-Guides-Q3-to-108B (search-result title only).
