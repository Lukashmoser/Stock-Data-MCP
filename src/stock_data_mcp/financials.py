"""Turn trimmed EDGAR company facts into standardized statement tables.

Periods are identified by their start/end dates, never by a fact's fy/fp
tags: a 10-K for FY2024 also carries FY2023/FY2022 comparatives tagged
fy=2024. The fy tag is only trusted for a filing's own (latest) period,
where it gives the company's fiscal-year label.

Quarterly flows: a reported ~3-month fact is used directly. Otherwise the
quarter is derived from year-to-date facts (10-Q cash flows are YTD, and
Q4 is never filed on its own): Q = YTD(end) - YTD(previous quarter end),
which for Q4 is FY - 9M. Derived values are listed under "derived".
Per-share and share-count lines are never derived; subtraction is wrong
for them, so missing quarters stay null.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from .errors import NotFound
from .sources.xbrl_map import COMPUTED, STATEMENTS

ANNUAL_DAYS = (350, 380)
QUARTER_DAYS = (80, 100)
_TOL = timedelta(days=6)  # 52/53-week calendars shift period edges by a few days


@dataclass(frozen=True)
class Fact:
    start: date | None
    end: date
    val: float
    filed: str

    @property
    def days(self) -> int:
        return (self.end - self.start).days if self.start else 0


@dataclass
class Period:
    label: str
    start: date
    end: date
    quarter: int | None = None  # None for a fiscal year


@dataclass
class FiscalYear:
    start: date
    end: date | None  # None while the year is in progress
    label: str = ""
    quarters: list[Period] = field(default_factory=list)


def _d(s: str | None) -> date | None:
    return date.fromisoformat(s) if s else None


def _rows(facts: dict, concept: str, unit: str) -> list[list]:
    return facts.get(concept, {}).get(unit, [])


def _parse(rows: list[list]) -> list[Fact]:
    """Dedupe by (start, end), keeping the latest filing (restatements win)."""
    best: dict[tuple, Fact] = {}
    for start, end, val, _fy, _fp, _form, filed, _accn in rows:
        f = Fact(_d(start), _d(end), val, filed or "")
        key = (f.start, f.end)
        if key not in best or f.filed > best[key].filed:
            best[key] = f
    return list(best.values())


def _in(days: int, rng: tuple[int, int]) -> bool:
    return rng[0] <= days <= rng[1]


def _near(a: date, b: date) -> bool:
    return abs(a - b) <= _TOL


# ---------------------------------------------------------------- calendar


def build_calendar(facts: dict) -> list[FiscalYear]:
    """Infer fiscal years and their quarter ends from all duration facts."""
    spans: set[tuple[date, date]] = set()
    fy_by_end: dict[date, int] = {}
    accn_max_end: dict[str, str] = {}
    all_rows = [r for units in facts.values() for rows in units.values() for r in rows]
    for r in all_rows:
        if r[7] and (r[7] not in accn_max_end or r[1] > accn_max_end[r[7]]):
            accn_max_end[r[7]] = r[1]
    for start, end, _v, fy, _fp, _form, _filed, accn in all_rows:
        if start:
            spans.add((_d(start), _d(end)))
        if fy and accn and end == accn_max_end.get(accn):
            fy_by_end[_d(end)] = int(fy)

    annual = [(s, e) for s, e in spans if _in((e - s).days, ANNUAL_DAYS)]
    ytd_starts = [s for s, e in spans if 100 < (e - s).days < ANNUAL_DAYS[0]]
    starts = sorted({s for s, _ in annual} | set(ytd_starts))
    # An in-progress year with only Q1 filed has no YTD fact; it starts after the last FY end.
    if annual:
        last_end = max(e for _, e in annual)
        if not any(s > last_end for s in starts) and any(e > last_end + timedelta(days=60) for _, e in spans):
            starts.append(last_end + timedelta(days=1))

    kept: list[date] = []
    for s in sorted(starts):
        if not kept or (s - kept[-1]).days > 300:
            kept.append(s)

    years: list[FiscalYear] = []
    for i, s in enumerate(kept):
        bound = kept[i + 1] if i + 1 < len(kept) else s + timedelta(days=ANNUAL_DAYS[1] + 1)
        ends = Counter(e for a, e in annual if _near(a, s))
        fy = FiscalYear(start=s, end=ends.most_common(1)[0][0] if ends else None)
        q_ends = sorted(
            {e for a, e in spans if a > s - _TOL and s < e < bound and _in((e - a).days, QUARTER_DAYS)}
            | {e for a, e in spans if _near(a, s) and s < e < bound and (e - a).days <= ANNUAL_DAYS[1]}
        )
        seen: set[int] = set()
        for e in q_ends:
            q = min(4, max(1, round((e - s).days / 91.3)))
            if q not in seen:
                seen.add(q)
                fy.quarters.append(Period("", s, e, q))
        years.append(fy)

    used: set[str] = set()
    for fy in years:
        tagged = [fy_by_end[e] for e in [fy.end, *(q.end for q in fy.quarters)] if e in fy_by_end]
        n = tagged[0] if tagged else (fy.start + timedelta(days=364)).year
        if f"FY{n}" in used:
            n = (fy.start + timedelta(days=364)).year
        fy.label = f"FY{n}"
        used.add(fy.label)
        for q in fy.quarters:
            q.label = f"{fy.label}Q{q.quarter}"
    return years


# ---------------------------------------------------------------- values


def _flow_values(facts: list[Fact], years: list[FiscalYear], quarterly: bool, derive: bool):
    """{label: (value, derived)} for one concept's duration facts."""
    out: dict[str, tuple[float, bool]] = {}
    by_end: dict[date, list[Fact]] = defaultdict(list)
    for f in facts:
        if f.start:
            by_end[f.end].append(f)

    def span(start: date, end: date) -> float | None:
        for f in by_end.get(end, []):
            if _near(f.start, start):
                return f.val
        return None

    def three_month(end: date) -> float | None:
        for f in by_end.get(end, []):
            if _in(f.days, QUARTER_DAYS):
                return f.val
        return None

    for fy in years:
        if not quarterly:
            if fy.end is not None and (v := span(fy.start, fy.end)) is not None:
                out[fy.label] = (v, False)
            continue
        done: dict[int, float] = {}
        prev: Period | None = None
        for q in fy.quarters:
            v, derived = three_month(q.end), False
            if v is None and derive and q.quarter > 1:
                ytd = span(fy.start, q.end)
                if ytd is not None:
                    prior = None
                    if prev is not None and prev.quarter == q.quarter - 1:
                        prior = span(fy.start, prev.end)
                    if prior is None and all(k in done for k in range(1, q.quarter)):
                        prior = sum(done[k] for k in range(1, q.quarter))
                    if prior is not None:
                        v, derived = ytd - prior, True
            if v is not None:
                done[q.quarter] = v
                out[q.label] = (v, derived)
            prev = q
    return out


def _instant_values(facts: list[Fact], periods: list[Period]):
    by_end = {f.end: f.val for f in facts if f.start is None}
    return {p.label: (by_end[p.end], False) for p in periods if p.end in by_end}


def _scale(v: float | None, unit: str) -> float | None:
    if v is None:
        return None
    if unit == "USD/shares":
        return round(v, 4)
    return round(v / 1e6, 3 if unit == "shares" else 2)


def build_statement(company: dict, statement: str, years: int = 5, quarterly: bool = False) -> dict[str, Any]:
    """Build one statement table from Edgar.company_facts() output."""
    if statement not in STATEMENTS:
        raise ValueError(f"statement must be one of {sorted(STATEMENTS)}")
    facts = company["facts"]
    if not facts:
        if "ifrs-full" in company.get("taxonomies", []):
            raise NotFound(
                "Company reports under IFRS (e.g. a 20-F filer); only US GAAP is supported",
                hint="Use get_filings to locate the 20-F instead.",
            )
        raise NotFound("No US GAAP financial data found for this company")

    calendar = build_calendar(facts)
    if quarterly:
        periods = [q for fy in calendar for q in fy.quarters]
    else:
        periods = [Period(fy.label, fy.start, fy.end) for fy in calendar if fy.end is not None]

    items: dict[str, dict[str, float]] = {}
    concepts_used: dict[str, list[str]] = {}
    derived: dict[str, list[str]] = {}
    for item in STATEMENTS[statement]:
        merged: dict[str, tuple[float, bool]] = {}
        used: list[str] = []
        for concept in item.concepts:
            parsed = _parse(_rows(facts, concept, item.unit))
            if not parsed:
                continue
            if item.kind == "instant":
                vals = _instant_values(parsed, periods)
            else:
                vals = _flow_values(parsed, calendar, quarterly, derive=item.unit == "USD")
            added = {k: v for k, v in vals.items() if k not in merged}
            if added:
                merged.update(added)
                used.append(concept)
        if merged:
            items[item.name] = {k: v for k, (v, _) in merged.items()}
            concepts_used[item.name] = used
            if d := sorted(k for k, (_, isd) in merged.items() if isd):
                derived[item.name] = d

    computed: dict[str, str] = {}
    for name, (stmt, formula, a, b) in COMPUTED.items():
        if stmt != statement or a not in items or b not in items:
            continue
        filled = {
            k: items[a][k] - items[b][k] for k in items[a] if k in items[b] and k not in items.get(name, {})
        }
        if filled:
            items.setdefault(name, {}).update(filled)
            computed[name] = formula + (" (where not reported)" if name in concepts_used else "")
            both = set(derived.get(a, [])) | set(derived.get(b, []))
            if d := sorted(set(derived.get(name, [])) | (both & set(filled))):
                derived[name] = d

    # Keep the latest N periods that have any data.
    with_data = [p for p in periods if any(p.label in v for v in items.values())]
    limit = years * 4 if quarterly else years
    chosen = with_data[-limit:] if limit > 0 else []

    units = {i.name: i.unit for i in STATEMENTS[statement]}
    out_items = {}
    missing = []
    for name in [*(i.name for i in STATEMENTS[statement]), *(n for n in COMPUTED if n not in units)]:
        if name not in items:
            if name in units:
                missing.append(name)
            continue
        row = [_scale(items[name].get(p.label), units.get(name, "USD")) for p in chosen]
        if any(v is not None for v in row):
            out_items[name] = row
        else:
            missing.append(name)

    labels = {p.label for p in chosen}
    out: dict[str, Any] = {
        "statement": statement,
        "period": "quarterly" if quarterly else "annual",
        "units": "USD millions; eps_* in USD; shares_* in millions",
        "periods": [p.label for p in chosen],
        "period_end": [p.end.isoformat() for p in chosen],
        "items": out_items,
        "concepts": {k: v[0] if len(v) == 1 else v for k, v in concepts_used.items() if k in out_items},
    }
    if computed := {k: v for k, v in computed.items() if k in out_items}:
        out["computed"] = computed
    if derived := {k: [x for x in v if x in labels] for k, v in derived.items() if k in out_items}:
        if derived := {k: v for k, v in derived.items() if v}:
            out["derived"] = derived
    if missing:
        out["not_reported"] = missing
    return out
