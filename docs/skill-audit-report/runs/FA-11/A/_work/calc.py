import json, datetime as dt
from prices import *
def parse(s): return {l.split()[0]:(float(l.split()[1]),float(l.split()[2])) for l in s.strip().splitlines()}
def merge(api,page,ov):
    a,p=parse(api),parse(page); k=p[ov][1]/a[ov][1]
    out={d:v[1]*k for d,v in a.items()}; out.update({d:v[1] for d,v in p.items()}); return out,k
series={}
for t,(api,page,ov) in {"MSFT":(MSFT_API,MSFT_PAGE,"2026-09-22"),"QQQ":(QQQ_API,QQQ_PAGE,"2026-09-18"),"XLK":(XLK_API,XLK_PAGE,"2026-09-18")}.items():
    s,k=merge(api,page,ov); print(t,"k",round(k,6))
    series[t]=s
start=dt.date(2025,10,16); dates=[start+dt.timedelta(7*i) for i in range(53)]
res={"dates":[],"MSFT":[],"QQQ":[],"XLK":[],"used":{}}
for d in dates:
    res["dates"].append(d.isoformat())
    for t,s in series.items():
        ks=sorted(x for x in s if x<=d.isoformat() and x> (d-dt.timedelta(5)).isoformat())
        assert ks, (t,d); res[t].append(s[ks[-1]]); res["used"].setdefault(t,[]).append(ks[-1])
for t in ["MSFT","QQQ","XLK"]:
    b=res[t][0]; res[t+"_idx"]=[v/b*100 for v in res[t]]
    print(t,"points",len(res[t]),"TR %.1f%%"%((res[t][-1]/b-1)*100), "min", min(res[t+"_idx"]))
    # sanity: price return
# alt: from 2025-10-15
for t in series: print(t,"TR from 10-15: %.1f%%"%((series[t]["2026-10-15"]/series[t]["2025-10-15"]-1)*100))
json.dump(res,open('weekly.json','w'),indent=1)
