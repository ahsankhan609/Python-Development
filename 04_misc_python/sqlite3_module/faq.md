# SQLite3 Module — FAQ

## Q1. What is `cursor.executescript()` and why is the result assigned to `_`?

`executescript()` takes a string of SQL and runs all the statements in it at once,
separated by semicolons. It is typically used to run a `.sql` file that contains
setup queries such as `CREATE TABLE` and `INSERT INTO`.

```python
_: sqlite3.Cursor = cursor.executescript(sql_file.read_text())
```

The `_` is a Python convention for "I am intentionally discarding this return value."
`executescript()` returns a `Cursor` object, but since the goal is only to execute
the side effects (create tables, insert rows), the return value is not needed.

---

## Q2. What is the difference between `executescript()` and `execute()`?

| | `executescript()` | `execute()` |
|---|---|---|
| Statements | Multiple (from a string or file) | Single |
| Use case | Setup / DDL / bulk inserts | Queries where you need results |
| Return value | Usually discarded (`_`) | Cursor with result set ready for `fetchall()` |

`executescript()` is fire-and-forget. `execute()` begins a read — you must follow
it with `fetchall()`, `fetchone()`, or iteration to retrieve the rows.

---

## Q3. How do `execute()`, `fetchall()`, and the `for` loop work together?

```python
_cursor: sqlite3.Cursor = cursor.execute(
    "SELECT title FROM books WHERE published_year > 1950;")

records: list[tuple[str]] = cursor.fetchall()
for record in records:
    print(record)
```

1. `cursor.execute(...)` sends the SELECT to the database. The cursor now holds
   the result set internally.
2. `cursor.fetchall()` pulls all result rows into a Python list. Each row is a
   `tuple` — since only `title` was selected, each tuple has one element:
   `("Some Book Title",)`.
3. The `for` loop iterates the list and prints each tuple.

---

## Q4. What does the full file do, step by step?

```
main.py runs
  → Build paths to books.db and query.sql (relative to main.py's location)
  → Open (or create) books.db via sqlite3.connect()
    → Create a cursor — the handle for all SQL operations
    → Run query.sql with executescript() — creates table, inserts rows
    → SELECT titles of books published after 1950 with execute()
    → Fetch all matching rows with fetchall()
    → Print each row
  → Context manager closes the connection cleanly
```

---

## Q5. Why use `with sqlite3.connect(...) as connection`?

Using `with` (a context manager) ensures the connection is properly closed when
the block exits, and automatically commits the transaction on success or rolls it
back on error — without needing explicit `connection.commit()` or
`connection.close()` calls.

---

## Q6. What is `Path(__file__).parent / "db" / "books.db"`?

`__file__` is the absolute path of the running script (`main.py`). `.parent` moves
up one level to the `sqlite3_module/` directory. The `/` operator on `Path` objects
joins path segments, so the full expression builds:

```
sqlite3_module/db/books.db
```

This keeps paths relative to the script's own location, so the code works
regardless of where it is run from.
