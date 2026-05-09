def add(x: float, y: float) -> float:
    return x+y


def minus(x: float, y: float) -> float:
    return y-x


def multipl(x: float, y: float) -> float:
    return x*y


if __name__ == "__main__": # it will run this module when it is called upon
    print(f"this is a scimple calcualtor. provide values to perform actions")
    x: float = float(input("Number 1: "))
    y: float = float(input("Number 2: "))

    print(f"Addition of your Numbers is: {x+y:,.2f}")
    print(f"Minus Second value form first of your Numbers is: {y+x:,.2f}")
    print(f"Multiplication of your Numbers is: {x*y:,.2f}")
