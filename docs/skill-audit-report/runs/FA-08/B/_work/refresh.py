import sys, os, re, shutil, zipfile, openpyxl
from xml.sax.saxutils import escape

SRC = sys.argv[1]   # unzipped dir (copied)
OUT = sys.argv[2]   # output pptx

# exact <a:t> text replacements per part (old -> new); each must match exactly the expected count
R = {
 'ppt/slides/slide1.xml': [
  ('Fiscal year ended June 30, 2025', 'Fiscal year ended June 30, 2026'),
  ('Data as of 2025-06-30', 'Data as of 2026-10-15'),
 ],
 'ppt/slides/slide2.xml': [
  ('Key stats: FY2025 at a glance', 'Key stats: FY2026 at a glance'),
  ('$497.41', '$539.44'),
  ('Close, 2025-06-30', 'Close, 2026-10-15'),
  ('$3.70T', '$4.01T'),
  ('7,434M shares outstanding', '7,427M shares outstanding'),
  ('$281.7B', '$331.8B'),
  ('FY2025 revenue', 'FY2026 revenue'),
  ('Fiscal year to 6/30/25', 'Fiscal year to 6/30/26'),
  ('14.9%', '17.8%'),
  ('vs. FY2024 $245.1B', 'vs. FY2025 $281.7B'),
  ('45.6%', '46.8%'),
  ('Op. income $128.5B', 'Op. income $155.2B'),
  ('$71.6B', '$67.0B'),
  ('$13.64', '$17.95'),
  ('FY2025 GAAP', 'FY2026 GAAP'),
 ],
 'ppt/slides/slide3.xml': [
  ('Revenue and operating income, FY2021–FY2025', 'Revenue and operating income, FY2021–FY2026'),
  ('13.8%', '14.6%'),
  ('Revenue CAGR, FY2021–FY2025', 'Revenue CAGR, FY2021–FY2026'),
  ('16.4%', '17.3%'),
  ('Operating income CAGR, FY2021–FY2025', 'Operating income CAGR, FY2021–FY2026'),
  ('45.6%', '46.8%'),
  ('FY2025 operating margin (FY2021: 41.6%)', 'FY2026 operating margin (FY2021: 41.6%)'),
 ],
 'ppt/slides/slide4.xml': [
  ('FY2025: double-digit growth amid a capex surge', 'FY2026: double-digit growth amid a capex surge'),
  ('14.9%', '17.8%'),
  ('Revenue rose 14.9% YoY to $281.7B in FY2025, up from $245.1B in FY2024.',
   'Revenue rose 17.8% YoY to $331.8B in FY2026, up from $281.7B in FY2025.'),
  ('25.4%', '20.2%'),
  ('Free cash flow of $71.6B equals a 25.4% FCF margin, down from 30.2% in FY2024 as investment stepped up.',
   'Free cash flow of $67.0B equals a 20.2% FCF margin, down from 25.4% in FY2025 as investment stepped up.'),
  ('$64.6B', '$115.9B'),
  ('Capital expenditures climbed 45.1% to $64.6B (22.9% of revenue), driven by datacenter build-out for cloud and AI.',
   'Capital expenditures climbed 79.6% to $115.9B (34.9% of revenue), driven by datacenter build-out for cloud and AI.'),
 ],
 'ppt/slides/slide5.xml': [
  ('Valuation at FY2025 year-end', 'Valuation as of 2026-10-15'),
  ('Share price (6/30/25 close)', 'Share price (10/15/26 close)'),
  ('$497.41', '$539.44'),
  ('7,434', '7,427'),
  ('$3,697,746M', '$4,006,421M'),
  ('$43,151M', '$40,294M'),
  ('($94,565M)', '($76,843M)'),
  ('$3,646,332M', '$3,969,872M'),
  ('FY2025 revenue', 'FY2026 revenue'),
  ('$281,724M', '$331,839M'),
  ('FY2025 free cash flow', 'FY2026 free cash flow'),
  ('$71,611M', '$66,987M'),
  ('FY2025 diluted EPS', 'FY2026 diluted EPS'),
  ('$13.64', '$17.95'),
  ('36.5x', '30.1x'),
  ('$497.41 ÷ $13.64', '$539.44 ÷ $17.95'),
  ('12.9x', '12.0x'),
  ('$3,646,332M ÷ $281,724M', '$3,969,872M ÷ $331,839M'),
  ('50.9x', '59.3x'),
  ('$3,646,332M ÷ $71,611M', '$3,969,872M ÷ $66,987M'),
 ],
 'ppt/slides/slide6.xml': [
  ('Financial statements: Microsoft Form 10-K for the fiscal year ended June 30, 2025 (SEC XBRL data); FY2021–FY2024 from prior 10-K filings. All periods end June 30.',
   'Financial statements: Microsoft Form 10-K for the fiscal year ended June 30, 2026 (SEC XBRL data); FY2021–FY2025 from prior 10-K filings. All periods end June 30.'),
  ('Share price: Nasdaq closing price on June 30, 2025 ($497.41), unadjusted (Yahoo Finance daily history).',
   'Share price: Nasdaq closing price on October 15, 2026 ($539.44), unadjusted (Yahoo Finance daily history).'),
  ('Market cap = share price × 7,434M common shares outstanding as reported in the FY2025 10-K balance sheet data.',
   'Market cap = share price × 7,427M common shares outstanding as reported in the FY2026 10-K balance sheet data.'),
  ('Enterprise value = market cap + total debt (current portion $2,999M + long-term $40,152M) − cash &amp; equivalents ($30,242M) − short-term investments ($64,323M); leases excluded.',
   'Enterprise value = market cap + total debt (current portion $9,227M + long-term $31,067M) − cash &amp; equivalents ($20,935M) − short-term investments ($55,908M); leases excluded.'),
  ('Free cash flow = cash from operations ($136,162M) − additions to property and equipment ($64,551M). Finance-lease additions not deducted.',
   'Free cash flow = cash from operations ($182,935M) − additions to property and equipment ($115,948M). Finance-lease additions not deducted.'),
  ('Data compiled October 13, 2026; figures reflect the June 30, 2025 point in time and do not include later events.',
   'Data compiled October 15, 2026; financials reflect the June 30, 2026 fiscal year-end; share price is as of October 15, 2026.'),
 ],
 'ppt/slideLayouts/slideLayout3.xml': [
  ('Microsoft (MSFT) Company Snapshot  |  FY2025', 'Microsoft (MSFT) Company Snapshot  |  FY2026'),
 ],
}

changed = 0
for part, pairs in R.items():
    p = os.path.join(SRC, part)
    s = open(p, encoding='utf-8').read()
    for old, new in pairs:
        pat = '<a:t>' + old + '</a:t>'
        n = s.count(pat)
        if n < 1:
            sys.exit(f'MISS {part}: {old!r}')
        s = s.replace(pat, '<a:t>' + new + '</a:t>')
        changed += n
    open(p, 'w', encoding='utf-8').write(s)

# chart: add FY2026 point to both series, extend refs, raise axis max
cp = os.path.join(SRC, 'ppt/charts/chart1.xml')
c = open(cp, encoding='utf-8').read()
c = c.replace('$A$2:$A$6', '$A$2:$A$7').replace('$B$2:$B$6', '$B$2:$B$7').replace('$C$2:$C$6', '$C$2:$C$7')
c = c.replace('<c:ptCount val="5"/>', '<c:ptCount val="6"/>')
c = c.replace('<c:pt idx="4"><c:v>FY2025</c:v></c:pt>', '<c:pt idx="4"><c:v>FY2025</c:v></c:pt><c:pt idx="5"><c:v>FY2026</c:v></c:pt>')
assert c.count('<c:v>FY2026</c:v>') == 2
c = c.replace('<c:pt idx="4"><c:v>281.7</c:v></c:pt>', '<c:pt idx="4"><c:v>281.7</c:v></c:pt><c:pt idx="5"><c:v>331.8</c:v></c:pt>')
c = c.replace('<c:pt idx="4"><c:v>128.5</c:v></c:pt>', '<c:pt idx="4"><c:v>128.5</c:v></c:pt><c:pt idx="5"><c:v>155.2</c:v></c:pt>')
assert '331.8' in c and '155.2' in c
c = c.replace('<c:max val="320"/>', '<c:max val="400"/>')
assert '<c:max val="400"/>' in c
open(cp, 'w', encoding='utf-8').write(c)

xp = os.path.join(SRC, 'ppt/embeddings/Microsoft_Excel_Worksheet1.xlsx')
wb = openpyxl.load_workbook(xp)
ws = wb['Sheet1']
ws['A7'] = 'FY2026'; ws['B7'] = 331.8; ws['C7'] = 155.2
wb.save(xp)

# repack with [Content_Types].xml first
if os.path.exists(OUT): os.remove(OUT)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(SRC, '[Content_Types].xml'), '[Content_Types].xml')
    for root, _, files in os.walk(SRC):
        for f in files:
            full = os.path.join(root, f); arc = os.path.relpath(full, SRC)
            if arc != '[Content_Types].xml':
                z.write(full, arc)
print('text instances changed:', changed)
