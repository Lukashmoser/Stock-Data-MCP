#!/usr/bin/env python3
"""Assemble watchlist_input.json from raw stock-data tool output.
mode 'raw'  : paste tool output unchanged (tests the script's shape handling)
mode 'shaped': reshape get_price_history {columns, rows} -> [{date,high,low,close}] (raw close)
"""
import json, sys, os
W = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1]
qf = json.load(open(os.path.join(W, "raw_quotes_filings.json")))
out = {"as_of": "2026-10-18", "tickers": {}}
for t in ["AAPL", "NVDA", "META"]:
    h = json.load(open(os.path.join(W, f"raw_{t}_history.json")))
    if mode == "shaped":
        cols = h["columns"]
        hist = [{"date": r[cols.index("date")], "high": r[cols.index("high")],
                 "low": r[cols.index("low")], "close": r[cols.index("close")]} for r in h["rows"]]
    else:
        hist = h
    out["tickers"][t] = {"quote": qf["quotes"][t], "history": hist, "filings": qf["filings"][t]}
fn = os.path.join(W, f"watchlist_input_{mode}.json")
json.dump(out, open(fn, "w"), indent=1)
print(fn)
