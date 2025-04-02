# Functions in Python

## Mixing multiple types of Arguments

1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Variable length positional arguments
5. Variable length keyword arguments

> Exact order to Follow: positional arguments → variable length positional arguments → keyword arguments → variable length keyword arguments → default arguments

## LMABDA Function

- [Python Lambda Functions Explained](https://youtu.be/HQNiSfb795A?si=OtKsHZcpkRBSmVb2)
- [Python Lambda Functions??](https://youtu.be/KR22jigJLok?si=8reNpkI8vsBFkRKp)
- It is created using `lambda` keyword
- They are nameless functiontion, that's why called annonymous functions as well

Syntax:-

```python
lambda arg_list:expression/python statement
```

- We can't write multiple python statements or multiple statements. We can write only short python statements
- we can have multiple arguments values, seperated by commas,  Such as default argument, Keyword Arguments or Positinal Arguments
- there is no return keyword here, by default it is present here
- So what ever expression will be evaluated, it will be return automatically
- to call lambda function we will use alias. For example: add = lambda a,b:a+b
- Alternatively, using TypeAlias (Python 3.10+):

```python
from typing import TypeAlias

AddFunction: TypeAlias = Callable[[int, int], int]
add: AddFunction = lambda a, b: a + b
```

- If you want a flexible lambda function that can handle both int and float as arguments and also support more than two arguments, you can use variadic arguments (*args) along with TypeVar from typing.

```python
from typing import Callable, TypeVar

T = TypeVar("T", int, float)  # Allows int and float

add: Callable[[T, T], T] = lambda a, b: a + b  # For two arguments

```

- but to support any number of arguments (*args), we need a different approach:

```python
from typing import TypeVar

T = TypeVar("T", int, float)  # Allows only int and float

add: Callable[..., T] = lambda *args: sum(args)  # Accepts multiple arguments

```

> Explanation:
TypeVar("T", int, float): Allows only int and float, preventing unintended types like str.
> Callable[..., T]: Specifies that the function can take any number of arguments (*args).
> lambda *args: sum(args): Uses sum() to add all arguments.

```python
#Example Usage:
print(add(1, 2))          # 3
print(add(1.5, 2.5, 3.0)) # 7.0
print(add(10, 20, 30, 40, 50)) # 150
```
