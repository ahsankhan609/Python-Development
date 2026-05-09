"""
cal.py — Calculator module (the "library" file)

KEY CONCEPT: __name__
---------------------
Every Python file has a built-in variable called __name__.
Python sets its value automatically depending on HOW the file is used:

  1. Run directly  →  __name__ == "__main__"
                      e.g.  `python cal.py`

  2. Imported      →  __name__ == "cal"   (the module's own filename)
                      e.g.  from another file: `from cal import add`

This means we can put code inside the guard below:

    if __name__ == "__main__":
        ...

and it will ONLY execute when this file is the entry-point.
If another file imports cal, that block is completely skipped.
"""


def add(*numbers: float) -> float:
    """Return the sum of x and y."""
    return sum(numbers)


def minus(x: float, y: float) -> float:
    """Return y minus x  (second number minus first number)."""
    return y - x


def multiply(x: float, y: float) -> float:
    """Return the product of x and y."""
    return x * y


# -----------------------------------------------------------------------
# GUARD: this block runs ONLY when you execute `python cal.py` directly.
# When prog.py does `from cal import *`, Python sets cal.__name__ = "cal",
# so the condition below is False and the block is skipped entirely.
# -----------------------------------------------------------------------
if __name__ == "__main__":
    print("Running cal.py directly  ->  __name__ is '__main__'")
    print("This interactive block will execute.\n")

    print("Simple Calculator — enter two numbers to see all operations.")
    x: float = float(input("Number 1: "))
    y: float = float(input("Number 2: "))

    print(f"\nAddition       :  {add(x, y):,.2f}")
    # fixed: was y+x (addition again)
    print(f"Subtraction    :  {minus(x, y):,.2f}")
    print(f"Multiplication :  {multiply(x, y):,.2f}")
