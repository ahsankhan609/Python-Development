# ExceptionGroup — Practical Guide

Here is a practical way to think about `ExceptionGroup`, plus runnable examples in `exception_groups.py`.

## The problem it solves

Before 3.11, batch or parallel work often hid failures:

- **First error wins** — loop stops; you never see the other bad rows.
- **Or you swallow errors** — collect them in a list manually with no standard structure.

`ExceptionGroup` is the standard way to say: *"This operation failed in **multiple places** — here are **all** the reasons."*

Run the examples:

```bash
uv run python 02_intermediate_python/03_error_and_exceptions_handling/exception_groups.py
```

---

## 5 real-life scenarios (in `exception_groups.py`)

### 1. Bulk CSV / user import

**When:** Importing 10,000 users from a spreadsheet.

**Why:** Row 50 has a bad age, row 200 is missing a name, row 891 has `"abc"` as age. You want **all** bad rows in one error, not fix-one-at-a-time.

```python
raise ExceptionGroup("user import failed", row_errors)
```

### 2. Service health checks

**When:** A `/health` endpoint checks Postgres, Redis, and disk space before deploy.

**Why:** Ops needs **every** broken dependency in one report — not just the first timeout.

### 3. Config file validation

**When:** A microservice loads `app.toml`, `db.toml`, `secrets.toml` on startup.

**Why:** Two files missing and one empty — fail fast with a **full** picture.

### 4. `except*` — handle some errors, re-raise others

**When:** Import pipeline: some rows have bad data (`ValueError`), some missing columns (`KeyError`).

**Why:** Log data errors, but let structural errors bubble up.

```python
try:
    import_users(rows)
except* ValueError as group:
    for exc in group.exceptions:
        print(exc)
```

Note: `except*` is **only** for `ExceptionGroup` — regular `except ValueError` does not unwrap nested group members.

### 5. `asyncio.TaskGroup` (production source)

**When:** Fetching user profiles from an API concurrently.

**Why:** Users 2 and 4 fail for different reasons — `TaskGroup` raises an `ExceptionGroup` automatically:

```text
network errors: (ConnectionError('API timeout for user 2'),)
data errors: (ValueError('invalid user payload for user 4'),)
```

This is the most common place you'll see `ExceptionGroup` in real async Python code.

---

## Mental model

| Situation | Use |
|-----------|-----|
| One thing failed | Regular `raise ValueError(...)` |
| Many independent things failed in one operation | `ExceptionGroup("summary", [exc1, exc2, ...])` |
| Handle only some failures in a group | `except* ConnectionError` |
| Async parallel tasks | `asyncio.TaskGroup` (built-in groups) |

---

## Quick API cheat sheet

```python
group = ExceptionGroup("batch failed", [exc1, exc2])
group.exceptions          # tuple of nested exceptions
str(group)                # "batch failed (2 sub-exceptions)"
len(group.exceptions)     # 2
```

Groups can **nest** — an outer group may contain inner groups (common with `TaskGroup` + sub-tasks).

---

All five examples live in `exception_groups.py`. Next steps: add a custom `ImportErrors(ExceptionGroup)` subclass or walk through nested groups step by step.
