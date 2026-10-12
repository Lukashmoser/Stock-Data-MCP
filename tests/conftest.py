import json
from pathlib import Path

import httpx
import pytest

from stock_data_mcp.cache import Cache
from stock_data_mcp.sources.edgar import Edgar
from stock_data_mcp.sources.fred import Fred

FIXTURES = Path(__file__).parent / "fixtures"


def load(name: str):
    return json.loads((FIXTURES / name).read_text())


@pytest.fixture
def cache(tmp_path):
    c = Cache(tmp_path / "cache.sqlite")
    yield c
    c.close()


@pytest.fixture
async def http():
    async with httpx.AsyncClient(headers={"User-Agent": "Test test@example.com"}) as client:
        yield client


@pytest.fixture
def edgar(http, cache):
    return Edgar(http, cache, max_rps=1000)


@pytest.fixture
def fred(http, cache):
    return Fred(http, cache, api_key="test-key")
