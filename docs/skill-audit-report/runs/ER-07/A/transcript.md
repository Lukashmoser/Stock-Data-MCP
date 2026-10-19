# ER-07 / Arm A transcript

- Start: Wed Oct 14 07:49:13 UTC 2026
- End: Wed Oct 14 07:53:11 UTC 2026

## Final reply to user

**MSFT model update: FY2026Q4 (quarter ended 2026-06-30) actuals plugged in, estimates rolled forward to FY2027**

Updated workbook: `MSFT_quarterly_model_updated.xlsx`, in the run folder. The original file is unchanged.

### What changed in the workbook
- **Quarterly IS, FY2026Q4:** this column is now actual (A). Reported revenue, cost of revenue, opex (R&D + S&M + G&A), other income, tax and diluted shares are entered as blue hardcodes. Gross profit, operating income, net income, EPS and the ratios are formulas, as in the other actual columns. The Q1–Q3 actuals already in the model tie exactly to the reported FY2026 annual totals (revenue $331,839mm, opex $70,228mm, tax $32,185mm).
- **New "Est vs Actual" tab:**
  - prior estimate vs actual for FY2026Q4, with deltas;
  - an estimate-revision table: FY2027Q1E, FY2027E, NTM EPS and target price, old vs new;
  - guidance and context notes from the call.
- **Assumptions tab:** revised inputs, with the prior values kept in column D and the reason for each change in column E.
  - Revenue growth raised from 12% to **16.4%**. This is the midpoint of the FY27Q1 guide ($89.85–90.95bn) against FY26Q1 revenue.
  - Opex growth raised from 6% to **10%**. FY26Q3 opex grew +9.4% and FY26Q4 +9.8%.
  - Tax rate raised from 18% to **19%**. The FY26 effective rate was 19.4%.
  - Gross margin method changed from the trailing-4Q average to **the latest actual quarter (67.2%) held flat**. GM has now declined for four quarters in a row.
  - Unchanged: share reduction 0.3% per quarter, other income 0 and P/E 30x.
- **Annual Summary:** FY2026 is now 4A. FY2027E is 4E.
- **Valuation:** the NTM window moved forward to FY2027Q1E–Q4E. I also added the prior target price, the % change, the current price, upside and implied P/E.
- The model recalculates with no formula errors.

### FY2026Q4: estimate vs actual (USD mm except per share)
| Metric | Prior est. | Actual | Delta % |
|---|---|---|---|
| Revenue | 85,614 | 90,007 | +5.1% |
| Gross profit | 58,496 | 60,482 | +3.4% |
| Gross margin | 68.3% | 67.2% | -1.1 pts |
| Operating income | 39,305 | 40,603 | +3.3% |
| Other income | 0 | 3,444 | n/m |
| Net income | 32,230 | 35,766 | +11.0% |
| Diluted EPS ($) | 4.34 | 4.81 | +10.8% |
| Diluted shares (mm) | 7,423 | 7,443 | +0.3% |

### Estimate roll-forward
| Metric | Prior | New | Change |
|---|---|---|---|
| FY2027Q1E revenue | 86,994 | 90,411 | +3.9% |
| FY2027Q1E EPS ($) | 4.74 | 4.75 | +0.2% |
| FY2027E revenue | 366,739 | 386,261 | +5.3% |
| FY2027E op. margin | 48.0% | 47.2% | -0.8 pts |
| FY2027E EPS ($) | 19.61 | 19.99 | +1.9% |
| NTM EPS ($) | 18.92 | 19.99 | +5.7% |
| Target price ($) | 567.58 | 599.76 | +5.7% |

At $541.15 (close on 2026-10-12), the new target implies **+10.8% upside**. The stock trades at 27.1x NTM EPS.

### What changes the thesis
1. **Growth is stronger than the model assumed. This is positive.**
   - Revenue grew +17.7% YoY against the 12% the model used.
   - Intelligent Cloud grew +31.6%.
   - Management guides Azure to +45% in constant currency for FY27Q1, and total revenue to +16–17%.
   - The top-line thesis has strengthened. The old 12% growth rate is no longer credible.
2. **Gross margin keeps falling. This is the main risk.**
   - FY26Q4 GM was 67.2%, 113 bp below the model. GM has declined four quarters in a row: 69.0% → 68.0% → 67.6% → 67.2%.
   - With AI infrastructure depreciation building, the new estimates no longer assume GM recovers.
   - Operating income beat by only 3.3% against a 5.1% revenue beat.
3. **The EPS beat is lower quality than it looks.**
   - About $3.4bn of other income, including a $3.2bn gain on the Anthropic investment, plus ~$0.27 of net discrete benefits drove much of the +10.8% EPS beat.
   - Non-GAAP EPS was $4.74, against about $4.24 consensus.
   - FY27Q1E EPS barely moves ($4.74 → $4.75) despite +3.9% more revenue. Lower GM, faster opex growth and a higher tax rate absorb the revenue upside.
4. **Opex growth has sped up to about 10%.** Management also flagged slightly lower operating margins in FY27. My model still has the FY27 operating margin at 47.2%, up from 46.8% in FY26. If management's comment proves right, FY27 EPS has downside risk.
5. **Capex.** The CY2026 capex guide was reportedly cut to about $175bn from about $190bn, with about $50bn in FY27Q1. This would support free cash flow. It comes from a single secondary source.
6. **Valuation.** The target rises 5.7% to $599.76. The stock has reportedly re-rated from $390.54 on 2026-07-29 to about $541, so upside is now about 11% rather than the much larger gap that existed at the print. The thesis is intact. The risk/reward is now more balanced.

Sources: [8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm), [INDmoney Q4 recap](https://www.indmoney.com/blog/us-stocks/microsoft-q4-results-why-msft-stock-jumped), [Investing.com MSFT quote](https://www.investing.com/equities/microsoft-corp), [Trading Economics](https://tradingeconomics.com/msft:us/news/567251).

## Comparison Block

### 1. Key figures
| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Quarter updated | FY2026Q4 (quarter ended 2026-06-30) | n/a | 2026-06-30 | 8-K Ex. 99.1 (accession 0001193125-26-323632) | H |
| Filing date of quarter | 2026-07-29 | date | 2026-07-29 | 8-K Ex. 99.1 press release date (sec.gov URL above) | M |
| Revenue: prior estimate | 85,614 | USD mm | FY2026Q4 | Attached model (recalculated) | H |
| Revenue: actual | 90,007 | USD mm | FY2026Q4 | 8-K Ex. 99.1, filed 2026-07-29 | H |
| Revenue: delta % | +5.1 | % | FY2026Q4 | Computed | H |
| Gross profit: prior estimate | 58,496 | USD mm | FY2026Q4 | Attached model | H |
| Gross profit: actual | 60,482 | USD mm | FY2026Q4 | 8-K Ex. 99.1, filed 2026-07-29 | H |
| Gross profit: delta % | +3.4 | % | FY2026Q4 | Computed | H |
| Operating income: prior estimate | 39,305 | USD mm | FY2026Q4 | Attached model | H |
| Operating income: actual | 40,603 | USD mm | FY2026Q4 | 8-K Ex. 99.1, filed 2026-07-29 | H |
| Operating income: delta % | +3.3 | % | FY2026Q4 | Computed | H |
| Net income: prior estimate | 32,230 | USD mm | FY2026Q4 | Attached model | H |
| Net income: actual | 35,766 | USD mm | FY2026Q4 | 8-K Ex. 99.1, filed 2026-07-29 | H |
| Net income: delta % | +11.0 | % | FY2026Q4 | Computed | H |
| Diluted EPS: prior estimate | 4.34 | USD | FY2026Q4 | Attached model | H |
| Diluted EPS: actual | 4.81 | USD | FY2026Q4 | 8-K Ex. 99.1, filed 2026-07-29 | H |
| Diluted EPS: delta % | +10.8 | % | FY2026Q4 | Computed | H |
| Diluted shares: prior estimate | 7,423 | mm shares | FY2026Q4 | Attached model | H |
| Diluted shares: actual | 7,443 | mm shares | FY2026Q4 | 8-K Ex. 99.1, filed 2026-07-29 | H |
| Diluted shares: delta % | +0.3 | % | FY2026Q4 | Computed | H |
| New next-quarter revenue estimate | 90,411 | USD mm | FY2027Q1E (2026-09-30) | Updated model | M |
| New next-quarter EPS estimate | 4.75 | USD | FY2027Q1E (2026-09-30) | Updated model | M |
| New next-FY revenue estimate | 386,261 | USD mm | FY2027E (FYE 2027-06-30) | Updated model | M |
| New next-FY EPS estimate | 19.99 | USD | FY2027E (FYE 2027-06-30) | Updated model | M |
| Old target price | 567.58 | USD | Model as of late July 2026 | Attached model (NTM EPS 18.92 x 30) | H |
| New target price | 599.76 | USD | 2026-10-14 | Updated model (NTM EPS 19.99 x 30) | M |

### 2. Sources used
- Skill equity-research:model-update: 1 load
- WebSearch: 4 calls
- WebFetch: 4 calls
  - sec.gov 8-K Ex. 99.1: 1
  - indmoney.com: 1
  - tradingeconomics.com: 1
  - investing.com: 1
- Bash: 10 calls
  - the curl to data.sec.gov was blocked by the proxy (403)
  - LibreOffice was used for recalculation
- Write: 2 calls
- Attached workbook MSFT_quarterly_model.xlsx: read
- stock-data tools: not used (disabled)

### 3. Estimates and gaps
- **FY2026Q4 opex** = R&D 9,997 + S&M 7,595 + G&A 2,287 = 19,879.
- **Diluted EPS rounding:** the model computes Q4 EPS as $4.805 (NI / shares) against the reported $4.81. FY2026 annual EPS computes as $17.94 against the reported $17.95, because the model uses the average of quarterly share counts.
- **Prior estimates** are the original model's recalculated values. They are hardcoded on the "Est vs Actual" tab.
- **Revenue growth** (default): 16.4% for all FY2027 quarters. This is the FY27Q1 guide midpoint of $90.4bn against $77,673mm. No deceleration is assumed in later quarters.
- **Gross margin** (default): the FY2026Q4 actual of 67.2% is held flat. This replaces the trailing-4Q average.
- **Opex growth** (default): 10% YoY.
- **Tax rate** (default): 19.0%.
- **Unchanged:** other income 0, diluted share reduction 0.3% per quarter, target P/E 30x.
- **Unverified secondary-source items:** guidance figures (revenue range, segment ranges, Azure +45% cc, capex ~$50bn and ~$175bn) and the ~$4.24 consensus EPS came only from the indmoney.com recap. They were not checked against the call transcript.
- **Management margin comment:** the "op margin down slightly in FY27" comment is not reflected in the model, which shows 47.2% against 46.8% in FY26. This is flagged as a risk.
- **8-K filing date:** inferred from the press release date (2026-07-29). The EDGAR filing index could not be reached.
- **Share price:** $541.15 (close 2026-10-12) comes from Investing.com only. It is a large move from $390.54 on 2026-07-29, and Trading Economics shows inconsistent figures (395.58 on 2026-07-15 and an undated 535.07). Treat it with medium/low confidence. It affects only the upside calculation, not the target.
- **No balance sheet or cash flow:** the model has neither, so the capex and FCF implications are qualitative only.

### 4. Freshness
- Latest market price used: 2026-10-12 close ($541.15).
- Latest financial reporting period used: FY2026Q4, the quarter ended 2026-06-30 (8-K dated 2026-07-29).

## Run log
| Tool | Calls | Notes |
|---|---|---|
| Bash | 10 | start/end `date -u`; read rules and prompt; curl to data.sec.gov (blocked, 403); dump workbook; check tools; recalc original via LibreOffice; inspect styles; build and recalc the updated model; verify and copy |
| Skill | 1 | equity-research:model-update |
| WebSearch | 4 | FY26Q4 results; FY27Q1 guidance; MSFT price Oct 2026; MSFT close 2026-10-12 |
| WebFetch | 4 | sec.gov msft-ex99_1.htm; indmoney.com Q4 recap; tradingeconomics.com; investing.com |
| Write | 2 | scratchpad update.py; transcript.md |
| ToolSearch | 0 | none |

Files delivered:
- /home/claude/results/2026-10-13/runs/ER-07/A/MSFT_quarterly_model_updated.xlsx
- /home/claude/results/2026-10-13/runs/ER-07/A/transcript.md
