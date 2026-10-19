# Transcript: ER-07 / arm B

- Start: 2026-10-14T07:49:15Z (`date -u`: Wed Oct 14 07:49:15 UTC 2026)
- End: 2026-10-14T07:51:08Z (`date -u`: Wed Oct 14 07:51:08 UTC 2026)

## Final reply to user

I updated the MSFT model for **FY2026Q4** (quarter ended 2026-06-30). It was reported on 2026-07-29 in the earnings 8-K (Item 2.02) and the Form 10-K filed the same day. FY2027Q1 (September quarter) has not been reported yet; Microsoft usually reports it in late October.

**Updated workbook:** `/home/claude/results/2026-10-13/runs/ER-07/B/MSFT_quarterly_model_updated_FY26Q4.xlsx`. The original file is unchanged. The workbook has been fully recalculated and has no formula errors.

What changed in the workbook:
- **Quarterly IS:** column J (FY2026Q4) now holds the reported actuals and is marked "A". Gross profit, margins, tax rate, net income and EPS are still formulas.
- **Annual Summary:** FY2026 is now 4 actual quarters. FY2027E is 4 estimate quarters.
- **Valuation:** the next-twelve-months window moved forward to FY2027Q1E–FY2027Q4E. I also added the old target price, the change in target price, the share price, upside and the implied P/E.
- **Est vs Actual (new tab):** compares the prior estimate with the actual for each line item, and shows how the key estimates and the target price were revised.
- **Assumptions:** the estimate rules are unchanged. I added an update log.

### Estimate vs. actual, FY2026Q4

| Line | Prior est. | Actual | Delta % |
|---|---|---|---|
| Revenue | 85,613.9 | 90,007.0 | +5.1% |
| Gross profit | 58,495.6 | 60,482.0 | +3.4% (GM 67.2% vs 68.3% est, -1.1 pts) |
| Operating income | 39,305.4 | 40,603.0 | +3.3% (OM 45.1% vs 45.9%) |
| Net income | 32,230.4 | 35,766.0 | +11.0% |
| Diluted EPS ($) | 4.34 | 4.81 | +10.7% |
| Diluted shares (mm) | 7,422.7 | 7,441.0 | +0.2% |

About 40% of the net income beat came from non-operating items. Other income was $3,444mm against $0 in the model, which adds roughly $0.38 of EPS before tax effects. The tax rate was 18.8% against 18.0% in the model.

### Roll-forward

| Item | Old | New | Change |
|---|---|---|---|
| FY2027Q1E revenue | 86,993.8 | 86,993.8 | 0.0% |
| FY2027Q1E EPS ($) | 4.74 | 4.70 | -0.8% |
| FY2027E revenue | 366,739.4 | 371,659.7 | +1.3% |
| FY2027E EPS ($) | 19.61 | 19.68 | +0.4% |
| NTM EPS ($) | 18.92 | 19.69 | +4.1% |
| Target price ($, 30x NTM) | 567.58 | 590.60 | +4.1% |

At $543.45 (2026-10-14) the new target is 8.7% above the current price. The stock trades at 27.6x the new NTM EPS.

The target rose mostly because the valuation window moved forward by one quarter. The FY2026Q4 beat itself changed the forward estimates very little. The FY2027Q1 EPS estimate fell slightly because the share-count base rose and the trailing gross margin went down.

### Flags that matter for the thesis

1. **Revenue growth assumption looks too conservative.** FY2026 revenue grew 17.8%, and FY2026Q4 grew 17.7% year over year. The model's 12% rule gives FY2027Q1E revenue of $86,994mm, which is 3.3% *below* the June quarter just reported. Last year the same seasonal step was +1.6% (FY2025Q4 to FY2026Q1). At 17% growth, NTM EPS would be about $20.93 and the target about $628. I kept the 12% rule as the default but think it should be revisited.
2. **Gross margin keeps falling.** It was 69.1% in FY2026Q1, 68.0% in Q2, 67.6% in Q3 and 67.2% in Q4. FY2026 gross margin was 67.9% against 68.8% in FY2025. This is consistent with depreciation from AI data-center spending growing faster than revenue. The trailing-average rule (about 67.6–68.0% for FY2027E) lags the trend, so there is downside risk to margins if the decline continues.
3. **Operating costs grew faster than modeled.** FY2026Q4 operating expenses rose 9.8% year over year against the 6% rule. Even so, the operating margin held at 45.1%, and FY2026 operating margin was 46.8%, up 1.2 pts. Operating leverage is intact for now.
4. **Earnings quality.** FY2026 other income was $10,697mm, including +$9,971mm in Q2 and +$3,444mm in Q4. The model assumes zero going forward, so year-over-year EPS growth in FY2027E looks lower than the growth in underlying operations.
5. **Net effect on the thesis:** the story is unchanged and slightly better. Revenue beat, operating income beat, and the target rises 4.1%. The main risk is margin pressure from AI capital spending (gross margin), not demand.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Quarter updated | FY2026Q4 (quarter ended 2026-06-30) | n/a | 2026-06-30 | stock-data get_financials (quarterly) | H |
| Filing date | 2026-07-29 (Form 10-K; earnings 8-K Item 2.02 same day) | date | 2026-07-29 | stock-data get_filings (10-K filed 2026-07-29; 8-K filed 2026-07-29) | H |
| Revenue: prior estimate | 85,613.9 | USD mm | FY2026Q4 | Original model (MSFT_quarterly_model.xlsx) | H |
| Revenue: actual | 90,007.0 | USD mm | FY2026Q4 | stock-data get_financials (10-K filed 2026-07-29; Q4 = FY - 9M) | H |
| Revenue: delta % | +5.1% | % | FY2026Q4 | Calculated | H |
| Gross profit: prior estimate | 58,495.6 | USD mm | FY2026Q4 | Original model | H |
| Gross profit: actual | 60,482.0 | USD mm | FY2026Q4 | stock-data get_financials (10-K filed 2026-07-29) | H |
| Gross profit: delta % | +3.4% | % | FY2026Q4 | Calculated | H |
| Operating income: prior estimate | 39,305.4 | USD mm | FY2026Q4 | Original model | H |
| Operating income: actual | 40,603.0 | USD mm | FY2026Q4 | stock-data get_financials (10-K filed 2026-07-29) | H |
| Operating income: delta % | +3.3% | % | FY2026Q4 | Calculated | H |
| Net income: prior estimate | 32,230.4 | USD mm | FY2026Q4 | Original model | H |
| Net income: actual | 35,766.0 | USD mm | FY2026Q4 | stock-data get_financials (10-K filed 2026-07-29) | H |
| Net income: delta % | +11.0% | % | FY2026Q4 | Calculated | H |
| Diluted EPS: prior estimate | 4.34 | USD | FY2026Q4 | Original model | H |
| Diluted EPS: actual | 4.81 | USD | FY2026Q4 | Calculated: NI 35,766 / derived shares 7,441 (Q4 EPS not in XBRL) | M |
| Diluted EPS: delta % | +10.7% | % | FY2026Q4 | Calculated | M |
| Diluted shares: prior estimate | 7,422.7 | mm shares | FY2026Q4 | Original model | H |
| Diluted shares: actual | 7,441.0 | mm shares | FY2026Q4 | Derived: 4 x FY2026 weighted diluted shares 7,453 - (7,466+7,460+7,445), stock-data get_financials | M |
| Diluted shares: delta % | +0.2% | % | FY2026Q4 | Calculated | M |
| New next-quarter revenue estimate | 86,993.8 | USD mm | FY2027Q1E (quarter ending 2026-09-30) | Updated model | M |
| New next-quarter EPS estimate | 4.70 | USD | FY2027Q1E | Updated model | M |
| New next-fiscal-year revenue estimate | 371,659.7 | USD mm | FY2027E (FY ending 2027-06-30) | Updated model | M |
| New next-fiscal-year EPS estimate | 19.68 | USD | FY2027E | Updated model | M |
| Old target price | 567.58 | USD | Model as of late July 2026 (NTM FY2026Q4E-FY2027Q3E) | Original model | H |
| New target price | 590.60 | USD | 2026-10-14 (NTM FY2027Q1E-FY2027Q4E x 30) | Updated model | M |

### 2. Sources used
- stock-data MCP `get_financials`: 2 calls (quarterly income statement; annual income statement)
- stock-data MCP `get_filings`: 3 calls (all forms; 10-K; 8-K)
- stock-data MCP `get_quote`: 1 call (MSFT price $543.45)
- WebFetch on the SEC 8-K primary document (https://www.sec.gov/Archives/edgar/data/789019/000119312526323632/msft-20260729.htm): 1 call. It confirmed the 2026-07-29 earnings release but contained no figures.
- The attached workbook MSFT_quarterly_model.xlsx (read with openpyxl and recalculated with LibreOffice).

### 3. Estimates and gaps
- **FY2026Q4 diluted shares (7,441mm) are derived, not reported.** The figure is 4 x FY2026 weighted diluted shares minus the Q1–Q3 counts. FY2026Q4 diluted EPS ($4.81) is therefore calculated. As a check, the quarterly EPS sums to $17.96 against the reported FY2026 diluted EPS of $17.95.
- **FY2026Q4 figures come from subtraction.** Every Q4 line item is FY2026 annual minus 9 months (derived by the tool). Other income (+$3,444mm) is pretax income minus operating income.
- **Exhibit 99.1 (the press release) was not read.** That means no management guidance, segment detail or non-GAAP figures were used or checked.
- **Default: the estimate rules were left unchanged.** These are 12% revenue growth, 6% opex growth, an 18% tax rate, zero other income, 0.3% share reduction per quarter, trailing-4-quarter gross margin, and 30x NTM P/E. The roll-forward changes only the actual base and the NTM window.
- **Default: next quarter = FY2027Q1; next fiscal year = FY2027.** NTM = FY2027Q1E–FY2027Q4E.
- **Sensitivity (not in the base case):** at 17% revenue growth, NTM EPS is about $20.93 and the target about $628.04.
- **Old and prior estimates** were taken from the original workbook's formulas as they evaluate before the update.
- **Share price** is the stock-data quote fetched at 2026-10-14T07:49Z. It may be delayed or reflect the prior close.
- **Formatting:** the updated file was recalculated through LibreOffice so that values are cached. The original file is preserved unchanged.

### 4. Freshness
- Latest market price: $543.45 as of 2026-10-14
- Latest financial reporting period: FY2026Q4, quarter ended 2026-06-30 (10-K filed 2026-07-29)

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 7 | read rules, prompt and run folder; date -u (x2); dump workbook; check tooling and cached values; build workbook (python/openpyxl); recalculate and verify (LibreOffice); sensitivity run and finalize |
| Skill | 1 | equity-research:model-update |
| ToolSearch | 1 | select:mcp__remote-devices__stock-data__get_financials,get_filings,get_quote |
| mcp__remote-devices__stock-data__get_financials | 2 | MSFT quarterly income; MSFT annual income |
| mcp__remote-devices__stock-data__get_filings | 3 | all forms; 10-K; 8-K |
| mcp__remote-devices__stock-data__get_quote | 1 | MSFT |
| WebFetch | 1 | SEC 8-K 2026-07-29 primary document |
| Write | 1 | transcript.md |

Files delivered:
- /home/claude/results/2026-10-13/runs/ER-07/B/MSFT_quarterly_model_updated_FY26Q4.xlsx
- /home/claude/results/2026-10-13/runs/ER-07/B/transcript.md
