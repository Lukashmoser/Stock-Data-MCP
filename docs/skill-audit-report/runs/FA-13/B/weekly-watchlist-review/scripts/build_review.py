#!/usr/bin/env python3
"""Build the weekly watchlist review table from raw stock-data tool results.

Usage:
    python build_review.py watchlist_data.json [--out review.md] [--all-forms] [--json]

Input JSON:
    {"as_of": "YYYY-MM-DD",            # optional, defaults to today (UTC)
     "tickers": {"AAPL": {"quote": {...}, "history": {...},
                          "filings": {...}, "filings_8k": {...}}, ...}}
Each value is the tool's JSON result verbatim, or {"error": "..."} if the call failed.
Missing keys are treated as errors. Only the standard library is used.
"""
import argparse
import calendar
import json
import sys
from datetime import date, datetime, timedelta

OWNERSHIP_FORMS = {"3", "4", "5", "144", "SC 13D", "SC 13G", "SCHEDULE 13D", "SCHEDULE 13G"}


def parse_date(s):
    return datetime.strptime(s[:10], "%Y-%m-%d").date()


def minus_month(d):
    y, m = (d.year, d.month - 1) if d.month > 1 else (d.year - 1, 12)
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def is_err(obj):
    return obj is None or not isinstance(obj, dict) or "error" in obj


def base_form(form):
    return form.upper().split("/")[0].strip()


def close_on_or_before(rows, target, idx):
    best = None
    for r in rows:
        if parse_date(r[0]) <= target:
            best = r
        else:
            break
    return best[idx] if best else None


def pct(a, b):
    if a is None or b in (None, 0):
        return None
    return (a / b - 1.0) * 100.0


def fmt_pct(x, signed=True):
    if x is None:
        return "n/a"
    return f"{x:+.1f}%" if signed else f"{x:.1f}%"


def analyse(ticker, d, as_of, all_forms):
    issues = []
    out = {"ticker": ticker}
    q, h = d.get("quote"), d.get("history")
    f, f8 = d.get("filings"), d.get("filings_8k")

    rows = []
    if is_err(h):
        issues.append(f"get_price_history: {(h or {}).get('error', 'missing')}")
    else:
        cols = h.get("columns", [])
        ai = cols.index("adj_close") if "adj_close" in cols else 5
        ci = cols.index("close") if "close" in cols else 4
        rows = [r for r in h.get("rows", []) if r and r[ai] is not None]

    price = None
    if is_err(q):
        issues.append(f"get_quote: {(q or {}).get('error', 'missing')}")
    else:
        price = q.get("price")
    if price is None and rows:
        price = rows[-1][ci]
        out["price_source"] = "last close (quote unavailable)"
    out["price"] = price
    out["close_date"] = rows[-1][0] if rows else None

    if rows:
        last_d = parse_date(rows[-1][0])
        last_adj = rows[-1][ai]
        out["chg_1w"] = pct(last_adj, close_on_or_before(rows, last_d - timedelta(days=7), ai))
        out["chg_1m"] = pct(last_adj, close_on_or_before(rows, minus_month(last_d), ai))
    else:
        out["chg_1w"] = out["chg_1m"] = None

    hi = lo = None
    if not is_err(q):
        hi, lo = q.get("high_52w"), q.get("low_52w")
    if (hi is None or lo is None) and rows and len(rows) >= 200:
        hi = max(r[2] for r in rows)
        lo = min(r[3] for r in rows)
    if price is not None and hi is not None and lo is not None and hi > lo:
        out["pos_52w"] = (price - lo) / (hi - lo) * 100.0
        out["range_52w"] = (lo, hi)
    else:
        out["pos_52w"], out["range_52w"] = None, None

    out["latest_filing"] = out["latest_any"] = None
    if is_err(f):
        issues.append(f"get_filings: {(f or {}).get('error', 'missing')}")
    else:
        fl = f.get("filings", [])
        if fl:
            out["latest_any"] = (fl[0]["form"], fl[0]["filed"])
        for x in fl:
            if all_forms or base_form(x["form"]) not in OWNERSHIP_FORMS:
                out["latest_filing"] = (x["form"], x["filed"])
                break

    out["flag_8k"] = None
    window_start = as_of - timedelta(days=6)
    src = f8 if not is_err(f8) else (f if not is_err(f) else None)
    if is_err(f8) and not is_err(f):
        issues.append("get_filings(8-K): failed, used all-forms list instead")
    elif is_err(f8):
        issues.append(f"get_filings(8-K): {(f8 or {}).get('error', 'missing')}")
    if src is not None:
        hits = [x for x in src.get("filings", [])
                if base_form(x["form"]) == "8-K" and window_start <= parse_date(x["filed"]) <= as_of]
        out["flag_8k"] = hits
    out["issues"] = issues
    return out


def render(results, as_of, all_forms):
    close_dates = sorted({r["close_date"] for r in results if r["close_date"]})
    lines = [f"# Weekly watchlist review — week ending {as_of.isoformat()}",
             f"Prices as of close {close_dates[-1] if close_dates else 'n/a'} (Yahoo Finance via get_quote/"
             "get_price_history); filings from SEC EDGAR via get_filings.", "",
             "| Ticker | Last price (USD) | 1W % | 1M % | 52w position | Latest SEC filing | 8-K last 7d |",
             "|---|---|---|---|---|---|---|"]
    for r in results:
        price = f"{r['price']:,.2f}" if r["price"] is not None else "n/a"
        pos = "n/a"
        if r["pos_52w"] is not None:
            lo, hi = r["range_52w"]
            pos = f"{r['pos_52w']:.1f}% ({lo:,.2f}–{hi:,.2f})"
        lf = f"{r['latest_filing'][0]} {r['latest_filing'][1]}" if r["latest_filing"] else "n/a"
        if r["flag_8k"] is None:
            flag = "n/a"
        elif r["flag_8k"]:
            flag = "; ".join(f"YES {x['form']} {x['filed']}" + (f" ({x['items']})" if x.get("items") else "")
                             for x in r["flag_8k"])
        else:
            flag = "—"
        lines.append(f"| {r['ticker']} | {price} | {fmt_pct(r['chg_1w'])} | {fmt_pct(r['chg_1m'])} | "
                     f"{pos} | {lf} | {flag} |")
    bad = [r for r in results if r["issues"]]
    if bad:
        lines += ["", "Data issues: " + "; ".join(f"{r['ticker']} — " + ", ".join(r["issues"]) for r in bad)]
    notes = [f"{r['ticker']} {r['latest_any'][0]} {r['latest_any'][1]}" for r in results
             if r["latest_any"] and r["latest_filing"] and r["latest_any"] != r["latest_filing"]]
    lines += ["", "Notes: 1W/1M use adjusted closes vs the last close on/before 7 days / 1 calendar month "
              "earlier. 52w position: 0% = 52-week low, 100% = high. 8-K window: "
              f"{(as_of - timedelta(days=6)).isoformat()} to {as_of.isoformat()}."
              + ("" if all_forms else " Latest SEC filing excludes insider-ownership forms (3/4/5/144/13D/13G)"
                 + (f"; newest filing of any form: {', '.join(notes)}." if notes else "."))]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data")
    ap.add_argument("--out")
    ap.add_argument("--all-forms", action="store_true")
    ap.add_argument("--json", action="store_true", help="also print computed metrics as JSON")
    a = ap.parse_args()
    data = json.load(open(a.data))
    as_of = parse_date(data["as_of"]) if data.get("as_of") else datetime.utcnow().date()
    results = [analyse(t, d or {}, as_of, a.all_forms) for t, d in data["tickers"].items()]
    if all(r["price"] is None for r in results):
        print("All tickers failed — no review produced.", file=sys.stderr)
        for r in results:
            print(f"{r['ticker']}: {r['issues']}", file=sys.stderr)
        sys.exit(2)
    md = render(results, as_of, a.all_forms)
    if a.out:
        open(a.out, "w").write(md + "\n")
    print(md)
    if a.json:
        print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()
