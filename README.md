# Learn Python by Doing

A self-study repository organized by skill level, covering Python concepts through Jupyter notebooks and standalone scripts. This is not a production application — notebooks and scripts are the primary learning artifacts.

## Getting Started

Requires [uv](https://docs.astral.sh/uv/) and **Python 3.14**. The virtual environment lives in `.venv/`.

```bash
# Install / sync dependencies
uv sync

# Add a runtime dependency
uv add <package>

# Add a dev-only dependency
uv add --dev <package>

# Run a script
uv run python <file.py>

# Launch Jupyter
uv run jupyter notebook
```

Use `uv` for all package management — do not use `pip` directly.

## Tooling

### Linting & Formatting — Ruff

```bash
# Check for lint errors
uv run ruff check .

# Auto-fix lint errors
uv run ruff check --fix .

# Format code
uv run ruff format .

# Check formatting without writing (CI mode)
uv run ruff format --check .
```

### Type Checking — ty

```bash
# Type-check the whole project
uv run ty check

# Type-check a specific file
uv run ty check <file.py>
```

### Testing — pytest

All tests live in the `tests/` folder at the project root.

```bash
# Run all tests
uv run pytest

# Run a specific test file
uv run pytest tests/<test_file.py>

# Run with verbose output
uv run pytest -v
```

- Name test files `test_<module>.py`.
- Name test functions `test_<what_is_tested>`.
- Do not use `unittest`; write plain `pytest` functions.

## Repository Structure

```text
01_basic_python/        # Strings, lists, list comprehensions, named tuples
02_intermediate_python/ # Error handling, functions/recursion, logging
03_advance_python/      # File I/O, multithreading, regex, type annotations, __name__/__main__
04_misc_python/         # Miscellaneous experiments
05_projects/            # Project work (currently sparse)
tests/                  # All pytest test files
```

Each topic directory typically contains:

- `README.md` with curated learning links (YouTube, docs, blogs)
- `notes.ipynb` for interactive exploration
- `.py` scripts for standalone examples or exercises

## Coding Standards

All `.py` files in this repo follow these conventions.

### Type Annotations (PEP 484 / PEP 526)

- Annotate every function parameter and return type.
- Annotate every variable at the point of assignment when the type is not obvious.
- Use built-in generics (`list[str]`, `dict[str, int]`) — not `typing.List` / `typing.Dict`.

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

## Notes

- `04_misc_python/test.py` is a scratch script, not a test runner.
- `tests/` is the authoritative location for all pytest tests.
