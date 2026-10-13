"""Shared httpx client and GET with retries, rate limiting and error mapping.

The client only talks HTTPS to a fixed set of hosts and never follows
redirects, so neither tool arguments nor a misbehaving upstream can point it
at anything else (e.g. services on localhost).
"""

from __future__ import annotations

import json
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

ALLOWED_HOSTS = frozenset({"www.sec.gov", "data.sec.gov", "api.stlouisfed.org"})
MAX_BODY_BYTES = 150 * 1024 * 1024  # largest companyfacts files are well under this


class BlockedRequest(SourceError):
    """A request to a host outside ALLOWED_HOSTS (or not over HTTPS)."""


async def _enforce_allowlist(request: httpx.Request) -> None:
    if request.url.scheme != "https" or request.url.host not in ALLOWED_HOSTS:
        raise BlockedRequest(f"blocked outbound request to {request.url.scheme}://{request.url.host}")


def make_client(user_agent: str) -> httpx.AsyncClient:
    return httpx.AsyncClient(
        headers={"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"},
        timeout=httpx.Timeout(30.0, connect=10.0),
        follow_redirects=False,
        event_hooks={"request": [_enforce_allowlist]},
    )


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

    async def once() -> tuple[int, bytes]:
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
                status, body = await once()
    except _Retryable as exc:
        status = exc.args[0] if exc.args else None
        if status == 429:
            raise RateLimited(f"{source} rate limit hit", hint="Wait a minute and retry.") from exc
        raise SourceError(f"{source} unavailable ({status})") from exc

    if status == 404:
        raise NotFound(f"{source}: not found ({url})")
    if status == 403 and source == "SEC EDGAR":
        raise SourceError(
            "SEC EDGAR refused the request (403)",
            hint="Check SEC_USER_AGENT is set to 'Name email' and request rate is under 10/s.",
        )
    if 300 <= status < 400:
        raise SourceError(f"{source} answered with a redirect ({status}); redirects are not followed")
    if status >= 400:
        raise SourceError(f"{source} error {status}: {body[:200].decode(errors='replace')}")
    try:
        return json.loads(body)
    except ValueError as exc:
        raise SourceError(f"{source} returned non-JSON response") from exc


async def _send(client: httpx.AsyncClient, url: str, params: dict[str, Any] | None) -> tuple[int, bytes]:
    try:
        async with client.stream("GET", url, params=params) as resp:
            if resp.status_code == 429 or resp.status_code >= 500:
                raise _Retryable(resp.status_code)
            declared = resp.headers.get("Content-Length")
            if declared and declared.isdigit() and int(declared) > MAX_BODY_BYTES:
                raise SourceError(f"response too large ({int(declared) // 2**20} MB)")
            body = bytearray()
            async for chunk in resp.aiter_bytes():
                body += chunk
                if len(body) > MAX_BODY_BYTES:
                    raise SourceError(f"response exceeded {MAX_BODY_BYTES // 2**20} MB")
            return resp.status_code, bytes(body)
    except httpx.TransportError as exc:
        raise _Retryable(f"network error: {type(exc).__name__}") from exc
