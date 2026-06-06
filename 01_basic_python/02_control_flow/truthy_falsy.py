from typing import Any


def main() -> None:
    """truthy and falsy statements."""
    var1: str = ""
    var2: str = "it returns true because it has some value."
    print(bool(var1))
    print(bool(var2))

    if var1:
        print(var1)
    if var2:
        print(var2)

    """
    let's see some cases where something can be considered false
    """

    empty_string: str = ""
    empty_list: list[Any] = []
    empty_tuple: tuple[()] = ()
    empty_set: set[Any] = set()
    empty_range: range = range(0)

    zero_int: int = 0
    zero_float: float | int = 0.0
    zero_complex: complex | float | int = complex()
    none: None = None


if __name__ == "__main__":
    main()
