# Error Handling - Exception Handling In Python - try except finally else

## Course resources

* [Complete Error Handling in just 2 hours - Mayank Aggarwal - YouTube](https://www.youtube.com/watch?v=zu9Hc9aSWFc) ✅
* [YT Video resource to practice - Mayank Aggarwal](https://github.com/mayank953/Youtube/tree/main/Error%20Handling) ✅
* [Exception handling in python - Code-Yug](https://www.youtube.com/playlist?list=PLI4OVrCFuY54VPjKLvwdOj7ToznPIhSaj) ✅
* [Blog - Exception Handling in Python - Programiz](https://www.programiz.com/python-programming/exception-handling) 📚
* [Python Exception Handling (Use Try..Except to Catch Errors!) - Programiz](https://www.youtube.com/watch?v=brICUKrzVR0) ✅
* [Blog - Python Custom Exceptions: How to Create and Organize Them](https://jacobpadilla.com/writing/Custom-Python-Exceptions) ✅
* [Python's raise: Effectively Raising Exceptions in Your Code - realpython](https://realpython.com/python-raise-exception/) 📚

```python
# my code example

# import traceback
from collections import namedtuple

columns = "_id name class name"

try:
    Passenger = namedtuple("Passenger", columns)
    print(Passenger)
except Exception as e:
    print("You Encounter with ", type(e).__name__, ":",  e)
    # You Encounter with  ValueError : Type names and field names cannot be a keyword: 'class'
    # traceback.print_exc() # it will print all errors, helpfull in multiple errors
```
