# `__name__` and `__main__` in Python

## Overview

In Python, `__name__` is a special built-in variable that indicates how a module is being run.

## Course resources

- [What is Python's Main Function Useful For? - NeuralNine](https://www.youtube.com/watch?v=lVUOrPunRxQ)📚 Sep 09, 2021
- [if __name__ == '__main__' for Python beginners - Brocode](https://www.youtube.com/watch?v=8A0E1dSyjFM)
- [What is Name Variable in Python - Code-Yug](https://youtu.be/9x48vK-QCfY?si=Uv4GEGadfutjr0Tf) ✅ July 25, 2022
- [If __name__ == "__main__" for Python Developers](https://www.youtube.com/watch?v=NB5LGzmSiCs) ✅ Nov 27, 2022
- [If __name__ == '__main__' for Python Beginners - Indently.io](https://www.youtube.com/watch?v=hZ9rsHdcxtY) ✅ Mar 06, 2023
- [You should put this in all your Python scripts](https://www.youtube.com/watch?v=g_wlZ9IhbTs) 📚 July 24, 2021
- ["__new__ VS __init__" In Python - Indently.io](https://www.youtube.com/watch?v=Anw4F1jM3BU) 📚 June 08, 2023

## How It Works

- When a Python file is __run directly__, `__name__` is set to `"__main__"`
- When a Python file is __imported as a module__, `__name__` is set to the __module's filename__ (without `.py`)

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

The `if __name__ == "__main__":` guard ensures that certain code (like test runs or script entry points) only executes when the file is run directly, __not__ when it is imported by another module.

## Example

__`greet.py`__

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))  # Only runs when executed directly
```

__`main.py`__

```python
import greet

print(greet.greet("Python"))  # greet() works, but the direct-run block is skipped
```
