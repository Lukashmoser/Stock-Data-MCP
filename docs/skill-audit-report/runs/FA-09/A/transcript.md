# Transcript: FA-09 / Arm A

- Start: Fri Oct 16 03:25:10 UTC 2026
- End: Fri Oct 16 03:27:44 UTC 2026

---

# Deck Check Report: Project_Horizon.pptx (Strategic Alternatives for Zoom, ZM)

## Summary
The deck is **not client-ready**. Two of its headline figures are wrong when checked against Zoom's filings.

- **Market cap is overstated by about 25%.** The deck shows $35.8B. The verified figure is about $28.6B: 291.8M shares outstanding (10-Q cover, 2026-08-14) at the deck's own $98.16 price.
- **LTM revenue is understated by $499MM.** The deck shows $4,494MM. The verified figure is $4,993MM.

These two errors carry through to the margins, the EV, the trading multiples and the valuation chart. Fixing them also undercuts two storylines in the deck: the "premium to peers" takeaway and the "growth is accelerating" title.

- Total issues: 16. Critical: 9. Important: 4. Minor: 3.
- By category: internal 6, external 6, narrative 2, language 2.

## Critical Issues

### Number consistency (internal)
1. **EBITDA mismatch** (slides 2, 3 vs 6)
   - Slides 2 and 3 show LTM EBITDA of $1,316MM, which ties to the filings.
   - Slide 6 uses $1,361MM (transposed digits), which overstates the EBITDA range at 24,498–32,664.
   - Action: use $1,316MM, which gives an implied EV of $23,688–31,584MM at 18.0x–24.0x.
2. **Net cash table does not foot** (slide 3)
   - Cash of 932 plus marketable securities of 6,138 equals 7,070, not 7,250.
   - The 10-Q shows marketable securities of $6,317.7MM. "6,138" is a transposition of 6,318.
   - Action: change the line to 6,318. The $7,250MM net cash total is correct.
3. **One-year return is miscalculated** (slide 4)
   - $98.16 / $80.01 − 1 = **+22.7%**. The slide shows +27.2%.
   - Action: correct it to +22.7%, or +23.1% if the price is refreshed to $98.51.

### Factual accuracy (external)
4. **LTM revenue is wrong** (slides 2, 3, 5, 6)
   - The deck shows $4,494MM.
   - The filings give **$4,993.1MM**: FY26 $4,868.8MM + 1H FY27 $2,516.2MM − 1H FY26 $2,391.9MM.
   - Gross profit ($3,860MM), EBIT ($1,185MM), EBITDA ($1,316MM), FCF ($1,926MM) and buybacks ($1,460MM) all tie, so the revenue denominator is the only error in that set.
5. **Derived margins are overstated** (slides 2, 3, 5)
   - Gross margin: 85.9% → **77.3%**
   - EBIT margin: 26.4% → **23.7%**
   - EBITDA margin: 29.3% → **26.3%**
   - FCF margin: 42.9% → **38.6%**
6. **Market cap is overstated** (slides 2, 4, 5)
   - $35,802MM implies 364.7M shares. The 10-Q cover shows 291.78M shares (263.23M Class A + 28.55M Class B).
   - Corrected: **$28,641MM at $98.16**, or $28,744MM at today's $98.51 close.
7. **EV and multiples are overstated** (slides 5, 6)
   - EV: $28,552MM → **$21,392MM** (at $98.16)
   - EV / LTM revenue: 6.4x → **4.3x**
   - EV / LTM EBIT: 24.1x → **18.1x**
   - EV / LTM EBITDA: **16.3x**
   - Slide 6 revenue range: 22,470–31,458 → **24,965–34,951**
   - With the corrected EV, the current value sits **below every illustrative range**, so the framing of slide 6 needs to be rewritten.

### Data-narrative alignment
8. **"Zoom's growth is accelerating"** (slide 2)
   - The chart shows 4.4%, 5.3%, 5.5% then **4.9%**. The latest quarter decelerated.
   - Suggested title: "Situation overview: steady ~5% growth with strong cash generation".
9. **"Best-in-class margins support a premium to peer multiples"** (slide 5)
   - Zoom's EBIT margin is below the peer median: 26.4% as shown, 23.7% corrected, against a median of 28.7%.
   - Zoom also trades at a **discount** to peers, not a premium: 4.3x / 18.1x against medians of 8.4x / 29.4x.
   - Only gross margin leads the peer set. Reframe as "gross-margin leadership; trades at a discount to peers".

## Important Issues

### Language polish
10. **Typo and title-case drift** (slide 7)
    - "Potential Buyer Univrese" → "Potential buyer universe". All other titles are in sentence case.
11. **Unsupported or colloquial phrasing** (slides 3, 5)
    - "best-in-class" is not supported by the data.
    - "fortress balance sheet" is colloquial; consider "net cash balance sheet with no funded debt".

### Sourcing
12. **Missing or vague sources** (slides 4, 5, 6)
    - Slide 6 has a "Note" but no source line.
    - Slides 4 and 5 cite "market data" without naming the provider.
    - Action: add a source line to slide 6 and name the data vendor on slides 4 and 5.

### Freshness (external)
13. **Pricing date is stale** (slides 1, 2, 4, 5, 6)
    - Market data is dated 2026-10-13. The latest close is **$98.51 on 2026-10-15**, up 0.4% versus the deck's price.
    - Action: refresh to the send date.

## Minor Issues
14. **Unit style drift.** The deck mixes $B (slides 2, 4), $MM (slides 2, 3, 5) and $M (slide 6). Standardize on $MM.
15. **Date format drift.** The deck uses "October 13, 2026", "10/13/2025", "13-Oct-2026", "7/31/2026" and "2026-10-20". Pick one format.
16. **Monthly price points do not match month-end closes** (slide 4)
    - Several points differ from month-end closes, e.g. Apr-26 $103.44 vs $97.15 and Aug-26 $101.33 vs $96.68.
    - The footnote says "last weekly close", so this may be a methodology difference. Confirm the series and its vendor.

The 52-week high and low ($114.74 / $70.70) match third-party data. On the visual check, I found no overlaps, overflow or contrast problems. Fonts are consistent: Cambria for headings and KPI figures, Calibri for body text. The peer medians and peer multiples on slide 5 recompute correctly from the deck's own inputs.

### Final checklist
- [ ] Numbers reconciled (items 1–3)
- [ ] Market and financial figures verified (items 4–7, 13)
- [ ] Narrative matches data (items 8–9)
- [ ] Language meets IB standards (items 10–11)
- [ ] Charts sourced (item 12)
- [ ] Formatting consistent (items 14–16)

## Comparison Block

### 1. Key figures
| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Slide 6 | EBITDA input 1,361 vs 1,316 on slides 2/3; range should be 23,688–31,584 | internal | LTM to 2026-07-31 | Deck; Form 8-K Ex. 99.1 (filed 2026-08-25) | H |
| Slide 3 | Net cash table does not foot (932 + 6,138 ≠ 7,250); marketable securities should be 6,318 | internal | 2026-07-31 | Form 10-Q (Q2 FY27); Form 8-K Ex. 99.1 (2026-08-25) | H |
| Slide 4 | 1-year return 27.2% should be 22.7% (98.16 / 80.01) | internal | 2025-10-13 to 2026-10-13 | Deck arithmetic | H |
| Slides 2, 3, 5, 6 | LTM revenue 4,494 should be 4,993.1 | external | LTM to 2026-07-31 | Form 8-K Ex. 99.1 (2026-02-25 and 2026-08-25) | H |
| Slides 2, 3, 5 | Margins overstated: GM 85.9%→77.3%, EBIT 26.4%→23.7%, EBITDA 29.3%→26.3%, FCF 42.9%→38.6% | external | LTM to 2026-07-31 | Derived from the 8-Ks above | H |
| Slides 2, 4, 5 | Market cap 35.8B overstated (implies 364.7M shares vs 291.8M) | external | 2026-10-13 | Form 10-Q cover (shares as of 2026-08-14) | H |
| Slides 5, 6 | EV 28,552 should be about 21,392; EV/Rev 6.4x→4.3x, EV/EBIT 24.1x→18.1x; current EV below all ranges | external | 2026-10-13 | Derived | H |
| Slides 1, 2, 4, 5, 6 | Pricing as of 2026-10-13; latest close $98.51 (2026-10-15) | external | 2026-10-15 | https://equibles.com/stocks/zm/summary, https://chartrow.com/quote/zm | M |
| Slide 4 | Monthly chart points differ from month-end closes (e.g. Apr-26 103.44 vs 97.15) | external | Oct-25 to Oct-26 | https://www.digrin.com/stocks/detail/ZM/price | L |
| Slide 2 | Title "growth is accelerating" contradicted by Q2 FY27 slowdown to 4.9% from 5.5% | narrative | Q2 FY27 | Deck; Form 8-K Ex. 99.1 (2026-08-25) | H |
| Slide 5 | "Best-in-class margins support a premium" contradicted: EBIT margin below median; trades at discount | narrative | 2026-10-13 | Deck; derived | H |
| Slide 7 | Typo "Univrese" and Title Case inconsistent with other titles | language | N/A | Deck | H |
| Slides 3, 5 | Unsupported or colloquial phrasing ("best-in-class", "fortress balance sheet") | language | N/A | Deck | M |
| Slides 4, 5, 6 | Missing source on slide 6; vendor not named on slides 4/5 | internal | N/A | Deck (visual check) | H |
| Slides 2–6 | Unit style drift ($B / $MM / $M) | internal | N/A | Deck | H |
| Slides 1–8 | Date format drift (5 different styles) | internal | N/A | Deck | H |
| ZM market cap: deck | 35,802 | USD millions | 2026-10-13 | Deck slide 5 | H |
| ZM market cap: verified | 28,641 (at $98.16); 28,744 (at $98.51) | USD millions | 2026-10-13 / 2026-10-15 | 10-Q cover shares 291,783,711 × price; equibles.com / chartrow.com | M |
| ZM LTM revenue: deck | 4,494 | USD millions | LTM to 2026-07-31 | Deck slides 2/3/5/6 | H |
| ZM LTM revenue: verified | 4,993.1 | USD millions | LTM to 2026-07-31 | Form 8-K Ex. 99.1 (2026-02-25; 2026-08-25) | H |
| Total issues by category | internal 6; external 6; narrative 2; language 2 (total 16) | count | N/A | This review | H |

### 2. Sources used
- Skill financial-analysis:ib-check-deck: 1 load; its extract_numbers.py script run 2 times
- Bash (python-pptx extraction, LibreOffice render, calculations): 9 calls
- Read (rendered slide grid): 1
- WebSearch: 5
- WebFetch: 7
  - SEC 8-K Ex. 99.1 Q2 FY27: 1
  - SEC 8-K Ex. 99.1 Q4 FY26: 1
  - SEC 10-Q Q2 FY27: 1
  - equibles.com ZM: 1
  - equibles.com RNG: 1
  - digrin.com: 1
  - chartrow.com: 1

### 3. Estimates and gaps
- **LTM build.** LTM = FY26 (ended 2026-01-31) + 6M FY27 − 6M FY26. EBITDA = GAAP operating income + D&A, and FCF = OCF − capex, both matching the deck's definitions.
- **Shares outstanding.** I used the basic count from the 10-Q cover (291,783,711 as of 2026-08-14), with no adjustment for dilution or buybacks since then. A diluted (treasury stock method) count would be higher; the Q2 weighted diluted count was about 299.7M.
- **Prices.** The verified market cap uses the deck's $98.16 price for 2026-10-13, which I could not independently confirm. Today's $98.51 close (2026-10-15) comes from third-party sites, not an exchange feed.
- **Not verified:** the 2025-10-13 close of $80.01 and the 52-week high/low (which matched third-party sites but may be intraday).
- **Q3 FY26 growth (4.4%)** relies on the Q3 FY25 revenue base of about $1,177.5MM from model knowledge.
- **Peer data (MSFT, GOOGL, CSCO) was not verified.** I only checked that the medians and multiples recompute. RNG market cap roughly matches a third-party quote (about $6.3–6.7B).
- **Net cash.** I kept "no debt", per the 10-Q (no borrowings line). Noncurrent debt securities of $4MM held within strategic investments are excluded.
- **Category mapping.** The brief allows only four categories, so formatting and sourcing issues are categorized as "internal".
- **Severity** follows the skill's Critical / Important / Minor scale. No edits were made to the deck; this was a review-only pass.

### 4. Freshness
- Latest market price used: ZM $98.51 close on 2026-10-15 (deck price $98.16 on 2026-10-13).
- Latest financial reporting period: Q2 FY27, quarter ended 2026-07-31 (8-K filed 2026-08-25; 10-Q share count as of 2026-08-14).

---

## Run log
| Tool | Calls | Notes |
|---|---|---|
| Bash | 9 | Read rules/prompt; date ×2; pptx extraction; extract_numbers.py ×2; LibreOffice render + grid; theme fonts; calculations |
| Skill | 1 | financial-analysis:ib-check-deck |
| Read | 1 | Rendered slide grid image |
| WebSearch | 5 | ZM Q2 FY27 results; ZM price/market cap; ZM Q4 FY26 results; ZM 10-Q shares; RNG market cap |
| WebFetch | 7 | SEC 8-K Q2 FY27; SEC 8-K Q4 FY26; SEC 10-Q Q2 FY27; equibles ZM; digrin ZM; chartrow ZM; equibles RNG |
| Write | 1 | transcript.md |
| ToolSearch | 0 | none |

Stock-data tools: not loaded or called.

Files delivered:
- /home/claude/results/2026-10-13/runs/FA-09/A/transcript.md

Working files (in _work/):
- deck_content.md
- script_out.json
- Project_Horizon.pdf
- slide PNGs
- grid.png
