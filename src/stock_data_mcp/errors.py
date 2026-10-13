"""Exceptions raised by data sources and turned into tool errors by the server."""


class SourceError(Exception):
    """An upstream data source failed or returned something unusable."""

    def __init__(self, message: str, hint: str | None = None):
        super().__init__(message)
        self.hint = hint


class NotFound(SourceError):
    """The requested ticker, series, or data does not exist."""


class RateLimited(SourceError):
    """The upstream rejected the request for exceeding its rate limit."""
