# Data sources and field mapping

## 1. Primary: stock-data MCP tools
Tool names: `get_quote`, `get_price_history`, `get_filings` (prefix
`mcp__remote-devices__stock-data__` in cloud sessions linked to the user's machine). Check the
loaded schema for exact parameter names before calling; do not guess enums.

Fields `build_review.py` looks for (first match wins, case-sensitive list):

| Input block | Field | Accepted keys |
|---|---|---|
| quote | price | price, last, lastPrice, last_price, regularMarketPrice, close, c |
| quote | date | date, as_of, asOf, timestamp, time, t, lastTradeDate |
| history row | date | date, Date, t, timestamp, time, datetime (ISO string, MM/DD/YYYY, YYYYMMDD or epoch s/ms) |
| history row | close | close, Close, c, adjClose, adj_close, adjusted_close, price |
| history row | high / low | high, High, h / low, Low, l (optional; closes used if absent) |
| filings row | form | form, formType, form_type, type, filing_type |
| filings row | filed | filingDate, filing_date, filed, filed_at, filedAt, date, acceptanceDate |

List wrappers unwrapped automatically: data, results, bars, history, prices, filings, items,
values; also columnar dicts of equal-length lists.
If a tool returns a shape not covered, reshape it to `[{"date":..,"close":..}]` /
`[{"form":..,"filingDate":..}]` before writing the input file rather than editing the script.

Adjusted vs raw closes: prefer one series consistently. Splits inside the window distort 1M / 52-wk
figures on raw closes; if a split occurred, note it.

## 2. Fallbacks (only if stock-data is unavailable)
- Filings: SEC EDGAR submissions JSON via WebFetch:
  `https://data.sec.gov/submissions/CIK##########.json` (10-digit zero-padded CIK; map ticker to
  CIK from `https://www.sec.gov/files/company_tickers.json`). Use `filings.recent.form` and
  `filings.recent.filingDate` (columnar - pass `filings.recent` straight in as `filings`).
- Prices: WebSearch / WebFetch a quote page for last price and 52-wk range only; 1W / 1M changes
  need two dated closes - if they cannot be sourced, leave n/a and say so. Never fill from memory.
- Mark every fallback figure as such in the footnote.

## 3. Non-US / non-SEC tickers
ADRs and foreign filers file 6-K/20-F, not 8-K: show their latest form; the 8-K flag will be "-"
(state that 6-Ks are not flagged). Tickers with no SEC filer (ETFs may file N-CSR etc., foreign
listings none) will show "n/a" for filings - that is PARTIAL, not ERROR.
