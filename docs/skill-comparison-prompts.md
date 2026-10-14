# Skill comparison prompts: with vs. without Stock-Data-MCP

This file has one test prompt for every skill in the **Equity Research** and **Financial Analysis** plugins. Each prompt runs twice: once with the `stock-data` MCP server off and once with it on. Every prompt ends with the same **Comparison Block** footer, so the two runs produce the same table of figures and can be compared row by row.

Contents:

1. [Test protocol](#1-test-protocol)
2. [Test universe](#2-test-universe)
3. [Reference snapshot (ground truth)](#3-reference-snapshot-ground-truth)
4. [Fixtures for file-based skills](#4-fixtures-for-file-based-skills)
5. [Equity Research prompts](#5-equity-research-prompts)
6. [Financial Analysis prompts](#6-financial-analysis-prompts)
7. [Scoring and comparison](#7-scoring-and-comparison)

---

## 1. Test protocol

### Arms

| Arm | `stock-data` MCP | Web search | Everything else |
|---|---|---|---|
| **A: baseline** | **Off** | On | Same |
| **B: with MCP** | **On** | On | Same |

Web search stays on in both arms. Without it the baseline can only answer from memory, so the test would show how much better live data is than memory, not how much the MCP adds over what Claude can already reach. An optional **arm A0** (MCP off, web off) shows the memory-only floor.

To turn the server off for arm A, toggle `stock-data` off in the chat's tools menu, or remove it from `claude_desktop_config.json` and restart Claude. Check that it's really off: Claude should list no `get_quote`, `get_financials` or similar tools.

### Rules that keep the runs comparable

1. **Same day, close together.** Run both arms of a test within about an hour of each other, since prices move. Record the start time of each run.
2. **Fresh chat per run.** Start a new chat for every prompt and arm, so no data carries over from an earlier answer.
3. **Same model and plugins in both arms.** Keep other data connectors identical. The plugins' bundled `.mcp.json` lists paid providers (FactSet, S&P Kensho, Daloopa, and others); make sure none of them is authenticated in either arm, or the skills will use them instead.
4. **Paste prompts exactly as written**, footer included. The prompts never mention the MCP, so arm B also tests whether the skill finds the tools by itself.
5. **Same reply at every checkpoint.** Several skills stop to confirm a plan. Answer with the canned replies below, word for word, in both arms:
   - **C1 (any confirmation or clarifying question):** `Proceed with your recommended defaults and don't stop for further confirmation. List the assumptions you made under "Estimates and gaps" in the Comparison Block.`
   - **C2 (deck-refresh approval gate):** `Approved. Apply every change in the plan, including the flagged derived numbers.`
   - **C3 (the reply ended without a Comparison Block):** `Please add the Comparison Block now, exactly as specified at the end of my first message.`
6. **Log tool use in arm B.** Note whether the `stock-data` tools were called, and which ones. If arm B never called them, record **"MCP not invoked"**. That is a finding in itself: the skill didn't pick up the tools.
7. **Save everything.** Suggested layout, kept outside the test chats:

   ```
   results/<run-date>/
     reference/R0.md
     ER-03/A/transcript.md   + any .xlsx/.docx/.pptx produced
     ER-03/B/transcript.md   + files
     ...
     scorecard.md
   ```

8. **Optional: repeat runs.** If budget allows, run each arm twice. A gap between arms only counts if it's larger than the gap between two runs of the same arm. **FA-10** (ppt-template-creator) uses no market data and serves as the control: any difference there is run-to-run noise.

### The Comparison Block footer

Every prompt ends with this footer. Only the `Key figures:` line changes from test to test.

```
---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: <test-specific list>
```

---

## 2. Test universe

All prompts use these tickers, so results can also be checked against each other (the ADBE revenue in ER-03 should match the ADBE revenue in FA-04). If a ticker has been acquired or delisted by the time you run the tests, swap in the alternate and make the same swap in both arms.

| Role | Ticker | Alternate | Why it was chosen |
|---|---|---|---|
| Primary company | **ADBE** | ORCL | Fiscal year ends late Nov/early Dec (52/53-week), so fiscal labels don't match calendar years |
| Comps peers | **CRM, NOW, INTU, WDAY, ADSK** | TEAM, HUBS | Fiscal years end Jan, Dec, Jul, Jan and Jan, so LTM figures must be aligned |
| Initiation target | **DDOG** | SNOW | Less covered in training data than mega-caps, so memory helps less |
| Next to report | **MSFT** | GOOGL | Reports in late October |
| LBO target | **DBX** | DOCU | Cash-generative, low growth, plausible take-private |
| Recent IPO, short history | **FIG** (Figma) | — | Edge case: few XBRL periods on file |
| Private competitor | Canva | — | No public data: should be N/A in **both** arms |
| Screen universe (15) | ADBE CRM NOW INTU WDAY ADSK DDOG TEAM HUBS SNOW PANW CRWD FTNT ZS DOCU | — | Many tickers per prompt |
| Benchmarks | **^GSPC, QQQ, IGV** | — | Index and ETF tickers |
| Macro (FRED) | **DGS10, SOFR, BAMLH0A0HYM2, T10Y2Y, CPIAUCSL** | — | 10y Treasury, SOFR, high-yield spread, curve slope, CPI |

---

## 3. Reference snapshot (ground truth)

Run this **once on test day, in arm B**, before the tests. It calls the MCP tools directly and gives you the reference values to score both arms against. Spot-check five values by hand (two on sec.gov, two on Yahoo Finance, one on FRED). When the reference itself is wrong, the bug is in the MCP: note it and open an issue on this repo.

### R0: Reference snapshot

```
Using only the stock-data tools (no web search, no memory), build a reference data sheet. Make every call explicitly and show the raw values; don't round beyond one decimal.

1. get_quote for: ADBE CRM NOW INTU WDAY ADSK DDOG MSFT DBX FIG TEAM HUBS SNOW PANW CRWD FTNT ZS DOCU ^GSPC QQQ IGV. Table: ticker, price, change %, market cap, 52-week low, 52-week high.
2. get_financials for ADBE, all three statements, annual, 5 years. Then income statement, quarterly, 2 years.
3. get_financials, income + cashflow, annual, 3 years, for CRM NOW INTU WDAY ADSK DDOG DBX FIG. Table per ticker: fiscal-year labels, revenue, operating income, net income, diluted EPS, operating cash flow, capex, free cash flow, diluted shares.
4. get_financials, balance, annual, 1 year, for the same tickers plus ADBE: cash, short-term investments, short-term debt, long-term debt.
5. get_filings for ADBE, MSFT, DDOG, DBX: latest 10-K, latest 10-Q, latest 3 8-Ks (form, filing date, period).
6. get_price_history for ADBE, QQQ, IGV, ^GSPC: 1y daily. Report the start close, end close and total return.
7. get_macro_series latest value and date for DGS10, SOFR, BAMLH0A0HYM2, T10Y2Y; CPIAUCSL YoY % for the latest month.
Finish with a list of any tool errors or stale-data flags.
```

Save the output as `reference/R0.md`.

---

## 4. Fixtures for file-based skills

Some skills work on a file the user provides (a model to audit, a deck to refresh). Both arms must get the **identical** file, so build each fixture **once, in a separate setup chat with the MCP on** (so its numbers are real), then freeze it.

- Save fixtures to `fixtures/` and upload the same copy in both arms.
- **Never upload an answer key to a test chat.** Keys stay with you for scoring.
- Give fixture files neutral names. A name like `model_with_errors.xlsx` tells the skill what to look for.

| ID | File(s) | Used by |
|---|---|---|
| F1 | `ADBE_model.xlsx` + `F1_key.md` | FA-05 audit |
| F2 | `quarterly_export.csv` + `F2_key.md` | FA-07 clean data |
| F3 | `ADBE_snapshot.pptx` + `F3_key.md` | FA-08 deck refresh |
| F4 | `Project_Canvas.pptx` + `F4_key.md` | FA-09 deck QC |
| F5 | `Northwind_template.pptx` | FA-10 template skill |
| F6 | `3S_template.xlsx` | FA-01 3-statement model |
| F7 | `ADBE_quarterly_model.xlsx` + `F7_key.md` | ER-07 model update |

### F1: Seeded model for the audit test

```
Build an Excel 3-statement model for Adobe (ADBE) and save it as ADBE_model.xlsx: historicals FY2022 to FY2025 from SEC data (use the stock-data tools), projections FY2026 to FY2030 driven by an Assumptions tab, live formulas throughout, blue inputs and black formulas, a Checks row showing the balance sheet balances, and a small valuation block (share price, diluted shares, market cap, net debt, EV/Revenue).

Once it works, plant exactly these 7 errors. Don't mark them in the workbook (no comments, colours or notes that give them away):
Data errors (only detectable against external data):
 D1. FY2024 revenue hardcode set 8% above the reported value.
 D2. Diluted shares in the valuation block set to the FY2022 count instead of the latest.
 D3. FY2025 ending cash typed as the FY2024 value.
Formula errors (detectable from the workbook alone):
 M1. FY2027 total current assets: SUM range skips the receivables row.
 M2. FY2028 revenue replaced by a hardcoded number equal to its current formula result.
 M3. FY2029 retained earnings adds prior-year instead of current-year net income, so the balance sheet stops balancing (leave the Checks row formula intact).
 M4. FY2030 D&A references the capex row.

Then write F1_key.md listing each error: ID, sheet, cell, what's wrong, the correct value or formula.
```

### F2: Messy data export for the cleaning test

```
Use the stock-data tools to get revenue, operating income and net income (USD millions) for ADBE, CRM, NOW and INTU for each of their last 8 reported quarters. Write them as a long-format CSV, quarterly_export.csv, with columns: ticker, period_end, fiscal_label, metric, value.

Then make it messy the way a real export is:
 - three date formats mixed in period_end (2025-08-29, 08/29/2025, 29-Aug-25)
 - tickers with inconsistent casing and stray whitespace (" adbe", "Crm ")
 - values as text with "$" and thousands separators in about a third of rows
 - 3 exact duplicate rows and 1 near-duplicate (same key, value differs by rounding)
 - a "notes" column mixing numbers, text and blanks
 - CRM values for 2 quarters expressed in thousands instead of millions
 - 2 values replaced with wrong but plausible numbers (±12%), in different tickers

Write F2_key.md listing every perturbation with row numbers and the original values.
```

### F3: Stale deck for the refresh test

```
Create a 6-slide PowerPoint, ADBE_snapshot.pptx, titled "Adobe (ADBE) Company Snapshot", as of the end of Adobe's fiscal 2024. Use real values for that point in time from the stock-data tools (statement data for FY2020-FY2024; share price = the close on the last trading day of fiscal 2024, from price history).
 1. Title slide with "Data as of <FY2024 fiscal year-end date>".
 2. Key stats: share price, market cap, FY2024 revenue, revenue growth YoY, operating margin, free cash flow, diluted EPS.
 3. Native bar chart (real chart data, not an image): revenue and operating income, FY2020-FY2024.
 4. Narrative slide with three bullets that quote numbers (growth rate, FCF margin, buyback amount).
 5. Valuation: P/E, EV/Revenue, EV/FCF computed from those numbers, in a table.
 6. Sources and notes footnote slide with dates.
Use mixed number formats the way real decks do ($21.5B on one slide, $21,505M in a table, "21.5" on the chart axis).

Write F3_key.md listing every number in the deck: slide, exact text, metric, period.
```

### F4: Pitch deck with planted errors for the QC test

```
Create an 8-slide sell-side pitch deck, Project_Canvas.pptx, titled "Project Canvas: Strategic Alternatives for Dropbox (DBX)". Slides: title, situation overview, key financials (LTM revenue, EBITDA, FCF, margins), share price performance (1y), trading comps vs. 4 peers, illustrative valuation range, potential buyer universe, next steps. Use real figures from the stock-data tools.

Then plant these errors without marking them:
 I1-I3 internal inconsistencies: one metric shows different values on two slides; one table total doesn't sum; one percentage doesn't match the numbers it's computed from.
 X1-X2 external factual errors: market cap overstated by about 25%; LTM revenue understated by about 10%, consistently on every slide (so it's internally consistent but wrong).
 N1-N2 narrative mismatches: a headline says "accelerating growth" while the numbers decelerate; a takeaway claims "best-in-class margins" while two peers in the comps table are higher.
 L1-L3 language/format issues: mixed "$MM" and "$M"; one typo in a headline; mixed date formats.

Write F4_key.md listing each error ID, slide, and the correct value or wording.
```

### F5: Branded template for the template-creator test

```
Create a PowerPoint template, Northwind_template.pptx, for a fictitious research firm called "Northwind Research": navy (#1F2A44) and grey palette, a text-box logo placeholder top-left, a footer with a disclaimer line and slide number. Include one example slide for each of these layouts: title, section header, title + content, two content, title + chart placeholder, full-page disclaimer. No real content.
```

### F6: Blank 3-statement template

```
Create an empty Excel 3-statement model template, 3S_template.xlsx, with tabs: Cover, Assumptions, IS, BS, CFS, Schedules (D&A/PP&E, working capital, debt), Checks. Columns: 4 historical years then 5 projected years, labelled FY-4A ... FY-1A, FY+1E ... FY+5E. Standard row labels on every statement and schedule, and a balance check row and a cash tie-out row on Checks. Leave every value and formula cell empty. Nothing company-specific.
```

### F7: Prior-estimates model for the model-update test

```
Using the stock-data tools, build ADBE_quarterly_model.xlsx: a quarterly income statement for Adobe with actuals for the 8 quarters BEFORE the most recently reported one, then 5 estimate columns starting with the most recently reported quarter (so that quarter is still an estimate, as if the model was last updated before the print). Mark columns "A" or "E".
Estimate rules: revenue = same quarter last year x 1.10; gross margin = trailing-4-quarter average; operating expenses = same quarter last year x 1.08; tax rate 18.5%; diluted shares = latest actual minus 1% per quarter.
Add an annual summary tab and a Valuation tab: NTM EPS x 22 = target price.
Write F7_key.md with the reported actuals for the most recent quarter (revenue, gross profit, operating income, net income, diluted EPS, diluted shares) and its 10-Q filing date.
```

---

## 5. Equity Research prompts

Summary of what each test exercises:

| ID | Skill | Command | `stock-data` tools expected | Expected gap A→B |
|---|---|---|---|---|
| ER-01 | catalyst-calendar | `/catalysts` | filings, quote, macro | Medium |
| ER-02 | earnings-preview | `/earnings-preview` | financials (quarterly), price history, filings | Medium |
| ER-03 | earnings-analysis | `/earnings` | financials (quarterly), filings, quote, price history | High |
| ER-04 | initiating-coverage, Task 1 | `/initiate` | filings, financials, quote | Medium-High |
| ER-05 | initiating-coverage, Task 2 | `/initiate` | financials (all statements) | High |
| ER-06 | initiating-coverage, Task 3 | `/initiate` | quote, macro, price history | High |
| ER-07 | model-update | `/model-update` | financials (quarterly), filings | High |
| ER-08 | morning-note | `/morning-note` | quote, filings, macro | Medium |
| ER-09 | idea-generation | `/screen` | quote ×15, financials ×15 | High |
| ER-10 | sector-overview | `/sector` | financials, quote, price history, macro | Medium |
| ER-11 | thesis-tracker | `/thesis` | financials, quote, price history, filings | Medium-High |

> Plugin commands may show as `/earnings` or `/equity-research:earnings` depending on the client. Use whichever form your client offers, the same way in both arms.

### ER-01: Catalyst calendar

```
/catalysts next 4 weeks

Coverage universe: ADBE, CRM, NOW, INTU, WDAY, ADSK, DDOG, MSFT. Build the catalyst calendar for the next 4 weeks from today: earnings dates (with confirmed vs. estimated status), investor days and conferences, product events, and the macro releases that matter for software multiples (FOMC, CPI, jobs). For each company, also show its most recent SEC filing and current price vs. its 52-week range, and rank the 3 catalysts most likely to move the group.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: for each of the 8 tickers: next earnings date (and confirmed/estimated), most recent SEC filing (form + date), current price, % of 52-week range. Then: next FOMC decision date, next CPI release date, current 10-year Treasury yield.
```

### ER-02: Earnings preview

```
/earnings-preview MSFT

Build the preview for Microsoft's next quarterly report (identify the quarter and the date). Include consensus for revenue, EPS and Azure growth; reported results for the last 4 quarters, so the trend into the print is visible; the stock's 1-day reaction to each of the last 4 prints; bull/base/bear scenarios with implied stock moves; and the 3-5 things that will decide the reaction.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: quarter being previewed and report date; consensus revenue; consensus diluted EPS; revenue and diluted EPS for each of the last 4 reported quarters; operating margin last quarter; 1-day stock move after each of the last 4 prints; current price; base-case revenue and EPS.
```

### ER-03: Earnings update

```
/earnings ADBE most recent quarter

Write the earnings update for Adobe's most recently reported quarter. Identify which fiscal quarter that is and when it was reported. Cover beat/miss vs. consensus on revenue and EPS, revenue by segment, margin trends over the last 5 quarters, guidance changes, the stock's reaction, updated estimates, and the thesis impact.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: fiscal quarter label and period-end date; 10-Q filing date; revenue; revenue growth YoY; gross margin; GAAP operating income; GAAP operating margin; GAAP diluted EPS; operating cash flow; free cash flow; diluted shares; consensus revenue; consensus EPS; stock move on the day after the report; current price; rating and price target.
```

### ER-04: Initiating coverage, Task 1 (company research)

```
/initiate DDOG

Start with Task 1 (company research) for Datadog. Run Task 1 only and deliver its output document.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: latest 10-K filing date and fiscal year; latest 10-Q filing date and quarter; revenue for each of the last 3 fiscal years; revenue growth for each of those years; latest-quarter revenue and YoY growth; GAAP operating margin last fiscal year; free cash flow last fiscal year; stock-based compensation last fiscal year; current price; market cap; cash + short-term investments; total debt.
```

### ER-05: Initiating coverage, Task 2 (financial model)

Run in the **same chat** as ER-04 (same arm), right after it finishes.

```
Now run Task 2 (financial modeling) for DDOG using the Task 1 output. Deliver the Excel model.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: for each historical fiscal year in the model: revenue, gross profit, operating income, net income, diluted EPS, operating cash flow, capex, total assets, stockholders' equity. Then: number of historical years; number of historical quarters; whether the balance sheet balances in every period (yes/no); first-projected-year revenue and operating margin.
```

### ER-06: Initiating coverage, Task 3 (valuation)

Run in the **same chat** as ER-05.

```
Now run Task 3 (valuation) for DDOG using the Task 2 model. Use DCF plus trading comps, and arrive at a price target and rating.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: current price; diluted shares; net cash/(debt); risk-free rate and its source date; beta and how it was derived; equity risk premium; WACC; terminal growth; DCF value per share; peer median EV/NTM revenue; comps-implied value per share; price target; implied upside %; rating.
```

> Tasks 4 (charts) and 5 (report assembly) mostly reformat earlier outputs. Run them only if you also want to compare the finished report; in that case score only on whether figures carried over correctly from Tasks 1-3.

### ER-07: Model update

Upload fixture **F7** (`ADBE_quarterly_model.xlsx`).

```
/model-update ADBE

The attached model was last updated before Adobe's most recent quarterly report, so that quarter is still an estimate. Plug in the reported actuals, show estimate vs. actual deltas, roll forward the next-quarter and next-fiscal-year estimates, and recalculate the target price. Flag anything that changes the thesis. Return the updated workbook.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: quarter updated and its 10-Q filing date; for revenue, gross profit, operating income, net income, diluted EPS and diluted shares: prior estimate, actual, delta %; new next-quarter revenue and EPS estimates; new next-fiscal-year revenue and EPS estimates; old and new target price.
```

### ER-08: Morning note

```
/morning-note

Write today's morning note for a US software coverage list: ADBE, CRM, NOW, INTU, WDAY, ADSK, DDOG, MSFT. Include the prior session's moves, any SEC filings in the last 2 trading days, the rates backdrop (10y yield level and change), today's key events, a top call, and one trade idea with a risk.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: for each of the 8 tickers: last price, 1-day % change, any SEC filing in the last 2 trading days (form + date, or "none"). Then: IGV 1-day % change; 10-year Treasury yield and its 1-day change in bp; the trade idea's ticker, direction and entry price.
```

### ER-09: Stock screen

```
/screen quality software at a reasonable price

Screen exactly this universe: ADBE CRM NOW INTU WDAY ADSK DDOG TEAM HUBS SNOW PANW CRWD FTNT ZS DOCU. Rank on TTM revenue growth, TTM free-cash-flow margin, EV/TTM FCF and the "Rule of 40" (growth + FCF margin). Surface 3 long ideas and 1 short idea, with a short pitch and the key risk for each.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: for each of the 15 tickers (one row each, Metric = ticker, with the values comma-separated in the Value column): price, market cap, TTM revenue, TTM revenue growth %, TTM FCF, FCF margin %, EV/TTM FCF, Rule of 40 score, and the end date of the latest quarter used. Then: the 3 longs and 1 short.
```

### ER-10: Sector overview

```
/sector US application software

Write the sector overview: market structure, the 6 largest public players by market cap, growth and margin profiles, valuation vs. history, how rates have affected multiples, the AI disruption debate, and investment implications.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: the 6 largest players you chose, each with market cap, last-fiscal-year revenue, revenue growth % and GAAP operating margin %; IGV 1-year total return; S&P 500 1-year total return; 10-year Treasury yield now and 1 year ago; median EV/revenue of the 6 players.
```

### ER-11: Thesis tracker

```
/thesis ADBE

Create a long thesis for Adobe: thesis statement, 3-5 pillars, 3-5 risks, catalysts, target price and stop-loss trigger. Then score each pillar against the latest reported data (the most recent quarter and fiscal year) and the stock's performance over the last 6 months, and give a current conviction level.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: latest quarter label; latest-quarter revenue growth YoY; latest-quarter GAAP operating margin; TTM free cash flow; TTM share repurchases; diluted share count change YoY %; current price; 6-month price return %; 52-week low and high; trailing P/E; target price; stop-loss level; conviction.
```

---

## 6. Financial Analysis prompts

| ID | Skill | Command / trigger | `stock-data` tools expected | Expected gap A→B |
|---|---|---|---|---|
| FA-01 | 3-statement-model | `/3-statement-model` + F6 | financials ×3 statements | High |
| FA-02 | competitive-analysis | `/competitive-analysis` | financials, quote | Medium |
| FA-03 | comps-analysis | `/comps` | quote ×6, financials ×6 | High |
| FA-04 | dcf-model (+ comps) | `/dcf` | financials, quote, macro, price history | High |
| FA-05 | audit-xls | `/debug-model` + F1 | financials (to check hardcodes) | Medium (data errors only) |
| FA-06 | lbo-model | `/lbo` | financials, quote, macro | High |
| FA-07 | clean-data-xls | skill name + F2 | financials (validation) | Low-Medium |
| FA-08 | deck-refresh | skill name + F3 | financials, quote | High |
| FA-09 | ib-check-deck | skill name + F4 | quote, financials | Medium (external errors only) |
| FA-10 | ppt-template-creator | `/ppt-template` + F5 | none | **Control** (should be none) |
| FA-11 | pptx-author | skill name | price history, financials | Medium |
| FA-12 | xlsx-author | skill name | price history, macro | High |
| FA-13 | skill-creator | skill name | none at run time | Low (checks whether the skill names the tools) |

### FA-01: 3-statement model

Upload fixture **F6** (`3S_template.xlsx`).

```
/3-statement-model

Fill out the attached template for Adobe (ADBE). Historical columns = the last 4 fiscal years as reported in Adobe's 10-Ks; projections = the next 5 fiscal years with drivers on the Assumptions tab. All three statements must link, the balance sheet must balance, and cash must tie out in every period. Return the completed workbook.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: fiscal-year labels of the 4 historical columns; for each historical year: revenue, operating income, net income, diluted EPS, cash, total assets, total liabilities, stockholders' equity, operating cash flow, capex, share repurchases. Then: balance check passes in all periods (yes/no); cash tie-out passes in all periods (yes/no); FY+1E revenue, net income and ending cash.
```

### FA-02: Competitive analysis

```
/competitive-analysis Adobe in creative and design software

Map Adobe's competitive landscape against Figma (FIG), Microsoft (MSFT, Designer/Copilot), Canva (private) and DocuSign (DOCU, document workflows): positioning, product overlap, financial comparison, AI threat and opportunity, and a strategic synthesis.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: for ADBE, FIG, DOCU and Canva: TTM or last-fiscal-year revenue, revenue growth %, gross margin %, R&D as % of revenue, sales & marketing (or SG&A) as % of revenue, market cap or latest private valuation. For FIG: number of fiscal periods of public financial history available. For MSFT: the segment or revenue line you used as the comparable, with its value.
```

### FA-03: Comparable company analysis

```
/comps ADBE

Build the trading comps for Adobe against CRM, NOW, INTU, WDAY and ADSK. Purpose: valuation for an investment committee. Use LTM figures aligned to each company's latest reported quarter, and deliver the Excel file with the statistical summary (max, 75th, median, 25th, min).

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: for each of the 6 companies (one row each, values comma-separated): latest quarter end date used for LTM, share price, market cap, enterprise value, LTM revenue, LTM revenue growth %, LTM EBITDA, EBITDA margin %, EV/LTM revenue, EV/LTM EBITDA, P/E. Then: peer median EV/LTM revenue, peer median EV/LTM EBITDA, peer median P/E.
```

### FA-04: DCF valuation

```
/dcf ADBE

Value Adobe with a DCF informed by comps (peers: CRM, NOW, INTU, WDAY, ADSK). Base the risk-free rate on the current 10-year Treasury yield and estimate beta from 5 years of monthly returns against the S&P 500. Show bear/base/bull cases and the WACC x terminal growth sensitivity table. Deliver the Excel models.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: current price; diluted shares; cash + short-term investments; total debt; revenue, operating income and free cash flow for each of the last 3 fiscal years; risk-free rate (value + date); beta (value + number of observations); equity risk premium; cost of debt; WACC; terminal growth; terminal value as % of EV; base/bear/bull value per share; implied upside %; DCF-implied EV/EBITDA vs. peer median.
```

### FA-05: Model audit

Upload fixture **F1** (`ADBE_model.xlsx`).

```
/debug-model

Audit the attached Adobe model end to end: formulas, hardcodes, balance-sheet balance, cash tie-out, roll-forwards, and whether the historical inputs match what Adobe actually reported. List every issue with sheet, cell, severity and the fix.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: one row per issue found (Metric = sheet!cell, Value = short description, Units = severity), then: total issues found; how many are input/data issues vs. formula issues; for each historical revenue figure in the model, the value you checked it against and that value's source.
```

Score against `F1_key.md`: count hits on D1-D3 (data errors, where the MCP should help) and M1-M4 (formula errors, which both arms should catch) separately.

### FA-06: LBO model

```
/lbo Dropbox (DBX)

Build an LBO for a take-private of Dropbox. Use the standard template. Assume a 30% premium to the current share price, a 5-year hold, and an exit at the entry EV/EBITDA multiple. Size and price the debt off today's market: SOFR plus a spread for the term loan, and the current high-yield spread for the notes. Report IRR and MOIC with sensitivities on entry premium and exit multiple.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: current price; offer price; diluted shares; equity purchase price; existing cash and debt; entry EV; LTM revenue; LTM EBITDA (and how it was built: operating income + D&A, with SBC treatment stated); entry EV/EBITDA; SOFR (value + date); high-yield spread (value + date); total debt raised and leverage multiple; sponsor equity; base-case IRR; base-case MOIC.
```

### FA-07: Clean data

Upload fixture **F2** (`quarterly_export.csv`).

```
Use the clean-data-xls skill on the attached quarterly_export.csv. Standardize tickers and dates, convert text numbers, dedupe, and flag mixed-type columns. Also flag any values that look wrong (unit errors or numbers that don't match what the company reported) and, where you can, give the corrected value with its source. Return the cleaned file and a change log.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: rows in, rows out; duplicates removed; date formats normalized (count); text-to-number conversions (count); unit errors found (rows + corrected values); wrong values found (rows + corrected values + source).
```

Score against `F2_key.md`. The formatting fixes are the control; the unit and wrong-value catches are where the MCP should help.

### FA-08: Deck refresh

Upload fixture **F3** (`ADBE_snapshot.pptx`).

```
Use the deck-refresh skill on the attached deck. Roll it forward from fiscal 2024 to Adobe's latest completed fiscal year, with current market data (today's price). I don't have a mapping: find the new numbers yourself, and recalculate the derived numbers (growth, margins, multiples). Extend the chart to include the new year. Return the updated deck.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: new fiscal year label; share price; market cap; revenue; revenue growth YoY; operating margin; free cash flow; diluted EPS; buyback amount; P/E; EV/Revenue; EV/FCF; number of number instances changed; number of old-value instances missed (any old number still in the deck).
```

At the approval gate, reply with **C2**. Score against `F3_key.md`: every old instance found and replaced (mechanics, same for both arms) plus correct new values (data, where the MCP should help).

### FA-09: Deck QC

Upload fixture **F4** (`Project_Canvas.pptx`).

```
Use the ib-check-deck skill to do a final QC pass on the attached pitch before it goes to the client: number consistency across slides, numbers vs. narrative, language polish, formatting, and whether the key market and financial figures are accurate as of today.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: one row per issue found (Metric = slide number, Value = short description, Units = category: internal / external / narrative / language). Then: DBX market cap per the deck vs. your verified value; DBX LTM revenue per the deck vs. your verified value; total issues by category.
```

Score against `F4_key.md`: X1-X2 are the MCP-sensitive errors; I, N and L errors are the in-test control.

### FA-10: PPT template skill (control)

Upload fixture **F5** (`Northwind_template.pptx`).

```
/ppt-template

Turn the attached Northwind Research template into a reusable template skill named "northwind-ppt-template", for equity research notes and sector decks. Generate the example presentation to validate it and package the skill.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: number of layouts detected; layout names; slide width x height; content-area top offset; whether the example presentation was generated (yes/no); files in the packaged skill.
```

Arm B should not call `stock-data` here. Any difference between the arms is noise, and sets the bar the other tests' gaps must clear.

### FA-11: PowerPoint file (pptx-author)

```
Use the pptx-author skill to produce a 5-slide .pptx file: "Adobe: 1-Year Stock Performance and Fundamentals". Slides: title; ADBE vs. QQQ vs. IGV 1-year total return line chart (native chart, weekly data); last 8 quarters of revenue and operating margin (combo chart); free cash flow and buybacks by fiscal year for the last 4 years; key takeaways with the numbers.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: 1-year total return for ADBE, QQQ and IGV (with start and end dates); number of weekly data points per series; revenue and operating margin for each of the last 8 quarters; free cash flow and share repurchases for each of the last 4 fiscal years; whether the charts are native (yes/no).
```

### FA-12: Excel file (xlsx-author)

```
Use the xlsx-author skill to produce an Excel workbook: Inputs tab with ADBE monthly adjusted closes and month-end 10-year Treasury yields for the last 5 years; Calc tab with monthly returns, the monthly change in yield, a 12-month rolling correlation between them, and the full-period correlation, all as live formulas; a Summary tab with a chart. Note the data source of every input column.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: first and last month in the data; number of monthly rows; first and last ADBE adjusted close; first and last 10-year yield; full-period correlation; latest 12-month rolling correlation; whether every Calc cell is a formula (yes/no); whether any input values were estimated or interpolated (yes/no, and which).
```

### FA-13: Skill creator

```
Use the skill-creator skill to create a new skill called "weekly-watchlist-review". Every Monday it should take a watchlist of tickers and produce a table with: last price, 1-week and 1-month % change, position in the 52-week range, latest SEC filing (form + date), and a flag for any 8-K filed in the last 7 days, followed by a 3-bullet summary. Make it work with the data tools available in this environment, and package it.

---
Don't pause for confirmations: take sensible defaults and list them under "Estimates and gaps".
Report money in USD millions (per-share values in USD), percentages to one decimal place, dates as YYYY-MM-DD.
End your reply with a section headed exactly "## Comparison Block" containing:
1. Key figures: a table with columns Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L). One row per metric listed below, in the order listed. Write N/A instead of dropping a row. Source = the tool name, the filing (form + filing date) or the URL; write "model knowledge" for anything recalled from memory.
2. Sources used: each tool, connector or website you called, with a call count.
3. Estimates and gaps: every figure you estimated, assumed, or could not verify, and every default you chose.
4. Freshness: the date of the latest market price and the latest financial reporting period you used.
Key figures: data tools or sources the skill tells Claude to use (each by name); whether it handles a ticker that errors (yes/no); whether it was test-run on a sample watchlist (yes/no, and with which tickers); files in the packaged skill.
```

Then, in a new chat in **arm B** for both outputs, install each generated skill and run `Run weekly-watchlist-review for ADBE, DDOG, DBX`. Compare which version produces a correct table without edits.

---

## 7. Scoring and comparison

### 7.1 Tolerances against the reference snapshot (R0)

| Data type | Counts as correct if within |
|---|---|
| Reported financials (revenue, income, cash flow, balance sheet) | ±0.5%, or ±$1M for small items |
| Per-share figures (EPS) | ±$0.01 |
| Share price, market cap | ±2% (runs happen at slightly different times) |
| Derived ratios (margins, growth) | ±0.3 percentage points |
| Multiples (EV/EBITDA, P/E) | ±5% (they compound several inputs) |
| Macro series (yields, spreads) | Exact for the same observation date; otherwise ±10bp |
| Dates (filings, period ends, earnings dates) | Exact |
| Fiscal-period labels | Exact (for example ADBE's fiscal Q3 is not calendar Q3) |

Valuation outputs (target price, WACC, IRR, DCF value) have no single right answer. Don't score them for accuracy. Instead check that the **inputs** behind them are correct, and note how far the outputs moved between arms.

### 7.2 Scorecard per test

Score each arm 0-2 on each dimension.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| **Accuracy** | <70% of key figures within tolerance | 70-95% | >95% |
| **Freshness** | Latest period used is 2+ periods stale | 1 period stale | Latest filed period and same-day prices |
| **Sourcing** | Most figures "model knowledge" or uncited | Mixed | Every figure cites a tool, filing or URL |
| **Completeness** | Deliverable missing or >20% of rows N/A without reason | Some gaps | Deliverable produced, all rows filled or N/A explained |
| **Fabrication** (inverted) | 3+ figures stated with High confidence that are wrong | 1-2 | None |

Also record, without scoring: wall-clock time, number of turns (including canned replies), number of `stock-data` calls in arm B, any MCP tool errors or `"stale": true` flags, and whether arm B fell back to web search for data the MCP has.

### 7.3 Results table

Copy into `results/<run-date>/scorecard.md`:

```markdown
| ID | Skill | A acc | B acc | A fresh | B fresh | A src | B src | A compl | B compl | A fab | B fab | A total | B total | Δ (B−A) | MCP invoked? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | catalyst-calendar | | | | | | | | | | | | | | | |
| ER-02 | earnings-preview | | | | | | | | | | | | | | | |
| ER-03 | earnings-analysis | | | | | | | | | | | | | | | |
| ER-04 | initiating-coverage T1 | | | | | | | | | | | | | | | |
| ER-05 | initiating-coverage T2 | | | | | | | | | | | | | | | |
| ER-06 | initiating-coverage T3 | | | | | | | | | | | | | | | |
| ER-07 | model-update | | | | | | | | | | | | | | | |
| ER-08 | morning-note | | | | | | | | | | | | | | | |
| ER-09 | idea-generation | | | | | | | | | | | | | | | |
| ER-10 | sector-overview | | | | | | | | | | | | | | | |
| ER-11 | thesis-tracker | | | | | | | | | | | | | | | |
| FA-01 | 3-statement-model | | | | | | | | | | | | | | | |
| FA-02 | competitive-analysis | | | | | | | | | | | | | | | |
| FA-03 | comps-analysis | | | | | | | | | | | | | | | |
| FA-04 | dcf-model | | | | | | | | | | | | | | | |
| FA-05 | audit-xls | | | | | | | | | | | | | | | |
| FA-06 | lbo-model | | | | | | | | | | | | | | | |
| FA-07 | clean-data-xls | | | | | | | | | | | | | | | |
| FA-08 | deck-refresh | | | | | | | | | | | | | | | |
| FA-09 | ib-check-deck | | | | | | | | | | | | | | | |
| FA-10 | ppt-template-creator (control) | | | | | | | | | | | | | | | |
| FA-11 | pptx-author | | | | | | | | | | | | | | | |
| FA-12 | xlsx-author | | | | | | | | | | | | | | | |
| FA-13 | skill-creator | | | | | | | | | | | | | | | |
```

For the fixture tests, add the answer-key hit rates to Notes, for example `FA-05: A 0/3 data + 4/4 formula; B 3/3 data + 4/4 formula`.

### 7.4 Judge prompt (optional)

To speed up scoring, paste both Comparison Blocks and the matching part of R0 into a **new chat with the MCP off and web search off**, so the judge can't fetch its own data:

```
You are scoring two runs of the same task against a reference. Use only the text below; do not use tools or memory.

REFERENCE (ground truth, captured <date/time>):
<paste the relevant R0 rows, or the fixture answer key>

RUN A (Comparison Block):
<paste>

RUN B (Comparison Block):
<paste>

Tolerances: reported financials ±0.5%; EPS ±$0.01; price and market cap ±2%; margins and growth ±0.3pp; multiples ±5%; dates and fiscal labels exact; macro exact for the same date, else ±10bp. Valuation outputs (target price, WACC, IRR, DCF value) are not scored for accuracy.

Produce:
1. A row-by-row table: Metric | Reference | A value | A ok? | B value | B ok? | Note. Mark a figure "unverifiable" if the reference has no value for it.
2. For each run: accuracy % (over verifiable rows), count of stale periods used, count of "model knowledge" sources, and count of wrong figures marked High confidence.
3. Scores 0-2 for Accuracy, Freshness, Sourcing, Completeness, Fabrication using this rubric: <paste the table from section 7.2>.
4. One paragraph on the most important difference between the runs.
```

### 7.5 Reading the results

- **Gap larger in a test than in the FA-10 control:** the MCP made a real difference for that skill.
- **Arm B gave wrong numbers that match R0:** the MCP returned the wrong value. Check the `concepts` field in `get_financials` output and the XBRL mapping in `src/stock_data_mcp/sources/xbrl_map.py`.
- **Arm B didn't call the MCP:** the skill's data-source instructions don't steer it to these tools. Possible fixes: clearer tool descriptions in `server.py`, or naming the tools in your prompt.
- **Arm B called the MCP, then still used web search for the same data:** look for tool errors or missing line items (banks, IFRS filers, recent IPOs) in the transcript.
- **No gap on consensus, guidance, segments or news rows:** that's expected. The MCP has none of these, so both arms must use web search.
