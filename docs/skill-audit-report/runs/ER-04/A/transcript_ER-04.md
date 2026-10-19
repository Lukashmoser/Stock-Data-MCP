# Transcript: ER-04 (Arm A)

- **Start:** Wed Oct 14 07:49:08 UTC 2026
- **End:** Wed Oct 14 07:56:56 UTC 2026

## User message

/initiate AMD. Start with Task 1 (company research) for AMD. Run Task 1 only and deliver its output document. (Full text: prompts/ER-04.txt)

## Final reply to user

I've finished Task 1 (company research) for AMD. The research document is about 7,800 words, not counting tables and source URLs. It covers the overview, history, four management bios, products, customers and go-to-market, industry, eight competitors, TAM, and 15 risks across four categories.

**Deliverable:** `/home/claude/results/2026-10-13/runs/ER-04/A/AMD_Research_Document_2026-10-14.md`

**Key points:**
- **Revenue is growing fast.** FY2025 revenue was USD 34,639m, up 34.3%. In the latest quarter (Q2 FY2026, ended 2026-06-27) revenue was USD 11,536m, up 50.1% year over year. Data Center made up USD 6,718m of that, up 107%.
- **The next leg depends on AI racks.** The H2 2026 ramp of MI450/Helios is the main swing factor. OpenAI has committed to 6 GW, starting with 1 GW of MI450 in H2 2026, and Anthropic to up to 2 GW. Q3 FY2026 guidance is about USD 13,000m.
- **The balance sheet is strong.** Cash and short-term investments were USD 13,111m against USD 3,226m of debt.
- **Valuation is demanding.** At USD 605.53 per share, the market cap of about USD 988.5bn is roughly 28.5x FY2025 sales.
- **Main risks:**
  - delivering the first rack-scale systems on time;
  - reliance on a few very large customers;
  - competition from Nvidia and from hyperscalers' own chips;
  - US export controls on China;
  - dependence on TSMC;
  - dilution from stock-based pay and the OpenAI warrant.

I could only partly check some background facts this session. The pre-2025 history, executive biographies, competitor sizes and market-share and TAM splits come from memory, and the document marks them that way. Task 2 (financial model) is the natural next step whenever you want it.

## Comparison Block

### 1. Key figures

| Metric | Value | Units | Period or as-of date | Source | Confidence (H/M/L) |
|---|---|---|---|---|---|
| Latest 10-K filing date and fiscal year | 2026-02-04; FY2025 (ended 2025-12-27) | date / FY | Filed 2026-02-04 | ir.amd.com/financial-information/sec-filings (10-K filter); last10k.com (accession 0000002488-26-000018); sec.gov R1.htm | H |
| Latest 10-Q filing date and quarter | 2026-08-05; Q2 FY2026 (ended 2026-06-27) | date / quarter | Filed 2026-08-05 | ir.amd.com/financial-information/sec-filings (10-Q filter); last10k.com (accession 0000002488-26-000123) | H |
| Revenue FY2025 | 34,639 | USD m | FY2025 | Q4/FY2025 earnings release, ir.amd.com/news-events/press-releases/detail/1276/ (8-K 2026-02-03) | H |
| Revenue FY2024 | 25,785 | USD m | FY2024 | Q4/FY2025 earnings release (ir.amd.com …/1276/) | H |
| Revenue FY2023 | 22,680 | USD m | FY2023 | model knowledge | M |
| Revenue growth FY2025 | 34.3 | % | FY2025 vs FY2024 | Calculated from earnings release | H |
| Revenue growth FY2024 | 13.7 | % | FY2024 vs FY2023 | Calculated (FY2023 base from model knowledge) | M |
| Revenue growth FY2023 | -3.9 | % | FY2023 vs FY2022 (23,601) | model knowledge | M |
| Latest-quarter revenue | 11,536 | USD m | Q2 FY2026 (ended 2026-06-27) | Q2 FY2026 earnings release, ir.amd.com/news-events/press-releases/detail/1295/ | H |
| Latest-quarter revenue YoY growth | 50.1 | % | Q2 FY2026 vs Q2 FY2025 (7,685) | Q2 FY2026 earnings release (calculated; release says 50%) | H |
| Latest-quarter Data Center segment revenue | 6,718 | USD m | Q2 FY2026 | Q2 FY2026 earnings release | H |
| GAAP operating margin last FY | 10.7 | % | FY2025 (3,694 / 34,639) | Q4/FY2025 earnings release (calculated) | H |
| Free cash flow last FY | 5,519 | USD m | FY2025 | Q4/FY2025 earnings release (company non-GAAP FCF) | H |
| Stock-based compensation last FY | 1,638 | USD m | FY2025 | Q4/FY2025 earnings release | H |
| Current price | 605.53 | USD per share | 2026-10-13 close | https://stockevents.app/en/stock/AMD (cross-check robinhood.com: 608.10) | M |
| Market cap | 988,510 | USD m | 2026-10-13 | https://stockevents.app/en/stock/AMD | M |
| Cash + short-term investments | 13,111 | USD m | 2026-06-27 | Q2 FY2026 earnings release | H |
| Total debt | 3,226 | USD m | 2026-06-27 | Q2 FY2026 earnings release (875 current + 2,351 long-term) | H |

### 2. Sources used

| Tool / connector / website | Calls |
|---|---|
| Skill (equity-research:initiate, equity-research:initiating-coverage) | 2 |
| WebSearch | 9 |
| WebFetch (total) | 18 (2 failed: sec.gov EDGAR browse blocked by robots; investsmart.com.au error) |
| ir.amd.com (press releases 1295 x2, 1276, 1266, 1260; SEC filings pages x3) | 8 (via WebFetch) |
| sec.gov (R1.htm) | 1 (via WebFetch) |
| last10k.com | 2 (via WebFetch) |
| stockevents.app | 1 (via WebFetch) |
| robinhood.com | 1 (via WebFetch) |
| marketscreener.com | 1 (via WebFetch) |
| vectorshift.ai | 1 (via WebFetch) |
| overclockers.ru | 1 (via WebFetch) |
| Bash (incl. curl to data.sec.gov, blocked by proxy 403) | 7 |
| Write | 2 |

### 3. Estimates and gaps

- FY2023 revenue (22,680) and FY2022 revenue (23,601), and therefore FY2023 growth (-3.9%) and FY2024 growth's base, come from model knowledge. I did not re-verify them against a filing this session.
- I could not read the 10-K or 10-Q full text directly: data.sec.gov was blocked by the proxy and sec.gov EDGAR browse was blocked by robots. Figures come from AMD's earnings releases (8-K exhibits), which match the filed financial statements.
- The 10-K filing date is 2026-02-04 per the AMD IR SEC-filings index. last10k shows it submitted 2026-02-03 and accepted 2026-02-04. Similarly, the 10-Q is 2026-08-05 (submitted 2026-08-04). I used the AMD IR index dates.
- Free cash flow is AMD's own non-GAAP definition: operating cash flow from continuing operations of 6,493 minus capex.
- Current price: the stockevents.app quote is labeled "Tuesday 20:00", which I interpreted as the 2026-10-13 close. Robinhood showed 608.10 (session/time unclear). Market cap is as reported by stockevents. My own calculation (605.53 × 1,630.4m shares at 2026-01-30) gives about 987,256.
- Total debt is the carrying value (current portion plus long-term debt), excluding operating leases.
- Executive bios (education, prior roles), board roles, insider ownership, history before 2025, competitor scales, market shares and TAM splits come from model knowledge or third-party aggregators. The FY2026 DEF 14A was not read. Forrest Norrod's current status was confirmed only via a third-party page updated 2026-08-03.
- I did not extract the 10%-customer concentration disclosure.
- The Q3 FY2026 quarter-end date (2026-09-26) is estimated from AMD's fiscal calendar.
- Defaults: Task 1 only; markdown deliverable named per the skill convention; four executives profiled (CEO, CFO, CTO, Data Center GM); no extra files.

### 4. Freshness

- Latest market price: 2026-10-13 (close).
- Latest financial reporting period: Q2 FY2026, quarter ended 2026-06-27 (10-Q filed 2026-08-05).

## Run log

| Tool | Calls | Notes |
|---|---|---|
| Bash | 7 | read rules/list dirs; date+read prompt; curl data.sec.gov (403); read task1 reference; date; wc; date |
| Skill | 2 | equity-research:initiate; equity-research:initiating-coverage |
| WebSearch | 9 | Q2 2026 results; Q4/FY2025 results; 10-Q; 10-K; price; exec changes; Norrod; Analyst Day; OpenAI deal |
| WebFetch | 18 | 2 failed (sec.gov browse robots; investsmart) |
| Write | 2 | research document; this transcript |
| ToolSearch | 0 | none |

**Files delivered:**
- /home/claude/results/2026-10-13/runs/ER-04/A/AMD_Research_Document_2026-10-14.md
- /home/claude/results/2026-10-13/runs/ER-04/A/transcript_ER-04.md
