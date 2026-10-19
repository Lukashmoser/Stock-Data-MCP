---
name: northwind-ppt-template
description: Northwind Research PowerPoint template for equity research notes and sector decks. Use when creating Northwind Research-branded presentations such as company/earnings notes, initiation summaries, sector overviews, thematic decks or any slide deck that must follow the Northwind Research template (navy palette, 16:9, cover / section / content / two-column / chart / disclosures layouts).
---

# Northwind Research PPT Template

Template: `assets/template.pptx` (13.33" x 7.50", 16:9, 7 layouts, 1 master)

Brand: navy palette, Cambria headings (theme major font), Calibri body (theme minor font).
Every layout already carries the "NORTHWIND RESEARCH" logo box (top left), the
footer disclaimer line and a slide number position. Do not re-draw these.

## Quick Start

Paste the helper block below into your build script, then build slides with it.
All helpers use only `python-pptx`.

```python
import copy
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.oxml.ns import qn
from pptx.enum.shapes import PP_PLACEHOLDER

TEMPLATE = "path/to/northwind-ppt-template/assets/template.pptx"

# Layout indices
L_DEFAULT, L_COVER, L_SECTION, L_CONTENT, L_TWO_COL, L_CHART, L_DISCLAIMER = range(7)

# Brand colours (theme "Northwind Research")
NAVY      = RGBColor(0x1F, 0x2A, 0x44)  # dk1 / accent1 - titles, primary series
SLATE     = RGBColor(0x3A, 0x42, 0x55)  # dk2 (tx2) - body text, section bg
GREY      = RGBColor(0x6B, 0x72, 0x80)  # accent2 - sources, footers, 2nd series
MID_GREY  = RGBColor(0x9C, 0xA3, 0xAF)  # accent3
STEEL     = RGBColor(0x4A, 0x5A, 0x7A)  # accent4
LIGHT     = RGBColor(0xC9, 0xCE, 0xD6)  # accent5 - section numbers, gridlines
INDIGO    = RGBColor(0x2E, 0x3B, 0x5E)  # accent6
PALE      = RGBColor(0xEE, 0xF0, 0xF3)  # lt2 - table banding, disclaimer bg
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
SERIES_COLORS = [NAVY, GREY, STEEL, MID_GREY, INDIGO, LIGHT]

# Content area (inches) - from the layout placeholders
CONTENT = dict(left=0.50, top=2.05, width=12.33, height=4.60)   # bottom = 6.65"
LEFT_COL = dict(left=0.50, top=2.05, width=5.92, height=4.60)
RIGHT_COL = dict(left=6.91, top=2.05, width=5.92, height=4.60)


def new_presentation(path=TEMPLATE):
    """Open the template and delete its 6 sample slides."""
    prs = Presentation(path)
    sldIdLst = prs.slides._sldIdLst
    while len(sldIdLst) > 0:
        rId = sldIdLst[0].rId
        prs.part.drop_rel(rId)
        del sldIdLst[0]
    return prs


def add_slide(prs, layout_idx, slide_number=True):
    """Add a slide from a layout. python-pptx does NOT copy the slide-number
    placeholder from the layout, so it is cloned here (cover included, as in
    the template sample slides)."""
    layout = prs.slide_layouts[layout_idx]
    slide = prs.slides.add_slide(layout)
    if slide_number:
        for sp in layout.placeholders:
            if sp.placeholder_format.type == PP_PLACEHOLDER.SLIDE_NUMBER:
                slide.shapes._spTree.append(copy.deepcopy(sp.element))
    return slide


def ph(slide, idx):
    """Return the placeholder with the given idx (102 / 103 / 104)."""
    for shape in slide.placeholders:
        if shape.placeholder_format.idx == idx:
            return shape
    raise KeyError(f"placeholder idx={idx} not on this slide")


def set_text(shape, text):
    """Replace the text of a single-line placeholder; keeps layout formatting."""
    shape.text_frame.text = text


def _fmt_run(run, size=16, bold=False, italic=False, color=MSO_THEME_COLOR.TEXT_2):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if isinstance(color, RGBColor):
        run.font.color.rgb = color
    else:
        run.font.color.theme_color = color


def _bullet(p, level):
    """Northwind bullet format (matches template sample slide 3)."""
    pPr = p._p.get_or_add_pPr()
    marL = 342900 if level == 0 else 685800          # 0.375" / 0.75"
    pPr.set('marL', str(marL))
    pPr.set('indent', '-342900')
    if level:
        pPr.set('lvl', str(level))
    for tag in ('a:buNone', 'a:buChar', 'a:buSzPct'):
        for el in pPr.findall(qn(tag)):
            pPr.remove(el)
    buSz = pPr.makeelement(qn('a:buSzPct'), {'val': '100000'})
    buCh = pPr.makeelement(qn('a:buChar'), {'char': '•'})
    pPr.append(buSz)
    pPr.append(buCh)


def _space_after(p, pts=8):
    p.space_after = Pt(pts)


def fill_body(shape, items, size=16):
    """Fill a body placeholder.
    items: list of (text, kind) where kind is
      'h'  - bold heading line, no bullet
      0    - first-level bullet
      1    - second-level bullet
      'p'  - plain paragraph, no bullet
    """
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    for i, (text, kind) in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        run = p.add_run()
        run.text = text
        if kind == 'h':
            _fmt_run(run, size=size, bold=True)
        elif kind in (0, 1):
            _bullet(p, kind)
            _fmt_run(run, size=size)
        else:
            _fmt_run(run, size=size)
        _space_after(p)
    return tf


def cover(prs, title, subtitle):
    s = add_slide(prs, L_COVER)
    set_text(ph(s, 102), title)
    set_text(ph(s, 103), subtitle)          # e.g. "Sector Update  |  2026-10-15"
    return s


def section(prs, number, title):
    s = add_slide(prs, L_SECTION)
    set_text(ph(s, 102), number)            # "01" - NOTE: idx 102 is the number
    set_text(ph(s, 103), title)             #        idx 103 is the TITLE here
    return s


def content(prs, title, items):
    s = add_slide(prs, L_CONTENT)
    set_text(ph(s, 102), title)
    fill_body(ph(s, 103), items)
    return s


def two_col(prs, title, left_items, right_items):
    s = add_slide(prs, L_TWO_COL)
    set_text(ph(s, 102), title)
    fill_body(ph(s, 103), left_items)
    fill_body(ph(s, 104), right_items)
    return s


def chart_slide(prs, title, categories, series, source,
                chart_type=XL_CHART_TYPE.COLUMN_CLUSTERED, number_format='#,##0',
                legend=True, data_labels=False):
    """series: dict name -> list of values."""
    s = add_slide(prs, L_CHART)
    set_text(ph(s, 102), title)
    cd = CategoryChartData()
    cd.categories = categories
    for name, vals in series.items():
        cd.add_series(name, vals)
    gf = ph(s, 103).insert_chart(chart_type, cd)
    style_chart(gf.chart, number_format, legend and len(series) > 1, data_labels)
    src = ph(s, 104)
    src.text_frame.text = source
    r = src.text_frame.paragraphs[0].runs[0]
    _fmt_run(r, size=10, italic=True, color=GREY)
    return s


def style_chart(chart, number_format='#,##0', legend=True, data_labels=False):
    chart.font.size = Pt(11)
    chart.font.color.rgb = SLATE
    chart.has_title = False
    plot = chart.plots[0]
    is_line = chart.chart_type in (XL_CHART_TYPE.LINE, XL_CHART_TYPE.LINE_MARKERS)
    if hasattr(plot, 'gap_width') and not is_line:
        plot.gap_width = 80
    for i, s in enumerate(plot.series):
        c = SERIES_COLORS[i % len(SERIES_COLORS)]
        if is_line:
            s.format.line.color.rgb = c
            s.format.line.width = Pt(2.25)
            s.smooth = False
        else:
            s.format.fill.solid()
            s.format.fill.fore_color.rgb = c
    if data_labels:
        plot.has_data_labels = True
        plot.data_labels.number_format = number_format
        plot.data_labels.number_format_is_linked = False
        plot.data_labels.font.size = Pt(10)
        from pptx.enum.chart import XL_LABEL_POSITION
        plot.data_labels.position = (XL_LABEL_POSITION.ABOVE if is_line
                                     else XL_LABEL_POSITION.OUTSIDE_END)
    try:
        va = chart.value_axis
        va.has_major_gridlines = True
        va.major_gridlines.format.line.color.rgb = LIGHT
        va.format.line.fill.background()
        va.tick_labels.number_format = number_format
        va.tick_labels.number_format_is_linked = False
        chart.category_axis.format.line.color.rgb = MID_GREY
    except Exception:
        pass
    chart.has_legend = legend
    if legend:
        chart.legend.position = XL_LEGEND_POSITION.BOTTOM
        chart.legend.include_in_layout = False
        chart.legend.font.size = Pt(10)


def add_table(slide, header, rows, area=CONTENT, col_widths=None, font_size=11,
              row_height=0.32, text_cols=(0,)):
    """Branded table inside the content area. Columns listed in text_cols are
    left-aligned; all other (numeric) columns are right-aligned."""
    from pptx.enum.text import PP_ALIGN
    n_rows, n_cols = len(rows) + 1, len(header)
    height = min(area['height'], row_height * n_rows)
    gf = slide.shapes.add_table(n_rows, n_cols, Inches(area['left']), Inches(area['top']),
                                Inches(area['width']), Inches(height))
    tbl = gf.table
    # drop the default table style banding look
    tblPr = gf._element.graphic.graphicData.tbl.tblPr
    tblPr.set('bandRow', '0'); tblPr.set('firstRow', '0')
    if col_widths:
        for i, w in enumerate(col_widths):
            tbl.columns[i].width = Inches(w)
    for r in range(n_rows):
        tbl.rows[r].height = Inches(row_height)
        for c in range(n_cols):
            cell = tbl.cell(r, c)
            val = header[c] if r == 0 else rows[r - 1][c]
            cell.text_frame.clear()
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if c in text_cols else PP_ALIGN.RIGHT
            run = p.add_run()          # works for empty strings too
            run.text = str(val)
            cell.fill.solid()
            if r == 0:
                cell.fill.fore_color.rgb = NAVY
                _fmt_run(run, size=font_size, bold=True, color=WHITE)
            else:
                cell.fill.fore_color.rgb = PALE if r % 2 == 0 else WHITE
                _fmt_run(run, size=font_size, color=SLATE)
    return gf


def add_source(slide, text, top=6.68):
    """Source line for content/two-column slides (chart layout has its own)."""
    tb = slide.shapes.add_textbox(Inches(0.50), Inches(top), Inches(10.50), Inches(0.22))
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True
    tf.text = text
    from pptx.enum.text import PP_ALIGN
    tf.paragraphs[0].alignment = PP_ALIGN.LEFT
    _fmt_run(tf.paragraphs[0].runs[0], size=9, italic=True, color=GREY)
    return tb


def disclaimer(prs, sections, title="Important Disclosures"):
    """sections: list of (heading, paragraph_text)."""
    s = add_slide(prs, L_DISCLAIMER)
    set_text(ph(s, 102), title)
    items = []
    for head, body in sections:
        items += [(head, 'h'), (body, 'p')]
    tf = fill_body(ph(s, 103), items, size=11)
    for p in tf.paragraphs:
        p.space_after = Pt(4)
    return s
```

Then:

```python
prs = new_presentation()
cover(prs, "Acme Corp (ACME): 3Q26 Earnings Review", "Equity Research  |  2026-10-15")
section(prs, "01", "Investment Summary")
content(prs, "Key Takeaways", [("Results", 'h'), ("Revenue beat consensus", 0), ("Driven by pricing", 1)])
prs.save("output.pptx")
```

## Layouts

| Index | Name | Background | Use For |
|-------|------|-----------|---------|
| 0 | DEFAULT | master (white) | Blank - no placeholders, no logo/footer. Avoid. |
| 1 | Northwind Title | navy `#1F2A44` | Cover slide: report title, company/sector, date |
| 2 | Northwind Section Header | slate `#3A4255` | Section dividers ("01 Investment Thesis") |
| 3 | Northwind Title and Content | white | Bullets, or a title + custom table/shapes |
| 4 | Northwind Two Content | white | Bull/bear, thesis/risks, estimate changes vs. commentary |
| 5 | Northwind Title and Chart | white | One native chart + source line |
| 6 | Northwind Disclaimer | pale grey `#EEF0F3` | Important disclosures / analyst certification (last slide) |

## Placeholder Mapping (exact positions, inches)

All placeholders use idx 102/103/104 (not 0/1). All share the shape name "Text 2",
so always address by **idx**, never by name. Each layout also has a slide-number
placeholder (idx 4294967295, x=12.20, y=6.95, w=0.63, h=0.30) that `add_slide()` clones.

### Layout 1: Northwind Title
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50, y=2.40, w=10.50, h=1.40 | Report title (white, bold) |
| 103 | BODY (2) | x=0.50, y=3.95, w=10.50, h=0.90 | Subtitle, e.g. "Sector Update  \|  2026-10-15" |

### Layout 2: Northwind Section Header
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | BODY (2) | x=0.50, y=2.20, w=3.00, h=0.60 | Section number "01" (20pt bold, `#C9CED6`) |
| 103 | TITLE (1) | x=0.50, y=2.85, w=11.00, h=1.20 | Section title (40pt bold, white) |

**Watch out:** on this layout idx 102 is the *number* and idx 103 is the *title* - reversed versus every other layout.

### Layout 3: Northwind Title and Content
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50, y=0.95, w=12.33, h=0.90 | Slide title (32pt bold navy) |
| 103 | BODY (2) | x=0.50, y=2.05, w=12.33, h=4.60 | Body text, 16pt slate |

### Layout 4: Northwind Two Content
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50, y=0.95, w=12.33, h=0.90 | Slide title |
| 103 | BODY (2) | x=0.50, y=2.05, w=5.92, h=4.60 | Left column (bold heading + bullets) |
| 104 | BODY (2) | x=6.91, y=2.05, w=5.92, h=4.60 | Right column |

### Layout 5: Northwind Title and Chart
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50, y=0.95, w=12.33, h=0.90 | Chart title (state the takeaway) |
| 103 | CHART (8) | x=0.50, y=2.05, w=12.33, h=4.10 | Native chart via `insert_chart()` |
| 104 | BODY (2) | x=0.50, y=6.30, w=12.33, h=0.35 | Source line, 10pt italic grey |

### Layout 6: Northwind Disclaimer
| idx | Type | Position | Use |
|-----|------|----------|-----|
| 102 | TITLE (1) | x=0.50, y=0.95, w=12.33, h=0.90 | "Important Disclosures" |
| 103 | BODY (2) | x=0.50, y=1.90, w=12.33, h=4.80 | Bold 11pt headings + 11pt paragraphs |

### Fixed layout elements (do not cover)
| Element | Position | Notes |
|---------|----------|-------|
| Logo box "NORTHWIND RESEARCH" | x=0.50, y=0.30, w=3.00, h=0.45 | Dashed-outline text stand-in for the logo |
| Footer disclaimer | x=0.50, y=6.95, w=10.50, h=0.30 | 9pt grey, "For illustrative purposes only..." |
| Slide number | x=12.20, y=6.95, w=0.63, h=0.30 | 9pt grey, right aligned |

## Content Area Boundaries

The template has no OBJECT placeholder; the body placeholders define the content area.

```
Content Area (Layouts 3 and 4):
- Left margin: 0.50"   Right edge: 12.83"  (0.50" right margin)
- Top: 2.05"           (title ends at 1.85"; 0.20" gap)
- Width: 12.33"
- Height: 4.60"        (bottom = 6.65"; footer starts 6.95")

Two columns (Layout 4 geometry - reuse for custom shapes):
- Left column:  x=0.50", width=5.92"
- Right column: x=6.91", width=5.92"   (gutter 0.49")

4-quadrant grid inside the content area:
- Left column: x=0.50", width=5.92";  Right column: x=6.91", width=5.92"
- Top row: y=2.05", height=2.15";     Bottom row: y=4.50", height=2.15" (0.30" gap)

Chart layout (5): chart y=2.05"-6.15"; source line y=6.30"-6.65".
Disclaimer layout (6): body starts higher, at y=1.90".
Optional source line on layouts 3/4: y=6.68", h=0.22" (use add_source()).
```

Custom textboxes, tables and charts must stay inside these boundaries so they do
not collide with the logo (top 0.30"-0.75"), title (0.95"-1.85") or footer (6.95"+).

## Formatting Rules (template-specific)

1. **Bullets must be set explicitly.** The body placeholders' level-1 style is
   `buNone` and the master's level-2 style is 28pt with an en-dash, so setting only
   `paragraph.level` gives an un-bulleted first level and a huge second level.
   Use `fill_body()` - it applies the template's own bullet spec (sample slide 3):
   `•` bullets, marL 0.375" (level 0) / 0.75" (level 1), hanging indent 0.375",
   16pt, colour tx2 (`#3A4255`), 8pt space after.
   Never type bullet characters ("•", "-") into the text itself.
2. **Column headings** inside two-column slides: bold 16pt tx2, no bullet (`'h'`).
3. **Fonts:** leave the typeface unset so theme fonts apply (Cambria titles, Calibri body).
4. **Slide titles:** one line, <= ~60 characters at 32pt; make it the takeaway
   ("Margins expand 150bp as mix shifts to software"), not a label.
5. **Body density:** at 16pt the body area fits ~12 lines; for more, drop to 14pt
   (`fill_body(..., size=14)`) or split the slide.
6. **Charts:** series colours in order navy, grey, steel, mid-grey, indigo, light;
   light-grey gridlines; legend bottom; always fill the source placeholder (idx 104).
7. **Tables:** navy header row with white bold text, alternating white / `#EEF0F3`
   rows, text columns left-aligned (`text_cols`), numbers right-aligned, 10-12pt.
8. **Units:** state units in the title or column header ("USD m", "%", "x").
9. **Deck order for research notes:** Cover -> (Section) -> Content / Chart / Two-column
   slides -> Disclaimer as the final slide. Every external deck ends with layout 6.
10. Do not use layout 0 (DEFAULT): it has no logo, footer or slide number.

## Typical Deck Structures

**Equity research note (6-10 slides):** Cover - Key takeaways (content) - Results vs.
estimates (content + table) - Revenue/margin chart (chart) - Bull vs. bear (two-column)
- Estimate changes & valuation (content + table) - Risks (content) - Disclosures.

**Sector deck (10-20 slides):** Cover - Executive summary - Section "01 Market" -
market size chart - drivers (two-column) - Section "02 Competitive landscape" - comps
table - share chart - Section "03 Top picks" - one slide per pick - Disclosures.

## Verify Before Delivering

```bash
soffice --headless --convert-to pdf output.pptx && pdftoppm -png -r 50 output.pdf preview
```
Check every slide image for: text overflowing placeholders, content overlapping the
footer (y > 6.65"), empty placeholders left with prompt text, and a slide number on
each slide. Remove any placeholder you did not use:
`sp = ph(slide, idx); sp.element.getparent().remove(sp.element)`.
