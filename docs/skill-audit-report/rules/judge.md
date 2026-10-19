# Judge instructions

You score paired runs (arm A = stock-data MCP off, arm B = on) of the same test against reference data. Use only the files listed here. Do not call any data, web or stock-data tool: use Read, Bash (to read files and compute), Grep, Glob and Write only.

**Inputs**
- Protocol, sections 7.1 (tolerances) and 7.2 (rubric): /mnt/user-data/uploads/skill-comparison-prompts.md
- Prompts: /home/claude/results/2026-10-13/prompts/<ID>.txt
- Transcripts: /home/claude/results/2026-10-13/runs/<ID>/A/transcript*.md and .../B/transcript*.md (ER-04 to ER-06 are transcript_ER-04/05/06.md in runs/ER-04/A and B). Each ends with a Comparison Block and a Run log. You may open deliverable files in the run folders to check figures.
- Reference data in /home/claude/results/2026-10-13/reference/:
  - R0.html: full snapshot at the 2026-10-13 close (quotes, MSFT 5y statements, peer annuals, quarterly NVDA/AMZN/GOOGL, balance sheets, filings, 1y returns, macro). Applies to ER-01, ER-02, ER-03, ER-08, ER-09, ER-04/05/06, ER-07, ER-10, ER-11, FA-02.
  - R0b_2026-10-14.md: prices/rates at the 2026-10-14 close. Applies to FA-01, FA-03, FA-04, FA-05.
  - R0c_2026-10-15.md: prices/rates at the 2026-10-15 close, plus a known MCP bug (get_quote prev_close and change % were wrong on 10-15). Applies to FA-06 to FA-13.
  - Financial statements in R0 apply to every test.
- Fixture answer keys: /home/claude/results/2026-10-13/keys_for_judges/ (F1 → FA-05, F2 → FA-07, F3 → FA-08, F4 → FA-09, F7 → ER-07).

**Rules**
- Where R0 has no value for a figure (consensus, segments, guidance, earnings dates, valuation outputs), mark it "unverifiable"; don't use your own memory as a reference. For the fixture tests also score key hit rates. FA-05: data errors D1–D3 and formula errors M1–M4 separately. FA-07: unit and wrong-value catches separately from formatting fixes. FA-08: new values correct and old instances missed. FA-09: X1–X2 (external) separately from I/N/L.
- A figure counts as Fabrication only when it is marked High confidence and is outside tolerance against a reference value.
- Freshness: compare the latest period and price date used against what was available on the run date in the transcript.
- Note per test whether arm B called stock-data tools (from its Run log), and anything in the transcript showing arm A used them.
- Valuation outputs (target, WACC, IRR, DCF value) are not scored for accuracy; note the spread between arms.

**Output**
Write one file per test to /home/claude/results/2026-10-13/scores/<ID>.md (ER-04, ER-05 and ER-06 each get their own file) containing:
1. A table: Metric | Reference | A value | A ok? | B value | B ok? | Note (verifiable rows; summarise unverifiable rows in one line).
2. Per arm: accuracy % over verifiable rows, stale periods used, count of "model knowledge" sources, wrong figures marked High.
3. A score line exactly like: `SCORES | <ID> | A acc,fresh,src,compl,fab = x,x,x,x,x | B ... = x,x,x,x,x | MCP invoked: yes/no | key hits: <text or n/a>`
4. One paragraph on the most important difference.
Finally reply with only the SCORES lines and a one-line note per test.
