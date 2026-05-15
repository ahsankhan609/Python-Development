from typing import Any


def fact(n: int) -> Any | int:
    return 1 if n == 1 else n * fact(n-1)


if (__name__ == '__main__'):
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))

# python fact.py 6