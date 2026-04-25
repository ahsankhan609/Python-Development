## Error Handling - Exception Handling In Python - try except finally else

* [Youtube Video](https://www.youtube.com/watch?v=zu9Hc9aSWFc)
* [GIT Repo](https://github.com/mayank953/Youtube/tree/main/Error%20Handling)
* [Blog](https://www.programiz.com/python-programming/exception-handling)
* [Blog - Explaination](https://www.youtube.com/watch?v=brICUKrzVR0)

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