"""
An exception is an event which occurs during the execution of program that disrupts the normal flow of program. It is a situation that python can't cope with it.
"""

"""
Why it is dangerous?

- Lead to sudden termination of program.
- Can block the application.
- Data loss problem can occur.
- Corrupt data files
"""
"""
Exception vs Error

. Errors cannot be handled.
. Exceptions can be handled using exception handling syntax.

ex. print ( "hello) # we miss the closing ", so it throw error.
"""
"""
python has 4 blocks for exception handling, and all are keywords:

. try block - code that may raise an exception
. except block - code that will be executed if an exception is raised, due to error in try block
. else block - code that will be executed if no exception is raised and the try block is executed successfully
. finally block - code that will be executed(always) regardless of whether an exception is raised or not. for example: closing a file, closing a database connection, etc.
"""

# let's take an example to understand the exception handling with all 4 blocks:
try:
    # code that may raise an exception
    print("Hello, World!, from try block.")
except:
    # code that will be executed if an exception is raised, due to error in try block
    print("An exception occurred. from except block.")
else:
    # code that will be executed if no exception is raised and the try block is executed
    # successfully
    print("No exception occurred. from else block.")
finally:
    # code that will be executed(always) regardless of whether an exception is raised or not
    # for example: closing a file, closing a database connection, etc.
    print("Finally block executed. from finally block.")

# now let's see when there is an error in try block:
try:
    # code that may raise an exception
    division_by_zero: float = 10 / 0
    print(f"Division result: {division_by_zero}")
    # we are raising an exception manually, so it will raise an exception
    # and go to except block
    raise Exception("This is a test exception.")
except Exception as e:
    # code that will be executed if an exception is raised, due to error in try block
    print(
        f"An exception occurred. from except block. {type(e).__name__}: {e}, is not allowed."
    )
else:
    # code that will be executed if no exception is raised
    # and the try block is executed successfully
    print(
        "No exception occurred. from else block. No error in try block. So this block will not be executed."
    )
finally:
    # code that will be executed(always) regardless of whether an exception is raised or not.
    # for example: closing a file, closing a database connection, etc.
    print(
        "Finally block executed. from finally block. Even if there is an exception, this block will be executed."
    )

    """
    all built-in exceptions are subclasses of Exception class.
    so we can handle all built-in exceptions with a single except block.
    """
