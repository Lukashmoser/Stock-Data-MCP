import json, math
from datetime import date, timedelta
as_of = date(2026,10,12)  # Monday
def series(start, drift, vol, days=400):
    out=[]; p=start; d=as_of-timedelta(days=days)
    i=0
    while d<=as_of-timedelta(days=3):  # last bar Friday 2026-10-09
        if d.weekday()<5:
            p*=1+drift+vol*math.sin(i/7.0); i+=1
            out.append((d,round(p,2)))
        d+=timedelta(days=1)
    return out
aapl=series(180,0.0008,0.01)
msft=series(420,-0.0003,0.008)
nvda=series(120,0.0015,0.015)
fix={"as_of":as_of.isoformat(),"tickers":{
 "AAPL":{"quote":{"symbol":"AAPL","price":aapl[-1][1],"timestamp":"2026-10-09T20:00:00Z"},
         "history":{"data":[{"date":d.isoformat(),"open":c,"high":round(c*1.01,2),"low":round(c*0.99,2),"close":c} for d,c in aapl]},
         "filings":[{"form":"8-K","filingDate":"2026-10-07"},{"form":"10-Q","filingDate":"2026-08-01"}]},
 "MSFT":{"quote":{},  # empty quote -> falls back to last close
         "history":[{"Date":d.strftime("%m/%d/%Y"),"Close":c} for d,c in msft],
         "filings":{"results":[{"formType":"10-K","filed":"2026-07-30"},{"formType":"8-K","filed":"2026-09-20"}]}},
 "NVDA":{"history":{"date":[int((d-date(1970,1,1)).total_seconds()*1000) for d,c in nvda],"close":[c for d,c in nvda]},
         "filings":{"form":["4","8-K/A","10-Q"],"filingDate":["2026-10-10","2026-10-05","2026-08-27"]}},
 "BADX":{"error":"get_quote: unknown symbol BADX"},
 "NEWCO":{"history":[{"date":(as_of-timedelta(days=k)).isoformat(),"close":10+k*0.1} for k in range(3,40)],"filings":"garbage"}
}}
json.dump(fix,open("watchlist_input.json","w"),indent=1)
