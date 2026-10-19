# Transcript: FA-09 / Arm B

- Start: 2026-10-16 03:25:12 UTC (`date -u`)
- End: 2026-10-16 03:27:03 UTC (`date -u`)

---

## Final reply to user

# Deck Check Report: Project Horizon (Zoom, ZM), 8 slides

**Bottom line: this deck is not ready for the client.** It has 11 critical issues. The main ones:

- **Wrong LTM revenue.** The deck shows $4,494MM. The 10-Q (filed 2026-08-26) gives $4,993.1MM.
- **Margins built on the wrong revenue.** Every margin that divides by revenue is too high as a result.
- **Overstated market cap and EV.** Market cap is overstated by about $7.1bn. EV is overstated by the same amount.

Once these are fixed, the slide 5 takeaway and the slide 6 valuation story both reverse.

I checked against SEC XBRL financials, the 10-Q for the quarter ended 2026-07-31 (filed 2026-08-26) and Yahoo Finance quotes and price history, with the latest close on 2026-10-15.

## Summary
- Total issues: 18
- Critical: 11 (number mismatches, factual errors, narrative contradicted by data)
- Important: 4 (stale data, language, unsupported superlatives, chart reference)
- Minor: 3 (units, date formats, chart month labels)

## Critical issues

### External accuracy (deck vs. filings and market data)
1. **LTM revenue is wrong** (Slides 2, 3, 5, 6)
   - The deck shows $4,494MM.
   - The four quarters ended 2026-07-31 sum to $4,993.1MM:
     - Q3 FY26: 1,229.8
     - Q4 FY26: 1,247.0
     - Q1 FY27: 1,239.0
     - Q2 FY27: 1,277.2
   - Gross profit ($3,860MM), EBIT ($1,185MM), EBITDA ($1,316MM), FCF ($1,926MM) and buybacks ($1,460MM) all tie to filings. Only revenue is wrong; $4,494MM looks like a keying error for $4,993MM.
2. **Every margin that divides by revenue is overstated** (Slides 2, 3, 5)

   | Margin | Deck | Correct |
   |---|---|---|
   | Gross margin | 85.9% | 77.3% |
   | EBIT margin | 26.4% | 23.7% |
   | EBITDA margin | 29.3% | 26.3% |
   | FCF margin | 42.9% | 38.6% |

3. **Market cap is overstated** (Slides 2, 4, 5)
   - The deck shows $35.8B ($35,802MM). That implies 364.7M shares at $98.16.
   - The 10-Q cover shows 291.8M shares outstanding as of 2026-08-14: 263.2M Class A plus 28.6M Class B.
   - Correct market cap is $28,641MM at the 2026-10-13 close of $98.16, or $28,744MM at the 2026-10-15 close of $98.51.
4. **EV and ZM multiples are overstated** (Slides 5, 6)
   - EV is $28,552MM in the deck. It should be $21,392MM at the 2026-10-13 close, or $21,494MM at 2026-10-15.
   - EV / LTM revenue should be 4.3x, not 6.4x.
   - EV / LTM EBIT should be 18.1x, not 24.1x.
5. **The 1-year return base price is wrong** (Slide 4)
   - The footnote says the 2025-10-13 close was $80.01. The actual close that day was $79.17; $80.01 was the 2025-10-17 close.
   - The correct 1-year return to 2026-10-13 is 24.0%.

### Internal number consistency
6. **The net cash table doesn't add up** (Slide 3)
   - Marketable securities are shown as 6,138. The filing shows 6,317.7, which looks like a transposition.
   - As shown, 932 + 6,138 = 7,070, not the 7,250 in the net cash line.
   - The 7,250 net cash figure itself is correct.
7. **EBITDA on slide 6 doesn't match slides 2 and 3** (Slide 6)
   - Slide 6 uses 1,361. Slides 2 and 3 use 1,316, which matches filings.
   - The EBITDA range should be 23,688 – 31,584, not 24,498 – 32,664. The chart bars need updating too.
8. **The 1-year return doesn't follow from the deck's own inputs** (Slide 4)
   - 98.16 / 80.01 − 1 = 22.7%, not the +27.2% shown.

### Data vs. narrative
9. **"Zoom's growth is accelerating" is not supported** (Slide 2)
   - Growth went from 5.5% in Q1 FY27 to 4.9% in Q2 FY27, which is a slowdown.
   - The title should say growth is stable at roughly 5%.
10. **The slide 5 takeaway is wrong** (Slide 5)
    - It says Zoom's "best-in-class margins support a premium to peer multiples". Zoom actually trades at a discount:
      - EV / revenue: 6.4x in the deck (4.3x verified) vs. an 8.4x peer median.
      - EV / EBIT: 24.1x in the deck (18.1x verified) vs. a 29.4x peer median.
    - The corrected EBIT margin of 23.7% is below the 28.7% peer median.
    - Only gross margin (77.3%) still leads the peer set.
11. **The valuation picture on slide 6 changes once inputs are fixed** (Slide 6)
    - With the correct revenue, the revenue range becomes 24,965 – 34,951.
    - The correct current EV (about 21,500) sits below the low end of all three ranges. In the deck it sits mid-range.
    - The commentary needs to be rewritten around that.

## Important issues
12. **Market data is two trading days old** (Slides 1, 2, 4, 5, 6)
    - Everything is as of 2026-10-13.
    - The 2026-10-15 close was $98.51 (+5.6% on the day), and peer caps moved 1–3%. Roll the date before sending.
13. **Typo and title case** (Slide 7)
    - "Potential Buyer Univrese" should be "Potential buyer universe". The other titles use sentence case.
14. **Informal phrasing and unsupported superlatives** (Slides 3, 5)
    - "Fortress balance sheet" should become "Net cash balance sheet with no funded debt".
    - "Best-in-class margins" is only true of gross margin. Say "Highest gross margin in the peer set".
15. **No current EV reference on the valuation chart** (Slide 6)
    - The football field doesn't mark current EV. Add a vertical line for it.

## Minor issues
16. **Units drift** between $MM (slides 2, 3, 5), $M (slide 6) and $B (slides 2, 4). Standardise on $MM.
17. **Date formats drift** across five styles:
    - "October 13, 2026"
    - "10/13/2025"
    - "13-Oct-2026"
    - "7/31/2026"
    - "2026-10-20"

    Pick one.
18. **Slide 4 chart month labels don't match the closes** (Slide 4)
    - Several points are weekly closes from the following month. For example, "Dec-25" ($83.32) is the 2026-01-02 close, and "Sep-26" ($92.88) is the 2026-10-02 close.
    - Either use month-end closes or relabel the points.

**Checked and found correct:**
- Peer medians.
- Peer multiples given their inputs.
- The FCF and revenue-multiple ranges on slide 6.
- Quarterly growth rates (4.4%, 5.3%, 5.5%, 4.9%).
- 52-week high and low ($114.74 and $70.70).
- The 2026-10-13 close of $98.16.
- No funded debt.
- Next-steps dates (all after today).

## Final checklist
- [ ] Numbers reconciled (items 1–8)
- [ ] Narrative matches data (9–11)
- [ ] Language meets IB standards (13–14)
- [ ] Charts sourced and referenced (15, 18)
- [ ] Formatting consistent (16–17)

## Comparison Block

### 1. Key figures
| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Slide 2 | Title "growth is accelerating" vs growth falling from 5.5% to 4.9% | narrative | Q1–Q2 FY27 | Deck; stock-data get_financials (XBRL) | H |
| Slides 2, 3, 5, 6 | LTM revenue 4,494 shown; filings give 4,993.1 | external | LTM to 2026-07-31 | 10-Q filed 2026-08-26; get_financials | H |
| Slides 2, 3, 5 | Margins overstated: gross 85.9→77.3%, EBIT 26.4→23.7%, EBITDA 29.3→26.3%, FCF 42.9→38.6% | external | LTM to 2026-07-31 | get_financials (calc) | H |
| Slides 2, 4, 5 | Market cap $35.8B (implies 364.7M shares) vs 28,641 (291.8M shares) | external | 2026-10-13 | 10-Q cover (filed 2026-08-26); get_price_history | H |
| Slides 5, 6 | ZM EV 28,552 vs 21,392; EV/rev 6.4x→4.3x; EV/EBIT 24.1x→18.1x | external | 2026-10-13 | Calc from verified inputs | H |
| Slide 4 | 2025-10-13 close shown as $80.01; actual $79.17, so 1Y return 24.0% | external | 2025-10-13 | get_price_history | H |
| Slide 3 | Marketable securities 6,138 (filed 6,317.7); table does not foot to 7,250 | internal | 2026-07-31 | Deck; 10-Q filed 2026-08-26 | H |
| Slide 6 | LTM EBITDA 1,361 vs 1,316 on slides 2–3; range should be 23,688–31,584 | internal | LTM to 2026-07-31 | Deck | H |
| Slide 4 | +27.2% 1Y return does not match the deck's own inputs (22.7%) | internal | 2026-10-13 | Deck | H |
| Slide 5 | Takeaway claims a premium to peer multiples, but ZM trades at a discount and EBIT margin is below median | narrative | 2026-10-13 | Deck; calc | H |
| Slide 6 | Corrected revenue range 24,965–34,951; current EV ~21,500 falls below all ranges, so commentary must change | narrative | 2026-10-15 | Calc | H |
| Slides 1, 2, 4, 5, 6 | Market data dated 2026-10-13; latest close 2026-10-15 $98.51 (+5.6%) | external | 2026-10-15 | get_quote | H |
| Slide 7 | Typo "Univrese" and title case inconsistent with other titles | language | N/A | Deck | H |
| Slides 3, 5 | "Fortress balance sheet" and unsupported "best-in-class" | language | N/A | Deck | H |
| Slide 6 | No current EV marker on valuation chart | internal | N/A | Deck render | M |
| Slides 2, 4, 6 | Units drift ($MM / $M / $B) | internal | N/A | Deck | H |
| Slides 1–8 | Five different date formats | internal | N/A | Deck | H |
| Slide 4 | Chart month labels map to closes from the following month (e.g. Dec-25 = 2026-01-02) | internal | N/A | get_price_history | M |
| ZM market cap: deck | 35,802 | USD millions | 2026-10-13 | Deck slide 5 | H |
| ZM market cap: verified | 28,744 (28,641 at the 2026-10-13 close) | USD millions | 2026-10-15 | get_quote (Yahoo); 291.8M shares from 10-Q filed 2026-08-26 | H |
| ZM LTM revenue: deck | 4,494 | USD millions | LTM to 2026-07-31 | Deck slides 2, 3, 5, 6 | H |
| ZM LTM revenue: verified | 4,993.1 | USD millions | LTM to 2026-07-31 | stock-data get_financials (XBRL); 10-Q filed 2026-08-26 | H |
| Total issues by category | 18 total: internal 7, external 6, narrative 3, language 2 | count | N/A | This review | H |

### 2. Sources used
- Skill financial-analysis:ib-check-deck: 1 load (extract_numbers.py run 2 times)
- stock-data get_quote (Yahoo Finance): 5 (ZM, MSFT, GOOGL, CSCO, RNG)
- stock-data get_financials (SEC XBRL): 3 (ZM income, balance and cash flow, quarterly)
- stock-data get_filings (EDGAR): 2
- stock-data get_price_history (Yahoo): 1 (ZM 2y daily)
- WebFetch on sec.gov, ZM 10-Q for 2026-07-31: 1
- ToolSearch: 1
- LibreOffice/pdftoppm render plus python-pptx extraction (local Bash): 6 Bash calls

### 3. Estimates and gaps
- I treated "today" as the 2026-10-15 close ($98.51), the latest close available. I also show 2026-10-13 figures so they match the deck's as-of date.
- Market cap uses basic shares outstanding from the 10-Q cover (291.8M as of 2026-08-14). Buybacks since then are not reflected, and I did not compute a treasury-method diluted count. Yahoo's $28,744MM matches the basic-share figure.
- EV = market cap − (cash + short-term marketable securities). The deck says no debt and XBRL reports none. I did not check the full balance sheet for long-term marketable securities or leases; the 10-Q read covered only the first 100k characters.
- Q4 FY26 and FY27 Q2 cash-flow figures are derived by subtraction (FY − 9M, or YTD differences) in the XBRL tool.
- EBITDA = GAAP operating income + D&A, matching the deck's definition. I did not adjust for SBC.
- I did not re-verify peer LTM financials (revenue, margins). I only checked that peer market caps are within 1–5% of 2026-10-15 quotes, and that the peer multiples and medians are internally consistent. Peer EV inputs (debt and cash) were not verified.
- Severity classification and the category labels for formatting items ("internal") are my own defaults.
- The deck was received as a .pptx. I did not edit it; this skill only reads and reports.

### 4. Freshness
- Latest market price used: 2026-10-15 close (ZM $98.51), fetched 2026-10-16 03:26 UTC.
- Latest financial reporting period used: Q2 FY27, quarter ended 2026-07-31 (10-Q filed 2026-08-26).

---

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 7 | date (start), extract plus number-check script, script summary plus render, montage, compute metrics, date (end); 1 initial read of rules/prompt |
| Skill | 1 | financial-analysis:ib-check-deck |
| Read | 1 | slide montage image |
| ToolSearch | 1 | `select:mcp__remote-devices__stock-data__get_quote,get_financials,get_filings,get_price_history` |
| mcp__remote-devices__stock-data__get_quote | 5 | ZM, MSFT, GOOGL, CSCO, RNG |
| mcp__remote-devices__stock-data__get_financials | 3 | ZM income, balance, cashflow (quarterly) |
| mcp__remote-devices__stock-data__get_filings | 2 | ZM all filings; ZM 10-Q |
| mcp__remote-devices__stock-data__get_price_history | 1 | ZM 2y daily |
| WebFetch | 1 | ZM 10-Q (zm-20260731.htm) on sec.gov |
| Write | 1 | this transcript |

Files delivered:
- /home/claude/results/2026-10-13/runs/FA-09/B/transcript.md
- Working files in /home/claude/results/2026-10-13/runs/FA-09/B/_work/ (deck_content.md, deck.pdf, slide PNGs, montage.png)
