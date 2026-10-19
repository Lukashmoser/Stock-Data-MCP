# AMD Valuation Analysis: Initiating Coverage (Task 3)

**Advanced Micro Devices, Inc. (NASDAQ: AMD)**
**Date:** 2026-10-14
**Pricing:** 2026-10-13 close
**Model:** `AMD_Financial_Model_2026-10-14.xlsx`. New tabs: DCF, Sensitivity, Comps, Valuation Summary.
**Units:** USD millions unless stated; per-share values in USD.

---

## 1. Executive Summary

| | |
|---|---|
| **Rating** | **SELL** |
| **12-month price target** | **USD 265.00** |
| Current price (2026-10-13 close) | USD 605.53 |
| Implied upside / (downside) | **-56.2%** |
| Market cap (1,659m diluted shares) | USD 1,004,574m |
| Net cash (2026-06-27) | USD 9,885m |
| Methodology | 50% two-stage DCF (USD 168.73) + 50% EV/NTM revenue trading comps at the peer median (USD 358.03) |

AMD is executing very well. FY2025 revenue grew 34.3% to USD 34,639m. Q2 FY2026 revenue grew 50.1%, with Data Center up 107%. Q3 FY2026 guidance is about USD 13,000m. The MI450/Helios ramp with OpenAI (6 GW) and Anthropic (up to 2 GW) is likely the strongest product cycle in the company's history. Our base case already reflects that: revenue rises from USD 34,639m in FY2025 to USD 119,929m in FY2030E (28.2% CAGR), and GAAP operating margin expands from 10.7% to 30.2%.

Even on those assumptions, the shares look expensive:

- **On the user-specified peer set.** At USD 605.53, AMD trades at 15.6x our NTM revenue estimate. The peer median is 9.2x (NVDA 10.0x, AVGO 11.1x, INTC 8.3x, QCOM 4.4x). NVIDIA is the AI accelerator leader with roughly 66% EBITDA margins and faster NTM growth, yet it trades at about 10x NTM revenue. AMD carries a roughly 70% premium to that multiple despite much lower margins.
- **On intrinsic value.** Our DCF is USD 168.73 per share at a 15.0% WACC. Even at an 8% WACC, which is well below CAPM for a stock with a beta near 2, the DCF gives only USD 448.90. The current price implies outcomes beyond our bull case: USD 165,637m of FY2030E revenue at a 34.9% operating margin, which gives a DCF of USD 235.57.
- **Positioning.** Our USD 265 target is well below the sell-side consensus target of USD 636.21 (stockanalysis.com). We are deliberately out of consensus. Section 6 sets out the conditions under which we would be wrong.

---

## 2. Discounted Cash Flow Analysis

### 2.1 Cost of capital

| Input | Value | Basis |
|---|---|---|
| Risk-free rate | 5.21% | US Treasury 10-year par yield, 2026-10-13 (home.treasury.gov) |
| AMD raw beta (5Y) | 2.45 | stockanalysis.com, accessed 2026-10-14 |
| Blume-adjusted beta | 1.97 | 0.67 × 2.45 + 0.33 |
| Peer median raw beta | 1.94 | NVDA 2.22, AVGO 1.48, INTC 2.23, QCOM 1.65 |
| **Selected beta** | **1.95** | Average of the Blume-adjusted and peer median betas |
| Equity risk premium | 5.0% | Assumption, middle of the 4.5–5.5% range |
| **Cost of equity** | **14.98%** | CAPM |
| Pre-tax / after-tax cost of debt | 6.21% / 5.28% | Treasury + 100 bp (A-rated); 15% tax |
| Weights (E / D) | 99.7% / 0.3% | Market cap USD 1,004,574m; debt USD 3,226m |
| **WACC** | **14.95%** | |
| Terminal growth | 3.0% | Nominal; long-run GDP plus secular compute demand |

A 15% WACC is high in absolute terms. It is the mechanical result of a 5.21% risk-free rate and a beta near 2. AMD's realised volatility relative to the market has been about twice the market's over five years, and every peer except Broadcom also has a beta above 1.6. Section 2.4 shows how sensitive the value is to WACC. The conclusion that the shares are overvalued holds across the full range we tested (8–17%).

### 2.2 Cash-flow build

- **Stage 1 (FY2026E–FY2030E)** comes from the Task 2 three-statement model, base case. Unlevered FCF is NOPAT plus D&A and acquisition amortization, minus capex and the increase in net working capital. Stock-based compensation is treated as a real cash cost and is not added back. That is about USD 2.2–4.0bn a year.
- **Stage 2 (FY2031E–FY2035E)** fades revenue growth through 12%, 10%, 8%, 6% and 4.5%. The UFCF margin glides linearly from 24.1% in FY2030E to 30.0% in FY2035E.
- **Timing:** mid-year convention. Only the 20% of FY2026E remaining after the valuation date is counted.

| USD m | FY26E* | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E | FY34E | FY35E |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 49,182 | 68,483 | 87,344 | 105,056 | 119,929 | 134,320 | 147,752 | 159,572 | 169,146 | 176,758 |
| Growth | 42.0% | 39.2% | 27.5% | 20.3% | 14.2% | 12.0% | 10.0% | 8.0% | 6.0% | 4.5% |
| UFCF | 6,462 | 10,415 | 17,367 | 23,677 | 28,910 | 33,963 | 39,101 | 44,110 | 48,750 | 53,027 |
| UFCF margin | 13.1% | 15.2% | 19.9% | 22.5% | 24.1% | 25.3% | 26.5% | 27.6% | 28.8% | 30.0% |
| PV of UFCF | 1,275 | 9,447 | 13,705 | 16,256 | 17,268 | 17,648 | 17,676 | 17,348 | 16,680 | 15,785 |

\*Only 20% of FY2026E UFCF (1,292) is valued.

### 2.3 Enterprise value to equity value

| Item | USD m |
|---|---|
| Sum of PV of UFCF | 143,086 |
| Terminal value at end-FY2035E (Gordon growth) | 457,240 |
| PV of terminal value | 126,949 |
| **Enterprise value** | **270,035** |
| Terminal value as % of EV | 47.0% (inside the 60–70% guardrail) |
| Implied terminal multiple of FY2035E UFCF | 8.6x |
| Plus: cash and short-term investments | 13,111 |
| Less: total debt | (3,226) |
| **Equity value** | **279,920** |
| Diluted shares (m) | 1,659 |
| **DCF value per share** | **USD 168.73** (-72.1% vs. price) |
| Memo: including the OpenAI warrant (+160m shares) | USD 153.94 |

### 2.4 Sensitivity analysis

**Table 1: value per share (USD), WACC versus terminal growth**

| WACC \ g | 2.0% | 2.5% | **3.0%** | 3.5% | 4.0% |
|---|---|---|---|---|---|
| 10.95% | 249.2 | 258.2 | 268.4 | 279.9 | 293.1 |
| 11.95% | 220.5 | 227.2 | 234.7 | 243.1 | 252.6 |
| 12.95% | 197.3 | 202.4 | 208.1 | 214.4 | 221.3 |
| 13.95% | 178.1 | 182.1 | 186.5 | 191.3 | 196.6 |
| **14.95%** | 162.1 | 165.3 | **168.7** | 172.5 | 176.5 |
| 15.95% | 148.6 | 151.1 | 153.8 | 156.8 | 160.0 |
| 16.95% | 136.9 | 139.0 | 141.2 | 143.6 | 146.1 |

**Table 2: value per share (USD), WACC versus terminal FY2035E UFCF margin**

| WACC \ margin | 24% | 27% | **30%** | 33% | 36% |
|---|---|---|---|---|---|
| 12.95% | 179.2 | 193.6 | 208.1 | 222.5 | 237.0 |
| **14.95%** | 147.0 | 157.9 | **168.7** | 179.6 | 190.4 |
| 16.95% | 124.3 | 132.8 | 141.2 | 149.6 | 158.0 |

**Implied-WACC check (3.0% terminal growth)**

| WACC | 8% | 9% | 10% | 11% | 12% | 13% |
|---|---|---|---|---|---|---|
| Value per share (USD) | 448.9 | 367.2 | 309.3 | 266.3 | 233.1 | 206.8 |

No reasonable discount rate gets our base-case cash flows to USD 605.53. The current price therefore depends on cash flows well above our base case, not on a lower discount rate.

---

## 3. Comparable Companies Analysis

The peer set is NVDA, AVGO, INTC and QCOM, as specified. Market data is from the 2026-10-13 close. LTM data comes from stockanalysis.com (S&P Global Market Intelligence).

| Company | Mkt cap (USD m) | EV (USD m) | LTM rev. | NTM rev. (est.) | EV/LTM rev. | **EV/NTM rev.** | EV/LTM EBITDA | LTM P/E | Fwd P/E | LTM EBITDA margin | NTM growth |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NVIDIA (NVDA) | 5,520,000 | 5,490,000 | 302,970 | 548,867 | 18.1x | **10.0x** | 27.3x | 28.9x | 18.9x | 66.4% | 81.2% |
| Broadcom (AVGO) | 1,710,000 | 1,740,000 | 89,100 | 157,000 | 19.5x | **11.1x** | 33.3x | 45.6x | 20.6x | 58.7% | 76.2% |
| Intel (INTC) | 540,220 | 560,780 | 57,030 | 67,170 | 9.8x | **8.3x** | 33.3x | n/m (loss) | 60.6x | 29.5% | 17.8% |
| QUALCOMM (QCOM) | 188,860 | 195,820 | 44,070 | 44,595 | 4.4x | **4.4x** | 16.3x | 20.6x | 19.1x | 27.2% | 1.2% |
| **Maximum** | 5,520,000 | | | | 19.5x | 11.1x | 33.3x | 44.7x | 60.6x | 66.4% | 81.2% |
| **75th percentile** | 2,662,500 | | | | 18.5x | 10.3x | 33.3x | 36.7x | 30.6x | 60.6% | 77.5% |
| **Median** | 1,125,110 | | | | 14.0x | **9.2x** | 30.3x | 28.6x | 19.9x | 44.1% | 47.0% |
| **25th percentile** | 452,380 | | | | 8.5x | 7.4x | 24.5x | 24.5x | 19.0x | 29.0% | 13.6% |
| **Minimum** | 188,860 | | | | 4.4x | 4.4x | 16.3x | 20.4x | 18.9x | 27.2% | 1.2% |
| **AMD** | 1,004,574 | 994,689 | 41,305 | 63,658 | 24.1x | **15.6x** | 104.0x | 156.1x | 54.5x | 23.1% | 54.1% |

**Notes on the comps table:**
- The LTM P/E column shows the reported stockanalysis figures. The statistics rows are calculated in the workbook as market cap divided by LTM net income, which gives NVDA 28.6x and AVGO 44.7x.
- NTM revenue blends the current and next fiscal-year revenue. Current-year figures are consensus. Next-year figures are our estimates where consensus was paywalled:
  - NVDA FY2028: +50% (management's outlook implies about 70%).
  - AVGO FY2027: USD 157bn (USD 115bn AI target plus about USD 42bn non-AI).
  - INTC FY2027: +8%.
  - QCOM FY2027: +4%.
- AMD's NTM revenue is 0.25 × FY2026E + 0.75 × FY2027E from our model.

**Choice of multiple.** EV/NTM revenue is the primary multiple. AMD's GAAP earnings are held down by about USD 2.2bn a year of Xilinx/ZT amortization, and margins are still ramping, so earnings multiples would understate its earnings power.

**Premium or discount.** We apply the median with no adjustment, for three reasons:
- AMD's NTM growth (54%) sits between NVDA/AVGO (about 76–81%) and INTC/QCOM.
- Its LTM EBITDA margin (23.1%) is below every peer.
- Growth and margin together do not justify a premium to NVDA. Using the 75th percentile would lift the comps value only to USD 400.13.

| Implied value (EV/NTM revenue) | Multiple | Implied EV (USD m) | Equity value (USD m) | Per share |
|---|---|---|---|---|
| Peer 25th percentile | 7.4x | 468,473 | 478,358 | USD 288.34 |
| **Peer median** | **9.2x** | **584,094** | **593,979** | **USD 358.03** |
| Peer 75th percentile | 10.3x | 653,927 | 663,812 | USD 400.13 |

**Cross-checks (not weighted):**
- Peer median forward P/E (19.9x) × AMD NTM adjusted EPS (about USD 9.55) gives USD 189.55.
- Peer median EV/LTM EBITDA (30.3x) × AMD LTM EBITDA (USD 9,560m) gives USD 180.48.

**Precedent transactions:** not applied. A company worth about USD 1tn is not a realistic takeover target, and no control transactions of comparable scale exist.

---

## 4. Valuation Summary and Football Field

| Method | Low | Base | High | Weight |
|---|---|---|---|---|
| DCF (WACC ±1 pt, g ∓0.5 pt) | 151.10 | 168.73 | 191.31 | 50% |
| Trading comps, EV/NTM revenue (25th / median / 75th) | 288.34 | 358.03 | 400.13 | 50% |
| Cross-check: forward P/E | – | 189.55 | – | 0% |
| Cross-check: EV/LTM EBITDA | – | 180.48 | – | 0% |
| Scenario DCF (Bear / Base / Bull) | 96.43 | 168.73 | 235.57 | 0% |
| 52-week range (reference) | 188.22 | 605.53 (current) | 658.52 | – |
| Consensus price target (reference) | – | 636.21 | – | – |
| **Weighted value → price target** | | **263.38 → USD 265** | | 100% |

```
USD/share     100       200       300       400       500       600       700
DCF                   [151====169==191]
Comps (EV/NTM)                       [288=====358===400]
Scenario DCF    [96==============169=========236]
52-week range              [188==========================================659]
Price target                     | 265
Current price                                                       | 606
```

**Scenario valuation.** These outputs come from flipping `Scenarios!C4` in the model.

| Scenario | FY2026E revenue | FY2030E revenue | FY25–30E CAGR | FY2030E op. margin | DCF / share | Comps median / share |
|---|---|---|---|---|---|---|
| Bear | 46,897 | 68,740 | 14.7% | 21.5% | 96.43 | 299.81 |
| Base | 49,182 | 119,929 | 28.2% | 30.2% | 168.73 | 358.03 |
| Bull | 51,902 | 165,637 | 36.7% | 34.9% | 235.57 | 402.23 |

Applying the same 50/50 weighting to each scenario gives price targets of USD 200 (bear), USD 265 (base) and USD 320 (bull). All three are well below the current price.

---

## 5. Investment Recommendation: SELL, Price Target USD 265

**Rating rule:**
- **BUY** if 12-month upside is above +15%.
- **SELL** if it is below -15%.
- **HOLD** otherwise.

At -56.2% implied downside, the rule gives SELL.

The SELL rating is a valuation call, not a call on fundamentals. Our view rests on three points:

1. **The price already reflects better-than-guided execution.** Management's November 2025 targets are revenue CAGR above 35% and non-GAAP EPS above USD 20 within three to five years. Our bull case delivers a 36.7% CAGR, yet its DCF value is only USD 235.57.
2. **The relative valuation does not hold up.** AMD trades at 15.6x NTM revenue against NVIDIA's 10.0x. NVIDIA has about three times AMD's EBITDA margin and faster NTM growth. AMD's GAAP P/E is 156.1x LTM and 54.5x forward (consensus non-GAAP), against a peer median of 19.9x forward.
3. **The capital structure works against shareholders.** Stock-based compensation runs at 4.5% of revenue. The OpenAI warrant adds up to 160m shares (about 9.6% dilution). Both reduce per-share value even if execution is perfect.

**Sanity checks:**
- Terminal value is 47% of EV, so the DCF is not dominated by the terminal value.
- At our DCF value, AMD would trade at 5.5x FY2026E EV/revenue and 20.9x FY2027E GAAP P/E. That is in line with peer forward P/Es.
- The market currently pays 20.2x FY2026E EV/revenue.
- A 12-month total return of -56% is clearly consistent with a SELL rating.

---

## 6. Catalysts and Risks to the Rating

### Catalysts (next 3–12 months)

1. **Q3 FY2026 results (expected early November 2026; date not confirmed).** Guidance is USD 13,000m ± 300m at about 56% non-GAAP gross margin. The Q4 guide is the first read on MI450/Helios revenue scale.
2. **First MI450/Helios shipments (H2 2026).** The first 1 GW for OpenAI, plus Anthropic, Meta, Microsoft and Oracle. Investors will watch for rack yields, HBM4 supply and gross-margin dilution from pass-through content.
3. **OpenAI warrant tranche vesting.** Vesting is tied to deployment and share-price milestones. It confirms volume but dilutes shareholders.
4. **MI500 and the 2027 roadmap** (likely at AMD's mid-2027 "Advancing AI" event), compared with Nvidia's Rubin Ultra.
5. **Changes in US export-control policy** affecting China AI GPU sales (MI308 and successors).

### Risks to the SELL rating (upside risks)

1. **The AI ramp beats our bull case** (high probability of a beat versus the base case; large impact). Each 1 pt of AI accelerator share in a market of about USD 700bn is worth about USD 7bn of revenue. If AMD's data-center AI revenue compounds at more than 80% through FY2028, as management targets, fair value could move well above USD 400.
2. **Lower discount rates** (medium probability). A 100 bp fall in the 10-year Treasury, or a lower market beta, lifts the DCF by about USD 15–35 per share. That is meaningful but not enough to close the gap alone.
3. **The sector rerates upward** (medium probability). If NVDA and AVGO rerate to 15x NTM revenue, the comps value rises to about USD 580, and the price target to about USD 375.
4. **Momentum and positioning** (high probability in the short term). The stock has risen about 220% from its 52-week low. Index and thematic flows can keep valuation detached from fundamentals for long periods.
5. **Strategic events.** Examples include more gigawatt-scale agreements with AI labs or hyperscalers, or a large buyback funded by FCF.

### Downside risks (would support the SELL)

- Delays to Helios or reliability problems.
- Funding stress at AI labs.
- Custom-ASIC share gains.
- Rack pass-through content diluting gross margin (the bear case keeps cost of sales at about 47% of revenue).
- Tighter export controls.

---

## 7. Key Assumptions and Data Notes

- **Market data, 2026-10-13 close.**
  - AMD at USD 605.53 (stockevents.app and stockanalysis.com).
  - Peers at NVDA USD 228.52, AVGO USD 357.31, INTC USD 102.81 and QCOM USD 176.86.
  - Peer market caps, EVs and LTM financials from stockanalysis.com (S&P Global Market Intelligence), accessed 2026-10-14.
- **Peer NTM revenue.** Next-fiscal-year revenue for NVDA, AVGO, INTC and QCOM is our estimate, because consensus was paywalled. A 10% error in any single estimate moves the peer median by at most about 0.5x and the comps value by about USD 20 per share.
- **Share count and net cash.** Diluted shares are 1,659m (Q2 FY2026 weighted average). Net cash of USD 9,885m is as of 2026-06-27.
- **No roll-forward.** The price target is not rolled forward 12 months. Rolling the DCF forward at the cost of equity would add about USD 25 per share to the DCF component and about USD 13 to the price target.
- **No precedent transactions.** None were applied.

**Sources:**
- US Treasury Daily Par Yield Curve (October 2026).
- stockanalysis.com statistics and forecast pages for AMD, NVDA, AVGO, INTC and QCOM.
- stockevents.app.
- S&P Global Market Intelligence research note (2026-09-04) on Nvidia's outlook.
- Sentisense (2026-09-08) on Broadcom's AI revenue target.
- AMD filings and model per Tasks 1–2.
