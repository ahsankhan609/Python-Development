# FAQ — Iterators & Generators

## Which built-in iterators are available in Python by default?

Python gives you iterators in a few layers — it helps to separate them.

### Built-in functions that return iterators

These are lazy: they produce values on demand.

| Function | What it yields |
|----------|----------------|
| `iter(obj)` | Iterator over any iterable |
| `enumerate(iterable)` | `(index, item)` pairs |
| `zip(*iterables)` | Items from multiple iterables |
| `map(func, iterable)` | `func(item)` for each item |
| `filter(func, iterable)` | Items where `func(item)` is true |
| `reversed(seq)` | Items in reverse order |
| `open(path)` | One line at a time when you loop |

Generator expressions also return iterators:

```python
(x * 2 for x in range(5))  # generator object
```

### Built-in iterables (you call `iter()` on them)

These are not iterators themselves, but each gives you one when you loop or call `iter()`:

- `list`, `tuple`, `str`
- `dict` (and `.keys()`, `.values()`, `.items()`)
- `set`, `frozenset`
- `range`
- `bytes`, `bytearray`
- `memoryview`

Example:

```python
it = iter([1, 2, 3])   # list_iterator
it = iter("hello")     # str_iterator
it = iter(range(10))   # range_iterator
```

### Iterator protocol (what makes something an iterator)

An iterator has both:

- `__iter__()` → returns `self`
- `__next__()` → returns the next value (or raises `StopIteration`)

```python
nums = iter([10, 20, 30])
next(nums)  # 10
next(nums)  # 20
```

### `itertools` (stdlib, not built-in without import)

Very common for iterators, but you must import:

```python
from itertools import chain, islice, cycle, count, permutations
```

### Quick mental model

| Category | Examples |
|----------|----------|
| **Lazy iterator factories** | `map`, `filter`, `zip`, `enumerate`, `reversed`, generators |
| **Iterables → iterators** | `list`, `str`, `dict`, `set`, `range`, files |
| **Stdlib iterator toolbox** | `itertools` module |

**Summary:** There is no single fixed list of "iterator types" in one place — you get iterators from built-in functions like `map`/`zip`/`enumerate`, from `iter()` on built-in iterables, from generator expressions, and from `itertools` after import. The core ones to remember for everyday use are `iter`, `enumerate`, `zip`, `map`, `filter`, `reversed`, file iteration, and generator expressions.

## Why does `next(gen_obj)` raise `StopIteration` after `list(gen_obj)`?

**Question:** In `generator_02.ipynb`, why is there an error on the line that calls `next()` after `list()`?

```python
gen_obj = my_gen_func()
print(list(gen_obj))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(next(gen_obj))   # StopIteration — why?
```

**Answer:** The error is `StopIteration`, and it is expected given the order of those lines.

A generator is a **one-time iterator**. It keeps internal state: each `next()` call or loop advances it, and values are not replayed.

When `list(gen_obj)` runs, it **fully consumes** the generator — it pulls every remaining value (`0` through `9`) until nothing is left. After that, the generator is **exhausted**.

Calling `next(gen_obj)` on an exhausted generator has nothing left to return, so Python raises `StopIteration`. Per the [CPython docs](https://docs.python.org/3/howto/functional.html), that is the normal signal that iteration is finished.

```text
next(gen_obj)  → 0
next(gen_obj)  → 1
...
next(gen_obj)  → 9
next(gen_obj)  → StopIteration   # no more values
```

The comment `# 0` on the `next()` line would only be correct if `next()` ran **before** `list()` drained the generator.

### Key idea

| Action | Effect |
|--------|--------|
| `next(gen_obj)` | Returns one value, advances state |
| `list(gen_obj)` | Drains **all remaining** values |
| `next()` after exhaustion | Raises `StopIteration` |

Unlike a `list`, you cannot rewind a generator — call `my_gen_func()` again to get a fresh one.

### Correct demo order

```python
gen_obj = my_gen_func()

# next() fetches one value at a time; each call advances the generator.
print(next(gen_obj))  # 0
print(next(gen_obj))  # 1

# list() drains the rest of the generator in one go.
print(list(gen_obj))  # [2, 3, 4, 5, 6, 7, 8, 9]

# After a generator is exhausted, next() raises StopIteration.
try:
    next(gen_obj)
except StopIteration:
    print("StopIteration — generator has no more values")
```
