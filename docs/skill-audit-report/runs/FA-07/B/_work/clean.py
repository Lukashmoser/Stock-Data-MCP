import csv, json, re, sys
from datetime import datetime
D='/home/claude/results/2026-10-13/runs/FA-07/B/'
ref=json.load(open(D+'_work/ref.json'))
rows=list(csv.DictReader(open(D+'quarterly_export.csv',newline='',encoding='utf-8')))
def pdate(s):
    s=s.strip()
    for f,lab in (('%Y-%m-%d','ISO'),('%m/%d/%Y','MM/DD/YYYY'),('%d-%b-%y','DD-Mon-YY')):
        try: return datetime.strptime(s,f).date().isoformat(),lab
        except ValueError: pass
    raise ValueError(s)
out=[];log=[]
stats=dict(ticker=0,date=0,t2n=0)
fmt_counts={}
notes_types={'text':0,'numeric':0,'blank':0}
for i,r in enumerate(rows, start=2):
    rid=i
    t=r['ticker']; tc=t.strip().upper()
    if tc!=t: stats['ticker']+=1; log.append((rid,'ticker','standardize ticker (trim/upper)',repr(t),tc))
    d,lab=pdate(r['period_end']); fmt_counts[lab]=fmt_counts.get(lab,0)+1
    if lab!='ISO': stats['date']+=1; log.append((rid,'period_end',f'date {lab} -> YYYY-MM-DD',r['period_end'],d))
    v=r['value']; vs=v.strip()
    if re.fullmatch(r'-?\d+(\.\d+)?',vs): num=float(vs)
    else:
        num=float(vs.replace('$','').replace(',',''))
        stats['t2n']+=1; log.append((rid,'value','text-to-number (strip $ and thousands commas)',v,f'{num:g}'))
    n=r['notes'].strip()
    if n=='': notes_types['blank']+=1
    elif re.fullmatch(r'-?\d+(\.\d+)?',n): notes_types['numeric']+=1
    else: notes_types['text']+=1
    out.append(dict(src_row=rid,ticker=tc,period_end=d,fiscal_label=r['fiscal_label'].strip(),metric=r['metric'].strip(),value_raw=num,notes=n))
json.dump(dict(out=out,log=log,stats=stats,fmt=fmt_counts,notes=notes_types),open(D+'_work/stage1.json','w'),indent=1)
print(stats,fmt_counts,notes_types,len(out))
# checks
for o in out:
    R=ref[o['ticker']]; 
    if o['period_end'] not in R['period_end']: print('period not in ref',o)
    k=R['period_end'].index(o['period_end']); rv=R[o['metric']][k]
    if abs(o['value_raw']-rv)>0.5: print(o['src_row'],o['ticker'],o['fiscal_label'],o['metric'],o['value_raw'],'ref',rv, 'ratio',round(o['value_raw']/rv,4))
