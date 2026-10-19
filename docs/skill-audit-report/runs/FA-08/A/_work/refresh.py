import sys, copy
from pptx import Presentation
from pptx.chart.data import CategoryChartData
src, dst = sys.argv[1], sys.argv[2]
p = Presentation(src)
S = list(p.slides)
# (slide_no, shape_name or None for any) -> list of (old, new)
R = {
1: [("Fiscal year ended June 30, 2025","Fiscal year ended June 30, 2026"),
    ("Data as of 2025-06-30","Data as of 2026-10-15")],
2: [("FY2025 at a glance","FY2026 at a glance"),("$497.41","$539.44"),("Close, 2025-06-30","Close, 2026-10-15"),
    ("$3.70T","$4.01T"),("7,434M shares","7,427M shares"),("$281.7B","$331.8B"),("FY2025 revenue","FY2026 revenue"),
    ("6/30/25","6/30/26"),("14.9%","17.8%"),("vs. FY2024 $245.1B","vs. FY2025 $281.7B"),("45.6%","46.8%"),
    ("Op. income $128.5B","Op. income $155.2B"),("$71.6B","$67.0B"),("$13.64","$17.95"),("FY2025 GAAP","FY2026 GAAP")],
3: [("FY2021–FY2025","FY2021–FY2026"),("13.8%","14.6%"),("16.4%","17.3%"),("45.6%","46.8%"),("FY2025 operating margin","FY2026 operating margin")],
4: [("FY2025: double","FY2026: double"),("14.9%","17.8%"),
    ("to $281.7B in FY2025, up from $245.1B in FY2024","to $331.8B in FY2026, up from $281.7B in FY2025"),
    ("$71.6B","$67.0B"),("25.4% FCF margin, down from 30.2% in FY2024","20.2% FCF margin, down from 25.4% in FY2025"),
    ("25.4%","20.2%"),("climbed 45.1% to $64.6B (22.9% of revenue)","climbed 79.6% to $115.9B (34.9% of revenue)"),("$64.6B","$115.9B")],
5: [("Valuation at FY2025 year-end","Valuation at current price, 2026-10-15"),
    ("Share price (6/30/25 close)","Share price (10/15/26 close)"),("$497.41","$539.44"),("7,434","7,427"),
    ("$3,697,746M","$4,006,421M"),("$43,151M","$40,294M"),("($94,565M)","($76,843M)"),("$3,646,332M","$3,969,872M"),
    ("FY2025 revenue","FY2026 revenue"),("$281,724M","$331,839M"),("FY2025 free cash flow","FY2026 free cash flow"),
    ("$71,611M","$66,987M"),("FY2025 diluted EPS","FY2026 diluted EPS"),("$13.64","$17.95"),
    ("36.5x","30.1x"),("12.9x","12.0x"),("50.9x","59.3x")],
6: [("fiscal year ended June 30, 2025 (SEC XBRL data); FY2021–FY2024 from prior 10-K filings",
     "fiscal year ended June 30, 2026, as presented in the FY2026 Q4 earnings release (Form 8-K Exhibit 99.1, 2026-07-29); FY2021–FY2025 from prior 10-K filings"),
    ("Nasdaq closing price on June 30, 2025 ($497.41), unadjusted (Yahoo Finance daily history)",
     "Nasdaq closing price on October 15, 2026 ($539.44), unadjusted (stockanalysis.com daily history; cross-checked with Investing.com)"),
    ("7,434M common shares outstanding as reported in the FY2025 10-K","7,427M common shares outstanding at June 30, 2026 as reported in the FY2026"),
    ("(current portion $2,999M + long-term $40,152M) − cash & equivalents ($30,242M) − short-term investments ($64,323M)",
     "(current portion $9,227M + long-term $31,067M) − cash & equivalents ($20,935M) − short-term investments ($55,908M)"),
    ("($136,162M) − additions to property and equipment ($64,551M)","($182,935M) − additions to property and equipment ($115,948M)"),
    ("Data compiled October 13, 2026; figures reflect the June 30, 2025 point in time and do not include later events.",
     "Data compiled October 15, 2026; financial figures reflect the fiscal year ended June 30, 2026; share price, market cap and multiples use the October 15, 2026 close."),
   ],
}
count = 0; log=[]
def runs_of(shape):
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            for r in para.runs: yield r
    if shape.has_table:
        for row in shape.table.rows:
            for c in row.cells:
                for para in c.text_frame.paragraphs:
                    for r in para.runs: yield r
for sn, pairs in R.items():
    used = {o:0 for o,_ in pairs}
    for sh in S[sn-1].shapes:
        for r in runs_of(sh):
            t = r.text
            import re
            mp=dict(pairs); orig=t
            pat=re.compile("|".join(re.escape(o) for o in sorted(mp,key=len,reverse=True)))
            def f(m):
                used[m.group(0)]+=1; log.append(f"S{sn} [{sh.name}] '{m.group(0)}' -> '{mp[m.group(0)]}'")
                return mp[m.group(0)]
            t=pat.sub(f,orig)
            if t != r.text: r.text = t
    for o,k in used.items():
        if k==0: print("UNUSED", sn, o)
# chart
ch = [s for s in S[2].shapes if s.has_chart][0].chart
cd = CategoryChartData(number_format='General')
cd.categories = ['FY2021','FY2022','FY2023','FY2024','FY2025','FY2026']
cd.add_series('Revenue ($B)', [168.1,198.3,211.9,245.1,281.7,331.8])
cd.add_series('Operating income ($B)', [69.9,83.4,88.5,109.4,128.5,155.2])
ch.replace_data(cd)
for lay in p.slide_layouts:
    for sh in lay.shapes:
        if sh.has_text_frame:
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    if r.text=="Microsoft (MSFT) Company Snapshot  |  FY2025":
                        r.text="Microsoft (MSFT) Company Snapshot  |  FY2026"; log.append("Layout footer FY2025 -> FY2026")
p.save(dst)
print("\n".join(log)); print(len(log),"replacement ops")
