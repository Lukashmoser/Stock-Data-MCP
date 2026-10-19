import json
# All USD millions
d = {}
# META
meta = dict(FY25=200966, H1_25=89830, H1_26=117111, FY24=164501, H1_24=75526,
            cogs=(36175, 16063, 21549), rnd=(57372, 25092, 39354), ms=(11991, 5735, 6339), ga=(12152, 4943, 8222),
            ad=(196175, 87955, 114387))
def ttm(t): return t[0] - t[1] + t[2]
m_ttm = meta['FY25'] - meta['H1_25'] + meta['H1_26']
m_prior = meta['FY24'] - meta['H1_24'] + meta['H1_25']
d['META'] = dict(ttm_rev=m_ttm, prior=m_prior, growth=(m_ttm/m_prior-1)*100,
                 gm=(1-ttm(meta['cogs'])/m_ttm)*100, rnd=ttm(meta['rnd'])/m_ttm*100,
                 sm=ttm(meta['ms'])/m_ttm*100, sga=(ttm(meta['ms'])+ttm(meta['ga']))/m_ttm*100,
                 ad_ttm=ttm(meta['ad']), q2_growth=(60801/47516-1)*100,
                 fy25_growth=(200966/164501-1)*100,
                 mcap=751.66*(2205.128509+342.377716))
# RDDT
r = dict(FY25=2202.5, H1_25=892.0, H1_26=1468.3, FY24=1300.2, H1_24=243.0+281.2,
         cogs=(194.2, 83.0, 126.6), rnd=(783.1, 387.9, 438.5), sm=(503.9, 211.3, 347.4), ga=(279.3, 138.2, 141.2))
r_ttm = r['FY25'] - r['H1_25'] + r['H1_26']
r_prior = r['FY24'] - r['H1_24'] + r['H1_25']
d['RDDT'] = dict(ttm_rev=r_ttm, prior=r_prior, growth=(r_ttm/r_prior-1)*100,
                 gm=(1-ttm(r['cogs'])/r_ttm)*100, rnd=ttm(r['rnd'])/r_ttm*100,
                 sm=ttm(r['sm'])/r_ttm*100, sga=(ttm(r['sm'])+ttm(r['ga']))/r_ttm*100,
                 q2_growth=(804.9/499.6-1)*100, fy25_growth=(2202.5/1300.2-1)*100, mcap=30770)
# Alphabet Google advertising
g = [74180, 82284, 158882]; gp = [65850, 72461, 138225]
d['GOOGL_ads'] = dict(ttm=sum(g), prior=sum(gp), growth=(sum(g)/sum(gp)-1)*100, q2_growth=(81629/71340-1)*100,
                      search_q2_growth=(63271/54190-1)*100, yt_q2_growth=(11055/9796-1)*100, net_q2_growth=(7303/7354-1)*100)
# Amazon advertising services
a = [17703, 21300, 17200, 19800]; ap = [14331, 17288, 13921, 15694]
d['AMZN_ads'] = dict(ttm=sum(a), prior=sum(ap), growth=(sum(a)/sum(ap)-1)*100, q2_growth=(19800/15694-1)*100)
# ByteDance (Sacra estimate)
d['BD'] = dict(rev25=186000, rev24=155000, growth=(186000/155000-1)*100, val=550000, ad_share=60)
# Share of digital ad TTM among the five (ad revenue only; BD ad ~60% of 2025 rev)
ads = {'Alphabet': sum(g), 'Meta': ttm(meta['ad']), 'ByteDance (est.)': 186000*0.60, 'Amazon': sum(a), 'Reddit': r_ttm}
d['ads_pool'] = ads
for k, v in d.items():
    print(k, json.dumps({kk: (round(vv, 1) if isinstance(vv, float) else vv) for kk, vv in v.items()}))
json.dump(d, open('/home/claude/results/2026-10-13/runs/FA-02/A/_work/calc.json', 'w'), indent=1)
