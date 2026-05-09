# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

"Learn Python by Doing" — a self-study repository organized by skill level, covering Python concepts through Jupyter notebooks and standalone scripts. Not a production application; notebooks are the primary learning artifact.

## Package Management & Environment

Uses `uv` (not pip directly) with Python 3.14. Virtual environment lives in `.venv/`.

```bash
# Install dependencies
uv sync

# Run a script
uv run python <file.py>

# Type-check a file
uv run mypy <file.py>

# Launch Jupyter
uv run jupyter notebook
```

## Repository Structure

```text
01_basic_python/        # Strings, lists, list comprehensions, named tuples
02_intermediate_python/ # Error handling, functions/recursion, logging
03_advance_python/      # File I/O, multithreading, regex, type annotations, __name__/__main__
04_misc_python/         # Miscellaneous experiments
05_projects/            # Project work (currently sparse)
```

Each topic directory typically contains:

- `README.md` with curated learning links (YouTube, docs, blogs)
- `notes.ipynb` for interactive exploration
- `.py` scripts for standalone examples or exercises

## Type Annotations

The `03_advance_python/type_annotations_in_Python/` module is actively developed. Run mypy against files there:

```bash
uv run mypy 03_advance_python/type_annotations_in_Python/notes.py
```

## Coding Standards

All `.py` files in this repo must follow these conventions.

### Type Annotations (PEP 484 / PEP 526)

- Annotate every function parameter and return type.
- Annotate every variable at the point of assignment when the type is not obvious.
- Use built-in generics (`list[str]`, `dict[str, int]`) — not `typing.List` / `typing.Dict` (requires Python 3.9+, this repo uses 3.14).

### Docstrings (PEP 257)

- Every module must have a module-level docstring that explains its purpose and, when relevant, key concepts being demonstrated.
- Every function/class must have a docstring.
- One-liner docstrings: use a single line enclosed in triple quotes — `"""Return the sum of x and y."""`
- Multi-line docstrings: summary line, blank line, then body.

### Comments (PEP 8)

- Inline comments: at least two spaces before `#`, one space after — `x = x + 1  # compensate for border`
- Block comments: full sentences, start with a capital letter, end with a period.
- Explain *why*, not *what* — the code already shows what is happening.

### Naming (PEP 8)

- `snake_case` for variables, functions, and module names.
- `PascalCase` for classes.
- `UPPER_CASE` for module-level constants.

## No Test Suite

There are no pytest or unittest test files. `04_misc_python/test.py` is a scratch script, not a test runner.
