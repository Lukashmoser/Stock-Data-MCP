# Scorecard (results/2026-10-13)

Scores 0–2 per dimension, max 10 per arm. Two rows adjusted from the judge's scores where the reference was wrong (noted). Judge scores are in scores/scorecard.json.

| ID | Skill | A acc | B acc | A fresh | B fresh | A src | B src | A compl | B compl | A fab | B fab | A total | B total | Δ (B−A) | MCP invoked? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | catalyst-calendar | 0 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 7 | 10 | +3 | yes |  Reference correction: R0's quote listed AAPL's 52-week high as 345.34 while showing a 348.15 day high the same day, and Yahoo rolled GOOGL's 52-week window minutes later. B's 348.15 and 244.15 were right at fetch time. |
| ER-02 | earnings-preview | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 9 | 10 | +1 | yes |   |
| ER-03 | earnings-analysis | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| ER-04 | initiating-coverage T1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 9 | 10 | +1 | yes |  Reference correction: R0's AMD FCF (6,735) is OCF minus capex including discontinued operations; both arms' 5,519 is AMD's reported figure. Counted as correct. |
| ER-05 | initiating-coverage T2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| ER-06 | initiating-coverage T3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| ER-07 | model-update | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 9 | 10 | +1 | yes | A 6/6 actuals + 6/6 prior estimates + filing date (cited 8-K, not 10-K) + old TP; B 6/6 actuals + 6/6 prior estimates + filing date (10-K) + old TP  |
| ER-08 | morning-note | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| ER-09 | idea-generation | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| ER-10 | sector-overview | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 7 | 10 | +3 | yes |   |
| ER-11 | thesis-tracker | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| FA-01 | 3-statement-model | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes | n/a (F6 is a blank template; both pass balance and cash checks)  |
| FA-02 | competitive-analysis | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 7 | 10 | +3 | yes |   |
| FA-03 | comps-analysis | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| FA-04 | dcf-model | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| FA-05 | audit-xls | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 7 | 9 | +2 | yes | A 3/3 data + 4/4 formula; B 3/3 data + 4/4 formula  |
| FA-06 | lbo-model | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 9 | 10 | +1 | yes |   |
| FA-07 | clean-data-xls | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 8 | 10 | +2 | yes | formatting (control) A 4/4 + B 4/4 (dupes 3+1, dates 70/70, text→number 32/32, tickers 81/81, notes flagged mixed-type); unit errors A 6/6 rows (5/6 values exact) vs B 6/6 rows (6/6 exact); wrong values A 2/2 vs B 2/2; false positives A 2 vs B 0  |
| FA-08 | deck-refresh | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes | old instances replaced A all (0 missed) vs B all (0 missed); new values correct A 12/12 + all derived vs B 12/12 + all derived; chart extended A yes but FY2026 bar clipped at axis max 320 vs B yes with axis rescaled to 400  |
| FA-09 | ib-check-deck | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 10 | 8 | -2 | yes | X (external) A 2/2 vs B 2/2; I/N/L A 8/8 vs B 8/8; extras: B valid catch of the mislabelled 1-year base date ($80.01 is the week-of-10-13 weekly close, not the 10-13 close; consistent with the key, no fixture error in the answer key), B wrong +5.6% 1-day move (MCP bug); A low-confidence month-end false positive  |
| FA-10 | ppt-template-creator (control) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | no | n/a (control; 6/6 template facts both arms)  |
| FA-11 | pptx-author | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| FA-12 | xlsx-author | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | 10 | +0 | yes |   |
| FA-13 | skill-creator | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 9 | 10 | +1 | yes | follow-up correct-without-edits: A no (raw paste gives a silent all-n/a price table; correct only after the reshape its reference doc prescribes) vs B no but nearly (all numbers right, one wrong cell: META latest filing n/a); B is closer  |
