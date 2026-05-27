"""
Python has many built-in exceptions, such as ValueError, TypeError, IndexError, and about 64 others, but they are all very general. Many times, it can be much better to make tailored exceptions for specific scenarios in your projects.

https://jacobpadilla.com/writing/Custom-Python-Exceptions
"""


class CustomException(Exception):
    """This is a Custom Exception class to raise custom exceptions for specific scenarios in your projects.

    Args:
        Exception (Exception): Exception class
    """
    pass


try:
    raise CustomException("This is a custom exception message.")
except CustomException as e:
    print(e)
