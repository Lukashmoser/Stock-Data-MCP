"""SEC EDGAR: ticker->CIK, filings list (submissions) and XBRL company facts."""

from __future__ import annotations

import re
from typing import Any

import httpx
from aiolimiter import AsyncLimiter

from ..cache import DAY, HOUR, Cache, CacheResult
from ..errors import NotFound
from ..http import get_json
from .xbrl_map import ALL_CONCEPTS, MAP_VERSION

SOURCE = "SEC EDGAR"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
ARCHIVE_URL = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{doc}"

# Only periodic-report facts feed the financial statements.
_FACT_FORMS = {"10-K", "10-K/A", "10-Q", "10-Q/A", "10-KT", "10-KT/A"}
_FILING_COLS = (
    "accessionNumber", "filingDate", "reportDate", "form",
    "primaryDocument", "primaryDocDescription", "items",
)  # fmt: skip


def normalize_ticker(ticker: str) -> str:
    """Upper-case and map class separators to SEC style (BRK.B / BRK/B -> BRK-B)."""
    t = ticker.strip().upper()
    return re.sub(r"[./]", "-", t)


class Edgar:
    def __init__(self, client: httpx.AsyncClient, cache: Cache, max_rps: float = 8.0):
        self.client = client
        self.cache = cache
        # Spread requests over the second rather than bursting.
        self.limiter = AsyncLimiter(1, 1 / max_rps)

    async def _get(self, url: str) -> Any:
        return await get_json(self.client, url, source=SOURCE, limiter=self.limiter)

    # ---- ticker -> CIK -------------------------------------------------

    async def ticker_map(self) -> dict[str, list]:
        """{TICKER: [cik_int, title]} from company_tickers.json (cached 24h)."""

        async def fetch() -> dict[str, list]:
            raw = await self._get(TICKERS_URL)
            return {
                normalize_ticker(row["ticker"]): [int(row["cik_str"]), row["title"]] for row in raw.values()
            }

        return (await self.cache.get_or_fetch("edgar:tickers", DAY, fetch)).value

    async def resolve(self, ticker: str) -> tuple[str, str]:
        """Return (10-digit CIK, company name). Accepts a ticker or a numeric CIK."""
        t = ticker.strip()
        if t.isdigit():
            return t.zfill(10), ""
        mapping = await self.ticker_map()
        hit = mapping.get(normalize_ticker(t))
        if hit is None:
            raise NotFound(
                f"Ticker '{ticker}' not found in SEC company list",
                hint="Use the US listing ticker (e.g. BRK-B), or pass the CIK number.",
            )
        return str(hit[0]).zfill(10), hit[1]

    # ---- submissions ---------------------------------------------------

    async def submissions(self, cik: str) -> CacheResult:
        """Company metadata plus the recent filings table (columnar), cached 6h."""

        async def fetch() -> dict:
            raw = await self._get(SUBMISSIONS_URL.format(cik=cik))
            recent = raw.get("filings", {}).get("recent", {})
            return {
                "name": raw.get("name"),
                "tickers": raw.get("tickers", []),
                "sic": raw.get("sic"),
                "sic_description": raw.get("sicDescription"),
                "fiscal_year_end": raw.get("fiscalYearEnd"),
                "recent": {c: recent.get(c, []) for c in _FILING_COLS},
            }

        return await self.cache.get_or_fetch(f"edgar:subs:{cik}", 6 * HOUR, fetch)

    async def filings(
        self,
        ticker: str,
        form_type: str | None = None,
        limit: int = 10,
        include_amendments: bool = True,
    ) -> dict:
        cik, name = await self.resolve(ticker)
        res = await self.submissions(cik)
        subs = res.value
        recent = subs["recent"]
        want = form_type.strip().upper() if form_type else None
        rows = []
        for i, form in enumerate(recent["form"]):
            if want:
                base = form[:-2] if form.endswith("/A") else form
                if form != want and not (include_amendments and base == want):
                    continue
            acc = recent["accessionNumber"][i]
            doc = recent["primaryDocument"][i]
            row = {
                "form": form,
                "filed": recent["filingDate"][i],
                "period": recent["reportDate"][i] or None,
                "accession": acc,
                "url": ARCHIVE_URL.format(cik=int(cik), acc=acc.replace("-", ""), doc=doc) if doc else None,
            }
            desc = recent["primaryDocDescription"][i]
            if desc and desc.upper() != form.upper():
                row["description"] = desc
            items = recent["items"][i] if i < len(recent["items"]) else ""
            if items:
                row["items"] = items  # 8-K item numbers, e.g. "2.02,9.01"
            rows.append(row)
            if len(rows) >= limit:
                break
        out = {
            "ticker": ticker.upper(),
            "cik": cik,
            "company": subs.get("name") or name,
            "form_type": want,
            "count": len(rows),
            "filings": rows,
        }
        if res.stale:
            out["stale"] = True
        return out

    # ---- company facts -------------------------------------------------

    async def company_facts(self, cik: str) -> CacheResult:
        """us-gaap facts for the mapped concepts only, trimmed to compact rows.

        Returns {"name": str, "taxonomies": [...], "facts": {concept: {unit: [row...]}}}
        where row = [start|None, end, val, fy, fp, form, filed, accn].
        The cache key includes MAP_VERSION so mapping changes re-trim.
        """

        async def fetch() -> dict:
            raw = await self._get(FACTS_URL.format(cik=cik))
            taxonomies = raw.get("facts", {})
            gaap = taxonomies.get("us-gaap", {})
            facts: dict[str, dict[str, list]] = {}
            for concept in ALL_CONCEPTS:
                units = gaap.get(concept, {}).get("units")
                if not units:
                    continue
                facts[concept] = {
                    unit: [
                        [f.get("start"), f["end"], f["val"], f.get("fy"), f.get("fp"),
                         f.get("form"), f.get("filed"), f.get("accn")]
                        for f in rows
                        if f.get("form") in _FACT_FORMS
                    ]
                    for unit, rows in units.items()
                }  # fmt: skip
            return {"name": raw.get("entityName"), "taxonomies": sorted(taxonomies), "facts": facts}

        return await self.cache.get_or_fetch(f"edgar:facts:{cik}:{MAP_VERSION}", DAY, fetch)
