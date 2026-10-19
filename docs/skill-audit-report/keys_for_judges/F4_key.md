# F4 key: Project_Horizon.pptx

Deck: `/home/claude/results/2026-10-13/fixtures/Project_Horizon.pptx` (8 slides, 16:9, built with pptxgenjs). It has native charts on slides 2 (column), 4 (line) and 6 (stacked-bar football field). It has no speaker notes or comments; the notes parts pptxgenjs writes are empty.
Market data is as of the close on 2026-10-13. Financials are LTM to the four quarters ended July 31, 2026 (Zoom Q3 FY26 to Q2 FY27).

## True reference values (stock-data MCP tools, pulled 2026-10-13)

| Item | True value | Derivation |
|---|---|---|
| ZM share price | $98.16 | get_quote |
| **ZM market cap** | **$28,641MM ($28.6B)** | get_quote market_cap 28,641,490,140; implies ~291.8M shares |
| **ZM LTM revenue** | **$4,993MM (4,993.06)** | 1,229.84 + 1,246.99 + 1,239.01 + 1,277.22 (Q3 FY26 to Q2 FY27) |
| Prior-year LTM revenue | $4,753.6MM | Q3 FY25 to Q2 FY26; LTM growth +5.0% |
| Gross profit (LTM) | $3,860MM; margin 77.3% | 958.07 + 951.29 + 964.72 + 985.50 |
| Operating income / EBIT (LTM) | $1,185MM; margin 23.7% | 310.41 + 249.89 + 310.47 + 314.32 |
| D&A (LTM) | $130MM | 32.39 + 32.96 + 32.78 + 32.33 |
| EBITDA (LTM) | $1,316MM (1,315.55); margin 26.3% | EBIT + D&A (GAAP; not adjusted for SBC) |
| FCF (LTM) | $1,926MM (1,925.66); margin 38.6% | OCF 2,000.21 − capex 74.55 |
| Buybacks (LTM) | $1,460MM | 413.71 + 323.70 + 361.68 + 360.51 |
| Cash & equivalents (7/31/26) | $932MM | 931.99 |
| Marketable securities, current (7/31/26) | $6,318MM | 6,317.73 |
| Debt | none reported | Zoom has no funded debt |
| Net cash | $7,250MM | 931.99 + 6,317.73 (long-term marketable securities excluded; default) |
| ZM EV | $21,392MM | 28,641 − 7,250 |
| ZM EV / LTM revenue | 4.3x | |
| ZM EV / LTM EBIT | 18.1x | |
| ZM EV / LTM EBITDA | 16.3x | |
| Quarterly revenue growth YoY | Q3 FY26 4.4%, Q4 FY26 5.3%, Q1 FY27 5.5%, Q2 FY27 4.9% | e.g. 1,277.22 / 1,217.23 − 1 = 4.93% |
| 1-year share price return | +22.7% | 98.16 / 80.01 − 1 (weekly close for the week of 2025-10-13) |
| 52-week high / low | $114.74 / $70.70 | get_quote (intraday) |

Peers (4 public video/communications peers: Microsoft/Teams, Alphabet/Meet, Cisco/Webex, RingCentral). LTM runs to each company's latest quarter (MSFT and RNG/GOOGL to 6/30/26; CSCO to 7/25/26). Market cap is from get_quote on 2026-10-13. EV = market cap + current and long-term debt − cash − short-term investments:

| Peer | Mkt cap $MM | EV $MM | LTM rev $MM | Gross mgn | EBIT mgn | EV/Rev | EV/EBIT |
|---|---|---|---|---|---|---|---|
| MSFT | 4,035,413 | 3,998,864 | 331,839 | 67.9% | 46.8% | 12.1x | 25.8x |
| GOOGL | 4,326,706 | 4,184,396 | 445,867 | 60.9% | 33.1% | 9.4x | 28.3x |
| CSCO | 453,673 | 467,288 | 63,325 | 64.5% | 24.3% | 7.4x | 30.4x |
| RNG | 6,571 | 7,580 | 2,584 | 71.8% | 6.7% | 2.9x | 43.7x |
| Median | | | | 66.2% | 28.7% | 8.4x | 29.4x |

The peer rows in the deck are correct as shown. RNG reports no short-term investments, so only cash is deducted.

## Planted errors

| ID | Type | Slide(s) | What the deck shows | Correct value / wording |
|---|---|---|---|---|
| I1 | Internal: metric differs across slides | 6 (valuation table, "EV / LTM EBITDA" row, Metric column) vs 2 and 3 | LTM EBITDA **1,361** on slide 6; **1,316** on slides 2 and 3 | 1,316 (transposed digits). With 1,316, the 18.0x–24.0x range is **23,688 – 31,584** (deck: 24,498 – 32,664, which is self-consistent with 1,361). On true figures it is ~23,680 – 31,573. |
| I2 | Internal: table total doesn't sum | 3 ("Net cash build ($MM)" table) | Cash 932 + Marketable securities **6,138** + debt — = Net cash 7,250 (932 + 6,138 = 7,070) | Marketable securities = **6,318**, so 932 + 6,318 = 7,250. The total is right; the component is transposed. |
| I3 | Internal: % doesn't match its inputs | 4 (card "1-year share price return") | **+27.2%**, with the footnote giving the $80.01 base and the current $98.16 | 98.16 / 80.01 − 1 = **+22.7%** |
| X1 | External: market cap overstated ~25% | 2 ("Market cap of $35.8B"), 4 ("$35.8B Market capitalization"), 5 (ZM market cap **35,802**); it also flows into ZM EV **28,552** (slides 5 and 6, "Current EV"), ZM EV/LTM rev **6.4x** and EV/LTM EBIT **24.1x** (slide 5) | Inflated by 1.25x | Market cap **$28,641MM ($28.6B)**. EV **$21,392MM**. With the deck's revenue (4,494), EV/Rev = 4.8x; with true revenue it is **4.3x**. EV/EBIT **18.1x**. |
| X2 | External: LTM revenue understated ~10% (consistent everywhere) | 2 ("LTM revenue of $4,494MM"), 3 (KPI tile $4,494MM; table Revenue 4,494), 5 (ZM LTM revenue 4,494), 6 (EV/LTM revenue metric 4,494 and range 22,470 – 31,458) | 4,494 = 0.9 × 4,993 | LTM revenue **$4,993MM**. Margins the deck computes on 4,494 are therefore overstated. True values: gross margin **77.3%** (deck 85.9%, slides 2, 3, 5); EBIT margin **23.7%** (deck 26.4%, slides 3, 5); EBITDA margin **26.3%** (deck 29.3%, slide 3); FCF margin **38.6%** (deck 42.9%, slide 3). True EV/Rev range at 5.0x–7.0x: **24,965 – 34,951**. |
| N1 | Narrative: "accelerating growth" vs decelerating numbers | 2 (title "Situation overview: Zoom's growth is accelerating") | Same slide's chart and bullet show YoY growth falling from 5.5% (Q1 FY27) to 4.9% (Q2 FY27) | Suggested wording: "Situation overview: growth is steady but decelerating (5.5% → 4.9% YoY)". Growth has been mid-single-digit and stable to slowing; the latest quarter decelerated. |
| N2 | Narrative: "best-in-class margins" contradicted by comps | 5 (Takeaway box: "Zoom's best-in-class margins support a premium to peer multiples…") | The table's EBIT margin column shows MSFT 46.8% and GOOGL 33.1% above ZM's 26.4%. On true numbers, ZM's 23.7% is also below CSCO's 24.3%. | Suggested wording: "Zoom's margins are above the UCaaS peer (RNG) but trail the large-cap platforms on EBIT margin; it leads on gross margin…". Drop "best-in-class". Note: ZM does have the highest gross margin, so the claim fails on operating (EBIT) margin. |
| L1 | Format: mixed "$MM" / "$M" | "$MM" on slides 2, 3, 5; **"$M"** on slide 6 (chart title "Implied enterprise value ($M)", series name, table headers "Metric ($M)", "Implied EV ($M)") | | Standardize on "$MM" (or on "$M") throughout. |
| L2 | Language: headline typo | 7 (title "Potential Buyer **Univrese**") | | "Potential Buyer **Universe**" |
| L3 | Format: mixed date formats | Long form "October 13, 2026" / "July 31, 2026" (slides 1, 2, 3 source, 6). Other formats: **"7/31/2026"** (slide 3 table header), **"10/13/2025 – 10/13/2026"** and "10/13/2025" (slide 4 footnote), **"13-Oct-2026"** (slide 5 footnote), ISO **"2026-10-20", "2026-10-27", "2026-11-09", "2026-12-07"** (slide 8 timeline) | | Use one format throughout, e.g. "October 13, 2026" / "Oct 20, 2026". |

Not planted, but worth knowing:
- The slide 4 chart and the "Mmm-YY" month labels on the chart axis (Oct-25 … Oct-26) are category labels, not one of the L3 dates.
- The "Q3 FY26 … Q2 FY27" labels follow Zoom's fiscal year (ends Jan 31).
- The 52-week high/low are intraday values from the quote. The chart plots the last weekly close of each month, so its max and min (103.44 / 73.94) differ by design and are not an error.
- EBITDA is GAAP (EBIT + D&A), not adjusted EBITDA.
- Peer EV/EBIT is used because the tools return no D&A for MSFT and CSCO.

## Defaults taken
- Peer choice: MSFT (Teams), GOOGL (Meet), CSCO (Webex), RNG (UCaaS). TWLO and FIVN were also pulled but not used. Zoom has the highest GAAP margins of the pure-plays, so N2 needed peers with higher operating margins. TWLO's balance data had no debt line either.
- LTM = sum of the latest four reported quarters (Q4 values the tool derived as FY − 9M).
- Net cash excludes long-term marketable securities and leases.
- Valuation multiple ranges (5–7x revenue, 18–24x EBITDA, 14–18x FCF) are illustrative choices.
- The buyer universe is qualitative (no figures).
- The I1, I2 and I3 values were placed so that X1 and X2 stay internally consistent everywhere else. All other percentages in the deck recompute correctly from the numbers shown.
