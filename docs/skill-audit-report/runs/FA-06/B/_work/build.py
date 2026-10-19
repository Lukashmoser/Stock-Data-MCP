import re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT = "/home/claude/results/2026-10-13/runs/FA-06/B/ZM_LBO_Model.xlsx"

wb = Workbook()
DARK = PatternFill("solid", fgColor="1F4E79")
LIGHT = PatternFill("solid", fgColor="D9E1F2")
INPUT = PatternFill("solid", fgColor="F2F2F2")
KEY = PatternFill("solid", fgColor="BDD7EE")

FMT_USD = '#,##0.0;(#,##0.0);"-"'
FMT_PS = '$#,##0.00'
FMT_PCT = '0.0%'
FMT_X = '0.0"x"'
FMT_X2 = '0.00"x"'
FMT_SH = '#,##0.000'

REF_RE = re.compile(r"^=('?[A-Za-z0-9 &]+'?!)?\$?[A-Z]{1,3}\$?\d+$")


def put(ws, addr, val, fmt=None, bold=False, fill=None, label=False):
    c = ws[addr]
    c.value = val
    if label:
        c.font = Font(bold=bold)
        return c
    if isinstance(val, str) and val.startswith("="):
        m = REF_RE.match(val)
        if m and m.group(1):
            color = "008000"
        elif m:
            color = "800080"
        else:
            color = "000000"
    elif isinstance(val, (int, float)):
        color = "0000FF"
        if fill is None:
            fill = INPUT
    else:
        color = "0000FF"
    c.font = Font(color=color, bold=bold)
    if fill:
        c.fill = fill
    if fmt:
        c.number_format = fmt
    c.alignment = Alignment(horizontal="right")
    return c


def section(ws, row, text, ncol):
    ws.cell(row=row, column=1, value=text)
    for col in range(1, ncol + 1):
        ws.cell(row=row, column=col).fill = DARK
        ws.cell(row=row, column=col).font = Font(color="FFFFFF", bold=True)


def colhead(ws, row, labels, start=1):
    for i, l in enumerate(labels):
        c = ws.cell(row=row, column=start + i, value=l)
        c.fill = LIGHT
        c.font = Font(bold=True)
        c.alignment = Alignment(horizontal="center" if i else "left")


def lab(ws, row, text, bold=False, col=1):
    c = ws.cell(row=row, column=col, value=text)
    c.font = Font(bold=bold)


# ---------------------------------------------------------------- Inputs
ws = wb.active
ws.title = "Inputs"
ws["A1"] = "Zoom Communications (ZM) - Take-Private LBO: Inputs"
ws["A1"].font = Font(bold=True, size=14)
ws["A2"] = "USD millions except per-share; blue = hard-coded input, black = formula, purple = same-tab link, green = cross-tab link"
ws["A2"].font = Font(italic=True, size=9)

section(ws, 3, "MARKET DATA", 7)
rows = [
    (4, "Current share price (USD)", 98.51, FMT_PS, "stock-data get_quote, close 2026-10-15"),
    (5, "Price date", "2026-10-15", None, ""),
    (6, "Basic shares outstanding (m)", 291.783711, FMT_SH, "10-Q filed 2026-08-26 cover: 263.233m Cl.A + 28.551m Cl.B as of 2026-08-14"),
    (7, "Dilutive securities, treasury method (m)", 6.867, FMT_SH, "Estimate: FY27Q2 weighted diluted 299.746m less basic 292.879m"),
    (8, "Diluted shares (m)", "=B6+B7", FMT_SH, ""),
    (9, "Cash & cash equivalents", 931.99, FMT_USD, "10-Q 2026-07-31"),
    (10, "Short-term marketable securities", 6317.73, FMT_USD, "10-Q 2026-07-31"),
    (11, "Existing debt", 0, FMT_USD, "10-Q 2026-07-31: no borrowings"),
    (12, "SOFR", 0.0388, '0.00%', "FRED SOFR, 2026-10-14"),
    (13, "High-yield OAS (ICE BofA US HY)", 0.0325, '0.00%', "FRED BAMLH0A0HYM2, 2026-10-14"),
    (14, "7-year US Treasury yield", 0.0509, '0.00%', "FRED DGS7, 2026-10-14"),
]
for r, l, v, f, s in rows:
    lab(ws, r, l)
    put(ws, f"B{r}", v, f)
    ws[f"C{r}"] = s
    ws[f"C{r}"].font = Font(italic=True, size=9)

section(ws, 16, "LTM FINANCIALS (four fiscal quarters to 2026-07-31; source: SEC XBRL via stock-data get_financials)", 7)
colhead(ws, 17, ["USD m", "FY26Q3", "FY26Q4", "FY27Q1", "FY27Q2", "LTM"])
q = {
    18: ("Revenue", [1229.84, 1246.99, 1239.01, 1277.22]),
    19: ("Operating income (GAAP)", [310.41, 249.89, 310.47, 314.32]),
    20: ("Depreciation & amortization", [32.39, 32.96, 32.78, 32.33]),
    21: ("Stock-based compensation", [185.28, 185.23, 178.95, 179.78]),
    22: ("Capital expenditures", [15.01, 16.08, 21.11, 22.35]),
}
for r, (l, vals) in q.items():
    lab(ws, r, l)
    for i, v in enumerate(vals):
        put(ws, f"{'BCDE'[i]}{r}", v, FMT_USD)
    put(ws, f"F{r}", f"=SUM(B{r}:E{r})", FMT_USD)
lab(ws, 23, "EBITDA = Op. income + D&A (SBC expensed)", bold=True)
for col in "BCDEF":
    put(ws, f"{col}23", f"={col}19+{col}20", FMT_USD, bold=True, fill=KEY if col == "F" else None)
lab(ws, 24, "Adj. EBITDA incl. SBC add-back (memo)")
for col in "BCDEF":
    put(ws, f"{col}24", f"={col}23+{col}21", FMT_USD)
lab(ws, 25, "EBITDA margin")
for col in "BCDEF":
    put(ws, f"{col}25", f"={col}23/{col}18", FMT_PCT)

section(ws, 27, "TRANSACTION & FINANCING ASSUMPTIONS", 7)
rows = [
    (28, "Offer premium to current price", 0.30, FMT_PCT, "Per user"),
    (29, "Minimum operating cash retained", 500, FMT_USD, "Default (~10% of LTM revenue)"),
    (30, "Transaction / advisory fees (% of EV)", 0.02, FMT_PCT, "Default"),
    (31, "Financing fees (% of debt raised)", 0.025, FMT_PCT, "Default"),
    (32, "Term Loan B size (x LTM EBITDA)", 4.0, FMT_X, "Default"),
    (33, "Term Loan B spread over SOFR", 0.0325, '0.00%', "Default (single-B software TLB)"),
    (34, "Term Loan B mandatory amortization (% p.a.)", 0.01, FMT_PCT, "Market standard"),
    (35, "Senior notes size (x LTM EBITDA)", 2.0, FMT_X, "Default"),
    (36, "Excess cash sweep to Term Loan B", 1.0, FMT_PCT, "Default"),
    (37, "Cash tax rate", 0.23, FMT_PCT, "Default (21% federal + state)"),
    (38, "Exit multiple vs entry multiple (+/- x)", 0.0, FMT_X, "Per user: exit at entry EV/EBITDA"),
    (39, "Holding period (years)", 5, '0', "Per user"),
]
for r, l, v, f, s in rows:
    lab(ws, r, l)
    put(ws, f"B{r}", v, f)
    ws[f"C{r}"] = s
    ws[f"C{r}"].font = Font(italic=True, size=9)

section(ws, 41, "OPERATING ASSUMPTIONS", 7)
colhead(ws, 42, ["", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"])
ops = {
    43: ("Revenue growth", [0.045, 0.045, 0.040, 0.040, 0.035], FMT_PCT),
    44: ("EBITDA margin (SBC expensed)", [0.265, 0.270, 0.275, 0.280, 0.285], FMT_PCT),
    45: ("D&A (% of revenue)", [0.026] * 5, FMT_PCT),
    46: ("Capex (% of revenue)", [0.015] * 5, FMT_PCT),
    47: ("Change in NWC (% of revenue change)", [-0.10] * 5, FMT_PCT),
}
for r, (l, vals, f) in ops.items():
    lab(ws, r, l)
    for i, v in enumerate(vals):
        put(ws, f"{'BCDEF'[i]}{r}", v, f)
ws["A48"] = "NWC: negative % = cash inflow from growth in deferred revenue (Zoom bills annual plans in advance)."
ws["A48"].font = Font(italic=True, size=9)
ws.column_dimensions["A"].width = 46
for col in "BCDEF":
    ws.column_dimensions[col].width = 13
ws.column_dimensions["C"].width = 13

# ---------------------------------------------------------------- S&U
su = wb.create_sheet("Sources & Uses")
su["A1"] = "Sources & Uses"
su["A1"].font = Font(bold=True, size=14)
section(su, 3, "PURCHASE PRICE", 4)
rows = [
    (4, "Current share price (USD)", "=Inputs!B4", FMT_PS),
    (5, "Offer premium", "=Inputs!B28", FMT_PCT),
    (6, "Offer price per share (USD)", "=B4*(1+B5)", FMT_PS),
    (7, "Diluted shares (m)", "=Inputs!B8", FMT_SH),
    (8, "Equity purchase price", "=B6*B7", FMT_USD),
    (9, "Less: cash & short-term investments", "=-(Inputs!B9+Inputs!B10)", FMT_USD),
    (10, "Plus: existing debt", "=Inputs!B11", FMT_USD),
    (11, "Entry enterprise value", "=B8+B9+B10", FMT_USD),
    (12, "LTM EBITDA (SBC expensed)", "=Inputs!F23", FMT_USD),
    (13, "Entry EV / LTM EBITDA", "=B11/B12", FMT_X),
    (14, "Entry EV / LTM Adj. EBITDA (SBC added back)", "=B11/Inputs!F24", FMT_X),
    (15, "Entry EV / LTM revenue", "=B11/Inputs!F18", FMT_X),
]
for r, l, v, f in rows:
    lab(su, r, l, bold=r in (6, 8, 11, 13))
    put(su, f"B{r}", v, f, bold=r in (6, 8, 11, 13), fill=KEY if r in (11, 13) else None)

section(su, 17, "SOURCES", 4)
colhead(su, 18, ["Source", "USD m", "% of total", "x EBITDA"])
lab(su, 19, "Term Loan B (SOFR + spread)")
put(su, "B19", "=Inputs!B32*B12", FMT_USD)
lab(su, 20, "Senior unsecured notes (UST + HY OAS)")
put(su, "B20", "=Inputs!B35*B12", FMT_USD)
lab(su, 21, "Existing cash used (above minimum)")
put(su, "B21", "=Inputs!B9+Inputs!B10-Inputs!B29", FMT_USD)
lab(su, 22, "Sponsor equity (plug)", bold=True)
put(su, "B22", "=B31-B19-B20-B21", FMT_USD, bold=True, fill=KEY)
lab(su, 23, "Total sources", bold=True)
put(su, "B23", "=SUM(B19:B22)", FMT_USD, bold=True)
for r in range(19, 24):
    put(su, f"C{r}", f"=B{r}/$B$23", FMT_PCT)
    put(su, f"D{r}", f"=B{r}/$B$12", FMT_X)

section(su, 25, "USES", 4)
colhead(su, 26, ["Use", "USD m", "% of total", ""])
lab(su, 27, "Purchase of diluted equity")
put(su, "B27", "=B8", FMT_USD)
lab(su, 28, "Refinance existing debt")
put(su, "B28", "=B10", FMT_USD)
lab(su, 29, "Transaction / advisory fees")
put(su, "B29", "=Inputs!B30*B11", FMT_USD)
lab(su, 30, "Financing fees")
put(su, "B30", "=Inputs!B31*(B19+B20)", FMT_USD)
lab(su, 31, "Total uses", bold=True)
put(su, "B31", "=SUM(B27:B30)", FMT_USD, bold=True)
for r in range(27, 32):
    put(su, f"C{r}", f"=B{r}/$B$31", FMT_PCT)
lab(su, 32, "Check: sources - uses (must be 0)")
put(su, "B32", "=ROUND(B23-B31,6)", FMT_USD)

section(su, 34, "CAPITAL STRUCTURE AT CLOSE", 4)
lab(su, 35, "Total debt raised")
put(su, "B35", "=B19+B20", FMT_USD, bold=True)
lab(su, 36, "Total leverage (x LTM EBITDA)")
put(su, "B36", "=B35/B12", FMT_X)
lab(su, 37, "Total leverage (x LTM Adj. EBITDA)")
put(su, "B37", "=B35/Inputs!F24", FMT_X)
lab(su, 38, "Net leverage (x LTM EBITDA, after minimum cash)")
put(su, "B38", "=(B35-Inputs!B29)/B12", FMT_X)
lab(su, 39, "Sponsor equity % of total capitalization")
put(su, "B39", "=B22/(B22+B35)", FMT_PCT)
su.column_dimensions["A"].width = 46
for col in "BCD":
    su.column_dimensions[col].width = 14

# ---------------------------------------------------------------- Operating model
om = wb.create_sheet("Operating Model")
om["A1"] = "Operating Model (USD m)"
om["A1"].font = Font(bold=True, size=14)
cols = "BCDEFG"
colhead(om, 3, ["USD m", "LTM Jul-26", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"])
section(om, 4, "INCOME STATEMENT", 7)
lab(om, 5, "Revenue", bold=True)
put(om, "B5", "=Inputs!F18", FMT_USD, bold=True)
lab(om, 6, "  growth %")
lab(om, 7, "EBITDA (SBC expensed)", bold=True)
put(om, "B7", "=Inputs!F23", FMT_USD, bold=True)
lab(om, 8, "  margin %")
put(om, "B8", "=B7/B5", FMT_PCT)
lab(om, 9, "Depreciation & amortization")
put(om, "B9", "=Inputs!F20", FMT_USD)
lab(om, 10, "EBIT")
put(om, "B10", "=B7-B9", FMT_USD)
lab(om, 11, "Interest expense")
lab(om, 12, "Pre-tax income")
lab(om, 13, "Taxes")
lab(om, 14, "Net income", bold=True)
section(om, 16, "FREE CASH FLOW", 7)
lab(om, 17, "Net income")
lab(om, 18, "Plus: D&A")
lab(om, 19, "Less: capex")
lab(om, 20, "Less: increase in NWC")
lab(om, 21, "Free cash flow available for debt service", bold=True)
lab(om, 22, "Memo: FCF / EBITDA")
inp = "BCDEF"
for i, col in enumerate("CDEFG"):
    prev = cols[i]
    ic = inp[i]
    put(om, f"{col}5", f"={prev}5*(1+Inputs!{ic}43)", FMT_USD, bold=True)
    put(om, f"{col}6", f"={col}5/{prev}5-1", FMT_PCT)
    put(om, f"{col}7", f"={col}5*Inputs!{ic}44", FMT_USD, bold=True)
    put(om, f"{col}8", f"={col}7/{col}5", FMT_PCT)
    put(om, f"{col}9", f"={col}5*Inputs!{ic}45", FMT_USD)
    put(om, f"{col}10", f"={col}7-{col}9", FMT_USD)
    put(om, f"{col}11", f"='Debt Schedule'!{col}26", FMT_USD)
    put(om, f"{col}12", f"={col}10-{col}11", FMT_USD)
    put(om, f"{col}13", f"=MAX(0,{col}12)*Inputs!$B$37", FMT_USD)
    put(om, f"{col}14", f"={col}12-{col}13", FMT_USD, bold=True)
    put(om, f"{col}17", f"={col}14", FMT_USD)
    put(om, f"{col}18", f"={col}9", FMT_USD)
    put(om, f"{col}19", f"=-{col}5*Inputs!{ic}46", FMT_USD)
    put(om, f"{col}20", f"=-({col}5-{prev}5)*Inputs!{ic}47", FMT_USD)
    put(om, f"{col}21", f"=SUM({col}17:{col}20)", FMT_USD, bold=True)
    put(om, f"{col}22", f"={col}21/{col}7", FMT_PCT)
om.column_dimensions["A"].width = 42
for col in cols:
    om.column_dimensions[col].width = 13

# ---------------------------------------------------------------- Debt schedule
ds = wb.create_sheet("Debt Schedule")
ds["A1"] = "Debt Schedule (USD m) - interest on beginning balances (no circularity)"
ds["A1"].font = Font(bold=True, size=14)
colhead(ds, 3, ["USD m", "Close", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"])
lab(ds, 4, "FCF available for debt service")
section(ds, 5, "CASH", 7)
lab(ds, 6, "Beginning cash")
lab(ds, 7, "Plus: FCF")
lab(ds, 8, "Less: debt repayment")
lab(ds, 9, "Ending cash", bold=True)
put(ds, "B9", "=Inputs!B29", FMT_USD, bold=True)
section(ds, 11, "TERM LOAN B", 7)
lab(ds, 12, "Beginning balance")
lab(ds, 13, "Mandatory amortization")
lab(ds, 14, "Optional repayment (cash sweep)")
lab(ds, 15, "Ending balance", bold=True)
put(ds, "B15", "='Sources & Uses'!B19", FMT_USD, bold=True)
lab(ds, 16, "Interest rate (SOFR + spread)")
lab(ds, 17, "Interest expense")
section(ds, 19, "SENIOR UNSECURED NOTES (bullet)", 7)
lab(ds, 20, "Beginning balance")
lab(ds, 21, "Ending balance", bold=True)
put(ds, "B21", "='Sources & Uses'!B20", FMT_USD, bold=True)
lab(ds, 22, "Coupon (7Y UST + HY OAS)")
lab(ds, 23, "Interest expense")
section(ds, 24, "SUMMARY", 7)
lab(ds, 25, "Total debt (ending)", bold=True)
put(ds, "B25", "=B15+B21", FMT_USD, bold=True)
lab(ds, 26, "Total interest expense")
lab(ds, 27, "Total debt / EBITDA")
put(ds, "B27", "=B25/'Operating Model'!B7", FMT_X)
lab(ds, 28, "Net debt / EBITDA")
put(ds, "B28", "=(B25-B9)/'Operating Model'!B7", FMT_X)
lab(ds, 29, "EBITDA / interest")
lab(ds, 30, "Cumulative Term Loan B repaid (%)")
for i, col in enumerate("CDEFG"):
    prev = cols[i]
    put(ds, f"{col}4", f"='Operating Model'!{col}21", FMT_USD)
    put(ds, f"{col}6", f"={prev}9", FMT_USD)
    put(ds, f"{col}7", f"={col}4", FMT_USD)
    put(ds, f"{col}8", f"={col}13+{col}14", FMT_USD)
    put(ds, f"{col}9", f"=SUM({col}6:{col}8)", FMT_USD, bold=True)
    put(ds, f"{col}12", f"={prev}15", FMT_USD)
    put(ds, f"{col}13", f"=-MIN({col}12,'Sources & Uses'!$B$19*Inputs!$B$34)", FMT_USD)
    put(ds, f"{col}14", f"=-MAX(0,MIN({col}12+{col}13,Inputs!$B$36*({col}6+{col}4+{col}13-Inputs!$B$29)))", FMT_USD)
    put(ds, f"{col}15", f"=SUM({col}12:{col}14)", FMT_USD, bold=True)
    put(ds, f"{col}16", f"=Inputs!$B$12+Inputs!$B$33", '0.00%')
    put(ds, f"{col}17", f"={col}12*{col}16", FMT_USD)
    put(ds, f"{col}20", f"={prev}21", FMT_USD)
    put(ds, f"{col}21", f"={col}20", FMT_USD, bold=True)
    put(ds, f"{col}22", f"=Inputs!$B$14+Inputs!$B$13", '0.00%')
    put(ds, f"{col}23", f"={col}20*{col}22", FMT_USD)
    put(ds, f"{col}25", f"={col}15+{col}21", FMT_USD, bold=True)
    put(ds, f"{col}26", f"={col}17+{col}23", FMT_USD)
    put(ds, f"{col}27", f"={col}25/'Operating Model'!{col}7", FMT_X)
    put(ds, f"{col}28", f"=({col}25-{col}9)/'Operating Model'!{col}7", FMT_X)
    put(ds, f"{col}29", f"='Operating Model'!{col}7/{col}26", FMT_X)
    put(ds, f"{col}30", f"=1-{col}15/$B$15", FMT_PCT)
ds.column_dimensions["A"].width = 38
for col in cols:
    ds.column_dimensions[col].width = 13

# ---------------------------------------------------------------- Returns
rt = wb.create_sheet("Returns")
rt["A1"] = "Returns Analysis"
rt["A1"].font = Font(bold=True, size=14)
section(rt, 3, "EXIT (END OF YEAR 5)", 7)
rows = [
    (4, "Year 5 EBITDA", "='Operating Model'!G7", FMT_USD),
    (5, "Exit EV / EBITDA (= entry multiple + adj.)", "='Sources & Uses'!B13+Inputs!B38", FMT_X),
    (6, "Exit enterprise value", "=B4*B5", FMT_USD),
    (7, "Less: debt at exit", "=-'Debt Schedule'!G25", FMT_USD),
    (8, "Plus: cash at exit", "='Debt Schedule'!G9", FMT_USD),
    (9, "Exit equity value", "=SUM(B6:B8)", FMT_USD),
    (10, "Sponsor equity invested", "='Sources & Uses'!B22", FMT_USD),
    (11, "MOIC", "=B9/B10", FMT_X2),
    (12, "IRR", "=IRR(B16:G16)", FMT_PCT),
]
for r, l, v, f in rows:
    lab(rt, r, l, bold=r in (9, 11, 12))
    put(rt, f"B{r}", v, f, bold=r in (9, 11, 12), fill=KEY if r in (9, 11, 12) else None)
colhead(rt, 14, ["Sponsor cash flows", "Year 0", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"])
lab(rt, 15, "Period")
for i, col in enumerate(cols):
    put(rt, f"{col}15", i, '0')
lab(rt, 16, "Cash flow to / (from) sponsor")
put(rt, "B16", "=-B10", FMT_USD)
for col in "CDEF":
    put(rt, f"{col}16", 0, FMT_USD)
put(rt, "G16", "=B9", FMT_USD)

# Sensitivities
def sens(top, title, kind):
    section(rt, top, title, 8)
    lab(rt, top + 1, "Rows: offer premium to current price; columns: exit EV/EBITDA. Center = base case.")
    rt.cell(row=top + 1, column=1).font = Font(italic=True, size=9)
    hdr = top + 2
    c = rt.cell(row=hdr, column=1, value="Premium \\ Exit multiple")
    c.fill = LIGHT; c.font = Font(bold=True)
    steps = [-2, -1, 0, 1, 2]
    for j, s in enumerate(steps):
        col = "BCDEF"[j]
        put(rt, f"{col}{hdr}", f"=$B$5+({s})" if s else "=$B$5", FMT_X, bold=True, fill=LIGHT)
    for lbl, col in (("Sponsor equity", "G"), ("Entry EV/EBITDA", "H")):
        c = rt[f"{col}{hdr}"]; c.value = lbl; c.fill = LIGHT; c.font = Font(bold=True)
    psteps = [-0.10, -0.05, 0, 0.05, 0.10]
    for i, p in enumerate(psteps):
        r = hdr + 1 + i
        put(rt, f"A{r}", f"=Inputs!$B$28+({p})" if p else "=Inputs!$B$28", FMT_PCT, bold=True, fill=LIGHT)
        eq = f"Inputs!$B$4*(1+$A{r})*Inputs!$B$8"
        put(rt, f"G{r}",
            f"={eq}+'Sources & Uses'!$B$10+Inputs!$B$30*({eq}+'Sources & Uses'!$B$9+'Sources & Uses'!$B$10)"
            f"+'Sources & Uses'!$B$30-'Sources & Uses'!$B$19-'Sources & Uses'!$B$20-'Sources & Uses'!$B$21",
            FMT_USD)
        put(rt, f"H{r}", f"=({eq}+'Sources & Uses'!$B$9+'Sources & Uses'!$B$10)/'Sources & Uses'!$B$12", FMT_X)
        for j in range(5):
            col = "BCDEF"[j]
            exit_eq = f"({col}${hdr}*$B$4-'Debt Schedule'!$G$25+'Debt Schedule'!$G$9)"
            if kind == "irr":
                f = f"=({exit_eq}/$G{r})^(1/Inputs!$B$39)-1"
                fmt = FMT_PCT
            else:
                f = f"={exit_eq}/$G{r}"
                fmt = FMT_X2
            center = (i == 2 and j == 2)
            put(rt, f"{col}{r}", f, fmt, bold=center, fill=KEY if center else None)
    return hdr

h1 = sens(18, "SENSITIVITY: IRR", "irr")
h2 = sens(27, "SENSITIVITY: MOIC", "moic")
lab(rt, 36, "Check: center IRR - model IRR")
put(rt, "B36", f"=ROUND(D{h1+3}-B12,8)", '0.0000%')
lab(rt, 37, "Check: center MOIC - model MOIC")
put(rt, "B37", f"=ROUND(D{h2+3}-B11,8)", '0.0000')
rt.column_dimensions["A"].width = 42
for col in "BCDEFGH":
    rt.column_dimensions[col].width = 14

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
    s.freeze_panes = "B3" if s.title != "Inputs" else None

wb.save(OUT)
print("saved", OUT)
