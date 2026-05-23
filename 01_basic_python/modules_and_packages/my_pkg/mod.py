# Several Objects are defined in mod.py

# write a simple string
s: str = "If Comrade Napoleon says it, it must be right."

# write a simple list of integers
a: list[int] = [100, 200, 300]

# define a simple function


def foo(arg: list[str]) -> None:
    print(f"arg = {arg}")

# define a Class definition


class Foo:
    pass


if __name__ == "__main__":
    print(f"from {__name__} file.")
    print("===" * 25)
    print(s)
    print("===" * 25)
    print("===" * 25)
    print(a)
    print("===" * 25)
    foo(["quux", "corge", "grault"])
    print("===" * 25)
    x: Foo = Foo()
    print(x)
    print("===" * 25)
