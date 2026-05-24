# `os.getcwd()` vs `Path.cwd()` — What's the Difference?

Both return the current working directory, but the **type they return** is the key difference:

| | `os.getcwd()` | `Path.cwd()` |
|---|---|---|
| Returns | `str` | `Path` object |
| Joining paths | `os.path.join(cwd, "sub", "file.txt")` | `Path.cwd() / "sub" / "file.txt"` |
| Check existence | `os.path.exists(path)` | `path.exists()` |
| Read a file | `open(os.path.join(...))` | `path.read_text()` |
| Type | Dumb string | Smart object with methods |

---

## The Core Problem with `os` + Strings

```python
# os approach — you're just gluing strings together
cwd = os.getcwd()                          # str
path = os.path.join(cwd, "data", "f.txt") # str
ext  = os.path.splitext(path)[1]          # str — awkward tuple unpack
```

Every operation needs a standalone function call. The string carries no meaning — it's just characters.

---

## The `pathlib` Approach — Object-Oriented

```python
# pathlib approach — the path IS the object
path = Path.cwd() / "data" / "f.txt"  # Path object
ext  = path.suffix                     # ".txt" — just an attribute
name = path.stem                       # "f"
text = path.read_text()               # reads the file directly
```

The `Path` object *knows* it is a path and exposes everything as attributes and methods.

---

## Why `ruff` (and Tools Like It) Flag `os.path`

Ruff rule **`PTH`** (from the `flake8-use-pathlib` plugin) flags `os.path` calls because:

1. **Readability** — `path / "sub"` beats `os.path.join(path, "sub")` every time.
2. **Type safety** — `Path` objects don't silently mix with arbitrary strings. Type checkers can reason about them precisely.
3. **Cross-platform by default** — `Path` automatically uses `PosixPath` on Unix and `WindowsPath` on Windows. No manual `os.sep` juggling.
4. **Fewer imports** — one `from pathlib import Path` replaces `os`, `os.path`, and sometimes `shutil`.
5. **Consistency** — modern Python stdlib (`tempfile`, `zipfile`, `open`) all accept `Path` objects directly.

---

## Rule of Thumb

Use `pathlib` for all new code. The only time you still need `os` is for things `pathlib` doesn't cover:

- `os.environ`
- `os.getpid()`
- `os.rename()` across filesystems
- etc.
