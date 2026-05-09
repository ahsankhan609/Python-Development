# `__name__` and `__main__` in Python

## Overview

In Python, `__name__` is a special built-in variable that indicates how a module is being run.

## Course resources

- [What is Name Variable in Python - Code-Yug](https://youtu.be/9x48vK-QCfY?si=Uv4GEGadfutjr0Tf) ✅ July 25, 2022
- [If __name__ == "__main__" for Python Developers](https://www.youtube.com/watch?v=NB5LGzmSiCs) ✅ Nov 27, 2022
- [If __name__ == '__main__' for Python Beginners - Indently.io](https://www.youtube.com/watch?v=hZ9rsHdcxtY) ✅ Mar 06, 2023

## How It Works

- When a Python file is **run directly**, `__name__` is set to `"__main__"`
- When a Python file is **imported as a module**, `__name__` is set to the **module's filename** (without `.py`)

## Common Usage

```python
def main():
    print("Running as main script")

if __name__ == "__main__":
    main()
```

## Why It Matters

| Scenario | `__name__` value |
|----------|-----------------|
| Run directly (`python script.py`) | `"__main__"` |
| Imported (`import script`) | `"script"` |

The `if __name__ == "__main__":` guard ensures that certain code (like test runs or script entry points) only executes when the file is run directly, **not** when it is imported by another module.

## Example

**`greet.py`**
```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))  # Only runs when executed directly
```

**`main.py`**
```python
import greet

print(greet.greet("Python"))  # greet() works, but the direct-run block is skipped
```
