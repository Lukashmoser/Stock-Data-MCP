import datetime as dt, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import LineChart, ScatterChart, Reference, Series
from openpyxl.workbook.defined_name import DefinedName

RUN = "/home/claude/results/2026-10-13/runs/FA-12/A"
os.makedirs(f"{RUN}/out", exist_ok=True)

# (date of month-end trading day, MSFT adj close (Yahoo), 10Y CMT (Treasury))
raw = """2021-09-30 270.57 1.52
2021-10-29 318.26 1.55
2021-11-30 317.86 1.43
2021-12-31 323.37 1.52
2022-01-31 299.00 1.79
2022-02-28 287.88 1.83
2022-03-31 297.05 2.32
2022-04-29 267.38 2.89
2022-05-31 262.55 2.85
2022-06-30 248.02 2.98
2022-07-29 271.11 2.67
2022-08-31 253.04 3.15
2022-09-30 225.39 3.83
2022-10-31 224.65 4.10
2022-11-30 247.61 3.68
2022-12-30 232.74 3.88
2023-01-31 240.50 3.52
2023-02-28 242.67 3.92
2023-03-31 280.49 3.48
2023-04-28 298.94 3.44
2023-05-31 320.20 3.64
2023-06-30 332.04 3.81
2023-07-31 327.54 3.97
2023-08-31 320.26 4.09
2023-09-29 308.52 4.59
2023-10-31 330.37 4.88
2023-11-30 370.99 4.37
2023-12-29 368.18 3.88
2024-01-31 389.27 3.99
2024-02-29 405.74 4.25
2024-03-28 412.69 4.20
2024-04-30 381.90 4.69
2024-05-31 407.94 4.51
2024-06-28 439.21 4.36
2024-07-31 411.10 4.09
2024-08-30 410.65 3.91
2024-09-30 423.61 3.81
2024-10-31 400.03 4.28
2024-11-29 417.71 4.18
2024-12-31 415.78 4.58
2025-01-31 409.42 4.58
2025-02-28 392.38 4.24
2025-03-31 371.03 4.23
2025-04-30 390.67 4.17
2025-05-30 455.85 4.41
2025-06-30 492.54 4.24
2025-07-31 528.28 4.37
2025-08-29 502.56 4.23
2025-09-30 513.72 4.16
2025-10-31 513.58 4.11
2025-11-28 488.91 4.02
2025-12-31 480.57 4.18
2026-01-30 427.58 4.26
2026-02-27 391.15 3.97
2026-03-31 368.68 4.30
2026-04-30 406.13 4.40
2026-05-29 449.39 4.45
2026-06-30 372.32 4.44
2026-07-31 463.85 4.75
2026-08-31 507.29 4.75
2026-09-30 512.90 5.29"""
rows = []
for line in raw.splitlines():
    d, p, y = line.split()
    rows.append((dt.date.fromisoformat(d), float(p), float(y)))
N = len(rows)
assert N == 61

BLUE = Font(color="0000FF"); BLACK = Font(color="000000"); GREEN = Font(color="008000")
BOLD = Font(bold=True); HDR = PatternFill("solid", fgColor="DDEBF7"); WRAP = Alignment(wrap_text=True, vertical="top")

wb = Workbook()
# ---------------- Inputs ----------------
ws = wb.active; ws.title = "Inputs"
ws["A1"] = "Inputs - MSFT monthly adjusted close and month-end 10-year Treasury yield"; ws["A1"].font = Font(bold=True, size=12)
ws["A2"] = "Blue = hardcoded input. Window: 61 month-ends 2021-09-30 to 2026-09-30 (Sep-2021 is the base month for the first return). Retrieved 2026-10-15/16."
hdr = ["Month-end date", "MSFT adjusted close (USD)", "10Y Treasury yield (% p.a.)"]
src = ["Source: last trading day of each month per U.S. Treasury Daily Par Yield Curve file (home.treasury.gov). Note: Treasury and NYSE trading calendars are aligned at every month-end in this window.",
       "Source: Yahoo Finance MSFT historical prices, monthly frequency, 'Adj Close' column (adjusted for splits and dividends; Yahoo month bar = last trading day close). https://finance.yahoo.com/quote/MSFT/history/?frequency=1mo",
       "Source: U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates, '10 Yr' column, value on the last trading day of the month. https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/<year>/all?type=daily_treasury_yield_curve (equivalent to FRED DGS10)"]
for j, (h, s) in enumerate(zip(hdr, src), start=1):
    c = ws.cell(row=4, column=j, value=h); c.font = BOLD; c.fill = HDR; c.alignment = WRAP
    c = ws.cell(row=5, column=j, value=s); c.alignment = WRAP; c.font = Font(italic=True, size=8)
FIRST = 6; LAST = FIRST + N - 1
for i, (d, p, y) in enumerate(rows):
    r = FIRST + i
    ws.cell(row=r, column=1, value=d).number_format = "yyyy-mm-dd"
    ws.cell(row=r, column=2, value=p).number_format = "#,##0.00"
    ws.cell(row=r, column=3, value=y).number_format = "0.00"
    for col in (1, 2, 3): ws.cell(row=r, column=col).font = BLUE
ws.column_dimensions["A"].width = 16; ws.column_dimensions["B"].width = 30; ws.column_dimensions["C"].width = 30
ws.row_dimensions[5].height = 150
ws.freeze_panes = "A6"

# ---------------- Calc ----------------
cs = wb.create_sheet("Calc")
cs["A1"] = "Calc - all cells are live formulas (green = link to Inputs, black = calculation)"; cs["A1"].font = Font(bold=True, size=12)
ch = ["Month-end date", "MSFT adj close", "10Y yield (%)", "MSFT monthly return", "Change in 10Y yield (pp)", "12m rolling correlation"]
for j, h in enumerate(ch, start=1):
    c = cs.cell(row=4, column=j, value=h); c.font = BOLD; c.fill = HDR; c.alignment = WRAP
for i in range(N):
    r = FIRST + i
    for col, L in ((1, "A"), (2, "B"), (3, "C")):
        c = cs.cell(row=r, column=col, value=f"=Inputs!{L}{r}"); c.font = GREEN
    cs.cell(row=r, column=1).number_format = "yyyy-mm-dd"
    cs.cell(row=r, column=2).number_format = "#,##0.00"
    cs.cell(row=r, column=3).number_format = "0.00"
    if i >= 1:
        c = cs.cell(row=r, column=4, value=f"=B{r}/B{r-1}-1"); c.number_format = "0.0%"
        c = cs.cell(row=r, column=5, value=f"=C{r}-C{r-1}"); c.number_format = "0.00"
    if i >= 12:
        c = cs.cell(row=r, column=6, value=f"=CORREL(D{r-11}:D{r},E{r-11}:E{r})"); c.number_format = "0.000"
RET0 = FIRST + 1
cs["H4"] = "Full-period statistics"; cs["H4"].font = BOLD; cs["H4"].fill = HDR; cs["I4"].fill = HDR
stats = [
    ("Full-period correlation (returns vs yield change)", f"=CORREL(D{RET0}:D{LAST},E{RET0}:E{LAST})", "0.000"),
    ("Number of monthly return observations", f"=COUNT(D{RET0}:D{LAST})", "0"),
    ("Number of 12m rolling windows", f"=COUNT(F{FIRST}:F{LAST})", "0"),
    ("Latest 12m rolling correlation", f"=INDEX(F{FIRST}:F{LAST},COUNTA(A{FIRST}:A{LAST}))", "0.000"),
    ("Average monthly MSFT return", f"=AVERAGE(D{RET0}:D{LAST})", "0.0%"),
    ("Std dev monthly MSFT return", f"=STDEV(D{RET0}:D{LAST})", "0.0%"),
    ("Average monthly yield change (pp)", f"=AVERAGE(E{RET0}:E{LAST})", "0.00"),
    ("Std dev monthly yield change (pp)", f"=STDEV(E{RET0}:E{LAST})", "0.00"),
    ("Beta of MSFT return to +1pp yield change", f"=SLOPE(D{RET0}:D{LAST},E{RET0}:E{LAST})", "0.0%"),
    ("Min 12m rolling correlation", f"=MIN(F{FIRST}:F{LAST})", "0.000"),
    ("Max 12m rolling correlation", f"=MAX(F{FIRST}:F{LAST})", "0.000"),
]
for k, (lab, f, nf) in enumerate(stats):
    r = 5 + k
    cs.cell(row=r, column=8, value=lab)
    c = cs.cell(row=r, column=9, value=f); c.number_format = nf
for col, w in zip("ABCDEFGHI", [14, 14, 12, 14, 14, 14, 3, 46, 12]):
    cs.column_dimensions[col].width = w
cs.freeze_panes = "A6"

wb.defined_names["FullPeriodCorrel"] = DefinedName("FullPeriodCorrel", attr_text="Calc!$I$5")
wb.defined_names["LatestRollingCorrel"] = DefinedName("LatestRollingCorrel", attr_text="Calc!$I$8")
wb.defined_names["MSFT_AdjClose"] = DefinedName("MSFT_AdjClose", attr_text=f"Inputs!$B${FIRST}:$B${LAST}")
wb.defined_names["UST10Y_Yield"] = DefinedName("UST10Y_Yield", attr_text=f"Inputs!$C${FIRST}:$C${LAST}")

# ---------------- Summary ----------------
ss = wb.create_sheet("Summary")
ss["A1"] = "MSFT returns vs 10-year Treasury yield changes - Summary"; ss["A1"].font = Font(bold=True, size=13)
items = [
    ("First month in data", f"=Calc!A{FIRST}", "yyyy-mm-dd"),
    ("Last month in data", f"=Calc!A{LAST}", "yyyy-mm-dd"),
    ("Monthly rows (prices/yields)", f"=COUNT(Calc!A{FIRST}:A{LAST})", "0"),
    ("First MSFT adj close (USD)", f"=Calc!B{FIRST}", "#,##0.00"),
    ("Last MSFT adj close (USD)", f"=Calc!B{LAST}", "#,##0.00"),
    ("First 10Y yield (%)", f"=Calc!C{FIRST}", "0.00"),
    ("Last 10Y yield (%)", f"=Calc!C{LAST}", "0.00"),
    ("Full-period correlation", "=FullPeriodCorrel", "0.000"),
    ("Latest 12m rolling correlation", "=LatestRollingCorrel", "0.000"),
    ("Beta: MSFT return per +1pp yield", "=Calc!I13", "0.0%"),
]
for k, (lab, f, nf) in enumerate(items):
    r = 3 + k
    ss.cell(row=r, column=1, value=lab)
    c = ss.cell(row=r, column=2, value=f); c.number_format = nf; c.font = GREEN
ss.column_dimensions["A"].width = 34; ss.column_dimensions["B"].width = 14
ss["A14"] = "Correlation = Pearson correlation of simple monthly MSFT total-return-proxy (adj close) returns with monthly change in 10Y CMT yield (percentage points)."
ss["A14"].font = Font(italic=True, size=8)

lc = LineChart()
lc.title = "MSFT monthly return vs change in 10Y yield: 12-month rolling correlation"
lc.y_axis.title = "Correlation"; lc.x_axis.title = "Month-end"
lc.y_axis.scaling.min = -1; lc.y_axis.scaling.max = 1
lc.x_axis.number_format = "yyyy-mm"
roll_first = FIRST + 12
data = Reference(cs, min_col=6, min_row=roll_first, max_row=LAST)
s = Series(data, title="12m rolling correlation"); lc.series.append(s)
# full-period reference line via helper column in Calc (formula)
cs.cell(row=4, column=11, value="Full-period correl (chart helper)").font = BOLD
for r in range(roll_first, LAST + 1):
    c = cs.cell(row=r, column=11, value="=FullPeriodCorrel"); c.number_format = "0.000"
cs.column_dimensions["K"].width = 16
s2 = Series(Reference(cs, min_col=11, min_row=roll_first, max_row=LAST), title="Full-period correlation")
s2.graphicalProperties.line.dashStyle = "dash"
lc.series.append(s2)
lc.set_categories(Reference(cs, min_col=1, min_row=roll_first, max_row=LAST))
lc.height = 9; lc.width = 22
lc.x_axis.delete = False; lc.y_axis.delete = False
lc.x_axis.tickLblPos = "low"
ss.add_chart(lc, "D3")

sc = ScatterChart()
sc.title = "Monthly MSFT return vs monthly change in 10Y yield"
sc.style = 13
sc.x_axis.title = "Change in 10Y yield (pp)"; sc.y_axis.title = "MSFT monthly return"
xs = Reference(cs, min_col=5, min_row=RET0, max_row=LAST)
ys = Reference(cs, min_col=4, min_row=RET0, max_row=LAST)
ser = Series(ys, xs, title="Monthly observations")
ser.marker.symbol = "circle"; ser.graphicalProperties.line.noFill = True
sc.series.append(ser)
sc.x_axis.delete = False; sc.y_axis.delete = False
sc.height = 9; sc.width = 22
sc.x_axis.tickLblPos = "low"; sc.y_axis.tickLblPos = "low"; sc.y_axis.number_format = "0%"
ss.add_chart(sc, "D22")

# ---------------- Checks ----------------
ck = wb.create_sheet("Checks")
ck["A1"] = "Checks"; ck["A1"].font = Font(bold=True, size=12)
checks = [
    ("Price and yield rows equal", f"=COUNT(Inputs!B{FIRST}:B{LAST})=COUNT(Inputs!C{FIRST}:C{LAST})"),
    ("No blank input cells", f"=COUNTBLANK(Inputs!A{FIRST}:C{LAST})=0"),
    ("Dates strictly increasing", f"=SUMPRODUCT(--(Inputs!A{FIRST+1}:A{LAST}<=Inputs!A{FIRST}:A{LAST-1}))=0"),
    ("Returns count = rows - 1", f"=COUNT(Calc!D{RET0}:D{LAST})=COUNT(Calc!A{FIRST}:A{LAST})-1"),
    ("Rolling windows = returns - 11", f"=COUNT(Calc!F{FIRST}:F{LAST})=COUNT(Calc!D{RET0}:D{LAST})-11"),
    ("Correlations within [-1,1]", f"=AND(MIN(Calc!F{FIRST}:F{LAST})>=-1,MAX(Calc!F{FIRST}:F{LAST})<=1,ABS(FullPeriodCorrel)<=1)"),
]
for k, (lab, f) in enumerate(checks):
    ck.cell(row=3 + k, column=1, value=lab); ck.cell(row=3 + k, column=2, value=f)
ck.cell(row=3 + len(checks), column=1, value="ALL CHECKS PASS").font = BOLD
ck.cell(row=3 + len(checks), column=2, value=f"=AND(B3:B{2+len(checks)})").font = BOLD
ck.column_dimensions["A"].width = 34

wb.move_sheet("Summary", offset=-2)  # order: Inputs? keep Summary first
wb._sheets = [wb["Summary"], wb["Inputs"], wb["Calc"], wb["Checks"]]
wb.active = 0
wb.calculation.fullCalcOnLoad = True
wb.save(f"{RUN}/out/MSFT_vs_10Y_correlation.xlsx")

# python cross-check
import statistics as st
P = [r[1] for r in rows]; Y = [r[2] for r in rows]
R = [P[i]/P[i-1]-1 for i in range(1, N)]; D = [Y[i]-Y[i-1] for i in range(1, N)]
def corr(a, b):
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    return num / (sum((x-ma)**2 for x in a)**.5 * sum((y-mb)**2 for y in b)**.5)
print("full", corr(R, D)); print("latest roll", corr(R[-12:], D[-12:]))
roll = [corr(R[i-11:i+1], D[i-11:i+1]) for i in range(11, len(R))]
print("nroll", len(roll), "min", min(roll), "max", max(roll))
