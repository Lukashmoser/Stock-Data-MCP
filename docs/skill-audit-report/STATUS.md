# Skill comparison run: status

Last updated 2026-10-18 PT. COMPLETE: all tests run, scored and published (results.html, scorecard.md, scores/).

## Completed (both arms, transcript with Comparison Block saved)

| Test | Skill | Run window (UTC) | Prices used | Arm B used stock-data? |
|---|---|---|---|---|
| ER-01 | catalyst-calendar | 10-14 04:04–04:08 | 10-13 close | Yes |
| ER-02 | earnings-preview | 10-14 04:04–04:07 | 10-13 close | Yes |
| ER-03 | earnings-analysis | 10-14 04:04–04:12 | 10-13 close | Yes |
| ER-04/05/06 | initiating-coverage T1–T3 (one session per arm) | 10-14 07:49–08:18 | 10-13 close | Yes |
| ER-07 | model-update (F7) | 10-14 07:49–07:53 | 10-13 close (A used 10-12 close) | Yes |
| ER-08 | morning-note | 10-14 04:04–04:08 | 10-13 close | Yes |
| ER-09 | idea-generation | 10-14 04:04–04:09 | 10-13 close | Yes |
| ER-10 | sector-overview | 10-14 08:20–08:26 | 10-13 close | Yes |
| ER-11 | thesis-tracker | 10-14 08:20–08:24 | 10-13 close | Yes |
| FA-01 | 3-statement-model (F6) | 10-15 01:58–02:04 | 10-14 close | Yes |
| FA-02 | competitive-analysis | 10-14 08:28–08:33 | A: META 09-25 cached, RDDT 10-12; B: 10-13 | Yes |
| FA-03 | comps-analysis | 10-15 01:58–02:05 | 10-14 close | Yes |
| FA-04 | dcf-model | 10-15 02:05–02:12 | 10-14 close | Yes |
| FA-05 | audit-xls (F1) | 10-15 02:05–02:07 | 10-14 close | Yes |

## Update 2026-10-15 20:45 PT: all 24 tests complete in both arms

FA-06 to FA-13 ran 2026-10-16 03:19–03:38 UTC on the 2026-10-15 close. Score them against `reference/R0c_2026-10-15.md`. Arm B used the stock-data tools in every test except FA-10 (the control, where neither arm used them, as expected).

New findings to carry into scoring:
- **MCP bug:** on 2026-10-15, get_quote returned a wrong prev_close, so change and change_pct were wrong (QQQ showed +0.82% on a −0.13% day). Details are in R0c.
- **Possible fixture error:** FA-09 arm B says Project_Horizon.pptx uses a 2025-10-13 ZM close of $80.01, against $79.17 in price history. Check F4_key.md before scoring I3.
- **FA-07 arm A:** "corrected" two values that were only 1-unit rounding differences (GOOGL Q4-25 revenue, META Q4-24 operating income). Treat these as false positives.

## Remaining

1. **FA-13 follow-up:** install each arm's generated skill and run "Run weekly-watchlist-review for AAPL, NVDA, META" in arm B. Write the results to runs/FA-13/followup_A and followup_B. The first attempt was cancelled; its partial folders are in `_partial/`.
2. **Scoring with judge agents**, following `rules/judge.md`. They write `scores/<ID>.md`. Run them in groups of 4 or fewer:
   - J1: ER-01, 02, 03, 08, 09
   - J2: ER-04, 05, 06, 07, 10, 11
   - J3: FA-01 to FA-06
   - J4: FA-07 to FA-13 (after the follow-up)

   The first judge run was cancelled. Its partial ER-01 to ER-05 score files are in `_partial/scores_cancelled/`; rerun them rather than reuse them.
3. **Assemble** the scorecard (protocol section 7.3) and publish the results page.

The agent prompts used are in rules/judge.md and in the follow-up prompt text recorded in this file's history. Follow-up prompt: "You are testing a skill someone wrote. The skill lives at runs/FA-13/<A|B>/weekly-watchlist-review/ ... user says 'Run weekly-watchlist-review for AAPL, NVDA, META' ... follow the skill as written, don't edit it, stock-data tools available, save to runs/FA-13/followup_<A|B>/, write result.md with the table, summary, deviations and a tool log."

## Reference data

- R0 (full, 2026-10-13 close): published artifact "R0 Reference Snapshot"; source `scratchpad/r0/R0.html`.
- R0c (prices and rates, 2026-10-15 close, plus the prev_close bug): `reference/R0c_2026-10-15.md`. Applies to FA-06 to FA-13.
- R0b (prices and rates, 2026-10-14 close): `scratchpad/r0/R0b_2026-10-14.md`. Applies to FA-01 and FA-03 onward. Copy in this bundle at `reference/`.
- Fixture answer keys F1, F2, F3, F4, F7: `scratchpad/keys/` (kept outside the results folder so test agents can't find them). Copies in this bundle at `keys/`.

## Deviations from the protocol (record in the scorecard)

- Runs used separate agents, not separate chats. Arm A was told the stock-data tools were switched off rather than having them removed, so arm A knew the tools existed.
- Canned replies C1–C3 were given up front in the session rules, since agents can't pause for input.
- ER-10 arm A accidentally ran a build script that arm B had left in the shared scratchpad. It then rebuilt its outputs from its own data, but treat ER-10 A as possibly contaminated. After this, all agents were told to keep scratch files in their own `_work/` folder.
- FA-01 and FA-03 onward ran a day later than the rest (10-14 close instead of 10-13), and 10-14 was a down day (MSFT −1.8%, ORCL −8.8%, ZM −3.8%). Score those against R0b.
- Several arm B runs hit transient device-bridge disconnects on their first stock-data calls and retried successfully.
- FA-01 was interrupted once by the usage limit, then rerun cleanly from the untouched template.
