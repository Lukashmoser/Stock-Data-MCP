"""Shared httpx GET with retries, rate limiting and error mapping."""

from __future__ import annotations

from typing import Any

import httpx
from aiolimiter import AsyncLimiter
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from .errors import NotFound, RateLimited, SourceError


class _Retryable(Exception):
    pass


async def get_json(
    client: httpx.AsyncClient,
    url: str,
    *,
    source: str,
    params: dict[str, Any] | None = None,
    limiter: AsyncLimiter | None = None,
    attempts: int = 3,
) -> Any:
    """GET ``url`` and decode JSON, retrying 429/5xx and transport errors."""

    async def once() -> httpx.Response:
        if limiter is not None:
            async with limiter:
                return await _send(client, url, params)
        return await _send(client, url, params)

    try:
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(attempts),
            wait=wait_exponential(multiplier=0.5, max=8),
            retry=retry_if_exception_type(_Retryable),
            reraise=True,
        ):
            with attempt:
                resp = await once()
    except _Retryable as exc:
        status = exc.args[0] if exc.args else None
        if status == 429:
            raise RateLimited(f"{source} rate limit hit", hint="Wait a minute and retry.") from exc
        raise SourceError(f"{source} unavailable ({status})") from exc

    if resp.status_code == 404:
        raise NotFound(f"{source}: not found ({url})")
    if resp.status_code == 403 and source == "SEC EDGAR":
        raise SourceError(
            "SEC EDGAR refused the request (403)",
            hint="Check SEC_USER_AGENT is set to 'Name email' and request rate is under 10/s.",
        )
    if resp.status_code >= 400:
        raise SourceError(f"{source} error {resp.status_code}: {resp.text[:200]}")
    try:
        return resp.json()
    except ValueError as exc:
        raise SourceError(f"{source} returned non-JSON response") from exc


async def _send(client: httpx.AsyncClient, url: str, params: dict[str, Any] | None) -> httpx.Response:
    try:
        resp = await client.get(url, params=params)
    except httpx.TransportError as exc:
        raise _Retryable(f"network error: {type(exc).__name__}") from exc
    if resp.status_code == 429 or resp.status_code >= 500:
        raise _Retryable(resp.status_code)
    return resp
