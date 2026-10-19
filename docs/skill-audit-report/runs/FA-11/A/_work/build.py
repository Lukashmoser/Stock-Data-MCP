import json, copy
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_TICK_LABEL_POSITION
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

OUT="/home/claude/results/2026-10-13/runs/FA-11/A/MSFT_1Y_Performance_Fundamentals.pptx"
w=json.load(open("weekly.json"))
NAVY=RGBColor(0x1F,0x2A,0x44); BLUE=RGBColor(0x00,0x67,0xB8); GREY=RGBColor(0x8C,0x95,0xA1); TEAL=RGBColor(0x2A,0x9D,0x8F); ORANGE=RGBColor(0xE0,0x7A,0x1F); DARK=RGBColor(0x33,0x33,0x33)
quarters=[("FQ1'25","2024-09-30",65585,30552),("FQ2'25","2024-12-31",69632,31653),("FQ3'25","2025-03-31",70066,32000),("FQ4'25","2025-06-30",76441,34323),
          ("FQ1'26","2025-09-30",77673,37961),("FQ2'26","2025-12-31",81273,38275),("FQ3'26","2026-03-31",82886,38398),("FQ4'26","2026-06-30",90007,40603)]
years=[("FY23",28107,59475,87582),("FY24",44477,74071,118548),("FY25",64551,71611,136162),("FY26",115948,66987,182935)]
tr={t:(w[t][-1]/w[t][0]-1)*100 for t in ["MSFT","QQQ","XLK"]}
start,end=w["dates"][0],w["dates"][-1]

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
blank=prs.slide_layouts[6]

def textbox(slide,x,y,cx,cy,text,size=14,bold=False,color=DARK,align=None):
    tb=slide.shapes.add_textbox(Inches(x),Inches(y),Inches(cx),Inches(cy)); tf=tb.text_frame; tf.word_wrap=True
    lines=text if isinstance(text,list) else [text]
    for i,l in enumerate(lines):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        r=p.add_run(); r.text=l; r.font.size=Pt(size); r.font.bold=bold; r.font.color.rgb=color; r.font.name="Calibri"
        if align: p.alignment=align
        p.space_after=Pt(6)
    return tb
def header(slide,title,sub=None):
    bar=slide.shapes.add_shape(1,0,0,prs.slide_width,Inches(0.12)); bar.fill.solid(); bar.fill.fore_color.rgb=BLUE; bar.line.fill.background()
    textbox(slide,0.5,0.3,12.3,0.8,title,26,True,NAVY)
    if sub: textbox(slide,0.5,0.95,12.3,0.5,sub,14,False,GREY)
def footer(slide,text):
    textbox(slide,0.5,6.85,12.3,0.5,text,9,False,GREY)

# 1 Title
s=prs.slides.add_slide(blank)
bg=s.shapes.add_shape(1,0,0,prs.slide_width,prs.slide_height); bg.fill.solid(); bg.fill.fore_color.rgb=NAVY; bg.line.fill.background()
textbox(s,0.8,2.4,11.7,1.2,"Microsoft: 1-Year Stock Performance and Fundamentals",36,True,RGBColor(255,255,255))
textbox(s,0.8,3.6,11.7,0.6,f"MSFT vs. QQQ vs. XLK, {start} to {end} | Fundamentals through FQ4'26 (quarter ended 2026-06-30)",16,False,RGBColor(0xC8,0xD3,0xE0))
textbox(s,0.8,6.5,11.7,0.5,"USD millions unless noted. Prices as of 2026-10-15 close. Sources: stockanalysis.com price history and financial statements.",11,False,RGBColor(0xC8,0xD3,0xE0))

# 2 Line chart
s=prs.slides.add_slide(blank)
header(s,f"MSFT lagged badly: +{tr['MSFT']:.1f}% total return vs. +{tr['QQQ']:.1f}% QQQ and +{tr['XLK']:.1f}% XLK",
       f"1-year total return, weekly (Thursday closes), indexed to 100 on {start}; dividends reinvested via adjusted closes")
cd=CategoryChartData(); cd.categories=w["dates"]
for t in ["MSFT","QQQ","XLK"]: cd.add_series(t,[round(v,2) for v in w[t+"_idx"]])
gf=s.shapes.add_chart(XL_CHART_TYPE.LINE,Inches(0.5),Inches(1.5),Inches(9.3),Inches(5.3),cd); ch=gf.chart
ch.has_legend=True; ch.legend.position=XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout=False; ch.legend.font.size=Pt(12)
for ser,c,wd in zip(ch.series,[BLUE,GREY,TEAL],[2.75,2,2]):
    ser.format.line.color.rgb=c; ser.format.line.width=Pt(wd); ser.smooth=False; ser.marker.style=None
    ser.marker.format.fill.background() if False else None
    m=ser._element.get_or_add_marker(); m.get_or_add_symbol().set("val","none")
va=ch.value_axis; va.minimum_scale=60; va.maximum_scale=150; va.has_major_gridlines=True; va.major_gridlines.format.line.color.rgb=RGBColor(0xE3,0xE6,0xEA)
va.tick_labels.font.size=Pt(11); va.tick_labels.number_format='0'; va.tick_labels.number_format_is_linked=False
ca=ch.category_axis; ca.tick_labels.font.size=Pt(10); ca.tick_label_position=XL_TICK_LABEL_POSITION.LOW
cax=ca._element
for tag,val in [("c:tickLblSkip","8"),("c:tickMarkSkip","4")]:
    e=etree.SubElement(cax,qn(tag)); e.set("val",val)
msft_min=min(w["MSFT_idx"]); imin=w["MSFT_idx"].index(msft_min)
textbox(s,10.0,1.6,2.9,5,[f"1-yr total return",f"MSFT  +{tr['MSFT']:.1f}%",f"QQQ   +{tr['QQQ']:.1f}%",f"XLK   +{tr['XLK']:.1f}%","",
    f"MSFT trough: {msft_min:.1f} on {w['dates'][imin]} ({msft_min-100:.1f}% from start)",
    "Rebound followed the late-July FQ4'26 report.",f"{len(w['dates'])} weekly points per series."],13,False,DARK)
footer(s,f"Source: stockanalysis.com daily close and dividend-adjusted close, sampled at each Thursday close (prior trading day if holiday). Period {start} to {end}.")

# 3 Combo chart
s=prs.slides.add_slide(blank)
g=(quarters[-1][2]/quarters[3][2]-1)*100
header(s,f"FQ4'26 revenue ${quarters[-1][2]:,}M (+{g:.1f}% YoY); margin steady at 44.9-48.9%",
       "Quarterly revenue (USD millions, bars, left axis) and operating margin (%, line, right axis); fiscal year ends June 30")
cd=CategoryChartData(); cd.categories=[q[0] for q in quarters]
cd.add_series("Revenue (USD M)",[q[2] for q in quarters])
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Inches(0.5),Inches(1.5),Inches(12.3),Inches(5.2),cd); ch=gf.chart
ser=ch.series[0]; ser.format.fill.solid(); ser.format.fill.fore_color.rgb=BLUE
pl=ch.plots[0]; pl.gap_width=60; pl.has_data_labels=True; dl=pl.data_labels; dl.number_format='#,##0'; dl.number_format_is_linked=False; dl.font.size=Pt(11)
from pptx.enum.chart import XL_LABEL_POSITION
dl.position=XL_LABEL_POSITION.INSIDE_END; dl.font.color.rgb=RGBColor(255,255,255)
ch.value_axis.minimum_scale=0; ch.value_axis.maximum_scale=130000; ch.value_axis.tick_labels.number_format='#,##0'; ch.value_axis.tick_labels.number_format_is_linked=False
ch.value_axis.has_major_gridlines=True; ch.value_axis.major_gridlines.format.line.color.rgb=RGBColor(0xE3,0xE6,0xEA)
ch.value_axis.tick_labels.font.size=Pt(11); ch.category_axis.tick_labels.font.size=Pt(11)
ch.has_legend=True; ch.legend.position=XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout=False; ch.legend.font.size=Pt(12)
# inject line chart on secondary axis
C="http://schemas.openxmlformats.org/drawingml/2006/chart"; A="http://schemas.openxmlformats.org/drawingml/2006/main"
cs=ch._chartSpace; plotArea=cs.find(".//{%s}plotArea"%C); bar=plotArea.find("{%s}barChart"%C)
margins=[round(q[3]/q[2]*100,1) for q in quarters]
pts="".join(f'<c:pt idx="{i}"><c:v>{q[0]}</c:v></c:pt>' for i,q in enumerate(quarters))
vals="".join(f'<c:pt idx="{i}"><c:v>{m}</c:v></c:pt>' for i,m in enumerate(margins))
xml=f'''<c:lineChart xmlns:c="{C}" xmlns:a="{A}"><c:grouping val="standard"/><c:varyColors val="0"/>
<c:ser><c:idx val="1"/><c:order val="1"/><c:tx><c:strRef><c:f>Sheet1!$C$1</c:f><c:strCache><c:ptCount val="1"/><c:pt idx="0"><c:v>Operating margin (%)</c:v></c:pt></c:strCache></c:strRef></c:tx>
<c:spPr><a:ln w="34925"><a:solidFill><a:srgbClr val="E07A1F"/></a:solidFill></a:ln></c:spPr>
<c:marker><c:symbol val="circle"/><c:size val="7"/><c:spPr><a:solidFill><a:srgbClr val="E07A1F"/></a:solidFill><a:ln><a:solidFill><a:srgbClr val="E07A1F"/></a:solidFill></a:ln></c:spPr></c:marker>
<c:dLbls><c:numFmt formatCode="0.0&quot;%&quot;" sourceLinked="0"/><c:spPr><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr><c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="1100" b="1"><a:solidFill><a:srgbClr val="E07A1F"/></a:solidFill></a:defRPr></a:pPr><a:endParaRPr lang="en-US"/></a:p></c:txPr><c:dLblPos val="t"/><c:showLegendKey val="0"/><c:showVal val="1"/><c:showCatName val="0"/><c:showSerName val="0"/><c:showPercent val="0"/><c:showBubbleSize val="0"/></c:dLbls>
<c:cat><c:strRef><c:f>Sheet1!$A$2:$A$9</c:f><c:strCache><c:ptCount val="8"/>{pts}</c:strCache></c:strRef></c:cat>
<c:val><c:numRef><c:f>Sheet1!$C$2:$C$9</c:f><c:numCache><c:formatCode>0.0</c:formatCode><c:ptCount val="8"/>{vals}</c:numCache></c:numRef></c:val><c:smooth val="0"/></c:ser>
<c:marker val="1"/><c:axId val="900001"/><c:axId val="900002"/></c:lineChart>'''
line=etree.fromstring(xml); bar.addnext(line)
axes_xml=f'''<root xmlns:c="{C}" xmlns:a="{A}"><c:catAx><c:axId val="900001"/><c:scaling><c:orientation val="minMax"/></c:scaling><c:delete val="1"/><c:axPos val="b"/><c:majorTickMark val="none"/><c:minorTickMark val="none"/><c:tickLblPos val="nextTo"/><c:crossAx val="900002"/><c:crosses val="autoZero"/><c:auto val="1"/><c:lblAlgn val="ctr"/><c:lblOffset val="100"/><c:noMultiLvlLbl val="0"/></c:catAx>
<c:valAx><c:axId val="900002"/><c:scaling><c:orientation val="minMax"/><c:max val="55"/><c:min val="0"/></c:scaling><c:delete val="0"/><c:axPos val="r"/><c:numFmt formatCode="0&quot;%&quot;" sourceLinked="0"/><c:majorTickMark val="out"/><c:minorTickMark val="none"/><c:tickLblPos val="nextTo"/><c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="1100"/></a:pPr><a:endParaRPr lang="en-US"/></a:p></c:txPr><c:crossAx val="900001"/><c:crosses val="max"/><c:crossBetween val="between"/></c:valAx></root>'''
last_ax=plotArea.findall("{%s}valAx"%C)[-1]
for el in reversed(list(etree.fromstring(axes_xml))): last_ax.addnext(el)
# write margin column into embedded workbook so "Edit data" shows it
from openpyxl import load_workbook
import io
wbpart=gf.chart.part.chart_workbook.xlsx_part; wb=load_workbook(io.BytesIO(wbpart.blob)); ws=wb.active
ws["C1"]="Operating margin (%)"
for i,m in enumerate(margins): ws.cell(row=i+2,column=3,value=m)
bio=io.BytesIO(); wb.save(bio); wbpart._blob=bio.getvalue()
footer(s,"Source: Microsoft quarterly income statements via stockanalysis.com (revenue, operating income); margin = operating income / revenue. FQ1'25 = quarter ended 2024-09-30.")

# 4 Capex & FCF
s=prs.slides.add_slide(blank)
cg=(years[-1][1]/years[-2][1]-1)*100; fg=(years[-1][2]/years[-2][2]-1)*100
header(s,f"FY26 capex +{cg:.1f}% to ${years[-1][1]:,}M; FCF down {abs(fg):.1f}% to ${years[-1][2]:,}M",
       "Capital expenditures and free cash flow by fiscal year (USD millions); FY ends June 30")
cd=CategoryChartData(); cd.categories=[y[0] for y in years]
cd.add_series("Capex (USD M)",[y[1] for y in years]); cd.add_series("Free cash flow (USD M)",[y[2] for y in years])
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Inches(0.5),Inches(1.5),Inches(8.8),Inches(5.2),cd); ch=gf.chart
for ser,c in zip(ch.series,[NAVY,TEAL]): ser.format.fill.solid(); ser.format.fill.fore_color.rgb=c
pl=ch.plots[0]; pl.gap_width=80; pl.overlap=-10; pl.has_data_labels=True; pl.data_labels.number_format='#,##0'; pl.data_labels.number_format_is_linked=False; pl.data_labels.font.size=Pt(11); pl.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END
ch.value_axis.minimum_scale=0; ch.value_axis.maximum_scale=130000; ch.value_axis.tick_labels.number_format='#,##0'; ch.value_axis.tick_labels.number_format_is_linked=False
ch.value_axis.major_gridlines.format.line.color.rgb=RGBColor(0xE3,0xE6,0xEA); ch.value_axis.tick_labels.font.size=Pt(11); ch.category_axis.tick_labels.font.size=Pt(12)
ch.has_legend=True; ch.legend.position=XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout=False; ch.legend.font.size=Pt(12)
rows=["Operating cash flow (USD M)"]+[f"{y[0]}: {y[3]:,}" for y in years]+["","Capex / OCF"]+[f"{y[0]}: {y[1]/y[3]*100:.1f}%" for y in years]
textbox(s,9.6,1.7,3.3,5,rows,13)
footer(s,"Source: Microsoft cash flow statements via stockanalysis.com. Capex = additions to property and equipment (excludes finance leases). FCF = operating cash flow - capex.")

# 5 Takeaways
s=prs.slides.add_slide(blank)
header(s,"Key takeaways: strong operations, but the market is pricing the capex bill")
m=margins
fy26rev=sum(q[2] for q in quarters[4:]); fy25rev=sum(q[2] for q in quarters[:4])
fy26oi=sum(q[3] for q in quarters[4:]); fy25oi=sum(q[3] for q in quarters[:4])
bul=[f"Stock: MSFT returned +{tr['MSFT']:.1f}% ({start} to {end}), trailing QQQ (+{tr['QQQ']:.1f}%) by {tr['QQQ']-tr['MSFT']:.1f} pts and XLK (+{tr['XLK']:.1f}%) by {tr['XLK']-tr['MSFT']:.1f} pts.",
     f"Drawdown: MSFT fell to {msft_min:.1f} on the index ({msft_min-100:.1f}%) by {w['dates'][imin]}, then rallied after FQ4'26 results; QQQ and XLK never fell more than {100-min(w['QQQ_idx']):.1f}% and {100-min(w['XLK_idx']):.1f}% below their start.",
     f"Growth: FY26 revenue ${fy26rev:,}M (+{(fy26rev/fy25rev-1)*100:.1f}% YoY); FQ4'26 revenue ${quarters[-1][2]:,}M (+{g:.1f}% YoY).",
     f"Profitability: FY26 operating margin {fy26oi/fy26rev*100:.1f}% vs. {fy25oi/fy25rev*100:.1f}% in FY25; quarterly margin peaked at {max(m):.1f}% (FQ1'26) and was {m[-1]:.1f}% in FQ4'26.",
     f"Investment: capex rose from ${years[0][1]:,}M (FY23) to ${years[-1][1]:,}M (FY26), {years[-1][1]/years[0][1]:.1f}x; FY26 capex was {years[-1][1]/years[-1][3]*100:.1f}% of operating cash flow.",
     f"Cash: FCF fell for a second year to ${years[-1][2]:,}M in FY26 ({fg:+.1f}%), even as operating cash flow grew {(years[-1][3]/years[-2][3]-1)*100:.1f}%. Watch FQ1'27 results (late 2026-10) for capex guidance."]
tb=s.shapes.add_textbox(Inches(0.6),Inches(1.3),Inches(12.1),Inches(5.4)); tf=tb.text_frame; tf.word_wrap=True
for i,b in enumerate(bul):
    p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
    r=p.add_run(); r.text="•  "+b; r.font.size=Pt(17); r.font.color.rgb=DARK; p.space_after=Pt(14)
footer(s,"Sources: stockanalysis.com price history (adjusted closes) and Microsoft financial statements. Figures in USD millions; percentages to one decimal place.")
prs.save(OUT)
print("saved",OUT); print("margins",margins); print("tr",tr)
print(bul)
