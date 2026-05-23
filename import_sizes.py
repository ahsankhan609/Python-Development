"""Analyze Python imports and report package on-disk sizes.

Parses import / from ... import ... statements from:
    . py files
    . ipynb notebooks
    . directories of Python sources

. Resolves local modules and installed packages
. Prints package on-disk size and location

Usage:
    for whole folder:
    >>> uv run import_sizes.py path/to/folder
    for single file:
    >>> uv run import_sizes.py path/to/file.py
    for notebook:
    >>> uv run import_sizes.py path/to/notebook.ipynb
    """
from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import sys
from pathlib import Path


def parse_python_file(path: Path) -> str:
    """Read a Python file and return its source code as a string."""
    return path.read_text(encoding="utf-8")


def parse_ipynb(path: Path) -> str:
    """Read a Jupyter notebook and return the concatenated source from code cells.

    Non-code cells are ignored.
    """
    notebook = json.loads(path.read_text(encoding="utf-8"))
    cells = notebook.get("cells", [])
    source_lines = []
    for cell in cells:
        if cell.get("cell_type") != "code":
            continue
        source = cell.get("source", [])
        source_lines.extend(source)
        source_lines.append("\n")
    return "".join(source_lines)


def extract_import_names(source: str) -> set[str]:
    """Return the set of top-level imported module names from Python source."""
    tree = ast.parse(source)
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            if module:
                imports.add(module.split(".")[0])
    return imports


def format_bytes(size: int) -> str:
    """Format a size in bytes into a human-readable string."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024 or unit == "GB":
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} GB"


def get_package_location(name: str, extra_paths: list[Path] | None = None) -> tuple[str, str | None] | None:
    """Resolve an import name to its package location or built-in marker.

    If the module is a local package, extra_paths may be inserted into sys.path
    temporarily to allow resolution from the analyzed source path.
    """
    original_sys_path = list(sys.path)
    try:
        if extra_paths:
            for extra in reversed(extra_paths):
                sys.path.insert(0, str(extra))
        spec = importlib.util.find_spec(name)
    finally:
        sys.path[:] = original_sys_path
    if spec is None:
        return None
    origin = spec.origin
    if origin is None:
        return (name, "built-in or frozen module")
    if origin in {"built-in", "frozen"}:
        return (name, origin)
    if spec.submodule_search_locations:
        return (name, str(Path(spec.submodule_search_locations[0]).resolve()))
    return (name, str(Path(origin).resolve()))


def compute_size(path: Path) -> int:
    """Return the total size in bytes of a file or directory recursively."""
    if not path.exists():
        return 0
    if path.is_file():
        return path.stat().st_size
    total = 0
    for child in path.rglob("*"):
        try:
            if child.is_file():
                total += child.stat().st_size
        except OSError:
            continue
    return total


def analyze_path(path: Path, show_all: bool) -> None:
    """Analyze imports in a path and print a package size report.

    The path may be a .py file, .ipynb notebook, or directory. Local source
    directories are included so local modules can resolve correctly.
    """
    source = ""
    search_paths: list[Path] = []
    if path.is_dir():
        for child in path.rglob("*.py"):
            source += parse_python_file(child) + "\n"
        for child in path.rglob("*.ipynb"):
            source += parse_ipynb(child) + "\n"
        search_paths.append(path)
    elif path.suffix == ".py":
        source = parse_python_file(path)
        search_paths.append(path.parent)
    elif path.suffix == ".ipynb":
        source = parse_ipynb(path)
        search_paths.append(path.parent)
    else:
        raise ValueError("Only .py, .ipynb, or directory paths are supported.")

    imports = sorted(extract_import_names(source))
    if not imports:
        print("No imports found.")
        return

    rows: list[tuple[str, str, int | None]] = []
    for name in imports:
        info = get_package_location(name, extra_paths=search_paths)
        if info is None:
            if show_all:
                rows.append((name, "not found", None))
            continue
        pkg_name, location = info
        if location is None or location in {"built-in or frozen module", "built-in", "frozen"}:
            if show_all:
                rows.append(
                    (pkg_name, location or "built-in or frozen module", None))
            continue
        size = compute_size(Path(location))
        rows.append((pkg_name, location, size))

    if not rows:
        print("No importable packages found.")
        return

    rows.sort(key=lambda row: row[2] or 0)
    print(f"Import size report for: {path}")
    print("Package".ljust(25) + "Size".rjust(12) + "  Location")
    print("-" * 80)
    for pkg_name, location, size in rows:
        size_text = format_bytes(size) if size is not None else "-"
        print(f"{pkg_name.ljust(25)}{size_text.rjust(12)}  {location}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Report on-disk sizes for packages imported by a Python file or notebook."
    )
    parser.add_argument(
        "path", type=str, help="Path to a .py file, .ipynb notebook, or directory to analyze.")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Include built-in/frozen modules and imports that cannot be resolved to disk sizes.",
    )
    args: argparse.Namespace = parser.parse_args()

    target_path: Path = Path(args.path).expanduser().resolve()
    if not target_path.exists():
        raise SystemExit(f"Path does not exist: {target_path}")

    try:
        analyze_path(target_path, show_all=args.all)
    except Exception as exc:
        raise SystemExit(f"Error: {exc}")
