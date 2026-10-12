"""Statement building against the synthetic TestCo facts (see factories.py)."""

import pytest

from stock_data_mcp.errors import NotFound
from stock_data_mcp.financials import build_calendar, build_statement
from stock_data_mcp.sources.edgar import Edgar

from .factories import companyfacts


class _NoNetwork:
    async def get(self, *a, **kw):  # pragma: no cover
        raise AssertionError("network used")


async def trimmed(cache, **kw) -> dict:
    """Run the synthetic facts through the real EDGAR trimming step."""
    edgar = Edgar(_NoNetwork(), cache)
    raw = companyfacts(**kw)

    async def fake_get(url):
        return raw

    edgar._get = fake_get
    return (await edgar.company_facts("0001234567")).value


@pytest.fixture
async def tco(cache):
    return await trimmed(cache)


def test_calendar_labels_and_quarters(tco):
    years = build_calendar(tco["facts"])
    assert [y.label for y in years] == ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
    fy24 = years[3]
    assert [q.label for q in fy24.quarters] == ["FY2024Q1", "FY2024Q2", "FY2024Q3", "FY2024Q4"]
    assert [q.end.isoformat() for q in fy24.quarters] == [
        "2023-12-30",
        "2024-03-30",
        "2024-06-29",
        "2024-09-28",
    ]
    assert years[4].end is None  # in progress
    assert [q.label for q in years[4].quarters] == ["FY2025Q1", "FY2025Q2"]


def test_annual_income(tco):
    out = build_statement(tco, "income", years=5)
    assert out["periods"] == ["FY2021", "FY2022", "FY2023", "FY2024"]
    assert out["period_end"][-1] == "2024-09-28"
    items = out["items"]
    # FY2021 only exists under the old tag.
    assert items["revenue"] == [300, 350, 380, 410]
    assert out["concepts"]["revenue"] == [
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "SalesRevenueNet",
    ]
    # Restated FY2023 net income wins over the original.
    assert items["net_income"][2:] == [52, 60]
    # Gross profit computed from revenue - cost_of_revenue.
    assert items["gross_profit"] == [None, None, 160, 180]
    assert "gross_profit" in out["computed"]
    assert items["eps_diluted"][-1] == 4.10
    assert items["shares_diluted"][-1] == 15000.0
    assert "derived" not in out
    assert "sga" in out["not_reported"]


def test_years_limit(tco):
    out = build_statement(tco, "income", years=2)
    assert out["periods"] == ["FY2023", "FY2024"]


def test_quarterly_income_derives_q4(tco):
    out = build_statement(tco, "income", years=3, quarterly=True)
    by = dict(zip(out["periods"], out["items"]["revenue"], strict=True))
    assert by["FY2023Q1"] == 100 and by["FY2023Q4"] == 110  # 380 - 270
    assert by["FY2024Q4"] == 120  # 410 - 290
    assert by["FY2025Q1"] == 125 and by["FY2025Q2"] == 100
    assert out["derived"]["revenue"] == ["FY2023Q4", "FY2024Q4"]
    # Per-share values are never derived by subtraction.
    eps = dict(zip(out["periods"], out["items"]["eps_diluted"], strict=True))
    assert eps["FY2024Q3"] == 0.85 and eps["FY2024Q4"] is None


def test_quarterly_cashflow_from_ytd(tco):
    out = build_statement(tco, "cashflow", years=1, quarterly=True)
    by = {k: dict(zip(out["periods"], v, strict=True)) for k, v in out["items"].items()}
    ocf = by["operating_cash_flow"]
    assert [ocf[f"FY2024Q{i}"] for i in (1, 2, 3, 4)] == [30, 25, 30, 35]
    capex = by["capex"]
    assert [capex[f"FY2024Q{i}"] for i in (1, 2, 3, 4)] == [5, 4, 5, 6]
    fcf = by["free_cash_flow"]
    assert [fcf[f"FY2024Q{i}"] for i in (1, 2, 3, 4)] == [25, 21, 25, 29]
    assert out["derived"]["operating_cash_flow"] == ["FY2024Q2", "FY2024Q3", "FY2024Q4"]
    assert out["derived"]["free_cash_flow"] == ["FY2024Q2", "FY2024Q3", "FY2024Q4"]
    assert out["computed"]["free_cash_flow"] == "operating_cash_flow - capex"


def test_balance_annual_and_quarterly(tco):
    out = build_statement(tco, "balance", years=2)
    assert out["periods"] == ["FY2023", "FY2024"]
    assert out["items"]["total_assets"] == [900, 1000]
    assert out["items"]["shares_outstanding"] == [None, 14900.0]
    q = build_statement(tco, "balance", years=2, quarterly=True)
    assets = dict(zip(q["periods"], q["items"]["total_assets"], strict=True))
    assert assets["FY2024Q4"] == 1000 and assets["FY2025Q2"] == 1020


async def test_in_progress_year_with_only_q1(cache):
    facts = await trimmed(cache, drop_accns={"Q225"})
    years = build_calendar(facts["facts"])
    assert years[-1].label == "FY2025"
    assert [q.label for q in years[-1].quarters] == ["FY2025Q1"]
    out = build_statement(facts, "income", years=1, quarterly=True)
    assert out["periods"][-1] == "FY2025Q1" and out["items"]["revenue"][-1] == 125


async def test_ifrs_filer_rejected(cache):
    facts = await trimmed(cache, ifrs=True)
    with pytest.raises(NotFound, match="IFRS"):
        build_statement(facts, "income")


def test_bad_statement(tco):
    with pytest.raises(ValueError):
        build_statement(tco, "equity")
