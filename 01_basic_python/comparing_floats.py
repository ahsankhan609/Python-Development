def compare_float(a: float, b: float, tol: float) -> bool:
    """
    :param tol: accepts float value
    :param b: accept float value
    :param a: accept float value
    """

    absolute = abs(a - b)
    print(absolute)
    print(f"{a} - {b} = {a - b}")
    return absolute < tol


first = 0.8
second = 0.1 + 0.7096587966654125

if __name__ == "__main__":
    print(compare_float(first, second, tol=1e-10))
