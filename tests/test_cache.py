import pytest

from stock_data_mcp.cache import Cache
from stock_data_mcp.errors import NotFound, SourceError


def test_roundtrip_and_expiry(cache: Cache):
    cache.set("k", {"a": [1, 2.5, None]}, ttl=60)
    assert cache.get("k").value == {"a": [1, 2.5, None]}
    cache.set("old", 1, ttl=-1)
    assert cache.get("old") is None
    hit = cache.get("old", allow_expired=True)
    assert hit.value == 1 and hit.stale


async def test_get_or_fetch_caches(cache: Cache):
    calls = 0

    async def fetch():
        nonlocal calls
        calls += 1
        return calls

    assert (await cache.get_or_fetch("k", 60, fetch)).value == 1
    assert (await cache.get_or_fetch("k", 60, fetch)).value == 1
    assert calls == 1


async def test_stale_fallback_on_source_error(cache: Cache):
    cache.set("k", "old", ttl=-1)

    async def boom():
        raise SourceError("down")

    res = await cache.get_or_fetch("k", 60, boom)
    assert res.value == "old" and res.stale

    with pytest.raises(SourceError):
        await cache.get_or_fetch("k", 60, boom, allow_stale=False)


async def test_not_found_is_not_masked_by_stale(cache: Cache):
    cache.set("k", "old", ttl=-1)

    async def missing():
        raise NotFound("gone")

    with pytest.raises(NotFound):
        await cache.get_or_fetch("k", 60, missing)


async def test_no_stale_entry_reraises(cache: Cache):
    async def boom():
        raise SourceError("down")

    with pytest.raises(SourceError):
        await cache.get_or_fetch("missing", 60, boom)


def test_persists_across_instances(tmp_path):
    path = tmp_path / "c.sqlite"
    a = Cache(path)
    a.set("k", "v", ttl=60)
    a.close()
    b = Cache(path)
    assert b.get("k").value == "v"
    b.close()
