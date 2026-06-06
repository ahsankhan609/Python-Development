# FAQ — Logging & Errors

## How to fix errors in the `notes.ipynb` logging cell?

**Question:** In `notes.ipynb` (logging levels demo), pull latest docs and fix errors — wrong output, `None` printed, and Ruff warnings. What was wrong?

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# be default it is set to 30 for warning, that's why it is not showing
print(logging.debug("this is a debug message"))
print(logging.info("this is a info message"))
print(logging.warning("this is a warning message"))
print(logging.error("this is a error message"))
print(logging.critical("this is a critical message"))
print(logging.exception("this is an exception message"))
```

**Answer:** Per the [CPython logging tutorial](https://docs.python.org/3/howto/logging.html), the cell had several issues:

| Error | Why it is wrong |
|-------|-----------------|
| `print(logging.debug(...))` | Logging functions return `None` and write to **stderr** themselves — `print()` shows `None` |
| Stale comments ("default is 30") | Misleading once `basicConfig(level=DEBUG)` is set in the same cell |
| `logging.exception()` outside `except` | `exception()` needs an active exception to log a traceback — alone it logs `NoneType: None` |
| Ruff `T201` / `LOG015` | Do not use `print()` for logging; prefer a named logger via `getLogger(__name__)` |

### Why does `print(logging.debug(...))` show `None`?

Logging functions **write to stderr themselves** and return **`None`**. They are not meant to be wrapped in `print()`.

Per the [CPython logging tutorial](https://docs.python.org/3/howto/logging.html), call them directly:

```python
import logging

logging.basicConfig(
    format="%(levelname)s:%(name)s:%(message)s",
    level=logging.DEBUG,
    force=True,
)

logger = logging.getLogger(__name__)

logger.debug("this is a debug message")
logger.info("this is an info message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")
```

### Other fixes in the same cell

| Issue | Fix |
|-------|-----|
| `print(logging.debug(...))` prints `None` | Call `logger.debug(...)` directly |
| `logging.exception()` outside `except` | Use inside `except` so the traceback is captured |

```python
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("this is an exception message")
```

---

## Why do DEBUG and INFO not appear in Jupyter notebook output?

**Question:** After setting `logging.basicConfig(level=logging.DEBUG)`, the cell only shows WARNING, ERROR, CRITICAL — not DEBUG or INFO. Why?

```text
WARNING:__main__:this is a warning message
ERROR:__main__:this is an error message
CRITICAL:__main__:this is a critical message
```

**Answer:** In **Jupyter**, the IPython kernel often configures the root logger **before** your cell runs. If handlers already exist, `logging.basicConfig()` is a **no-op** unless you pass `force=True` (Python 3.8+). The effective level stays at **WARNING (30)**, so DEBUG and INFO are filtered out.

### Fix for notebooks

```python
logging.basicConfig(
    format="%(levelname)s:%(name)s:%(message)s",
    level=logging.DEBUG,
    force=True,  # re-apply config when Jupyter already set up handlers
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
```

After this, re-run the cell. You should see all levels:

```text
DEBUG:__main__:this is a debug message
INFO:__main__:this is an info message
WARNING:__main__:this is a warning message
ERROR:__main__:this is an error message
CRITICAL:__main__:this is a critical message
```

### Key idea

| Context | Default root level | `basicConfig` without `force` |
|---------|-------------------|-------------------------------|
| Plain Python script | WARNING (30) | Works on first call |
| Jupyter / IPython | Often WARNING (30), handlers pre-installed | Ignored — use `force=True` |
