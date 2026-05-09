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

```
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

## No Test Suite

There are no pytest or unittest test files. `04_misc_python/test.py` is a scratch script, not a test runner.
