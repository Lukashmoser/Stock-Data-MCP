---
name: northwind-ppt-template
description: Northwind Research PowerPoint template for building branded equity research presentations. Use when creating Northwind Research equity research notes (initiations, earnings updates, company notes) or sector decks (industry overviews, comps, thematic pieces) as .pptx files.
---

# Northwind Research PPT Template

Template: `assets/template.pptx` (13.33" x 7.50", 16:9, 7 layouts, ships with 6 sample slides that must be deleted)

Brand: navy `#1F2A44` (dk1/accent1), slate `#3A4255` (dk2), grey `#6B7280` (accent2), light grey `#9CA3AF` / `#C9CED6`, off-white `#EEF0F3` (lt2), secondary navy `#4A5A7A` (accent4) and `#2E3B5E` (accent6). Headings: Cambria (theme major font). Body: Calibri (theme minor font).

Every layout except DEFAULT already carries the "NORTHWIND RESEARCH" logo box (top left) and the footer disclaimer (bottom left, y=6.95"). Never add them again.

## Creating Presentations

```python
from pptx import Presentation

prs = Presentation("path/to/skill/assets/template.pptx")

# DELETE all existing sample slides first
while len(prs.slides) > 0:
    rId = prs.slides._sldIdLst[0].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[0]

slide = prs.slides.add_slide(prs.slide_layouts[3])  # Title and Content
```

## Key Layouts

| Index | Name | Background | Use For |
|-------|------|-----------|---------|
| 0 | DEFAULT | white, no branding | Avoid. No placeholders, no logo/footer |
| 1 | Northwind Title | navy `#1F2A44` | Cover: report title, company/ticker, date |
| 2 | Northwind Section Header | slate `#3A4255` | Section dividers ("01", "Valuation") |
| 3 | Northwind Title and Content | white | Investment summary, key points, custom tables |
| 4 | Northwind Two Content | white | Bull vs bear, estimates vs consensus, pros/cons |
| 5 | Northwind Title and Chart | white | Native chart + source line |
| 6 | Northwind Disclaimer | off-white `#EEF0F3` | Analyst certification and disclosures (last slide) |

## Placeholder Mapping

**CRITICAL: placeholder idx values are 102/103/104, NOT 0/1.** Always select placeholders by `placeholder_format.idx`. In the Section Header layout the order is reversed (idx 102 is the BODY section number, idx 103 is the TITLE).

### Layout 1: Northwind Title
| idx | Type | Position | Size / colour | Use |
|-----|------|----------|---------------|-----|
| 102 | TITLE (1) | x=0.50", y=2.40", w=10.50", h=1.40" | Cambria 44pt, white | Report title |
| 103 | BODY (2) | x=0.50", y=3.95", w=10.50", h=0.90" | 20pt, `#C9CED6` | "Company (TICKER) \| Note type \| YYYY-MM-DD" |

### Layout 2: Northwind Section Header
| idx | Type | Position | Size / colour | Use |
|-----|------|----------|---------------|-----|
| 102 | BODY (2) | x=0.50", y=2.20", w=3.00", h=0.60" | 20pt, `#C9CED6` | Section number "01" |
| 103 | TITLE (1) | x=0.50", y=2.85", w=11.00", h=1.20" | Cambria 40pt, white | Section title |

### Layout 3: Northwind Title and Content
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50", y=0.95", w=12.33", h=0.90" | Slide title (32pt, use an action title) |
| 103 | BODY (2) | x=0.50", y=2.05", w=12.33", h=4.60" | Bullets (16pt) |

### Layout 4: Northwind Two Content
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50", y=0.95", w=12.33", h=0.90" | Slide title |
| 103 | BODY (2) | x=0.50", y=2.05", w=5.92", h=4.60" | Left column |
| 104 | BODY (2) | x=6.91", y=2.05", w=5.92", h=4.60" | Right column |

### Layout 5: Northwind Title and Chart
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50", y=0.95", w=12.33", h=0.90" | Chart title / takeaway |
| 103 | CHART (8) | x=0.50", y=2.05", w=12.33", h=4.10" | `insert_chart(...)` |
| 104 | BODY (2) | x=0.50", y=6.30", w=12.33", h=0.35" | "Source: ..." (10pt grey) |

### Layout 6: Northwind Disclaimer
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50", y=0.95", w=12.33", h=0.90" | "Important Disclosures" (28pt) |
| 103 | BODY (2) | x=0.50", y=1.90", w=12.33", h=4.80" | Disclosure text (11pt) |

All layouts 1-6 also have a SLIDE_NUMBER placeholder (idx 4294967295) at x=12.20", y=6.95", w=0.63", h=0.30". **python-pptx does not copy it onto new slides**; use `add_slide_number()` below.

### Content Area Boundaries

```
Content Area (Layouts 3, 4, 5):
- Left margin: 0.50"
- Top: 2.05"  (title ends at 1.85"; 0.20" gap is reserved, do not place content above 2.05")
- Width: 12.33"  (right edge 12.83")
- Height: 4.60"  (bottom 6.65"; footer disclaimer and slide number sit at 6.95")
- Chart layout: chart 2.05"-6.15", source line 6.30"-6.65"
- Disclaimer layout: body starts higher, at 1.90"

Two columns (Layout 4): left x=0.50" w=5.92"; right x=6.91" w=5.92" (0.49" gutter)

4-quadrant grid inside the content area (0.25" gutters):
- Left column: x=0.50", width=6.04"
- Right column: x=6.79", width=6.04"
- Top row: y=2.05", height=2.18"
- Bottom row: y=4.48", height=2.17"
```

Custom shapes, tables and charts must stay inside these boundaries so they never collide with the title, logo box, footer disclaimer or slide number. When a slide uses a custom table or shape instead of the body text, remove the unused body placeholder (`remove_placeholder`) so an empty "Click to add text" prompt does not show.

## Helpers (copy into your build script)

The layout body style has no bullets and the master falls back to 28-32pt for deeper levels, so write paragraphs with the explicit house formatting used in the template's own sample slides: bullet `•`, 16pt, slate text (`tx2`), 8pt space after, level 1 indented to 0.75". **Do not type bullet characters into the text.**

```python
import copy
from pptx.util import Pt, Inches, Emu
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.oxml.ns import qn

NAVY = RGBColor(0x1F, 0x2A, 0x44)
SLATE = RGBColor(0x3A, 0x42, 0x55)
GREY = RGBColor(0x6B, 0x72, 0x80)
LIGHT = RGBColor(0xEE, 0xF0, 0xF3)
SERIES_COLORS = [RGBColor(0x1F, 0x2A, 0x44), RGBColor(0x4A, 0x5A, 0x7A),
                 RGBColor(0x9C, 0xA3, 0xAF), RGBColor(0x6B, 0x72, 0x80)]

def ph(slide, idx):
    for shape in slide.placeholders:
        if shape.placeholder_format.idx == idx:
            return shape
    raise KeyError(f"placeholder idx {idx} not on slide")

def remove_placeholder(slide, idx):
    el = ph(slide, idx)._element
    el.getparent().remove(el)

def add_slide_number(slide):
    """Copy the layout's slide-number placeholder onto the slide."""
    for shape in slide.slide_layout.placeholders:
        if shape.placeholder_format.type == 13:  # SLIDE_NUMBER
            slide.shapes._spTree.append(copy.deepcopy(shape._element))
            return

def set_bullets(shape, items, size=16):
    """items: list of (text, level) or (text, level, style).
    level 0 = main point, level 1 = sub-point.
    style: "bullet" (default), "heading" (bold, no bullet), "plain" (no bullet, regular weight)."""
    tf = shape.text_frame
    tf.clear()
    for i, item in enumerate(items):
        text, level = item[0], item[1]
        style = item[2] if len(item) > 2 else "bullet"
        bullet = style == "bullet"
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.level = level
        pPr = p._p.get_or_add_pPr()
        if bullet:
            pPr.set("marL", str(342900 + 342900 * level))
            pPr.set("indent", "-342900")
        else:
            pPr.set("marL", str(342900 * level))
            pPr.set("indent", "0")
        p.space_after = Pt(8)
        for tag in ("a:buNone", "a:buChar", "a:buSzPct"):
            for el in pPr.findall(qn(tag)):
                pPr.remove(el)
        if bullet:
            bs = pPr.makeelement(qn("a:buSzPct"), {"val": "100000"}); pPr.append(bs)
            bc = pPr.makeelement(qn("a:buChar"), {"char": "•"}); pPr.append(bc)
        else:
            pPr.append(pPr.makeelement(qn("a:buNone"), {}))
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = style == "heading"
        r.font.color.theme_color = MSO_THEME_COLOR.TEXT_1 if style == "heading" else MSO_THEME_COLOR.TEXT_2

def add_table(slide, data, x=0.50, y=2.05, w=12.33, row_h=0.36, col_widths=None,
              font_size=12, first_col_align_left=True):
    """data[0] is the header row. Navy header, banded light rows, numbers right-aligned."""
    from pptx.enum.text import PP_ALIGN
    rows, cols = len(data), len(data[0])
    gf = slide.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(row_h * rows))
    tbl = gf.table
    if col_widths:
        for c, cw in enumerate(col_widths):
            tbl.columns[c].width = Inches(cw)
    for r in range(rows):
        for c in range(cols):
            cell = tbl.cell(r, c)
            cell.margin_left = cell.margin_right = Inches(0.08)
            para = cell.text_frame.paragraphs[0]
            para.alignment = PP_ALIGN.LEFT if (c == 0 and first_col_align_left) else PP_ALIGN.RIGHT
            run = para.add_run()          # works for empty strings too
            run.text = str(data[r][c])
            run.font.size = Pt(font_size)
            run.font.name = "Calibri"
            cell.fill.solid()
            if r == 0:
                cell.fill.fore_color.rgb = NAVY
                run.font.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            else:
                cell.fill.fore_color.rgb = LIGHT if r % 2 == 0 else RGBColor(0xFF, 0xFF, 0xFF)
                run.font.color.rgb = SLATE
    return tbl

def add_source(slide, text, y=6.30):
    """Source line under a custom table/shape (the chart layout has its own idx 104)."""
    from pptx.enum.text import PP_ALIGN
    tb = slide.shapes.add_textbox(Inches(0.50), Inches(y), Inches(12.33), Inches(0.35))
    tb.text_frame.word_wrap = True   # without this LibreOffice/Keynote centre the line
    p = tb.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run(); r.text = text
    r.font.size = Pt(10); r.font.color.rgb = GREY
    return tb

def style_chart(chart, number_format='#,##0'):
    chart.font.size = Pt(12)
    chart.font.name = "Calibri"
    chart.has_legend = len(chart.plots[0].series) > 1
    if chart.has_legend:
        from pptx.enum.chart import XL_LEGEND_POSITION
        chart.legend.position = XL_LEGEND_POSITION.TOP
        chart.legend.include_in_layout = False
    for i, s in enumerate(chart.plots[0].series):
        s.format.fill.solid()
        s.format.fill.fore_color.rgb = SERIES_COLORS[i % len(SERIES_COLORS)]
    va = chart.value_axis
    va.has_major_gridlines = True
    va.major_gridlines.format.line.color.rgb = RGBColor(0xC9, 0xCE, 0xD6)
    va.tick_labels.number_format = number_format
    va.tick_labels.number_format_is_linked = False
    va.format.line.fill.background()
```

## Example: Cover Slide

```python
slide = prs.slides.add_slide(prs.slide_layouts[1])
ph(slide, 102).text = "Acme Corp: Initiating at Overweight"
ph(slide, 103).text = "Acme Corp (ACME)  |  Initiation of Coverage  |  2026-10-15"
add_slide_number(slide)
```

## Example: Section Header

```python
slide = prs.slides.add_slide(prs.slide_layouts[2])
ph(slide, 102).text = "02"            # BODY = section number
ph(slide, 103).text = "Valuation"     # TITLE
add_slide_number(slide)
```

## Example: Content Slide

```python
slide = prs.slides.add_slide(prs.slide_layouts[3])
ph(slide, 102).text = "Margin expansion is under-appreciated"
set_bullets(ph(slide, 103), [
    ("Revenue grew 12.4% y/y to USD 1,250 million", 0),
    ("Subscription mix reached 61.0% of revenue", 1),
    ("Valuation", 0, "heading"),                  # bold run-in heading, no bullet
    ("Price target USD 85.00 (DCF, 9.0% WACC)", 0),
])
add_slide_number(slide)
```

## Example: Two-Column Slide (bull / bear)

```python
slide = prs.slides.add_slide(prs.slide_layouts[4])
ph(slide, 102).text = "Bull vs bear case"
set_bullets(ph(slide, 103), [("Bull case: USD 110.00", 0, "heading"), ("Share gains in enterprise", 0)])
set_bullets(ph(slide, 104), [("Bear case: USD 55.00", 0, "heading"), ("Pricing pressure", 0)])
add_slide_number(slide)
```

## Example: Chart Slide

```python
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

slide = prs.slides.add_slide(prs.slide_layouts[5])
ph(slide, 102).text = "Revenue (USD millions)"
cd = CategoryChartData()
cd.categories = ["FY2023", "FY2024", "FY2025E", "FY2026E"]
cd.add_series("Revenue", (980, 1112, 1250, 1390))
gf = ph(slide, 103).insert_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, cd)
style_chart(gf.chart)
ph(slide, 104).text = "Source: Company filings, Northwind Research estimates"
add_slide_number(slide)
```

## Example: Table Slide (comps / estimates)

```python
slide = prs.slides.add_slide(prs.slide_layouts[3])
ph(slide, 102).text = "Sector comps"
remove_placeholder(slide, 103)                      # free the content area
add_table(slide, [["Company", "Mkt cap (USD m)", "EV/EBITDA", "P/E"],
                  ["Acme", "12,400", "11.2x", "18.5x"]])
add_source(slide, "Source: Company filings, Northwind Research estimates")
add_slide_number(slide)
```

## Example: Disclaimer (always last)

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])
ph(slide, 102).text = "Important Disclosures"
set_bullets(ph(slide, 103), [("Analyst certification", 0, "heading"),
                             ("The research analyst(s) certify that ...", 0, "plain")], size=11)
add_slide_number(slide)
```

## Rules

1. Always start from `assets/template.pptx` and delete the 6 sample slides first.
2. Never use layout 0 (DEFAULT); it carries no branding.
3. Address placeholders by idx (102/103/104); never assume idx 0/1.
4. Call `add_slide_number(slide)` on every slide.
5. No manual bullet characters; use `set_bullets` levels.
6. Keep slide titles to one line: about 55 characters at 32pt on layouts 3-5 (a two-line title runs into the body at 2.05"). Shorten rather than shrink.
7. Keep custom content within x 0.50"-12.83", y 2.05"-6.65".
8. Equity research conventions: action titles, money in USD millions (per-share in USD), percentages to one decimal, dates YYYY-MM-DD, a source line under every chart/table, and the Disclaimer slide last.
9. After building, render to PDF/PNG (e.g. `soffice --headless --convert-to pdf`) and check for overflow or overlap before delivering.
