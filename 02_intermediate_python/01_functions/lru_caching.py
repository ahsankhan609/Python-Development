"""
Demonstrate the use of the lru_cache decorator in Python.

It caches function results using the Least Recently Used (LRU) strategy.

Learning outcome:

* What caching strategies are available and how to implement them using Python decorators
* What the LRU strategy is and how it works
* How to improve performance by caching with the `@lru_cache` decorator
* How to expand the functionality of the `@lru_cache` decorator and make it expire after a specific time
"""

from functools import lru_cache, wraps
from time import monotonic
from typing import Any, ParamSpec, Protocol, TypeVar, cast
from collections.abc import Callable

P = ParamSpec("P")
R = TypeVar("R")
R_co = TypeVar("R_co", covariant=True)


class CacheableFunction(Protocol[P, R_co]):
    """Callable protocol exposing lru_cache helper methods."""

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R_co:
        ...

    def cache_info(self) -> Any:
        ...

    def cache_clear(self) -> None:
        ...


# let's implement a custom cache decorator that expires after a specific time.


def expire_cache(
    seconds: int,
) -> Callable[[Callable[P, R]], CacheableFunction[P, R]]:
    """Expire a function cache after a given number of seconds."""
    if seconds <= 0:
        raise ValueError("seconds must be greater than 0")

    def decorator(func: Callable[P, R]) -> CacheableFunction[P, R]:
        cached_func: CacheableFunction[P, R] = cast(
            CacheableFunction[P, R],
            lru_cache(maxsize=3)(func),
        )
        expiry_time: float = monotonic() + seconds

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            nonlocal expiry_time
            current_time: float = monotonic()
            if current_time >= expiry_time:
                cached_func.cache_clear()
                expiry_time = current_time + seconds
            return cached_func(*args, **kwargs)

        setattr(wrapper, "cache_info", cached_func.cache_info)
        setattr(wrapper, "cache_clear", cached_func.cache_clear)
        return cast(CacheableFunction[P, R], wrapper)

    return decorator


# @lru_cache(maxsize=3)
@expire_cache(seconds=5)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# NOTE: `maxsize` is the maximum number of results to cache.
# If the number of results exceeds the `maxsize`, the least recently used result is discarded.
# The default value is 128.


if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci.cache_info())
    fibonacci.cache_clear()
    print(fibonacci.cache_info())
