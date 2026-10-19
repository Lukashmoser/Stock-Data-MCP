from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter as L

OUT = "/home/claude/results/2026-10-13/runs/FA-03/A/MSFT_Trading_Comps_2026-10-14.xlsx"
FONT = "Times New Roman"
NAVY = PatternFill("solid", fgColor="1F4E79")
LBLUE = PatternFill("solid", fgColor="D9E1F2")
GREY = PatternFill("solid", fgColor="F2F2F2")
BLUE = "0000FF"
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center")

def f(bold=False, color="000000", size=11):
    return Font(name=FONT, bold=bold, color=color, size=size)

def inp(ws, ref, val, note, fmt="#,##0"):
    c = ws[ref]
    c.value = val
    c.font = f(color=BLUE)
    c.alignment = CENTER
    c.number_format = fmt
    c.comment = Comment(note, "Comps build")
    return c

def fx(ws, ref, formula, fmt="#,##0", bold=False):
    c = ws[ref]
    c.value = formula
    c.font = f(bold=bold)
    c.alignment = CENTER
    c.number_format = fmt
    return c

def section(ws, row, text, ncol):
    ws.cell(row=row, column=1, value=text).font = f(True, "FFFFFF", 12)
    for c in range(1, ncol + 1):
        ws.cell(row=row, column=c).fill = NAVY
    ws.cell(row=row, column=1).alignment = LEFT

def headers(ws, row, labels):
    for i, h in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = f(True)
        c.fill = LBLUE
        c.alignment = CENTER

SEC = "https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{tag}.json"
CIK = {"MSFT": "0000789019", "GOOGL": "0001652044", "AMZN": "0001018724",
       "META": "0001326801", "AAPL": "0000320193", "ORCL": "0001341439"}
PR = {
    "MSFT": "MSFT 8-K Ex.99.1 filed 2026-07-29 (FY26 Q4 release); FY26 10-K filed 2026-07-29",
    "GOOGL": "GOOGL 8-K Ex.99.1 filed 2026-07-22 (Q2'26 release); 10-Q filed 2026-07-23",
    "AMZN": "AMZN 8-K Ex.99.1 filed 2026-07-30 (Q2'26 release); 10-Q filed 2026-07-31",
    "META": "META 8-K Ex.99.1 filed 2026-07-29 (Q2'26 release); 10-Q filed 2026-07-30",
    "AAPL": "AAPL 8-K Ex.99.1 filed 2026-07-30 (Q3 FY26 release); 10-Q filed 2026-07-31",
    "ORCL": "ORCL 8-K Ex.99.1 filed 2026-09-10 (Q1 FY27 release); 10-Q filed 2026-09-11",
}

# ---------------------------------------------------------------- data
# name, ticker, LTM quarter end, fiscal labels
COS = [
    ("Microsoft Corporation", "MSFT", "2026-06-30", "FY26 (Jun-26)", "n/a (FY end)", "n/a (FY end)"),
    ("Alphabet Inc.", "GOOGL", "2026-06-30", "FY25 (Dec-25)", "6M to Jun-25", "6M to Jun-26"),
    ("Amazon.com, Inc.", "AMZN", "2026-06-30", "FY25 (Dec-25)", "6M to Jun-25", "6M to Jun-26"),
    ("Meta Platforms, Inc.", "META", "2026-06-30", "FY25 (Dec-25)", "6M to Jun-25", "6M to Jun-26"),
    ("Apple Inc.", "AAPL", "2026-06-27", "FY25 (Sep-25)", "9M to Jun-25", "9M to Jun-26"),
    ("Oracle Corporation", "ORCL", "2026-08-31", "FY26 (May-26)", "3M to Aug-25", "3M to Aug-26"),
]
# metric -> ticker -> (FY, prior YTD, current YTD), USD millions
BUILD = {
    "Revenue": {
        "MSFT": (331839, 0, 0), "GOOGL": (402836, 186662, 229692), "AMZN": (716924, 323369, 382125),
        "META": (200966, 89830, 117111), "AAPL": (416161, 313695, 364357), "ORCL": (67357, 14926, 19345)},
    "Revenue - prior-year LTM": {
        "MSFT": (281724, 0, 0), "GOOGL": (350018, 165281, 186662), "AMZN": (637959, 291290, 323369),
        "META": (164501, 75527, 89830), "AAPL": (391035, 296105, 313695), "ORCL": (57399, 13307, 14926)},
    "Operating income (EBIT)": {
        "MSFT": (155237, 0, 0), "GOOGL": (129039, 61877, 80466), "AMZN": (79975, 37576, 51313),
        "META": (83276, 37997, 41647), "AAPL": (133050, 100623, 122432), "ORCL": (20606, 4277, 6728)},
    "D&A (cash flow statement)": {
        "MSFT": (38534, 0, 0), "GOOGL": (21136, 9485, 13586), "AMZN": (65756, 29489, 38933),
        "META": (18616, 8242, 12355), "AAPL": (11698, 8571, 9973), "ORCL": (9294, 1771, 3358)},
    "Net income (to parent)": {
        "MSFT": (133749, 0, 0), "GOOGL": (132170, 62736, 174771), "AMZN": (77670, 35291, 92902),
        "META": (60458, 34981, 42621), "AAPL": (112010, 84544, 101464), "ORCL": (17087, 2927, 4760)},
}
TAG = {"Revenue": "RevenueFromContractWithCustomerExcludingAssessedTax",
       "Revenue - prior-year LTM": "RevenueFromContractWithCustomerExcludingAssessedTax",
       "Operating income (EBIT)": "OperatingIncomeLoss",
       "D&A (cash flow statement)": "DepreciationDepletionAndAmortization",
       "Net income (to parent)": "NetIncomeLoss"}
SPECIAL = {
    ("GOOGL", "Revenue"): "SEC XBRL us-gaap:Revenues (GOOGL 10-K filed 2026-02-05; 10-Qs filed 2025-07-24, 2026-07-23)",
    ("GOOGL", "Revenue - prior-year LTM"): "SEC XBRL us-gaap:Revenues / RevenueFromContract... (GOOGL 10-K filed 2025-02-05; 10-Qs 2024-07-24, 2025-07-24)",
    ("GOOGL", "D&A (cash flow statement)"): "SEC XBRL us-gaap:Depreciation (depreciation of property & equipment; Alphabet does not present intangible amortization separately on the cash flow statement)",
    ("MSFT", "D&A (cash flow statement)"): "MSFT 8-K Ex.99.1 filed 2026-07-29, cash flow statement line 'Depreciation, amortization, and other' FY26 = 38,534 (FY25 = 29,433). Includes minor other non-cash items.",
    ("MSFT", "Operating income (EBIT)"): "SEC XBRL us-gaap:OperatingIncomeLoss, FY ended 2026-06-30, MSFT 10-K filed 2026-07-29",
    ("ORCL", "D&A (cash flow statement)"): "Depreciation + amortization of intangibles. FY26: 7,623 + 1,671 (10-K filed 2026-06-22, XBRL us-gaap:Depreciation & AmortizationOfIntangibleAssets); Q1 FY26: 1,351 + 420 (10-Q filed 2025-09-10); Q1 FY27: 3,156 + 202 (8-K Ex.99.1 filed 2026-09-10)",
    ("ORCL", "Operating income (EBIT)"): "FY26 and Q1 FY26 from SEC XBRL us-gaap:OperatingIncomeLoss; Q1 FY27 = 6,728 from ORCL 8-K Ex.99.1 filed 2026-09-10 (not yet in XBRL concept API)",
    ("AAPL", "Revenue - prior-year LTM"): "FY24 391,035 and 9M FY25 313,695 from SEC XBRL; 9M FY24 (to 2024-06-29) = 296,105 from model knowledge (Q1 119,575 + Q2 90,753 + Q3 85,777), not re-verified this session",
}

wb = Workbook()
ws = wb.active
ws.title = "Comps"
lb = wb.create_sheet("LTM_Build")
nt = wb.create_sheet("Notes")

# ---------------------------------------------------------------- LTM build sheet
lb["A1"] = "LTM BUILD - LTM = Last fiscal year - Prior-year YTD + Current YTD (USD millions)"
lb["A1"].font = f(True, size=12)
headers(lb, 3, ["Ticker", "Metric", "Last FY period", "Last FY value", "Prior-year YTD period",
                "Less: prior-year YTD", "Current YTD period", "Plus: current YTD", "LTM", "Source"])
ltm_ref = {}  # (ticker, metric) -> cell ref on LTM_Build
r = 4
for name, t, qe, fyl, pyl, cyl in COS:
    for m, d in BUILD.items():
        fy, py, cy = d[t]
        lb.cell(row=r, column=1, value=t).font = f(True)
        lb.cell(row=r, column=2, value=m).font = f()
        prior = m.startswith("Revenue - prior")
        if prior:
            if t == "MSFT":
                labs = ("FY25 (Jun-25)", "n/a", "n/a")
            elif t == "AAPL":
                labs = ("FY24 (Sep-24)", "9M to Jun-24", "9M to Jun-25")
            elif t == "ORCL":
                labs = ("FY25 (May-25)", "3M to Aug-24", "3M to Aug-25")
            else:
                labs = ("FY24 (Dec-24)", "6M to Jun-24", "6M to Jun-25")
        else:
            labs = (fyl, pyl, cyl)
        lb.cell(row=r, column=3, value=labs[0]).font = f()
        lb.cell(row=r, column=5, value=labs[1]).font = f()
        lb.cell(row=r, column=7, value=labs[2]).font = f()
        src = SPECIAL.get((t, m)) or f"SEC XBRL companyconcept us-gaap:{TAG[m]} ({SEC.format(cik=CIK[t], tag=TAG[m])}); filings: {PR[t]}"
        if t == "AMZN" and m.startswith("D&A"):
            src += ". Amazon D&A includes amortization of capitalized content, operating lease assets and other; LTM ties to company-reported TTM 75,200."
        inp(lb, f"D{r}", fy, src)
        inp(lb, f"F{r}", py, src)
        inp(lb, f"H{r}", cy, src)
        fx(lb, f"I{r}", f"=D{r}-F{r}+H{r}", bold=True)
        lb.cell(row=r, column=10, value=src).font = f(size=9)
        ltm_ref[(t, m)] = f"LTM_Build!$I${r}"
        r += 1
    r += 1
for c, w in zip("ABCDEFGHIJ", [9, 26, 15, 14, 16, 15, 16, 15, 14, 90]):
    lb.column_dimensions[c].width = w
lb.freeze_panes = "C4"

# ---------------------------------------------------------------- Comps sheet
NC = 13
ws["A1"] = "LARGE-CAP TECHNOLOGY - COMPARABLE COMPANY ANALYSIS (TARGET: MICROSOFT)"
ws["A1"].font = f(True, size=14)
ws["A2"] = "Microsoft (MSFT) vs. Alphabet (GOOGL) • Amazon (AMZN) • Meta Platforms (META) • Apple (AAPL) • Oracle (ORCL)"
ws["A2"].font = f(size=11)
ws["A3"] = ("Prices as of 2026-10-14 close | LTM aligned to each company's latest reported quarter | "
            "All figures in USD millions except per-share amounts and ratios | Statistics computed on the 5 peers (MSFT excluded)")
ws["A3"].font = f(size=10)

# Operating section
section(ws, 5, "OPERATING STATISTICS & FINANCIAL METRICS (LTM)", NC)
headers(ws, 6, ["Company", "Ticker", "LTM Qtr End", "LTM Revenue", "Prior-Yr LTM Revenue",
                "Revenue Growth (YoY) %", "LTM EBIT", "EBIT Margin %", "LTM D&A",
                "LTM EBITDA", "EBITDA Margin %", "LTM Net Income", "Net Margin %"])
OP = {}
row = 7
for i, (name, t, qe, *_rest) in enumerate(COS):
    if i == 1:
        row += 0
    OP[t] = row
    ws.cell(row=row, column=1, value=name + (" (target)" if t == "MSFT" else "")).font = f(True)
    ws.cell(row=row, column=2, value=t).font = f(True)
    inp(ws, f"C{row}", qe, f"Latest reported fiscal quarter end used for LTM. Source: {PR[t]}", "@")
    fx(ws, f"D{row}", "=" + ltm_ref[(t, "Revenue")])
    fx(ws, f"E{row}", "=" + ltm_ref[(t, "Revenue - prior-year LTM")])
    fx(ws, f"F{row}", f"=D{row}/E{row}-1", "0.0%")
    fx(ws, f"G{row}", "=" + ltm_ref[(t, "Operating income (EBIT)")])
    fx(ws, f"H{row}", f"=G{row}/D{row}", "0.0%")
    fx(ws, f"I{row}", "=" + ltm_ref[(t, "D&A (cash flow statement)")])
    fx(ws, f"J{row}", f"=G{row}+I{row}")
    fx(ws, f"K{row}", f"=J{row}/D{row}", "0.0%")
    fx(ws, f"L{row}", "=" + ltm_ref[(t, "Net income (to parent)")])
    fx(ws, f"M{row}", f"=L{row}/D{row}", "0.0%")
    row += 1
peer_first, peer_last = OP["GOOGL"], OP["ORCL"]
row += 1  # blank row
STATS = [("Maximum", "MAX({r})"), ("75th Percentile", "QUARTILE({r},3)"), ("Median", "MEDIAN({r})"),
         ("25th Percentile", "QUARTILE({r},1)"), ("Minimum", "MIN({r})")]
op_stat_rows = {}
for lab, tmpl in STATS:
    ws.cell(row=row, column=1, value=f"Peer {lab}").font = f(True)
    for c in range(1, NC + 1):
        ws.cell(row=row, column=c).fill = GREY
    for col in "FHKM":
        rng = f"{col}{peer_first}:{col}{peer_last}"
        fx(ws, f"{col}{row}", "=" + tmpl.format(r=rng), "0.0%")
    op_stat_rows[lab] = row
    row += 1

# Valuation section
row += 1
section(ws, row, "VALUATION MULTIPLES", NC)
row += 1
headers(ws, row, ["Company", "Ticker", "Share Price (USD)", "Diluted Shares (mm)", "Market Cap",
                  "Total Debt", "Cash & ST Investments", "Enterprise Value", "EV / LTM Revenue",
                  "EV / LTM EBITDA", "P/E (LTM GAAP)", "EV / LTM EBIT", "LTM Diluted EPS (USD)"])
row += 1
MKT = {  # price, shares, debt, cash, notes
    "MSFT": (533.69, 7443, 40294, 76843,
             "Shares: Q4 FY26 diluted weighted avg 7,443mm (8-K Ex.99.1 filed 2026-07-29).",
             "Debt 40,294 = current portion LTD 9,227 + LTD 31,067 at 2026-06-30 (8-K Ex.99.1 filed 2026-07-29). Leases excluded.",
             "Cash 76,843 = cash & equivalents 20,935 + short-term investments 55,908 at 2026-06-30. Equity & other investments (36,348) excluded."),
    "GOOGL": (347.64, 12306, 98165, 242474,
              "Shares: 12,306mm = Q2'26 net income to common 112,107 / diluted EPS $9.11 (derived from 8-K Ex.99.1 filed 2026-07-22). Basic outstanding at 2026-06-30 = 12,230mm.",
              "Debt 98,165 = long-term debt at 2026-06-30 (8-K Ex.99.1 filed 2026-07-22); no current-debt line shown. Leases and mandatory convertible preferred excluded.",
              "Cash 242,474 = cash & equivalents 55,911 + marketable securities 186,563 at 2026-06-30. Non-marketable equity securities excluded."),
    "AMZN": (254.08, 10903, 128894, 122988,
             "Shares: Q2'26 diluted weighted avg 10,903mm (8-K Ex.99.1 filed 2026-07-30).",
             "Debt 128,894 = long-term debt at 2026-06-30 (8-K Ex.99.1 filed 2026-07-30). Current portion sits in accrued expenses and is not separately shown; lease liabilities (94,338 LT) excluded.",
             "Cash 122,988 = cash & equivalents 78,213 + marketable securities 44,775 at 2026-06-30. Anthropic and other equity stakes excluded."),
    "META": (737.54, 2566, 83664, 90260,
             "Shares: Q2'26 diluted weighted avg 2,566mm (8-K Ex.99.1 filed 2026-07-29).",
             "Debt 83,664 = long-term debt at 2026-06-30 (8-K Ex.99.1 filed 2026-07-29). Operating leases excluded.",
             "Cash 90,260 = cash & equivalents 15,462 + marketable securities 74,798 at 2026-06-30."),
    "AAPL": (342.96, 14714.7, 84344, 146517,
             "Shares: Q3 FY26 diluted weighted avg 14,714.7mm (8-K Ex.99.1 filed 2026-07-30).",
             "Debt 84,344 = commercial paper 1,997 + term debt current 11,007 + term debt non-current 71,340 at 2026-06-27.",
             "Cash 146,517 = cash & equivalents 39,544 + current marketable securities 22,855 + non-current marketable securities 84,118 at 2026-06-27."),
    "ORCL": (130.55, 3000, 125337, 37077,
             "Shares: Q1 FY27 diluted weighted avg 3,000mm (8-K Ex.99.1 filed 2026-09-10).",
             "Debt 125,337 = notes payable & borrowings current 7,625 + non-current 117,712 at 2026-08-31 (8-K Ex.99.1 filed 2026-09-10). Leases and preferred stock excluded.",
             "Cash 37,077 = cash & equivalents 36,369 + marketable securities 708 at 2026-08-31."),
}
VAL = {}
for name, t, *_ in COS:
    p, sh, debt, cash, nsh, nd, nc = MKT[t]
    VAL[t] = row
    o = OP[t]
    ws.cell(row=row, column=1, value=name + (" (target)" if t == "MSFT" else "")).font = f(True)
    ws.cell(row=row, column=2, value=t).font = f(True)
    inp(ws, f"C{row}", p, f"Closing price 2026-10-14, stockanalysis.com/stocks/{t.lower()}/history/ (accessed 2026-10-14)", "#,##0.00")
    inp(ws, f"D{row}", sh, nsh, "#,##0.0")
    fx(ws, f"E{row}", f"=C{row}*D{row}")
    inp(ws, f"F{row}", debt, nd)
    inp(ws, f"G{row}", cash, nc)
    fx(ws, f"H{row}", f"=E{row}+F{row}-G{row}")
    fx(ws, f"I{row}", f"=H{row}/D{o}", '0.0"x"')
    fx(ws, f"J{row}", f"=H{row}/J{o}", '0.0"x"')
    fx(ws, f"K{row}", f"=E{row}/L{o}", '0.0"x"')
    fx(ws, f"L{row}", f"=H{row}/G{o}", '0.0"x"')
    fx(ws, f"M{row}", f"=L{o}/D{row}", "#,##0.00")
    row += 1
vf, vl = VAL["GOOGL"], VAL["ORCL"]
row += 1
val_stat_rows = {}
for lab, tmpl in STATS:
    ws.cell(row=row, column=1, value=f"Peer {lab}").font = f(True)
    for c in range(1, NC + 1):
        ws.cell(row=row, column=c).fill = GREY
    for col in "IJKL":
        fx(ws, f"{col}{row}", "=" + tmpl.format(r=f"{col}{vf}:{col}{vl}"), '0.0"x"')
    val_stat_rows[lab] = row
    row += 1
med = val_stat_rows["Median"]
ws.cell(row=row, column=1, value="MSFT premium / (discount) to peer median").font = f(True)
for col in "IJKL":
    fx(ws, f"{col}{row}", f"={col}{VAL['MSFT']}/{col}{med}-1", "0.0%;(0.0%)")
prem_row = row

# Implied valuation
row += 2
section(ws, row, "IMPLIED MSFT VALUE AT PEER MULTIPLES (USD per share)", NC)
row += 1
headers(ws, row, ["Multiple", "MSFT LTM Metric", "Peer 25th", "Peer Median", "Peer 75th",
                  "Implied Price @25th", "Implied Price @Median", "Implied Price @75th",
                  "Current Price", "Upside/(Down) @Median", "", "", ""])
row += 1
m = VAL["MSFT"]
o = OP["MSFT"]
for lab, metric_ref, col, is_ev in [("EV / LTM Revenue", f"D{o}", "I", True),
                                    ("EV / LTM EBITDA", f"J{o}", "J", True),
                                    ("P/E (LTM GAAP)", f"L{o}", "K", False)]:
    ws.cell(row=row, column=1, value=lab).font = f(True)
    fx(ws, f"B{row}", "=" + metric_ref)
    for dst, stat in zip("CDE", ["25th Percentile", "Median", "75th Percentile"]):
        fx(ws, f"{dst}{row}", f"={col}{val_stat_rows[stat]}", '0.0"x"')
    for dst, srcm in zip("FGH", "CDE"):
        if is_ev:
            fx(ws, f"{dst}{row}", f"=({srcm}{row}*B{row}-$F${m}+$G${m})/$D${m}", "#,##0.00")
        else:
            fx(ws, f"{dst}{row}", f"={srcm}{row}*B{row}/$D${m}", "#,##0.00")
    fx(ws, f"I{row}", f"=$C${m}", "#,##0.00")
    fx(ws, f"J{row}", f"=G{row}/I{row}-1", "0.0%;(0.0%)")
    row += 1

# formatting
for c in range(1, NC + 1):
    ws.column_dimensions[L(c)].width = 16
ws.column_dimensions["A"].width = 38
for rr in range(5, row + 1):
    ws.row_dimensions[rr].height = 22
ws.row_dimensions[6].height = 34
ws.freeze_panes = "C7"

# ---------------------------------------------------------------- Notes
notes = [
    "NOTES & METHODOLOGY",
    "",
    "Purpose: trading comparables for Microsoft (MSFT) for investment committee valuation review. Peer group as specified: GOOGL, AMZN, META, AAPL, ORCL.",
    "Statistics (Max / 75th / Median / 25th / Min) are computed over the five peers only; MSFT is shown for comparison and excluded from the ranges.",
    "",
    "DATA SOURCES",
    "- Financials: SEC EDGAR XBRL company-concept API (data.sec.gov) and each company's latest 8-K Exhibit 99.1 earnings release (see cell comments and LTM_Build column J).",
    "- Share prices: daily closes for 2026-10-14 from stockanalysis.com price history pages (ORCL 2026-10-13 close of 143.20 cross-checked on financialcontent.com).",
    "- No institutional data feed (FactSet / S&P / Daloopa / Bloomberg) was available in this session; figures were not cross-checked against a second vendor.",
    "",
    "PERIODS",
    "- LTM is aligned to each company's latest reported quarter: MSFT 2026-06-30 (FY26), GOOGL / AMZN / META 2026-06-30, AAPL 2026-06-27, ORCL 2026-08-31.",
    "- LTM = last fiscal year - prior-year YTD + current YTD (see LTM_Build). Revenue growth = LTM vs. the LTM period one year earlier.",
    "- Fiscal year ends differ (Jun / Dec / Sep / May); LTM quarter ends span 2026-06-27 to 2026-08-31.",
    "",
    "DEFINITIONS",
    "- EBITDA = GAAP operating income + depreciation & amortization from the cash flow statement. Unadjusted: stock-based compensation is NOT added back; restructuring / legal charges are NOT normalised.",
    "- MSFT D&A uses the cash flow line 'Depreciation, amortization, and other'; AMZN D&A includes amortization of capitalized content and lease assets; GOOGL D&A is depreciation of property & equipment only.",
    "- Market cap = 2026-10-14 close x latest-quarter diluted weighted-average shares (proxy for fully diluted shares).",
    "- Enterprise value = market cap + total financial debt - cash, cash equivalents and marketable securities. Lease liabilities, preferred stock, non-controlling interests and strategic equity stakes are excluded.",
    "- P/E = market cap / LTM GAAP net income attributable to the parent (equivalent to price / LTM diluted EPS).",
    "",
    "KEY CAVEATS FOR THE COMMITTEE",
    "- GOOGL and AMZN LTM GAAP net income is heavily inflated by unrealised gains on equity securities (GOOGL Q2'26 alone: +99.0bn pre-tax gain, +77.1bn to net income; AMZN Q2'26 non-operating income 53.4bn, primarily Anthropic). Their P/E ratios therefore understate the earnings multiple; prefer EV/EBITDA and EV/EBIT for those names.",
    "- META LTM net income includes the Q3'25 one-time income tax charge (net income 2.7bn that quarter) and Q2'26 legal (2.4bn) and severance (1.2bn) charges.",
    "- ORCL is in a heavy AI-infrastructure capex cycle (LTM free cash flow approx. -28.7bn) and carries high leverage; its 10-14 price fell 8.8% on the day.",
    "- AAPL's 9M FY24 revenue (296,105, used only for the prior-year LTM revenue denominator) was taken from model knowledge and not re-verified in this session.",
    "",
    "COLOR CONVENTION: blue font = hard-coded input (every input has a cell comment with its source); black font = formula.",
]
for i, t in enumerate(notes, 1):
    c = nt.cell(row=i, column=1, value=t)
    c.font = f(bold=(t.isupper() and t != ""))
    c.alignment = Alignment(wrap_text=True, vertical="top")
nt.column_dimensions["A"].width = 160

wb.save(OUT)
print("saved", OUT)
