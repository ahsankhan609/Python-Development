# https://youtu.be/KB_LuxEbVuI?si=bb2qBvAOX95KC824

name: str = "John"

# python is case-sensitive language
x: int = 10
X: int = 11

miles: float = 100.0
kilometers: float = miles * 1.60934

# CONSTANT variables in python
"""python is explainability no way to announce CONSTANT variables, so developers use
CAPITAL name for variables when they need to define any CONSTANT variable.
"""
PI: float = 3.1415
# we can change it anytime, but we should follow naming convention and don't change it

# another way to define CONSTANT variables
API_KEY = "hdsfas2439387eoiyqyr326975"

# chained assignment
var1, var2, var3 = 10, 20, 30

# chained assignment with type annotation
var1: int
var2: int
var3: int
var1, var2, var3 = 10, 20, 30

# boolean variables
is_connected: bool = True
is_online: bool = False

# none variables
is_empty: None = None

if __name__ == "__main__":
    print(name)
    print(x)
    print(X)
    print(miles)
    print(kilometers)
    print(PI)
    print(API_KEY)

    print(is_connected)
    print(is_online)
    print(is_empty)

    print(var1)
    print(var2)
    print(var3)
