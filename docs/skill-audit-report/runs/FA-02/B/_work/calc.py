m_rev=[40589,48385,42314,47516,51242,59893,56311,60801]
m_cogs=[9206,10906,10218,11330]; m_rd=[15144,17135,17699,21656]
ttm=sum(m_rev[4:]); prior=sum(m_rev[:4])
ms=11991+6339-5735; ga=12152+8222-4943
ad=196175+114387-87955
adprior=160633-0  # placeholder
print("META ttm",ttm,"g",round((ttm/prior-1)*100,1),"GM",round((1-sum(m_cogs)/ttm)*100,1),"RD",round(sum(m_rd)/ttm*100,1),"MS",ms,round(ms/ttm*100,1),"SGA",ms+ga,round((ms+ga)/ttm*100,1),"ad ttm",ad, "ad share",round(ad/ttm*100,1))
opi=[20535,24745,22872,18775]; print("META op margin",round(sum(opi)/ttm*100,1))
r_rev=[348.35,427.71,392.36,499.63,584.91,725.61,663.41,804.9]
rt=sum(r_rev[4:]); rp=sum(r_rev[:4])
rc=52.51+58.72+56.27+70.31; rrd=196.38+198.88+207.25+231.28
rsm=503.9+347.369-211.304; rga=279.3+141.222-138.2
print("RDDT ttm",round(rt,1),"g",round((rt/rp-1)*100,1),"GM",round((1-rc/rt)*100,1),"RD",round(rrd/rt*100,1),"SM",round(rsm,1),round(rsm/rt*100,1),"SGA",round((rsm+rga)/rt*100,1))
ropi=[138.54,231.83,182.91,231.72]; print("RDDT op margin",round(sum(ropi)/rt*100,1))
g=[74180,82284,158882-81629,81629]; gp=[65850,72461,138225-71340,71340]
print("GOOG ad ttm",sum(g),"prior",sum(gp),"g",round((sum(g)/sum(gp)-1)*100,1))
a=68630+17240+19800-13920-15700; ap=56220-11824-12771+13920+15700
print("AMZN ad ttm",a,"prior",ap,"g",round((a/ap-1)*100,1))
print("BD g",round((186/155-1)*100,1))
print("Q2 yoy META",round((60801/47516-1)*100,1),"RDDT",round((804.9/499.63-1)*100,1),"GOOG ad",round((81629/71340-1)*100,1),"AMZN",round((19.8/15.7-1)*100,1))
print("RDDT ad Q2 yoy",round((761.625/464.785-1)*100,1))
print("META P/S",round(1942473/ttm,1),"RDDT P/S",round(29877/rt,1),"BD P/S 480/186",round(480/186,1), "330/186", round(330/186,1))
