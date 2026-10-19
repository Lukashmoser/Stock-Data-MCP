# Transcript: FA-03 / Arm A

- Start: Thu Oct 15 01:58:44 UTC 2026
- End: Thu Oct 15 02:04:12 UTC 2026

---

## Final reply to the user

I built the Microsoft trading comps against GOOGL, AMZN, META, AAPL and ORCL. The deliverable is **MSFT_Trading_Comps_2026-10-14.xlsx**. It has three sheets:

- **Comps**: the operating statistics section, the valuation multiples section, the peer statistics (Max / 75th / Median / 25th / Min), MSFT's premium or discount to the peer median, and an implied MSFT share price at peer multiples.
- **LTM_Build**: for every metric, LTM = last fiscal year − prior-year YTD + current YTD, with the source on each row.
- **Notes**: methodology and caveats.

Every derived number is a live formula. Inputs are in blue font, and each has a cell comment giving its source. The peer statistics leave out MSFT.

**Data sources.** None of the institutional feeds (FactSet, S&P, Daloopa, Bloomberg) were available, and the stock-data tools were switched off. Financials therefore come from the SEC EDGAR XBRL API and each company's latest 8-K earnings release (Ex. 99.1). Share prices are the 2026-10-14 closes from stockanalysis.com.

**LTM periods.** Each company's LTM runs to its latest reported quarter:

| Company | LTM ends | Period |
|---|---|---|
| MSFT | 2026-06-30 | FY26 |
| GOOGL, AMZN, META | 2026-06-30 | Q2'26 |
| AAPL | 2026-06-27 | Q3 FY26 |
| ORCL | 2026-08-31 | Q1 FY27 |

**Results**

- **MSFT trades at a premium on most multiples.** It trades at 11.9x EV/LTM revenue against a peer median of 8.3x (+43.5%). On EV/LTM EBITDA it is 20.3x against 17.2x (+18.1%), and on GAAP P/E 29.7x against 20.7x (+43.5%). MSFT also has the highest LTM EBITDA margin in the group at 58.4% (peer median 38.8%), which supports some of that premium. Its LTM revenue growth of 17.8% is a little below the peer median of 20.1%.
- **On EV/EBIT, MSFT is cheaper than peers.** It trades at 25.4x against a 28.0x median, a 9.5% discount. The reason is that MSFT's D&A ("Depreciation, amortization, and other") has risen with its AI capex. That makes its EBITDA look larger relative to EBIT than its peers'.
- **Peer multiples alone don't support the current price.** The implied MSFT price at peer medians is $373 (EV/revenue), $453 (EV/EBITDA) and $372 (P/E), against $533.69. Only the peer 75th percentile on EV/EBITDA ($627) or P/E ($499) gets near the current price.

**Caveats the committee should see**

- **GOOGL and AMZN P/E ratios are understated.** Their GAAP P/E (17.5x and 20.5x) rests on large unrealised gains on equity investments. GOOGL's Q2'26 equity gains were $99.0bn pre-tax ($77.1bn after tax). AMZN's Q2'26 non-operating income was $53.4bn, mainly from Anthropic. This pulls the peer median P/E down, so EV/EBITDA and EV/EBIT are the cleaner comparisons for those two.
- **META's net income is depressed.** LTM net income includes the Q3'25 one-off tax charge and $3.6bn of Q2'26 legal and severance charges.
- **ORCL is an outlier on leverage and cash flow.** EV/EBITDA is 14.1x, but it carries $125bn of debt and its LTM free cash flow was about −$28.7bn. Its price also fell 8.8% on 2026-10-14.

## Comparison Block

### 1. Key figures

Company rows list values in this order: latest quarter end used for LTM; share price (USD); market cap (USD mm); enterprise value (USD mm); LTM revenue (USD mm); LTM revenue growth %; LTM EBITDA (USD mm); EBITDA margin %; EV/LTM revenue (x); EV/LTM EBITDA (x); P/E (x).

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| MSFT | 2026-06-30, 533.69, 3972255, 3935706, 331839, 17.8%, 193771, 58.4%, 11.9x, 20.3x, 29.7x | date, USD, USD mm, USD mm, USD mm, %, USD mm, %, x, x, x | LTM to 2026-06-30; price 2026-10-14 | 10-K filed 2026-07-29; 8-K Ex.99.1 filed 2026-07-29; SEC XBRL API (WebFetch); stockanalysis.com | H financials / M price |
| GOOGL | 2026-06-30, 347.64, 4278058, 4133749, 445866, 20.1%, 172865, 38.8%, 9.3x, 23.9x, 17.5x | same as above | LTM to 2026-06-30; price 2026-10-14 | 10-K filed 2026-02-05; 10-Q filed 2026-07-23; 8-K Ex.99.1 filed 2026-07-22; stockanalysis.com | M (share count derived; D&A excludes amortization) |
| AMZN | 2026-06-30, 254.08, 2770234, 2776140, 775680, 15.8%, 168912, 21.8%, 3.6x, 16.4x, 20.5x | same as above | LTM to 2026-06-30; price 2026-10-14 | 10-K filed 2026-02-06; 10-Q filed 2026-07-31; 8-K Ex.99.1 filed 2026-07-30; stockanalysis.com | H financials / M price |
| META | 2026-06-30, 737.54, 1892528, 1885932, 228247, 27.7%, 109655, 48.0%, 8.3x, 17.2x, 27.8x | same as above | LTM to 2026-06-30; price 2026-10-14 | 10-K filed 2026-01-29; 10-Q filed 2026-07-30; 8-K Ex.99.1 filed 2026-07-29; stockanalysis.com | H financials / M price |
| AAPL | 2026-06-27, 342.96, 5046554, 4984381, 466823, 14.2%, 167959, 36.0%, 10.7x, 29.7x, 39.1x | same as above | LTM to 2026-06-27; price 2026-10-14 | 10-K filed 2025-10-31; 10-Q filed 2026-07-31; 8-K Ex.99.1 (Q3 FY26); stockanalysis.com; model knowledge (9M FY24 revenue, growth only) | H (growth M) |
| ORCL | 2026-08-31, 130.55, 391650, 479910, 71776, 21.6%, 33938, 47.3%, 6.7x, 14.1x, 20.7x | same as above | LTM to 2026-08-31; price 2026-10-14 | 10-K filed 2026-06-22; 10-Q filed 2025-09-10; 8-K Ex.99.1 filed 2026-09-10; stockanalysis.com | M (price only on one source for 10-14) |
| Peer median EV/LTM revenue | 8.3 | x | 2026-10-14 prices / latest LTM | Calculated in workbook (GOOGL, AMZN, META, AAPL, ORCL) | M |
| Peer median EV/LTM EBITDA | 17.2 | x | 2026-10-14 prices / latest LTM | Calculated in workbook | M |
| Peer median P/E | 20.7 | x | 2026-10-14 prices / latest LTM | Calculated in workbook | L (distorted by GOOGL/AMZN investment gains) |

### 2. Sources used

| Source | Calls |
|---|---|
| WebFetch: data.sec.gov XBRL company-concept API (5 calls errored on tags that don't exist) | 31 |
| WebFetch: sec.gov Archives 8-K Ex. 99.1 earnings releases (MSFT, GOOGL, AMZN, META, AAPL, ORCL) | 6 |
| WebFetch: stockanalysis.com price history | 6 |
| WebFetch: financialcontent.com price history (ORCL cross-check) | 2 |
| WebSearch (locating releases and prices) | 9 |
| Skills: financial-analysis:comps, financial-analysis:comps-analysis | 2 |
| Bash: direct curl to data.sec.gov and other hosts, blocked by the proxy (403) | 2 |
| Bash: workbook build and LibreOffice recalculation | 2 |

### 3. Estimates and gaps

**Assumptions and defaults I chose**

- **Peer statistics.** These are computed on the 5 peers only. MSFT is excluded as the target.
- **Shares.** Market cap uses latest-quarter diluted weighted-average shares, not cover-page basic shares outstanding.
- **GOOGL share count.** I derived 12,306mm as Q2'26 net income to common ($112,107mm) divided by diluted EPS ($9.11). Basic shares outstanding were 12,230mm.
- **EBITDA definition.** EBITDA = GAAP EBIT + cash-flow D&A. It is not adjusted for stock-based compensation, restructuring, or legal charges.
- **D&A line used, by company:**
  - MSFT: "Depreciation, amortization, and other", which includes minor other items.
  - GOOGL: depreciation of property and equipment only; intangible amortization isn't disclosed separately.
  - AMZN: includes amortization of content and lease assets.
  - ORCL: depreciation plus amortization of intangibles.
- **Enterprise value.**
  - EV = market cap + financial debt − cash, cash equivalents and marketable securities.
  - Excluded from EV: leases, preferred stock (GOOGL mandatory convertibles; ORCL preferred), non-controlling interests, and strategic or non-marketable equity stakes (for example MSFT's $36.3bn of equity investments, AMZN's Anthropic stake, GOOGL's non-marketable securities).
  - AMZN and GOOGL debt is long-term debt only, because the release shows no separate current-debt line.
  - AAPL cash includes non-current marketable securities.
- **P/E.** P/E = market cap / LTM GAAP net income attributable to the parent. ORCL's preferred dividends ($81mm in Q1 FY27) are not deducted.

**Figures I could not fully verify**

- AAPL's 9M FY24 revenue ($296,105mm), used only in the prior-year LTM revenue for the growth rate, came from model knowledge and was not re-verified.
- ORCL's Q1 FY27 operating income, D&A and balance sheet come from the 8-K release, because that quarter isn't yet in the XBRL concept API for those tags.
- ORCL's 2026-10-14 close (130.55) comes from one source. financialcontent.com showed only the 10-13 close (143.20, which matches) and a 10-14 intraday price of 134.10.

**Gaps**

- No institutional data vendor was available, so nothing was cross-checked against a second vendor.
- Gross margin and consensus forward multiples (NTM) are not included.
- No normalised P/E excluding the GOOGL/AMZN equity gains was built.

### 4. Freshness

- **Latest market price:** 2026-10-14 close.
- **Latest financial reporting period:** quarter ended 2026-08-31 (ORCL Q1 FY27). For the others: MSFT, GOOGL, AMZN and META to 2026-06-30, and AAPL to 2026-06-27.

---

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 7 | Read rules/prompt; `date -u` start; curl to SEC (blocked); proxy check; openpyxl/LibreOffice check; build + recalc + verify; copy + `date -u` end |
| Skill | 2 | financial-analysis:comps, financial-analysis:comps-analysis |
| WebFetch | 45 | data.sec.gov XBRL ×31 (5 errors), sec.gov 8-K exhibits ×6, stockanalysis.com ×6, financialcontent.com ×2 |
| WebSearch | 9 | ORCL Q1 FY27 release; MSFT/GOOGL/AMZN/META/AAPL releases; prices ×3 |
| Write | 2 | _work/build.py, transcript.md |
| ToolSearch | 0 | none |
| stock-data tools | 0 | not used (disabled) |

**Files delivered:**

- /home/claude/results/2026-10-13/runs/FA-03/A/MSFT_Trading_Comps_2026-10-14.xlsx
- /home/claude/results/2026-10-13/runs/FA-03/A/transcript.md
- Build script: /home/claude/results/2026-10-13/runs/FA-03/A/_work/build.py
