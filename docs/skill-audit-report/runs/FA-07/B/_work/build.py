import csv, json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
D='/home/claude/results/2026-10-13/runs/FA-07/B/'
S=json.load(open(D+'_work/stage1.json')); ref=json.load(open(D+'_work/ref.json'))
out=S['out']; log=[list(x) for x in S['log']]
TOOL='stock-data get_financials (SEC XBRL)'
FIL={('GOOGL','2025-03-31'):'Alphabet 10-Q filed 2025-04-25',
     ('AMZN','2025-09-30'):'Amazon 10-Q filed 2025-10-31',
     ('META','2024-12-31'):'Meta 10-K filed 2025-01-30 (Q4 = FY less 9M)',
     ('META','2025-09-30'):'Meta 10-Q filed 2025-10-30'}
UNUSUAL={('GOOGL','2026-03-31','net_income'):'NI 57% of revenue; verified (pretax 77,412 incl. large non-operating gains)',
         ('GOOGL','2026-06-30','net_income'):'NI 94% of revenue; verified (pretax 138,753 incl. large non-operating gains)',
         ('AMZN','2026-06-30','net_income'):'NI ~2x prior quarter; verified (pretax 80,857 incl. non-operating gains)',
         ('META','2025-09-30','net_income'):'NI low after unit fix; verified (income tax 18,954 one-time charge)'}
unit_rows=[];wrong_rows=[];
for o in out:
    R=ref[o['ticker']]; k=R['period_end'].index(o['period_end']); rv=R[o['metric']][k]
    v=o['value_raw']; o['value_usd_m']=v; o['flag']=''; o['flag_detail']=''; o['source']=''
    if abs(v/1000-rv)<=0.5 and v>=1e6:
        o['value_usd_m']=v/1000; o['flag']='UNIT_ERROR_FIXED'
        o['flag_detail']=f'Exported in USD thousands ({v:,.0f}); divided by 1,000'
        o['source']=f"{FIL[(o['ticker'],o['period_end'])]}; {TOOL}"
        unit_rows.append(o); log.append([o['src_row'],'value','unit error: USD thousands -> USD millions',f'{v:,.0f}',f'{v/1000:,.0f}'])
    elif abs(v-rv)>0.5:
        o['value_usd_m']=float(rv); o['flag']='WRONG_VALUE_CORRECTED'
        o['flag_detail']=f'Exported {v:,.0f} vs reported {rv:,} (diff {v-rv:+,.0f}, {100*(v-rv)/rv:+.1f}%)'
        o['source']=f"{FIL[(o['ticker'],o['period_end'])]}; {TOOL}"
        wrong_rows.append(o); log.append([o['src_row'],'value','value does not match SEC filing; replaced with reported figure',f'{v:,.0f}',f'{rv:,}'])
    else:
        o['source']=TOOL+' (matches)'
    key=(o['ticker'],o['period_end'],o['metric'])
    if key in UNUSUAL and not o['flag']:
        o['flag']='OUTLIER_VERIFIED'; o['flag_detail']=UNUSUAL[key]
# dedup by key; keep first occurrence whose value matches reference
seen={};clean=[];dups=[]
for o in out:
    key=(o['ticker'],o['period_end'],o['metric'])
    if key in seen:
        f=seen[key]; exact = f['value_raw']==o['value_raw']
        kind='exact duplicate (after normalization)' if exact else f"near-duplicate (value {o['value_raw']:g} vs kept {f['value_raw']:g}; kept value matches filing)"
        dups.append((o,f,kind)); log.append([o['src_row'],'row','removed: '+kind+f" of source row {f['src_row']}",'','(deleted)'])
        continue
    seen[key]=o; clean.append(o)
# fiscal label check
for o in clean:
    if o['metric']=='revenue': pass
clean.sort(key=lambda o:(o['ticker'],o['period_end'],['revenue','operating_income','net_income'].index(o['metric'])))
cols=['ticker','period_end','fiscal_label','metric','value_usd_m','flag','flag_detail','source','notes_original','source_row']
with open(D+'quarterly_export_clean.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(cols)
    for o in clean: w.writerow([o['ticker'],o['period_end'],o['fiscal_label'],o['metric'],f"{o['value_usd_m']:.0f}",o['flag'],o['flag_detail'],o['source'],o['notes'],o['src_row']])
log.sort(key=lambda x:(x[0],x[1]))
with open(D+'change_log.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['source_row','column','change','before','after']); w.writerows(log)
# workbook
wb=Workbook(); H=Font(bold=True,color='FFFFFF'); HF=PatternFill('solid',fgColor='1F3864')
def hdr(ws,row):
    ws.append(row)
    for c in ws[ws.max_row]: c.font=H; c.fill=HF
def fit(ws):
    for i,col in enumerate(ws.columns,1):
        ws.column_dimensions[get_column_letter(i)].width=min(60,max(10,max(len(str(c.value or '')) for c in col)+2))
    ws.freeze_panes='A2'
ws=wb.active; ws.title='Cleaned'; hdr(ws,cols)
FL={'UNIT_ERROR_FIXED':'FCE4D6','WRONG_VALUE_CORRECTED':'F8CBAD','OUTLIER_VERIFIED':'FFF2CC'}
for o in clean:
    ws.append([o['ticker'],o['period_end'],o['fiscal_label'],o['metric'],round(o['value_usd_m']),o['flag'],o['flag_detail'],o['source'],o['notes'],o['src_row']])
    ws.cell(ws.max_row,5).number_format='#,##0'
    if o['flag']:
        for c in ws[ws.max_row]: c.fill=PatternFill('solid',fgColor=FL[o['flag']])
fit(ws)
# Raw with audit formulas
raw=list(csv.reader(open(D+'quarterly_export.csv',newline='')))
ws=wb.create_sheet('Raw_with_helpers'); hdr(ws,raw[0]+['ticker_clean (formula)','value_num (formula)','notes_is_number (formula)'])
for i,r in enumerate(raw[1:],start=2):
    ws.append(r+[f'=UPPER(TRIM(A{i}))',f'=VALUE(SUBSTITUTE(SUBSTITUTE(E{i},"$",""),",",""))',f'=ISNUMBER(VALUE(F{i}))'])
    ws.cell(i,8).number_format='#,##0.0'
fit(ws)
ws=wb.create_sheet('Change_Log'); hdr(ws,['source_row','column','change','before','after'])
for l in log: ws.append(l)
fit(ws)
ws=wb.create_sheet('Value_Flags'); hdr(ws,['source_row','ticker','fiscal_label','period_end','metric','exported','corrected_usd_m','flag','detail','source'])
for o in clean:
    if o['flag']: ws.append([o['src_row'],o['ticker'],o['fiscal_label'],o['period_end'],o['metric'],o['value_raw'],round(o['value_usd_m']),o['flag'],o['flag_detail'],o['source']])
fit(ws)
ws=wb.create_sheet('Column_Profile'); hdr(ws,['column','dominant type','issues found','count','fix applied'])
st=S['stats'];fm=S['fmt'];nt=S['notes']
for r in [['ticker','text','leading/trailing spaces, mixed case (googl/GOOGL/Amzn/Meta/Msft)',st['ticker'],'TRIM + UPPER'],
 ['period_end','date (stored as text)',f"3 formats: ISO {fm['ISO']}, MM/DD/YYYY {fm['MM/DD/YYYY']}, DD-Mon-YY {fm['DD-Mon-YY']}",st['date'],'parsed to YYYY-MM-DD'],
 ['fiscal_label','text','none; MSFT labels use its July-June fiscal year',0,'kept as-is'],
 ['metric','text','none',0,'kept'],
 ['value','number',f"{st['t2n']} text numbers with $ and commas; 6 values in USD thousands; 2 values not matching filings; 1 decimal near-duplicate",st['t2n'],'converted, unit-fixed, corrected'],
 ['notes','MIXED TYPE',f"text {nt['text']}, numeric {nt['numeric']}, blank {nt['blank']} (values like 0.5, 12.5, 'FY', '10-K' have no consistent meaning)",nt['numeric'],'flagged only; kept as text in notes_original']]:
    ws.append(r)
fit(ws)
wb.save(D+'quarterly_export_clean.xlsx')
print(len(out),len(clean),[(d[0]['src_row'],d[1]['src_row'],d[2]) for d in dups])
print('unit',[(o['src_row'],o['value_usd_m']) for o in unit_rows]); print('wrong',[(o['src_row'],o['value_raw'],o['value_usd_m']) for o in wrong_rows])
print(len(log))
