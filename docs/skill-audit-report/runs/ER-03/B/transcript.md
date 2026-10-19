# Transcript: ER-03, arm B

- Start: 2026-10-14 04:04:37 UTC (`date -u`)
- End: 2026-10-14 04:12:15 UTC (`date -u`)

## Final reply to the user

I wrote the earnings update for NVIDIA's most recently reported quarter: **Q2 fiscal 2027**, the 13 weeks ended 2026-07-26. NVIDIA reported it after the close on 2026-08-26 and filed the 10-Q the same day. Q3 FY27 ends in late October 2026 and hasn't been reported yet.

The report is a 10-page Word document with 11 charts and 3 summary tables, saved as `NVIDIA_Q2_FY27_Earnings_Update.docx`. The chart images are in `charts/`.

**Beat on revenue and EPS**
- **Revenue** was USD 96,221M against consensus of USD 92,170M, a beat of USD 4,051M (+4.4%). That's +105.9% YoY and +17.9% QoQ, and 5.7% above the USD 91,000M guide midpoint.
- **Non-GAAP diluted EPS** was USD 2.22 against USD 2.10 consensus (+5.7%). NVIDIA's non-GAAP figures now include stock-based compensation.
- **GAAP diluted EPS** was USD 2.46 (+127.8% YoY). It's inflated by USD 7,773M of other income, mostly gains on equity holdings.

**Revenue by segment**
- **Data Center:** USD 89,023M (+116.6% YoY), USD 3,943M (4.6%) above consensus. It splits into Hyperscale at USD 48,710M (+101.5%) and AI Clouds, Industrial & Enterprise at USD 40,313M (+138.1%, +25.2% QoQ).
- **Edge Computing:** USD 7,198M (+27.5% YoY), 7.5% of revenue.
- **No separate Gaming line.** Starting in FY27, NVIDIA folds Gaming, Professional Visualization, Automotive and Robotics into Edge Computing, so there is no Gaming figure for this quarter. The 10-Q still has two reportable segments: Compute & Networking at USD 88,299M and Graphics at USD 7,922M (+46.4% YoY).

**Margins over the last 5 quarters (GAAP)**

| Quarter | Gross margin | Operating margin |
|---|---|---|
| Q2 FY26 | 72.4% | 60.8% |
| Q3 FY26 | 73.4% | 63.2% |
| Q4 FY26 | 75.0% | 65.0% |
| Q1 FY27 | 74.9% | 65.6% |
| Q2 FY27 | 75.0% | 66.2% |

Operating margin is a record. Net margin fell to 62.0% from 71.5% in Q1 because Q1 had a larger equity-investment gain.

**Cash flow**
- Operating cash flow fell to USD 24,077M from USD 50,344M in Q1, because receivables rose by USD 22,349M.
- Days sales outstanding rose from 45 to 60.
- Free cash flow as NVIDIA defines it was USD 21,341M.
- About USD 26,000M went back to shareholders through buybacks and dividends.

**Guidance for Q3 FY27 vs. consensus**
- **Revenue:** USD 108,000M ±2%, 3.7% above consensus of about USD 104,190M (LSEG). The guide still assumes no Data Center compute sales to China.
- **Gross margin:** 74.0% ±50 bps, below the roughly 74.8% the Street expected. Management linked this mainly to higher memory costs.

**Stock reaction**
- The stock closed at USD 209.66 on 2026-08-26 and at USD 227.98 on 2026-08-27, up 8.7%.
- It gave back 4.6% on 2026-08-28.
- It closed at USD 228.52 on 2026-10-13.

**Updated estimates**

| Estimate | Before the print | Now |
|---|---|---|
| Q3 FY27 revenue | USD 104,190M | USD 110,000M |
| Q3 FY27 non-GAAP EPS | USD 2.35 | USD 2.50 |
| FY27 revenue | USD 393,800M | USD 407,800M |
| FY27 non-GAAP EPS | USD 8.85 | USD 9.26 |
| FY28 revenue | USD 520,000M | USD 560,000M |
| FY28 non-GAAP EPS | USD 11.40 | USD 12.25 |

The "before the print" numbers are my own assumed starting model, not a previously published one.

**Thesis impact: positive.** I rate NVIDIA BUY with a price target of USD 306, which is 25x FY28 estimated non-GAAP EPS and 33.9% above the current price.
- Demand is broadening beyond the hyperscalers, and Vera Rubin started shipping on schedule.
- Gross-margin pressure from memory costs and weaker cash conversion are the things to watch.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Fiscal quarter label and period-end date | Q2 FY2027; period end 2026-07-26 | label / date | Q2 FY27 | stock-data get_filings (10-Q, period 2026-07-26); Form 10-Q filed 2026-08-26 | H |
| 10-Q filing date | 2026-08-26 | date | Q2 FY27 | stock-data get_filings (accession 0001045810-26-000075) | H |
| Revenue | 96,221 | USD millions | Q2 FY27 | stock-data get_financials (SEC XBRL); Form 10-Q filed 2026-08-26 | H |
| Revenue growth YoY | 105.9 | % | Q2 FY27 vs Q2 FY26 (46,743) | Calculated from stock-data get_financials | H |
| Data Center revenue | 89,023 | USD millions | Q2 FY27 | Form 10-Q filed 2026-08-26 (via opencapital.sh); release on investingnews.com | H |
| Gross margin | 75.0 (GAAP) | % | Q2 FY27 | stock-data get_financials (72,142 / 96,221); earnings release 2026-08-26 | H |
| GAAP operating income | 63,734 | USD millions | Q2 FY27 | stock-data get_financials; earnings release 2026-08-26 | H |
| GAAP operating margin | 66.2 | % | Q2 FY27 | Calculated from stock-data get_financials | H |
| GAAP diluted EPS | 2.46 | USD | Q2 FY27 | stock-data get_financials; earnings release 2026-08-26 | H |
| Operating cash flow | 24,077 | USD millions | Q2 FY27 | stock-data get_financials (derived 6M less Q1); earnings release 2026-08-26 | H |
| Free cash flow | 21,341 (company definition); 21,400 (OCF less capex) | USD millions | Q2 FY27 | Earnings release 2026-08-26 (poder360 PDF / investingnews.com); stock-data get_financials | H |
| Diluted shares | 24,285 | millions (weighted average) | Q2 FY27 | stock-data get_financials; Form 10-Q filed 2026-08-26 | H |
| Consensus revenue | 92,170 | USD millions | Pre-print, as of 2026-08-26 | https://www.indmoney.com/blog/us-stocks/nvda-stock-rises-nvidia-q2-earnings-analysis (LSEG per Reuters; TIKR says 92,160) | M |
| Consensus EPS | 2.10 (non-GAAP, incl. SBC) | USD | Pre-print, as of 2026-08-26 | https://www.indmoney.com/blog/us-stocks/nvda-stock-rises-nvidia-q2-earnings-analysis (TIKR 2.09; investingLive ~2.08) | M |
| Next-quarter revenue guidance | 108,000 ±2% (105,840 to 110,160) | USD millions | Q3 FY27, guided 2026-08-26 | Earnings release 2026-08-26 (investingnews.com; pulse2.com) | H |
| Stock move on the day after the report | +8.7 (209.66 to 227.98) | % | 2026-08-27 vs 2026-08-26 close | stock-data get_price_history; corroborated by theedgemalaysia.com (Bloomberg) | H |
| Current price | 228.52 | USD | 2026-10-13 close (fetched 2026-10-14 04:06 UTC) | stock-data get_quote | H |
| Rating and price target | BUY; 306 | rating / USD | 2026-10-13 | Own analysis (25x FY28E non-GAAP EPS of USD 12.25) | M |

### 2. Sources used

- **stock-data connector** (on the user's device, Yahoo Finance and SEC XBRL/EDGAR), 8 calls:
  - get_filings: 3 (2 failed because the device bridge was disconnected)
  - get_financials: 3 (income, cash flow and balance sheet, quarterly)
  - get_quote: 1
  - get_price_history: 1
- **WebSearch:** 9 calls.
- **WebFetch:** 15 calls, one of which failed (sec.gov browse-edgar, blocked by robots.txt). Sites fetched:
  - pulse2.com
  - webull.com (no relevant data)
  - indmoney.com
  - investingnews.com (syndicated release)
  - static.poder360.com.br (release PDF)
  - sec.gov (Q4 FY26 release, 8-K exhibit)
  - sec.gov browse-edgar (failed)
  - opencapital.sh (10-Q text)
  - kucoin.com
  - cryptobriefing.com
  - report.az
  - theedgemalaysia.com
  - digrin.com
  - tikr.com
  - investinglive.com
- **Skills:** equity-research:earnings and equity-research:earnings-analysis.
- **ToolSearch:** 1 call.

### 3. Estimates and gaps

**Fiscal calendar and reporting changes**
- **Most recent quarter.** As of 2026-10-13 that is Q2 FY27. Q3 FY27 ends around 2026-10-25 and hasn't been reported.
- **Gaming not available.** From FY27 NVIDIA reports only Data Center (Hyperscale and AI Clouds, Industrial & Enterprise) and Edge Computing. Gaming, Pro Viz, Automotive and OEM aren't disclosed separately. I used Edge Computing (USD 7,198M) and the 10-Q's Graphics segment (USD 7,922M) as proxies. Data Center isn't split into compute and networking either.
- **Non-GAAP definition changed.** From Q1 FY27, non-GAAP results include stock-based compensation. The Q2 FY26 non-GAAP EPS of USD 1.05 is the restated, SBC-inclusive figure taken from third-party sources (INDmoney, investingLive); the original release showed USD 1.01. Consensus EPS of USD 2.10 is on the new basis.

**Consensus figures**
- Consensus comes from secondary reports (INDmoney citing LSEG via Reuters, TIKR, investingLive), not directly from Bloomberg or FactSet. Medium confidence.
- I could not verify the Street gross-margin expectation of about 74.8% or the Data Center consensus of USD 85,080M beyond INDmoney.

**Derived and calculated figures**
- **Quarterly cash flow** is year-to-date less Q1.
- **Q4 FY26 figures** are full year less nine months, from the stock-data connector.
- **Free cash flow:** the company figure (USD 21,341M) also deducts USD 59M of principal payments. Operating cash flow less capex is USD 21,400M.
- **DSO** is my own calculation: period-end receivables ÷ quarterly revenue × 91.

**Call commentary and unverified claims**
- I didn't read the earnings-call transcript directly. Commentary comes from TIKR and other summaries:
  - Rubin at about 20% of Q3 Data Center revenue
  - Gross margin possibly bottoming at 71-72% in Q4 FY27
  - Supply constraints
- TIKR also mentions about 70% FY28 revenue growth guidance. I couldn't verify that and didn't use it.
- The "Supply (our interpretation)" driver of the beat is my judgment, not a company statement.
- The USD 442bn market-value gain on 2026-08-27 is as reported (The Edge / Bloomberg; report.az). Other outlets said about USD 300bn.

**My estimates, rating and price target**
- **Q3 FY27:** revenue USD 110,000M, 74.0% gross margin, USD 9,000M non-GAAP opex, USD 500M other income, 17% tax rate, 24,200M shares, giving EPS of USD 2.50.
- **Q4 FY27:** revenue USD 120,000M, 72.5% gross margin, USD 9,700M opex, giving EPS of USD 2.67.
- **FY27:** revenue USD 407,800M, EPS USD 9.26.
- **FY28:** revenue USD 560,000M, 63% non-GAAP operating margin, 17% tax rate, 24,000M shares, giving EPS of USD 12.25.
- **Pre-print baseline** (FY27 USD 393,800M / EPS USD 8.85; FY28 USD 520,000M / EPS USD 11.40; Q3 EPS USD 2.35) is an assumed starting model, since no prior published estimates were available in this session.
- **Rating and target** (BUY, USD 306 at 25x FY28E EPS) and the bear case (USD 210) and bull case (USD 405) are my own illustrative views, not a broker consensus.

**Other defaults and notes**
- Report format: DOCX, Times New Roman body text, 10 pages, 11 charts, 3 tables. It runs about 2,700 words, a little under the skill's 3,000-word target.
- The press release was read through syndicated copies (investingnews.com, a poder360 PDF) and the 10-Q through opencapital.sh. NVIDIA's own investor-relations site wasn't fetched directly.
- A shared scratchpad file was overwritten by another process mid-run. I rebuilt the script in a private subfolder. There's no impact on the deliverable.

### 4. Freshness

- Latest market price: USD 228.52, the 2026-10-13 close (stock-data get_quote, fetched 2026-10-14 04:06 UTC).
- Latest financial reporting period: Q2 FY27, ended 2026-07-26 (10-Q filed 2026-08-26).

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 11 | Read rules/prompt; `date -u` ×2; library check; build script runs and patches; DOCX→PDF page/word check; listing |
| Skill | 2 | equity-research:earnings; equity-research:earnings-analysis |
| ToolSearch | 1 | `select:mcp__remote-devices__stock-data__get_quote,get_financials,get_filings,get_price_history` |
| WebSearch | 9 | Q2 FY27 results; vs estimates/LSEG; official release title; Q4 FY26 results; Aug 27 stock move ×3; 10-Q filing; price on 2026-10-13 |
| WebFetch | 15 | pulse2, webull, indmoney, investingnews, poder360 PDF, sec.gov q4fy26pr, sec.gov browse-edgar (failed), opencapital.sh 10-Q, kucoin, cryptobriefing, report.az, theedgemalaysia, digrin, tikr, investinglive |
| mcp__remote-devices__stock-data__get_filings | 3 | 2 failed (bridge disconnected), 1 succeeded (10-Q list) |
| mcp__remote-devices__stock-data__get_financials | 3 | income, cash flow, balance sheet (quarterly, 2y) |
| mcp__remote-devices__stock-data__get_quote | 1 | NVDA |
| mcp__remote-devices__stock-data__get_price_history | 1 | 6 months, daily |
| Write | 3 | build script ×2 (scratchpad), transcript.md |
| Read | 2 | rendered PDF page images (QA) |

Files delivered (in /home/claude/results/2026-10-13/runs/ER-03/B/):
- NVIDIA_Q2_FY27_Earnings_Update.docx
- charts/f1_revenue.png, f2_eps.png, f3_margins.png, f4_platform.png, f5_beat.png, f6_guide.png, f7_cash.png, f8_dso.png, f9_estimates.png, f10_price.png, f11_val.png
- transcript.md
