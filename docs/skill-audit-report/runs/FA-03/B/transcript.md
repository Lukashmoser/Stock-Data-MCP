# Transcript - FA-03 / arm B

- Start: Thu Oct 15 01:58:45 UTC 2026
- End: Thu Oct 15 02:03:43 UTC 2026

---

## Final reply to user

I built the Microsoft trading comps against GOOGL, AMZN, META, AAPL and ORCL: **MSFT_Trading_Comps_2026-10-14.xlsx**

**What's in the workbook**
- **Comps tab:** the operating statistics (LTM revenue, YoY growth, EBIT, D&A, EBITDA and net income, with margins) and the valuation table (market cap, EV, EV/Revenue, EV/EBITDA, GAAP P/E, and a supplementary P/E on after-tax operating income).
  - Each table has a peer statistics block: Max, 75th, Median, 25th and Min. It covers the 5 peers only, with MSFT shown as the target.
  - Rows show MSFT's premium or discount against the peer median.
  - A block shows MSFT's implied share price at the peer 25th percentile, median and 75th percentile.
- **Inputs tab:** every hard-coded number is in blue and has a cell comment giving its source (tool or SEC filing and date). Each company's LTM is built from its 8 quarters of revenue and 4 quarters of EBIT, net income, tax and pre-tax income. A separate D&A section shows how LTM D&A was built.
- **Notes tab:** sources, definitions (EBITDA, EV, LTM alignment) and caveats.
- Every derived value is a live formula. The workbook was recalculated in LibreOffice with no errors.

**Key read-outs (peer medians exclude MSFT)**
| | MSFT | Peer median | MSFT vs median |
|---|---|---|---|
| EV / LTM revenue | 11.8x | 8.2x | +44.3% |
| EV / LTM EBITDA | 20.3x | 17.1x | +18.7% |
| P/E (LTM GAAP) | 29.6x | 20.9x | +42.0% |
| P/E (LTM EBIT after tax) | 31.7x | 35.3x | -10.2% |
| EBITDA margin | 58.4% | 38.8% | +19.6 pp |
| LTM revenue growth | 17.8% | 20.1% | -2.3 pp |

**What this means for the IC**
- **Premium on EV multiples.** MSFT trades above the peers on EV/Revenue and EV/EBITDA. Its EBITDA margin is the highest in the group by a wide margin (58.4% against a 48.0% peer high), so the premium is supported by profitability rather than growth. MSFT's revenue growth is slightly below the peer median.
- **GAAP P/E needs care.**
  - GOOGL's LTM net income (USD 244.2bn) and AMZN's (USD 135.3bn) are inflated by large mark-to-market gains on equity securities in 2026. That puts their GAAP P/Es at about 17x and 20x and pulls the peer median P/E down to 20.9x.
  - On after-tax operating earnings, the peer median is 35.3x and MSFT, at 31.7x, sits at a discount.
  - I would put the operating-earnings P/E in front of the IC rather than the GAAP P/E.
- **Implied MSFT value per share at peer medians:**
  - EV/Revenue: USD 371
  - EV/EBITDA: USD 450
  - GAAP P/E: USD 376
  - P/E on EBIT after tax: USD 595
  - Current price: USD 533.69. The spread shows how much the result depends on which multiple you use.
- **Oracle is the outlier on leverage and timing.**
  - It is the only peer with material net debt (about USD 94bn including preferred stock and noncontrolling interests).
  - Its LTM ends 2026-08-31, two months after the others.
  - It fell 8.8% on the pricing date.

## Comparison Block

### 1. Key figures
Values per company are in this order: latest quarter end used for LTM, share price, market cap, enterprise value, LTM revenue, LTM revenue growth %, LTM EBITDA, EBITDA margin %, EV/LTM revenue, EV/LTM EBITDA, P/E (LTM GAAP).

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| MSFT | 2026-06-30, 533.69, 3,963,716, 3,927,167, 331,839, 17.8%, 193,771, 58.4%, 11.8x, 20.3x, 29.6x | date, USD, USD m, USD m, USD m, %, USD m, %, x, x, x | Price 2026-10-14; LTM to 2026-06-30 (FY26) | stock-data get_quote; stock-data get_financials (SEC XBRL); MSFT 10-K filed 2026-07-29; 8-K Ex.99.1 filed 2026-07-29 (D&A) | H (EBITDA M: D&A line includes "other") |
| GOOGL | 2026-06-30, 347.64, 4,251,637, 4,109,327, 445,867, 20.1%, 172,865, 38.8%, 9.2x, 23.8x, 17.4x | same as above | Price 2026-10-14; LTM to 2026-06-30 | stock-data get_quote; get_financials; 10-K filed 2026-02-05; 10-Q filed 2026-07-23 | M (D&A is depreciation only; GAAP P/E distorted by equity gains) |
| AMZN | 2026-06-30, 254.08, 2,739,745, 2,748,981, 775,680, 15.8%, 168,912, 21.8%, 3.5x, 16.3x, 20.3x | same as above | Price 2026-10-14; LTM to 2026-06-30 | stock-data get_quote; get_financials; 10-Q filed 2026-07-31 | H (P/E M: GAAP NI inflated by equity gains) |
| META | 2026-06-30, 737.54, 1,878,888, 1,872,292, 228,247, 27.7%, 109,656, 48.0%, 8.2x, 17.1x, 27.6x | same as above | Price 2026-10-14; LTM to 2026-06-30 | stock-data get_quote; get_financials; 10-Q filed 2026-07-30 (cover shares) | H (P/E M: Q3-25 one-off tax charge) |
| AAPL | 2026-06-27, 342.96, 5,010,290, 5,032,235, 466,823, 14.2%, 167,959, 36.0%, 10.8x, 30.0x, 38.9x | same as above | Price 2026-10-14; LTM to 2026-06-27 (FY26 Q3) | stock-data get_quote; get_financials; 10-Q filed 2026-07-31 | H |
| ORCL | 2026-08-31, 130.55, 394,783, 488,421, 71,777, 21.6%, 33,937, 47.3%, 6.8x, 14.4x, 20.9x | same as above | Price 2026-10-14; LTM to 2026-08-31 (FY27 Q1) | stock-data get_quote; get_financials; 10-K filed 2026-06-22; 10-Q filed 2026-09-11 | M |
| Peer median EV/LTM revenue | 8.2x | x | 2026-10-14 prices; latest LTM | Calculated from the figures above (GOOGL, AMZN, META, AAPL, ORCL) | H |
| Peer median EV/LTM EBITDA | 17.1x | x | 2026-10-14 prices; latest LTM | Calculated from the figures above | M |
| Peer median P/E | 20.9x (GAAP); 35.3x on after-tax EBIT basis | x | 2026-10-14 prices; latest LTM | Calculated from the figures above | M |

### 2. Sources used
| Tool / connector / website | Calls |
|---|---|
| stock-data get_quote (Yahoo Finance) | 6 |
| stock-data get_financials (SEC XBRL) | 18 |
| stock-data get_filings (SEC EDGAR) | 11 |
| WebFetch, sec.gov EDGAR documents (10-K, 10-Q, 8-K Ex.99.1, XBRL R pages, filing index) | 17 |
| curl to data.sec.gov companyfacts (blocked by the proxy, no data) | 1 Bash call (3 requests) |
| Skills: financial-analysis:comps, financial-analysis:comps-analysis | 2 |
| LibreOffice (local recalculation check) | 1 |

### 3. Estimates and gaps
**Defaults chosen**
- Peer statistics exclude MSFT. MSFT is the target and is shown against the peers.
- Each company's LTM runs to its own latest reported quarter. Fiscal calendars are not aligned:
  - ORCL's LTM ends 2026-08-31.
  - AAPL's ends 2026-06-27.
  - The others end 2026-06-30.
  - Calendar Q3-2026 results for GOOGL, AMZN, META and MSFT are not yet reported as of 2026-10-14.
- EBITDA = GAAP operating income + cash-flow D&A. Stock-based compensation is not added back and there are no one-off adjustments.
- Market cap = price x basic shares outstanding from the latest balance sheet or 10-Q cover. No treasury-method dilution.
- EV = market cap + debt (current + non-current, excluding all lease liabilities) + preferred stock + noncontrolling interests - cash - current short-term investments.
  - Non-current marketable securities and strategic equity stakes are excluded. For example, AAPL's USD 84,118m of non-current securities is excluded; including it would lower AAPL's EV by about 1.7%.
- P/E = market cap / LTM GAAP net income. I added a supplementary P/E on LTM EBIT x (1 - LTM effective tax rate) because GAAP net income is distorted for GOOGL and AMZN.
- Prices are the 2026-10-14 session last prices from Yahoo via get_quote, fetched 2026-10-15T01:58Z.

**Figures that are estimated, derived or not fully verified**
- Fourth fiscal quarters are derived by the data tool as full year less 9M YTD: MSFT Jun-quarters, calendar Dec-quarters, AAPL Sep-quarters and ORCL May-quarters. Some cash-flow quarters are derived the same way.
- MSFT D&A (USD 38,534m) is "Depreciation, amortization, and other", so it includes minor other non-cash items. This slightly overstates EBITDA.
- GOOGL D&A is "Depreciation of property and equipment" only (FY25 21,136 + 6M26 13,586 - 6M25 9,485 = 25,237). Intangible amortization is not in the cash flow statement, so EBITDA is slightly understated.
- ORCL D&A = FY26 (7,623 + 1,671) + Q1 FY27 (3,156 + 202) - Q1 FY26 (1,351 + 420) = 10,881.
- ORCL pre-tax income is not tagged, so I computed it as net income + tax.
- ORCL preferred stock is at carrying value (4,954). Liquidation value was not verified.
- META has no shares-outstanding tag in the data tool. I used the 10-Q cover (2,547.5m shares as of 2026-07-24), which is slightly later than the balance-sheet date.
- Possible missing debt:
  - AMZN's short-term borrowings inside accrued liabilities were not captured.
  - GOOGL's and META's small current debt balances may be incomplete.
  - Noncontrolling interests for GOOGL, AMZN, META and AAPL are assumed to be zero.
- GAAP net income includes material non-recurring items:
  - GOOGL and AMZN: equity-security gains (GOOGL 6M26 other income of 135,699).
  - MSFT: an investment-related gain in the Dec-25 quarter, recalled from model knowledge and not verified in the filing.
  - META: a Q3-25 one-off tax charge.
  - ORCL: a gain in the Nov-25 quarter, recalled from model knowledge and not verified.
- Lease liabilities are excluded from debt for every company. These are material for AMZN, MSFT and ORCL.
- data.sec.gov (the XBRL companyfacts API) was blocked by the network proxy. The 10-K full-text fetches were truncated, so I used the XBRL R pages and earnings-release exhibits instead.

### 4. Freshness
- Latest market price: 2026-10-14 (session close/last price, fetched 2026-10-15T01:58Z).
- Latest financial reporting period used: quarter ended 2026-08-31 (ORCL FY27 Q1, 10-Q filed 2026-09-11). For the others: 2026-06-30 (MSFT, GOOGL, AMZN, META) and 2026-06-27 (AAPL).

---

## Run log
| Tool | Calls | Notes |
|---|---|---|
| Read | 2 | rules/arm_B.md, prompts/FA-03.txt |
| Bash | 5 | start date/ls; curl to data.sec.gov (blocked); openpyxl/soffice check; build + LibreOffice recalc + verification; end date |
| Skill | 2 | financial-analysis:comps, financial-analysis:comps-analysis |
| ToolSearch | 1 | "select:mcp__remote-devices__stock-data__get_quote,get_financials,get_filings,get_price_history" |
| mcp__remote-devices__stock-data__get_quote | 6 | MSFT, GOOGL, AMZN, META, AAPL, ORCL |
| mcp__remote-devices__stock-data__get_financials | 18 | income, cashflow and balance (quarterly) x 6 tickers |
| mcp__remote-devices__stock-data__get_filings | 11 | 10-K/10-Q/8-K lookups |
| WebFetch | 17 | SEC EDGAR documents and XBRL R pages |
| Write | 2 | _work/build.py, transcript.md |

**Files delivered**
- /home/claude/results/2026-10-13/runs/FA-03/B/MSFT_Trading_Comps_2026-10-14.xlsx
- /home/claude/results/2026-10-13/runs/FA-03/B/transcript.md
- Build script: /home/claude/results/2026-10-13/runs/FA-03/B/_work/build.py (recalculated copy in _work/recalc/)
