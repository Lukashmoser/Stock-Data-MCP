"""Input validation and output sanitizing for tool boundaries.

Tool arguments come from the model, which can be steered by prompt injection.
Keeping every argument to a short, fixed alphabet means they cannot reach other
hosts or paths, and cannot be used to smuggle meaningful amounts of text out to
the upstream APIs.
"""

from __future__ import annotations

import re
from datetime import date

TICKER_PATTERN = r"^\^?[A-Za-z0-9][A-Za-z0-9.\-=]{0,14}$"  # leading ^ for indices (^GSPC)
SERIES_PATTERN = r"^[A-Za-z0-9_]{1,30}$"
FORM_PATTERN = r"^[A-Za-z0-9 \-/]{1,12}$"
DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}$"

_TICKER = re.compile(TICKER_PATTERN)
_SERIES = re.compile(SERIES_PATTERN)
_FORM = re.compile(FORM_PATTERN)
_CONTROL = re.compile(r"[\x00-\x1f\x7f-\x9f\u200b-\u200f\u202a-\u202e\u2060-\u2069]")  # control, zero-width and bidi characters
_SECRET = re.compile(r"(api_key=)[^&\s\"']+", re.IGNORECASE)

MAX_TEXT = 200


def ticker(value: str) -> str:
    v = value.strip()
    if not _TICKER.fullmatch(v):
        raise ValueError("ticker must be 1-15 letters, digits, '.', '-' or '=' (optionally a leading '^')")
    if v.isdigit() and len(v) > 10:
        raise ValueError("CIK must be at most 10 digits")
    return v


def series_id(value: str) -> str:
    v = value.strip()
    if not _SERIES.fullmatch(v):
        raise ValueError("series_id must be 1-30 letters, digits or underscores")
    return v


def form_type(value: str | None) -> str | None:
    if value is None or not value.strip():
        return None
    v = value.strip()
    if not _FORM.fullmatch(v):
        raise ValueError("form_type must be a short SEC form name like 10-K or DEF 14A")
    return v


def iso_date(value: str | None, name: str) -> str | None:
    if value is None or not value.strip():
        return None
    try:
        return date.fromisoformat(value.strip()).isoformat()
    except ValueError:
        raise ValueError(f"{name} must be a date in YYYY-MM-DD format") from None


def clean_text(value: object, limit: int = MAX_TEXT) -> str | None:
    """Third-party text: drop control/bidi characters, collapse whitespace, truncate."""
    if value is None:
        return None
    s = " ".join(_CONTROL.sub(" ", str(value)).split())
    return s if len(s) <= limit else s[: limit - 1] + "…"


def redact(text: str) -> str:
    """Mask API keys that may appear in URLs inside messages or logs."""
    return _SECRET.sub(r"\1***", text)
