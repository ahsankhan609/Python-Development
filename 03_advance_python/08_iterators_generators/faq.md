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
