# Functions in Python

---

### Code Resources:
- [Functions in Python - CodeYug](https://www.youtube.com/playlist?list=PLI4OVrCFuY54obnQ2gqfLKsy6l6a_o5dl) ✅
- [Lecture 6 : Functions & Recursion in Python](https://www.youtube.com/watch?v=OvTH-7ESoRA) 📚
- [You should put this in all your Python scripts | if __name__ == '__main__':](https://www.youtube.com/watch?v=g_wlZ9IhbTs)📚
- [49 Useful Built-In Functions in Python](https://www.youtube.com/watch?v=M16LicU5WfM) 📚
- [Why I Explicitly Return “None” In All My Functions (Python)](https://www.youtube.com/watch?v=GSZhXVjuLgA)✅
- [Please Master These 10 Python Functions](https://www.youtube.com/watch?v=kGcUtckifXc) 📚
- [These 12 Python Functions Are Built In (No Imports!)](https://www.youtube.com/watch?v=ho24rK_AYrQ)📚
- [All 71 built-in Python functions](https://www.youtube.com/watch?v=7Qu_KXc7xSI)
- [Functional Programming in Python is Awesome](https://www.youtube.com/watch?v=A7lGxqCuFN4) 📚

---

## LMABDA Function

- [Python Lambda Functions Explained](https://youtu.be/HQNiSfb795A?si=OtKsHZcpkRBSmVb2)
- [Python Lambda Functions??](https://youtu.be/KR22jigJLok?si=8reNpkI8vsBFkRKp)
- It is created using `lambda` keyword
- It is nameless function, that's why called anonymous functions as well

Syntax:-

```python
lambda arg_list:expression/python statement
```

- We can't write multiple python statements or multiple statements. We can write only short python statements
- we can have multiple arguments values, separated by commas,  Such as default argument, Keyword Arguments or Positinal Arguments
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
