"""Synthetic EDGAR companyfacts in the real API shape.

TestCo has an Apple-like 52/53-week fiscal year ending late September:
  FY2021 2020-09-27..2021-09-25   FY2022 2021-09-26..2022-09-24
  FY2023 2022-09-25..2023-09-30   FY2024 2023-10-01..2024-09-28
  FY2025 2024-09-29..  (in progress: Q1 to 2024-12-28, Q2 to 2025-03-29)
Values are in USD millions here and scaled to raw USD in the output JSON.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

M = 1_000_000

FY21 = ("2020-09-27", "2021-09-25")
FY22 = ("2021-09-26", "2022-09-24")
FY23 = ("2022-09-25", "2023-09-30")
FY24 = ("2023-10-01", "2024-09-28")
# FY2023 quarters
Q1_23, Q2_23, Q3_23 = ("2022-09-25", "2022-12-31"), ("2023-01-01", "2023-04-01"), ("2023-04-02", "2023-07-01")
H1_23, M9_23 = ("2022-09-25", "2023-04-01"), ("2022-09-25", "2023-07-01")
# FY2024 quarters
Q1_24, Q2_24, Q3_24 = ("2023-10-01", "2023-12-30"), ("2023-12-31", "2024-03-30"), ("2024-03-31", "2024-06-29")
H1_24, M9_24 = ("2023-10-01", "2024-03-30"), ("2023-10-01", "2024-06-29")
# FY2025 (in progress)
Q1_25, Q2_25 = ("2024-09-29", "2024-12-28"), ("2024-12-29", "2025-03-29")
H1_25 = ("2024-09-29", "2025-03-29")

# accession -> (form, fy, fp, filed)
FILINGS = {
    "A22": ("10-K", 2022, "FY", "2022-11-01"),
    "A23": ("10-K", 2023, "FY", "2023-11-03"),
    "A24": ("10-K", 2024, "FY", "2024-11-01"),
    "Q124": ("10-Q", 2024, "Q1", "2024-02-02"),
    "Q224": ("10-Q", 2024, "Q2", "2024-05-03"),
    "Q324": ("10-Q", 2024, "Q3", "2024-08-02"),
    "Q125": ("10-Q", 2025, "Q1", "2025-02-01"),
    "Q225": ("10-Q", 2025, "Q2", "2025-05-02"),
}

# (concept, unit, accn, span-or-instant, value in millions or per-share/shares raw)
REV_OLD = "SalesRevenueNet"
REV = "RevenueFromContractWithCustomerExcludingAssessedTax"
FACTS: list[tuple[str, str, str, Any, float]] = [
    # Revenue: FY2021 only under the pre-ASC 606 tag.
    (REV_OLD, "USD", "A22", FY22, 350), (REV_OLD, "USD", "A22", FY21, 300),
    (REV, "USD", "A23", FY23, 380), (REV, "USD", "A23", FY22, 350),
    (REV, "USD", "A24", FY24, 410), (REV, "USD", "A24", FY23, 380),
    (REV, "USD", "Q124", Q1_24, 110), (REV, "USD", "Q124", Q1_23, 100),
    (REV, "USD", "Q224", Q2_24, 95), (REV, "USD", "Q224", H1_24, 205),
    (REV, "USD", "Q224", Q2_23, 90), (REV, "USD", "Q224", H1_23, 190),
    (REV, "USD", "Q324", Q3_24, 85), (REV, "USD", "Q324", M9_24, 290),
    (REV, "USD", "Q324", Q3_23, 80), (REV, "USD", "Q324", M9_23, 270),
    (REV, "USD", "Q125", Q1_25, 125), (REV, "USD", "Q125", Q1_24, 110),
    (REV, "USD", "Q225", Q2_25, 100), (REV, "USD", "Q225", H1_25, 225),
    # Cost of revenue (no GrossProfit tag -> computed).
    ("CostOfGoodsAndServicesSold", "USD", "A24", FY24, 230), ("CostOfGoodsAndServicesSold", "USD", "A24", FY23, 220),
    # Net income: FY2023 restated from 50 to 52 in the FY2024 10-K.
    ("NetIncomeLoss", "USD", "A23", FY23, 50), ("NetIncomeLoss", "USD", "A24", FY23, 52),
    ("NetIncomeLoss", "USD", "A24", FY24, 60),
    # EPS: quarterly 3-month values only; Q4 must stay null.
    ("EarningsPerShareDiluted", "USD/shares", "A24", FY24, 4.10),
    ("EarningsPerShareDiluted", "USD/shares", "Q124", Q1_24, 1.10),
    ("EarningsPerShareDiluted", "USD/shares", "Q224", Q2_24, 0.95),
    ("EarningsPerShareDiluted", "USD/shares", "Q224", H1_24, 2.05),
    ("EarningsPerShareDiluted", "USD/shares", "Q324", Q3_24, 0.85),
    ("EarningsPerShareDiluted", "USD/shares", "Q324", M9_24, 2.90),
    ("WeightedAverageNumberOfDilutedSharesOutstanding", "shares", "A24", FY24, 15_000_000_000),
    # Cash flow: 10-Qs report year-to-date only.
    ("NetCashProvidedByUsedInOperatingActivities", "USD", "A24", FY24, 120),
    ("NetCashProvidedByUsedInOperatingActivities", "USD", "A24", FY23, 100),
    ("NetCashProvidedByUsedInOperatingActivities", "USD", "Q124", Q1_24, 30),
    ("NetCashProvidedByUsedInOperatingActivities", "USD", "Q224", H1_24, 55),
    ("NetCashProvidedByUsedInOperatingActivities", "USD", "Q324", M9_24, 85),
    ("PaymentsToAcquirePropertyPlantAndEquipment", "USD", "A24", FY24, 20),
    ("PaymentsToAcquirePropertyPlantAndEquipment", "USD", "A24", FY23, 18),
    ("PaymentsToAcquirePropertyPlantAndEquipment", "USD", "Q124", Q1_24, 5),
    ("PaymentsToAcquirePropertyPlantAndEquipment", "USD", "Q224", H1_24, 9),
    ("PaymentsToAcquirePropertyPlantAndEquipment", "USD", "Q324", M9_24, 14),
    # Balance sheet instants.
    ("Assets", "USD", "A23", "2023-09-30", 900), ("Assets", "USD", "A24", "2023-09-30", 900),
    ("Assets", "USD", "A24", "2024-09-28", 1000),
    ("Assets", "USD", "Q124", "2023-12-30", 920), ("Assets", "USD", "Q224", "2024-03-30", 940),
    ("Assets", "USD", "Q324", "2024-06-29", 960), ("Assets", "USD", "Q125", "2024-12-28", 1010),
    ("Assets", "USD", "Q225", "2025-03-29", 1020),
    ("CommonStockSharesOutstanding", "shares", "A24", "2024-09-28", 14_900_000_000),
    # Not in the mapping; must be trimmed away.
    ("SomeUnmappedConcept", "USD", "A24", FY24, 1),
]  # fmt: skip


def companyfacts(
    facts: list[tuple] = FACTS, *, drop_accns: set[str] = frozenset(), ifrs: bool = False
) -> dict:
    gaap: dict[str, Any] = defaultdict(lambda: {"label": "", "description": "", "units": defaultdict(list)})
    for concept, unit, accn, period, val in facts:
        if accn in drop_accns:
            continue
        form, fy, fp, filed = FILINGS[accn]
        row: dict[str, Any] = {}
        if isinstance(period, tuple):
            row["start"], row["end"] = period
        else:
            row["end"] = period
        scaled = val * M if unit == "USD" else val
        row.update(val=scaled, accn=accn, fy=fy, fp=fp, form=form, filed=filed)
        gaap[concept]["units"][unit].append(row)
    taxonomies: dict[str, Any] = {"dei": {"EntityCommonStockSharesOutstanding": {"units": {}}}}
    if ifrs:
        taxonomies["ifrs-full"] = {"Revenue": {"units": {}}}
    else:
        taxonomies["us-gaap"] = {k: {**v, "units": dict(v["units"])} for k, v in gaap.items()}
    # Non-periodic forms carry facts too; they must be ignored.
    if not ifrs:
        taxonomies["us-gaap"][REV]["units"]["USD"].append(
            {"start": FY24[0], "end": FY24[1], "val": 1, "accn": "S1", "fy": 2024, "fp": "FY",
             "form": "8-K", "filed": "2024-12-01"}
        )  # fmt: skip
    return {"cik": 1234567, "entityName": "TestCo Inc.", "facts": taxonomies}
