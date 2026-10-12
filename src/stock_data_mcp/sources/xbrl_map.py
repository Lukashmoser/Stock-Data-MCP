"""Standardized line items -> ordered us-gaap concept candidates.

For each period the first concept that has a value wins, so older tags
(e.g. SalesRevenueNet before ASC 606) can sit behind newer ones.
Edit freely: the companyfacts cache is keyed on MAP_VERSION, so changes
here take effect on the next call.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Literal

Kind = Literal["flow", "instant"]
Unit = Literal["USD", "USD/shares", "shares"]


@dataclass(frozen=True)
class Item:
    name: str
    concepts: tuple[str, ...]
    kind: Kind = "flow"
    unit: Unit = "USD"


def _flow(name: str, *concepts: str, unit: Unit = "USD") -> Item:
    return Item(name, concepts, "flow", unit)


def _instant(name: str, *concepts: str, unit: Unit = "USD") -> Item:
    return Item(name, concepts, "instant", unit)


STATEMENTS: dict[str, tuple[Item, ...]] = {
    "income": (
        _flow(
            "revenue",
            "Revenues",
            "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax",
            "SalesRevenueNet",
            "RevenuesNetOfInterestExpense",
        ),
        _flow(
            "cost_of_revenue",
            "CostOfRevenue",
            "CostOfGoodsAndServicesSold",
            "CostOfGoodsSold",
            "CostOfServices",
        ),
        _flow("gross_profit", "GrossProfit"),
        _flow(
            "research_development",
            "ResearchAndDevelopmentExpense",
            "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
        ),
        _flow("sga", "SellingGeneralAndAdministrativeExpense"),
        _flow("operating_expenses", "OperatingExpenses"),
        _flow("operating_income", "OperatingIncomeLoss"),
        _flow("interest_expense", "InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"),
        _flow(
            "pretax_income",
            "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
            "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
        ),
        _flow("income_tax", "IncomeTaxExpenseBenefit"),
        _flow("net_income", "NetIncomeLoss", "ProfitLoss", "NetIncomeLossAvailableToCommonStockholdersBasic"),
        _flow("eps_basic", "EarningsPerShareBasic", "EarningsPerShareBasicAndDiluted", unit="USD/shares"),
        _flow("eps_diluted", "EarningsPerShareDiluted", "EarningsPerShareBasicAndDiluted", unit="USD/shares"),
        _flow("shares_basic", "WeightedAverageNumberOfSharesOutstandingBasic", unit="shares"),
        _flow(
            "shares_diluted",
            "WeightedAverageNumberOfDilutedSharesOutstanding",
            "WeightedAverageNumberOfShareOutstandingBasicAndDiluted",
            unit="shares",
        ),
    ),
    "balance": (
        _instant(
            "cash",
            "CashAndCashEquivalentsAtCarryingValue",
            "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
        ),
        _instant(
            "short_term_investments",
            "ShortTermInvestments",
            "MarketableSecuritiesCurrent",
            "AvailableForSaleSecuritiesDebtSecuritiesCurrent",
        ),
        _instant("receivables", "AccountsReceivableNetCurrent"),
        _instant("inventory", "InventoryNet"),
        _instant("total_current_assets", "AssetsCurrent"),
        _instant("ppe_net", "PropertyPlantAndEquipmentNet"),
        _instant("goodwill", "Goodwill"),
        _instant("intangibles", "IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"),
        _instant("total_assets", "Assets"),
        _instant("accounts_payable", "AccountsPayableCurrent"),
        _instant("short_term_debt", "DebtCurrent", "LongTermDebtCurrent"),
        _instant("total_current_liabilities", "LiabilitiesCurrent"),
        _instant("long_term_debt", "LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"),
        _instant("total_liabilities", "Liabilities"),
        _instant(
            "stockholders_equity",
            "StockholdersEquity",
            "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
        ),
        _instant("shares_outstanding", "CommonStockSharesOutstanding", unit="shares"),
    ),
    "cashflow": (
        _flow(
            "operating_cash_flow",
            "NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
        ),
        _flow("capex", "PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"),
        _flow(
            "depreciation_amortization",
            "DepreciationDepletionAndAmortization",
            "DepreciationAndAmortization",
            "DepreciationAmortizationAndAccretionNet",
        ),
        _flow("stock_based_comp", "ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"),
        _flow("investing_cash_flow", "NetCashProvidedByUsedInInvestingActivities"),
        _flow("financing_cash_flow", "NetCashProvidedByUsedInFinancingActivities"),
        _flow("dividends_paid", "PaymentsOfDividends", "PaymentsOfDividendsCommonStock"),
        _flow("share_repurchases", "PaymentsForRepurchaseOfCommonStock"),
        _flow("acquisitions", "PaymentsToAcquireBusinessesNetOfCashAcquired"),
    ),
}

# Lines computed from other lines when not reported directly:
# name -> (statement, formula text, minuend, subtrahend)
COMPUTED: dict[str, tuple[str, str, str, str]] = {
    "gross_profit": ("income", "revenue - cost_of_revenue", "revenue", "cost_of_revenue"),
    "free_cash_flow": ("cashflow", "operating_cash_flow - capex", "operating_cash_flow", "capex"),
}

ALL_CONCEPTS: tuple[str, ...] = tuple(
    sorted({c for items in STATEMENTS.values() for item in items for c in item.concepts})
)
MAP_VERSION = hashlib.sha1("|".join(ALL_CONCEPTS).encode()).hexdigest()[:8]
