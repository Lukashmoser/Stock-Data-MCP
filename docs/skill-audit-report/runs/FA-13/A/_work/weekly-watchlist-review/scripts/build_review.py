#!/usr/bin/env python3
"""
Build the weekly watchlist review table from raw per-ticker data.

Input: a JSON file shaped like
{
  "as_of": "YYYY-MM-DD",               # review date (normally the Monday of the run)
  "tickers": {
    "AAPL": {
      "quote":   {...},                # optional; raw get_quote output (any common key names)
      "history": [...],                # daily bars, >= ~1 year; raw get_price_history output
      "filings": [...],                # recent filings; raw get_filings output
      "error":   "message"             # optional; set when a fetch failed
    },
    ...
  }
}

Key names are matched loosely (close/Close/c/adjClose, date/Date/t/timestamp,
form/formType/type, filingDate/filed/filed_at/date ...), so raw tool output can be
pasted in without hand-reshaping. A ticker with missing or unusable data never
aborts the run: its row is marked ERROR / n/a and the reason is reported.

Output: markdown table + facts block on stdout; optional --json path for the
computed rows (used to draft the 3-bullet summary).

Usage:
  python3 build_review.py input.json [--json out.json] [--md out.md]
"""
import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone

DATE_KEYS = ("date", "Date", "t", "timestamp", "time", "datetime")
CLOSE_KEYS = ("close", "Close", "c", "adjClose", "adj_close", "adjusted_close", "price")
HIGH_KEYS = ("high", "High", "h")
LOW_KEYS = ("low", "Low", "l")
QUOTE_PRICE_KEYS = ("price", "last", "lastPrice", "last_price", "regularMarketPrice", "close", "c")
QUOTE_DATE_KEYS = ("date", "as_of", "asOf", "timestamp", "time", "t", "lastTradeDate")
FORM_KEYS = ("form", "formType", "form_type", "type", "filing_type")
FILED_KEYS = ("filingDate", "filing_date", "filed", "filed_at", "filedAt", "date", "acceptanceDate")
LIST_WRAPPERS = ("data", "results", "bars", "history", "prices", "filings", "items", "values")


def pick(d, keys):
    for k in keys:
        if isinstance(d, dict) and k in d and d[k] not in (None, ""):
            return d[k]
    return None


def to_date(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        ts = v / 1000 if v > 1e11 else v  # ms or s epoch
        return datetime.fromtimestamp(ts, tz=timezone.utc).date()
    s = str(v).strip()
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        pass
    for fmt in ("%m/%d/%Y", "%Y%m%d", "%d-%b-%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def to_float(v):
    try:
        f = float(str(v).replace(",", "").replace("$", ""))
        return f if f == f else None  # drop NaN
    except (TypeError, ValueError):
        return None


def unwrap(obj):
    """Return the list inside common wrapper shapes ({"data": [...]}, column dicts, etc.)."""
    if obj is None:
        return []
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for k in LIST_WRAPPERS:
            if isinstance(obj.get(k), list):
                return obj[k]
        # columnar shape: {"date": [...], "close": [...]}
        cols = {k: v for k, v in obj.items() if isinstance(v, list)}
        if cols:
            n = max(len(v) for v in cols.values())
            return [{k: (v[i] if i < len(v) else None) for k, v in cols.items()} for i in range(n)]
    return []


def parse_history(raw):
    bars = []
    for row in unwrap(raw):
        d = to_date(pick(row, DATE_KEYS))
        c = to_float(pick(row, CLOSE_KEYS))
        if d is None or c is None:
            continue
        h = to_float(pick(row, HIGH_KEYS))
        lo = to_float(pick(row, LOW_KEYS))
        bars.append((d, c, h if h is not None else c, lo if lo is not None else c))
    bars.sort(key=lambda b: b[0])
    dedup = {}
    for b in bars:
        dedup[b[0]] = b
    return list(dedup.values())


def parse_filings(raw):
    out = []
    for row in unwrap(raw):
        form = pick(row, FORM_KEYS)
        filed = to_date(pick(row, FILED_KEYS))
        if form and filed:
            out.append((str(form).strip().upper(), filed))
    out.sort(key=lambda f: f[1], reverse=True)
    return out


def close_on_or_before(bars, target):
    cand = [b for b in bars if b[0] <= target]
    return cand[-1] if cand else None


def minus_month(d):
    m, y = d.month - 1, d.year
    if m == 0:
        m, y = 12, y - 1
    for day in (d.day, 30, 29, 28):
        try:
            return date(y, m, day)
        except ValueError:
            continue


def pct(a, b):
    if a is None or b in (None, 0):
        return None
    return (a / b - 1) * 100


def fmt_pct(v):
    return "n/a" if v is None else f"{v:+.1f}%"


def compute_row(tkr, rec, as_of):
    notes = []
    row = {"ticker": tkr, "status": "OK", "last_price": None, "price_date": None,
           "chg_1w_pct": None, "chg_1m_pct": None, "pos_52w_pct": None,
           "low_52w": None, "high_52w": None, "latest_form": None, "latest_filed": None,
           "recent_8k": None, "recent_8k_dates": [], "notes": notes}
    if rec.get("error"):
        notes.append(f"fetch error: {rec['error']}")

    bars = [b for b in parse_history(rec.get("history")) if b[0] <= as_of]
    quote = rec.get("quote") if isinstance(rec.get("quote"), dict) else {}
    q_price = to_float(pick(quote, QUOTE_PRICE_KEYS))
    q_date = to_date(pick(quote, QUOTE_DATE_KEYS))

    if q_price is not None:
        row["last_price"], row["price_date"] = q_price, q_date or (bars[-1][0] if bars else None)
    elif bars:
        row["last_price"], row["price_date"] = bars[-1][1], bars[-1][0]

    last, ref_date = row["last_price"], row["price_date"] or as_of
    if bars and last is not None:
        w = close_on_or_before(bars, ref_date - timedelta(days=7))
        m = close_on_or_before(bars, minus_month(ref_date))
        row["chg_1w_pct"] = pct(last, w[1]) if w else None
        row["chg_1m_pct"] = pct(last, m[1]) if m else None
        yr = [b for b in bars if b[0] > ref_date - timedelta(days=365)]
        if yr:
            hi = max(max(b[2] for b in yr), last)
            lo = min(min(b[3] for b in yr), last)
            row["high_52w"], row["low_52w"] = hi, lo
            row["pos_52w_pct"] = 100.0 if hi == lo else (last - lo) / (hi - lo) * 100
            if bars[0][0] > ref_date - timedelta(days=350):
                notes.append(f"history starts {bars[0][0]}; 52-wk range is partial")
        if w is None:
            notes.append("no close >= 7 days back; 1W n/a")
        if m is None:
            notes.append("no close >= 1 month back; 1M n/a")
    else:
        notes.append("no usable price data")

    if row["price_date"] and (as_of - row["price_date"]).days > 5:
        notes.append(f"stale price ({row['price_date']})")

    filings = [f for f in parse_filings(rec.get("filings")) if f[1] <= as_of]
    if filings:
        row["latest_form"], row["latest_filed"] = filings[0]
        cutoff = as_of - timedelta(days=7)
        eight_ks = [f[1] for f in filings if f[0].startswith("8-K") and f[1] >= cutoff]
        row["recent_8k"] = bool(eight_ks)
        row["recent_8k_dates"] = sorted({d.isoformat() for d in eight_ks})
    else:
        notes.append("no filings returned")

    if row["last_price"] is None and not filings:
        row["status"] = "ERROR"
    elif notes and any(n.startswith(("fetch error", "no usable", "no filings")) for n in notes):
        row["status"] = "PARTIAL"
    return row


def render(rows, as_of):
    hdr = ("| Ticker | Last price (USD) | Price date | 1W % | 1M % | 52-wk position | "
           "52-wk low-high (USD) | Latest SEC filing | 8-K last 7d | Status |")
    sep = "|" + "---|" * 10
    lines = [f"### Weekly watchlist review - as of {as_of}", "", hdr, sep]
    for r in rows:
        price = "n/a" if r["last_price"] is None else f"{r['last_price']:,.2f}"
        pos = "n/a" if r["pos_52w_pct"] is None else f"{r['pos_52w_pct']:.1f}%"
        rng = ("n/a" if r["low_52w"] is None
               else f"{r['low_52w']:,.2f}-{r['high_52w']:,.2f}")
        filing = ("n/a" if not r["latest_form"]
                  else f"{r['latest_form']} ({r['latest_filed']})")
        flag = ("n/a" if r["recent_8k"] is None
                else ("YES " + ", ".join(r["recent_8k_dates"]) if r["recent_8k"] else "-"))
        lines.append(f"| {r['ticker']} | {price} | {r['price_date'] or 'n/a'} | "
                     f"{fmt_pct(r['chg_1w_pct'])} | {fmt_pct(r['chg_1m_pct'])} | {pos} | "
                     f"{rng} | {filing} | {flag} | {r['status']} |")
    issues = [f"- {r['ticker']}: " + "; ".join(r["notes"]) for r in rows if r["notes"]]
    if issues:
        lines += ["", "Data notes:"] + issues
    return "\n".join(lines)


def facts(rows):
    ok = [r for r in rows if r["chg_1w_pct"] is not None]
    f = []
    if ok:
        avg = sum(r["chg_1w_pct"] for r in ok) / len(ok)
        best = max(ok, key=lambda r: r["chg_1w_pct"])
        worst = min(ok, key=lambda r: r["chg_1w_pct"])
        f.append(f"equal-weight 1W avg {avg:+.1f}% across {len(ok)} names; "
                 f"best {best['ticker']} {best['chg_1w_pct']:+.1f}%, worst {worst['ticker']} {worst['chg_1w_pct']:+.1f}%")
    near_hi = [r["ticker"] for r in rows if r["pos_52w_pct"] is not None and r["pos_52w_pct"] >= 90]
    near_lo = [r["ticker"] for r in rows if r["pos_52w_pct"] is not None and r["pos_52w_pct"] <= 10]
    if near_hi or near_lo:
        f.append(f"near 52-wk high (>=90%): {', '.join(near_hi) or 'none'}; "
                 f"near 52-wk low (<=10%): {', '.join(near_lo) or 'none'}")
    k8 = [f"{r['ticker']} ({', '.join(r['recent_8k_dates'])})" for r in rows if r["recent_8k"]]
    f.append("8-Ks in last 7 days: " + (", ".join(k8) if k8 else "none"))
    bad = [r["ticker"] for r in rows if r["status"] != "OK"]
    if bad:
        f.append("incomplete data: " + ", ".join(bad))
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--json")
    ap.add_argument("--md")
    a = ap.parse_args()
    data = json.load(open(a.input))
    as_of = to_date(data.get("as_of")) or date.today()
    rows = []
    for tkr, rec in (data.get("tickers") or {}).items():
        try:
            rows.append(compute_row(tkr.upper(), rec or {}, as_of))
        except Exception as e:  # never let one ticker kill the run
            rows.append({"ticker": tkr.upper(), "status": "ERROR", "last_price": None,
                         "price_date": None, "chg_1w_pct": None, "chg_1m_pct": None,
                         "pos_52w_pct": None, "low_52w": None, "high_52w": None,
                         "latest_form": None, "latest_filed": None, "recent_8k": None,
                         "recent_8k_dates": [], "notes": [f"processing error: {e}"]})
    md = render(rows, as_of) + "\n\nFacts for summary:\n" + "\n".join("- " + x for x in facts(rows))
    print(md)
    if a.md:
        open(a.md, "w").write(md + "\n")
    if a.json:
        json.dump({"as_of": as_of.isoformat(), "rows": rows, "facts": facts(rows)},
                  open(a.json, "w"), indent=2, default=str)


if __name__ == "__main__":
    sys.exit(main())
