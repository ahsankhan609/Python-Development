# FAQ — `lru_caching.py`

## Code Review Summary

### Status
No linter errors, no type errors, no syntax issues.

---

### Minor Issue — `print(fibonacci.cache_clear())`

`cache_clear()` returns `None`. Printing it always outputs `None`, which is misleading.

**Current (line 85):**
```python
print(fibonacci.cache_clear())
```

**Should be:**
```python
fibonacci.cache_clear()  # call only, no need to print
print(fibonacci.cache_info())
```

---

### Commented-out decorator (line 70)

```python
# @lru_cache(maxsize=3)
@expire_cache(seconds=5)
```

Stacking both decorators is wrong because `expire_cache` already wraps internally with `lru_cache(maxsize=3)`.
The comment is kept as a learning reminder of what was previously tried and why it was removed.

---

## How to Interpret the Output

Running the file produces:

```
55
CacheInfo(hits=8, misses=11, maxsize=3, currsize=3)
None
CacheInfo(hits=0, misses=0, maxsize=3, currsize=0)
```

| Line | Value | Meaning |
|------|-------|---------|
| 1st  | `55`  | Result of `fibonacci(10)` |
| 2nd  | `CacheInfo(hits=8, misses=11, maxsize=3, currsize=3)` | Cache stats after the call |
| 3rd  | `None` | Return value of `cache_clear()` — always `None` |
| 4th  | `CacheInfo(hits=0, misses=0, maxsize=3, currsize=0)` | Cache stats after clearing — all zeroed out |

---

## `CacheInfo` Fields Explained

| Field | Meaning |
|-------|---------|
| `hits` | Times the result was found in cache (fast, no recomputation) |
| `misses` | Times the result was NOT in cache and had to be computed |
| `maxsize` | Maximum number of results the cache can hold at once |
| `currsize` | Number of results currently stored in cache |

---

## Why `misses=11` for `fibonacci(10)`?

`fibonacci` calls itself recursively. There are 11 unique values of `n` (0 through 10),
each a cache miss on first call. Subsequent recursive calls to the same `n` are cache hits — hence 8 hits from repeated subproblems.

---

## `expire_cache` vs `lru_cache`

| Decorator | Eviction strategy |
|-----------|------------------|
| `@lru_cache(maxsize=N)` | By cache size only — evicts least recently used when full |
| `@expire_cache(seconds=N)` | By time (TTL) — clears entire cache after `N` seconds on next call; internally also uses LRU |
