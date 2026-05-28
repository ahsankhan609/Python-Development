def func() -> None:
    """
    Demonstrate the use of the nonlocal keyword in Python.

    nonlocal is used inside a nested function to refer to and modify
    a variable from the nearest enclosing function scope.
    """
    x: int = 20  # Outer function local variable.

    def inner_func() -> None:
        nonlocal x  # Refer to x from func().
        x = 50  # Modify the outer x (not a new local variable).
        print("Inner x after modification:", x)

    inner_func()  # Call the inner function.
    print("Outer x after inner_func call:", x)


if __name__ == "__main__":
    func()
