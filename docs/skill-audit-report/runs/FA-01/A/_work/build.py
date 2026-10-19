import openpyxl
from openpyxl.styles import Font
from copy import copy

RUN = '/home/claude/results/2026-10-13/runs/FA-01/A/'
wb = openpyxl.load_workbook(RUN + '3S_template.xlsx')
A, IS, BS, CF, SC, CK, CV = (wb[n] for n in ['Assumptions', 'IS', 'BS', 'CFS', 'Schedules', 'Checks', 'Cover'])

HC = list('BCDE')      # FY2023A..FY2026A
PC = list('FGHIJ')     # FY2027E..FY2031E
ALL = HC + PC
LABELS = ['FY2023A', 'FY2024A', 'FY2025A', 'FY2026A', 'FY2027E', 'FY2028E', 'FY2029E', 'FY2030E', 'FY2031E']

BLUE = Font(color='0000FF'); BLACK = Font(color='000000'); GREEN = Font(color='008000')
NUM = '#,##0;(#,##0);"-"'; PCT = '0.0%'; EPS = '0.00'; DAYS = '0.0'


def prev(c):
    return chr(ord(c) - 1)


def put(ws, ref, val, fmt=NUM):
    cell = ws[ref]
    cell.value = val
    if isinstance(val, str) and val.startswith('='):
        cross = '!' in val
        cell.font = GREEN if cross else BLACK
    else:
        cell.font = BLUE
    cell.number_format = fmt


def puthist(ws, row, vals, fmt=NUM):
    for c, v in zip(HC, vals):
        put(ws, f'{c}{row}', v, fmt)


for ws in [A, IS, BS, CF, SC, CK]:
    ws['A2'] = 'Units: USD millions unless stated (shares in millions; per-share in USD)'
    for c, l in zip(ALL, LABELS):
        ws[f'{c}4'] = l
    ws['A3'] = 'Fiscal years end June 30. FY2023A-FY2026A as reported in Microsoft Form 10-K; FY2027E-FY2031E projected.'

# ---------------- Cover ----------------
cover = {
    'B3': 'Microsoft Corporation', 'B4': 'MSFT', 'B5': 'June 30', 'B6': 'USD millions (per-share in USD)',
    'B7': '2026-10-14', 'B8': 'Claude (3-statement-model skill)',
    'B9': 'Microsoft Form 10-K FY2026 (period 2026-06-30; FY2026 and FY2025 columns), FY2025 10-K (FY2024), FY2024 10-K (FY2023), '
          'statements as reproduced in Microsoft FY2026/FY2025/FY2024 Q4 earnings releases (microsoft.com/investor)',
}
for k, v in cover.items():
    CV[k] = v
CV['A17'] = 'Model notes'
notes = [
    'Microsoft does not report D&A on the face of the income statement. Historical D&A = cash-flow line "Depreciation, amortization, and other"; cost of revenue is shown excluding that amount (all D&A assumed to sit in cost of revenue), so operating income equals the reported figure.',
    'Microsoft reports interest income and interest expense net within "Other income (expense), net"; historical interest lines are left at zero and the full reported net amount is in Other income.',
    'Other long-term assets = operating lease ROU assets + equity and other investments + other long-term assets. Accrued & other current liabilities = accrued compensation + short-term income taxes + short-term unearned revenue + other current liabilities. Deferred taxes & other LT liabilities = LT income taxes + LT unearned revenue + deferred income taxes + operating lease liabilities + other LT liabilities.',
    'Microsoft retires repurchased shares (no treasury stock). Projected buybacks and dividends are charged to retained earnings.',
    'Projected interest income is earned on beginning-of-year cash + short-term investments to avoid a circular reference.',
    'Short-term investments act as the liquidity buffer: they are sold only if cash would fall below the minimum cash balance.',
]
for i, n in enumerate(notes):
    CV[f'A{18 + i}'] = n

# ---------------- Historical inputs ----------------
# Income statement
puthist(IS, 6, [211915, 245122, 281724, 331839])
IS['A7'] = 'Cost of revenue (excl. D&A)'
IS['A13'] = 'Depreciation & amortization (hist.: incl. "other" per CFS)'
IS['A37'] = 'Memo: cost of revenue as reported (incl. D&A)'
IS['A38'] = 'Memo: FY2022 revenue (for FY2023 growth)'
puthist(IS, 37, [65863, 74114, 87831, 106374])
put(IS, 'B38', 198270)
puthist(IS, 9, ['=22759+7575', '=24456+7609', '=25654+7223', '=26710+7956'])
puthist(IS, 10, [27195, 29510, 32488, 35562])
puthist(IS, 11, [0, 0, 0, 0])
puthist(IS, 15, [0, 0, 0, 0])
puthist(IS, 16, [0, 0, 0, 0])
puthist(IS, 17, [788, -1646, -4901, 10697])
puthist(IS, 19, [16950, 19651, 21795, 32185])
puthist(IS, 23, [7446, 7431, 7433, 7429])
puthist(IS, 24, [7472, 7469, 7465, 7453])
puthist(IS, 27, [2.72, 3.00, 3.32, 3.64], EPS)

# Balance sheet
puthist(BS, 7, [34704, 18315, 30242, 20935])
puthist(BS, 8, [76558, 57228, 64323, 55908])
puthist(BS, 9, [48688, 56924, 69905, 80876])
puthist(BS, 10, [2500, 1246, 938, 1397])
puthist(BS, 11, [21807, 26021, 25723, 48594])
puthist(BS, 13, [95641, 135591, 204966, 313076])
puthist(BS, 14, [67886, 119220, 119509, 119651])
puthist(BS, 15, [9366, 27597, 22604, 18609])
puthist(BS, 16, ['=14346+9879+30601', '=18961+14600+36460', '=24823+15405+40565', '=24177+36348+38805'])
puthist(BS, 20, [18095, 21996, 27724, 42416])
puthist(BS, 21, ['=11009+4152+50901+14745', '=12564+5017+57582+19185', '=13709+7211+64555+25020', '=14945+2534+72965+26738'])
puthist(BS, 22, ['=0+5247', '=6693+2249', '=0+2999', '=0+9227'])
puthist(BS, 24, [41990, 42688, 40152, 31067])
puthist(BS, 25, ['=25560+2912+433+12728+17981', '=27931+2602+2618+15497+27064',
                 '=25986+2710+2835+17437+45186', '=28647+2747+3054+16532+65117'])
puthist(BS, 29, [93718, 100923, 109095, 117406])
puthist(BS, 30, [118848, 173144, 237731, 328265])
puthist(BS, 31, [-6343, -5590, -3347, -3284])
puthist(BS, 32, [0, 0, 0, 0])

# Cash flow statement
puthist(CF, 8, [13861, 22287, 29433, 38534])
puthist(CF, 9, [9611, 10734, 11974, 12405])
puthist(CF, 10, [-6059, -4738, -7056, 14189])
puthist(CF, 11, [-4087, -7191, -10581, -12737])
puthist(CF, 12, [1242, 1284, 309, -461])
puthist(CF, 13, [-1991, -1648, -3044, -2627])
puthist(CF, 14, [-2721, 3545, 569, 5268])
puthist(CF, 15, ['=5535+2272', '=5348+4867', '=5438+5922', '=9361+6847'])
puthist(CF, 16, ['=196-2833-358+553', '=305-6817+1687+749', '=5329-2950-38-975', '=-11047-3964-1875-4707'])
puthist(CF, 20, [-28107, -44477, -64551, -115948])
puthist(CF, 21, [-1670, -69132, -5978, -1743])
puthist(CF, 22, ['=-37651+33510+14354', '=-17732+24775+10894', '=-29775+16079+9309', '=-58351+34605+21798'])
puthist(CF, 23, [-3116, -1298, 2317, -19861])
puthist(CF, 27, [0, '=24395+5250', 0, 0])
puthist(CF, 28, [-2750, -29070, '=-3216-5746', -3000])
puthist(CF, 29, [-19800, -21771, -24082, -26445])
puthist(CF, 30, [-22245, -17254, -18420, -22271])
puthist(CF, 31, [1866, 2002, 2056, 2009])
puthist(CF, 32, [-1006, -1309, -2291, -2839])
puthist(CF, 35, [-194, -210, 63, -196])
put(CF, 'B37', 13931)

# Schedules historical opening balances (FY2022 year-end)
put(SC, 'B7', 74398)
put(SC, 'B11', 11298)
put(SC, 'B29', '=2749+47032')
SC['A36'] = 'Beginning cash + short-term investments (interest base)'

# ---------------- Assumptions ----------------
A['A2'] = 'Units: USD millions unless stated. Historical columns are calculated from reported figures; blue projection cells are inputs.'
A['A8'] = 'Cost of revenue excl. D&A (% of revenue)'
A['A9'] = 'SG&A: sales & marketing + G&A (% of revenue)'
A['A27'] = 'Amortization of intangibles (hist.: estimate)'
A['A35'] = 'Other assumptions'
A['A36'] = 'Stock-based compensation (% of revenue)'
A['A37'] = 'Proceeds from stock issuance'
A['A38'] = 'Basic shares outstanding'
A['A39'] = 'Other income / (expense) excl. interest'
A['A40'] = 'Short-term debt / current portion cap'
A['A35'].font = Font(bold=True)

proj = {
    7: ([.16, .14, .12, .11, .10], PCT),
    8: ([.205] * 5, PCT),
    9: ([.102, .100, .098, .096, .095], PCT),
    10: ([.105] * 5, PCT),
    11: ([0] * 5, PCT),
    12: ([.035] * 5, PCT),
    13: ([.035] * 5, PCT),
    14: ([.19] * 5, PCT),
    15: ([7430, 7410, 7390, 7370, 7350], NUM),
    18: ([89.0] * 5, DAYS),
    19: ([7.5] * 5, DAYS),
    20: ([225.0] * 5, DAYS),
    21: ([.145] * 5, PCT),
    22: ([.35] * 5, PCT),
    25: ([.35, .33, .30, .28, .26], PCT),
    26: ([.165] * 5, PCT),
    27: ([3800, 3500, 3200, 2900, 2600], NUM),
    30: ([-9227, -3000, -3000, -3000, -3000], NUM),
    31: ([.21] * 5, PCT),
    32: ([24000, 26000, 28000, 30000, 32000], NUM),
    33: ([15000] * 5, NUM),
    36: ([.037] * 5, PCT),
    37: ([2000] * 5, NUM),
    38: ([7405, 7385, 7365, 7345, 7325], NUM),
    39: ([0] * 5, NUM),
    40: ([3000] * 5, NUM),
}
for r, (vals, fmt) in proj.items():
    for c, v in zip(PC, vals):
        put(A, f'{c}{r}', v, fmt)

# historical amortization estimates (not separately disclosed in statements)
puthist(A, 27, [2500, 4800, 4800, 4000])
for c in HC:
    put(A, f'{c}7', f'=IS!{c}30', PCT)
    put(A, f'{c}8', f'=IS!{c}7/IS!{c}6', PCT)
    put(A, f'{c}9', f'=IS!{c}9/IS!{c}6', PCT)
    put(A, f'{c}10', f'=IS!{c}10/IS!{c}6', PCT)
    put(A, f'{c}11', f'=IS!{c}11/IS!{c}6', PCT)
    put(A, f'{c}14', f'=IS!{c}19/IS!{c}18', PCT)
    put(A, f'{c}15', f'=IS!{c}24', NUM)
    put(A, f'{c}18', f'=BS!{c}9/IS!{c}6*365', DAYS)
    put(A, f'{c}19', f'=BS!{c}10/IS!{c}7*365', DAYS)
    put(A, f'{c}20', f'=BS!{c}20/IS!{c}7*365', DAYS)
    put(A, f'{c}21', f'=BS!{c}11/IS!{c}6', PCT)
    put(A, f'{c}22', f'=BS!{c}21/IS!{c}6', PCT)
    put(A, f'{c}25', f'=-CFS!{c}20/IS!{c}6', PCT)
    put(A, f'{c}26', f'=Schedules!{c}9/Schedules!{c}7', PCT)
    put(A, f'{c}30', f'=CFS!{c}27+CFS!{c}28', NUM)
    put(A, f'{c}31', f'=-CFS!{c}29/IS!{c}20', PCT)
    put(A, f'{c}32', f'=-CFS!{c}30', NUM)
    put(A, f'{c}36', f'=CFS!{c}9/IS!{c}6', PCT)
    put(A, f'{c}37', f'=CFS!{c}31', NUM)
    put(A, f'{c}38', f'=IS!{c}23', NUM)
    put(A, f'{c}39', f'=IS!{c}17', NUM)
    put(A, f'{c}40', f'=BS!{c}22', NUM)

# ---------------- Income statement formulas ----------------
for c in ALL:
    h = c in HC
    p = prev(c)
    if not h:
        put(IS, f'{c}6', f'={p}6*(1+Assumptions!{c}7)')
        put(IS, f'{c}7', f'={c}6*Assumptions!{c}8')
        put(IS, f'{c}9', f'={c}6*Assumptions!{c}9')
        put(IS, f'{c}10', f'={c}6*Assumptions!{c}10')
        put(IS, f'{c}11', f'={c}6*Assumptions!{c}11')
        put(IS, f'{c}13', f'=Schedules!{c}14')
        put(IS, f'{c}15', f'=Schedules!{c}35')
        put(IS, f'{c}16', f'=Schedules!{c}38')
        put(IS, f'{c}17', f'=Assumptions!{c}39')
        put(IS, f'{c}19', f'={c}18*Assumptions!{c}14')
        put(IS, f'{c}23', f'=Assumptions!{c}38')
        put(IS, f'{c}24', f'=Assumptions!{c}15')
        put(IS, f'{c}27', f'=-CFS!{c}29/{c}23', EPS)
        put(IS, f'{c}37', f'={c}7+{c}13')
    else:
        put(IS, f'{c}7', f'={c}37-{c}13')
        put(IS, f'{c}13', f'=CFS!{c}8')
    put(IS, f'{c}8', f'={c}6-{c}7')
    put(IS, f'{c}12', f'={c}8-{c}9-{c}10-{c}11')
    put(IS, f'{c}14', f'={c}12-{c}13')
    put(IS, f'{c}18', f'={c}14-{c}15+{c}16+{c}17')
    put(IS, f'{c}20', f'={c}18-{c}19')
    put(IS, f'{c}25', f'={c}20/{c}23', EPS)
    put(IS, f'{c}26', f'={c}20/{c}24', EPS)
    put(IS, f'{c}30', f'={c}6/{p}6-1' if c != 'B' else '=B6/B38-1', PCT)
    put(IS, f'{c}31', f'={c}8/{c}6', PCT)
    put(IS, f'{c}32', f'={c}12/{c}6', PCT)
    put(IS, f'{c}33', f'={c}14/{c}6', PCT)
    put(IS, f'{c}34', f'={c}20/{c}6', PCT)
    put(IS, f'{c}35', f'={c}19/{c}18', PCT)

# ---------------- Balance sheet formulas ----------------
for c in ALL:
    p = prev(c)
    if c in PC:
        put(BS, f'{c}7', f'=CFS!{c}38')
        put(BS, f'{c}8', f'={p}8-CFS!{c}22')
        put(BS, f'{c}9', f'=Schedules!{c}17')
        put(BS, f'{c}10', f'=Schedules!{c}18')
        put(BS, f'{c}11', f'=Schedules!{c}19')
        put(BS, f'{c}13', f'=Schedules!{c}10')
        put(BS, f'{c}14', f'={p}14-CFS!{c}21')
        put(BS, f'{c}15', f'=Schedules!{c}13')
        put(BS, f'{c}16', f'={p}16-CFS!{c}23-CFS!{c}16')
        put(BS, f'{c}20', f'=Schedules!{c}20')
        put(BS, f'{c}21', f'=Schedules!{c}21')
        put(BS, f'{c}22', f'=MIN(Schedules!{c}32,Assumptions!{c}40)')
        put(BS, f'{c}24', f'=Schedules!{c}32-{c}22')
        put(BS, f'{c}25', f'={p}25+CFS!{c}10')
        put(BS, f'{c}29', f'={p}29+CFS!{c}9+CFS!{c}31+CFS!{c}32')
        put(BS, f'{c}30', f'={p}30+IS!{c}20+CFS!{c}29+CFS!{c}30')
        put(BS, f'{c}31', f'={p}31+CFS!{c}35')
        put(BS, f'{c}32', f'={p}32')
    put(BS, f'{c}12', f'=SUM({c}7:{c}11)')
    put(BS, f'{c}17', f'={c}12+SUM({c}13:{c}16)')
    put(BS, f'{c}23', f'=SUM({c}20:{c}22)')
    put(BS, f'{c}26', f'={c}23+{c}24+{c}25')
    put(BS, f'{c}33', f'=SUM({c}29:{c}32)')
    put(BS, f'{c}34', f'={c}26+{c}33')
# FX on cash flows through AOCI in projections (zero by assumption) - keeps BS balanced if user enters FX.

# ---------------- Cash flow formulas ----------------
for c in ALL:
    p = prev(c)
    put(CF, f'{c}7', f'=IS!{c}20')
    if c in PC:
        put(CF, f'{c}8', f'=Schedules!{c}14')
        put(CF, f'{c}9', f'=IS!{c}6*Assumptions!{c}36')
        put(CF, f'{c}10', 0)
        put(CF, f'{c}11', f'=BS!{p}9-BS!{c}9')
        put(CF, f'{c}12', f'=BS!{p}10-BS!{c}10')
        put(CF, f'{c}13', f'=BS!{p}11-BS!{c}11')
        put(CF, f'{c}14', f'=BS!{c}20-BS!{p}20')
        put(CF, f'{c}15', f'=BS!{c}21-BS!{p}21')
        put(CF, f'{c}16', 0)
        put(CF, f'{c}20', f'=-IS!{c}6*Assumptions!{c}25')
        put(CF, f'{c}21', 0)
        # liquidity plug: sell short-term investments only if cash would drop below minimum
        pre = f'({p}38+{c}17+{c}20+{c}21+{c}23+{c}33+{c}35)'
        put(CF, f'{c}22', f'=MIN(MAX(Assumptions!{c}33-{pre},0),BS!{p}8)')
        put(CF, f'{c}23', 0)
        put(CF, f'{c}27', f'=Schedules!{c}30')
        put(CF, f'{c}28', f'=Schedules!{c}31')
        put(CF, f'{c}29', f'=-IS!{c}20*Assumptions!{c}31')
        put(CF, f'{c}30', f'=-Assumptions!{c}32')
        put(CF, f'{c}31', f'=Assumptions!{c}37')
        put(CF, f'{c}32', 0)
        put(CF, f'{c}35', 0)
    put(CF, f'{c}17', f'=SUM({c}7:{c}16)')
    put(CF, f'{c}24', f'=SUM({c}20:{c}23)')
    put(CF, f'{c}33', f'=SUM({c}27:{c}32)')
    put(CF, f'{c}36', f'={c}17+{c}24+{c}33+{c}35')
    if c != 'B':
        put(CF, f'{c}37', f'={p}38')
    put(CF, f'{c}38', f'={c}37+{c}36')

# ---------------- Schedules ----------------
for c in ALL:
    p = prev(c)
    h = c in HC
    if c != 'B':
        put(SC, f'{c}7', f'=BS!{p}13')
        put(SC, f'{c}11', f'=BS!{p}15')
        put(SC, f'{c}29', f'={p}32')
    put(SC, f'{c}8', f'=-CFS!{c}20')
    put(SC, f'{c}12', f'=Assumptions!{c}27')
    if h:
        put(SC, f'{c}14', f'=CFS!{c}8')
        put(SC, f'{c}9', f'={c}14-{c}12')
        put(SC, f'{c}10', f'=BS!{c}13')
        put(SC, f'{c}13', f'=BS!{c}15')
        put(SC, f'{c}17', f'=BS!{c}9')
        put(SC, f'{c}18', f'=BS!{c}10')
        put(SC, f'{c}19', f'=BS!{c}11')
        put(SC, f'{c}20', f'=BS!{c}20')
        put(SC, f'{c}21', f'=BS!{c}21')
        put(SC, f'{c}30', f'=CFS!{c}27')
        put(SC, f'{c}31', f'=CFS!{c}28')
        put(SC, f'{c}32', f'=BS!{c}22+BS!{c}24')
    else:
        put(SC, f'{c}9', f'={c}7*Assumptions!{c}26')
        put(SC, f'{c}10', f'={c}7+{c}8-{c}9')
        put(SC, f'{c}13', f'={c}11-{c}12')
        put(SC, f'{c}14', f'={c}9+{c}12')
        put(SC, f'{c}17', f'=IS!{c}6*Assumptions!{c}18/365')
        put(SC, f'{c}18', f'=IS!{c}7*Assumptions!{c}19/365')
        put(SC, f'{c}19', f'=IS!{c}6*Assumptions!{c}21')
        put(SC, f'{c}20', f'=IS!{c}7*Assumptions!{c}20/365')
        put(SC, f'{c}21', f'=IS!{c}6*Assumptions!{c}22')
        put(SC, f'{c}30', f'=MAX(Assumptions!{c}30,0)')
        put(SC, f'{c}31', f'=MIN(Assumptions!{c}30,0)')
        put(SC, f'{c}32', f'={c}29+{c}30+{c}31')
        put(SC, f'{c}34', f'=Assumptions!{c}12', PCT)
        put(SC, f'{c}35', f'={c}33*{c}34')
        put(SC, f'{c}36', f'=BS!{p}7+BS!{p}8')
        put(SC, f'{c}37', f'=Assumptions!{c}13', PCT)
        put(SC, f'{c}38', f'={c}36*{c}37')
    put(SC, f'{c}22', f'={c}17+{c}18+{c}19-{c}20-{c}21')
    if c != 'B':
        put(SC, f'{c}23', f'={p}22-{c}22')
    put(SC, f'{c}24', f'={c}17/IS!{c}6*365', DAYS)
    put(SC, f'{c}25', f'={c}18/IS!{c}7*365', DAYS)
    put(SC, f'{c}26', f'={c}20/IS!{c}7*365', DAYS)
    put(SC, f'{c}33', f'=AVERAGE({c}29,{c}32)')
SC['A39'] = 'Historical PP&E and intangible roll-forwards do not foot (finance leases, acquisitions, impairments); ending balances are as reported. Historical interest is reported net in other income.'

# ---------------- Checks ----------------
CK['A8'] = 'Net income: IS less CFS (should be 0)'
CK['A9'] = 'Retained earnings roll-forward (projections): should be 0'
CK['A11'] = 'All checks pass (1 = yes)'
for c in ALL:
    p = prev(c)
    put(CK, f'{c}6', f'=ROUND(BS!{c}17-BS!{c}34,3)')
    put(CK, f'{c}7', f'=ROUND(CFS!{c}38-BS!{c}7,3)')
    put(CK, f'{c}8', f'=ROUND(IS!{c}20-CFS!{c}7,3)')
    if c in PC:
        put(CK, f'{c}9', f'=ROUND(BS!{c}30-(BS!{p}30+IS!{c}20+CFS!{c}29+CFS!{c}30),3)')
    put(CK, f'{c}11', f'=IF(AND({c}6=0,{c}7=0,{c}8=0,N({c}9)=0),1,0)', '0')
put(CK, 'B12', '=IF(SUM(B11:J11)=9,"ALL CHECKS PASS","CHECK ERRORS")', '@')
CK['A12'] = 'Model status'

wb.save(RUN + 'MSFT_3S_model.xlsx')
print('saved')
