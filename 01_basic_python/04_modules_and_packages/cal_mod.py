# local imports

from my_pkg import A, fact, mod

if __name__ == "__main__":

    print(A)

    print("===" * 25)
    print(f"from {__name__} file.")
    print("===" * 25)

    print(mod.s)
    print("===" * 25)

    print(mod.a)
    print("===" * 25)

    mod.foo(["grault"])
    print("===" * 25)

    x: mod.Foo = mod.Foo()
    print(x)
    print("===" * 25)

    print(fact.fact(6))
    print("===" * 25)
