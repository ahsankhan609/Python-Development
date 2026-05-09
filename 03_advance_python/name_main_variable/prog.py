"""
prog.py — Consumer / entry-point file

KEY CONCEPT: what happens when you import a module
--------------------------------------------------
When Python executes  `from cal import *`, it runs cal.py top-to-bottom
BUT it sets  cal.__name__ = "cal"  (not "__main__").

That means the guard in cal.py:

    if __name__ == "__main__":   # -> False when imported
        ...                      # -> this block is SKIPPED

So all the interactive input() prompts inside cal.py will NOT appear.
Only the three functions (add, minus, multiply) are made available here.

Run this file with:   python prog.py
Run cal.py directly:  python cal.py   ← that triggers cal's input block
"""

from cal import add, minus, multiply   # importing brings in the functions only


# This guard makes prog.py follow the same pattern as cal.py:
# the demo code below only runs when YOU execute prog.py directly.
if __name__ == "__main__":
    print("Running prog.py directly  ->  __name__ is '__main__'")
    print("Notice: cal.py was imported but its input() block did NOT run.\n")

    # Hardcoded demo values — no input() needed to prove the concept
    x: float = 10.0
    y: float = 4.0

    print(f"Demo values  ->  x = {x},  y = {y}\n")
    print(f"add(x, y)      = {add(x, y):,.2f}")       # calls cal.add
    print(f"minus(x, y)    = {minus(x, y):,.2f}")     # calls cal.minus  (y - x)
    print(f"multiply(x, y) = {multiply(x, y):,.2f}")  # calls cal.multiply
