# writing tests with builtin unittest module and pytest

## Course resources

* [Getting Started With Testing in Python - realpython](https://realpython.com/python-testing/) ✅
* [Unittesting in Python - NeuralNine -YouTube](https://youtu.be/UL0opWf3DeM?si=hV3NcXlFMuln9Esi) ✅
* [Unit Testing Your Code with the unittest Module - Corey Schafer - YouTube](https://www.youtube.com/watch?v=6tNS--WetLI) ✅
* [unittest documentation](https://docs.python.org/3/library/unittest.html#module-unittest)
* [assert methods documentation](https://docs.python.org/3/library/unittest.html#assert-methods)
* [PYTEST TUTORIA - youtube](https://www.youtube.com/playlist?list=PLL34mf651faNqwhZEM91zU3c-dcc4dLF0) 📚
* [Own pytest playlist - youtube](https://www.youtube.com/playlist?list=PLB9MjSg-h8wGwSnKcE-QjON_Bfgt2hVU6) 📚
* [pytest Tutorial: Effective Python Testing - realpython](https://realpython.com/pytest-python-testing/) 📚
* [pytest documentation](https://docs.pytest.org/en/stable/) 📚
* [code testing best practices - realpython](https://realpython.com/ref/best-practices/code-testing/) 📚
* [How to Use pytest: A Simple Guide to Testing in Python - freecodecamp](https://www.freecodecamp.org/news/how-to-use-pytest-a-guide-to-testing-in-python/) 📚
* [pytest tutorial - geeksforgeeks](https://www.geeksforgeeks.org/python/pytest-tutorial-testing-python-application-using-pytest/) 📚

### unittesting and mocking

* [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library)
* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock)
* [Using Python's Built-in Tools for Unit Test Parameterization - 4 part series](https://dev.to/lizzzzz/using-pythons-builtin-tools-for-unit-test-parameterization-a-closer-look-at-unittest-subtest-12ca)
* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock)

## Course Outcomes

* how to create a basic test and execute it
* find the bugs in the code
* check for application performance and reliability
* check for security in the code

## Introduction to testing

`unittest` has been built into the **Python standard library** since version **2.1**. You'll probably see it in commercial Python applications and open-source projects.

A unit test is a **smaller test**, one that checks that **a single component operates** such as functions or classes in the right way. A unit test helps you to isolate what is broken in your application and fix it faster. we have to write `unittets` when our codebase is medium to large.

You have just seen two types of tests:

* An **integration test** checks that components in your application operate with each other.
* A **unit test** checks a **small component** in your application.

If you have a fancy modern car, it will tell you when your light bulbs have gone. It does this using a form of **unit test**.

You can write both **integration tests** and **unit tests** in Python. To write a **unit test** for the built-in function `sum()`, you would check the output of `sum()` against a known output.

[simple_test.py](src/simple_test.py)

For example, here's how you check that the `sum()` of the numbers `(1, 2, 3)` equals `6`:

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

This will not output anything on the REPL because the values are correct. But if you change the value of the `sum()` to `7`, you will see the following output:

```python
assert sum([1, 2, 3]) == 7, "Should be 6"
```

`unittest` contains both a testing framework and a test runner. `unittest` has some important requirements for writing and executing tests.

`unittest` requires that:

* You put your tests into classes as methods
-You use a series of special assertion methods in the `unittest.TestCase` class instead of the built-in assert statement
* To convert the earlier example to a `unittest` test case, you would have to:

1. Import `unittest` from the standard library
2. Create a class called TestSum that inherits from the TestCase class
3. Convert the test functions into methods by adding self as the first argument
4. Change the assertions to use the self.assertEqual() method on the TestCase class
5. Change the command-line entry point to call unittest.main()

Follow those steps by creating a new file [test_sum_unittest.py](src/test_sum_unittest.py) with the following code:

```python
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == "__main__":
    unittest.main()
```

## Choosing a Python Test Runner

There are many test runners available for Python. The one built into the Python standard library is called unittest. In this tutorial, you will be using unittest test cases and the unittest test runner. The principles of unittest are easily portable to other frameworks. The three most popular test runners are:

* unittest
* nose or nose2
* pytest

Choosing the best test runner for your requirements and level of experience is important.

```bash
# Run the test from the command line
uv run -m unittest test_sum_unittest.py
```

## How to Write Assertions in Python with unittest

[How to Write Assertions in Python with unittest](https://realpython.com/python-testing/#how-to-write-assertions-in-python)

The final step in writing a test is to check that your program produces the expected output for a given input. This process is called making an **assertion**.

Here are some best practices for **assertions**:

* Ensure your tests are repeatable—run them several times to verify they consistently produce the same results.
* Assert outcomes that are directly related to your **input data**. For example, in the `sum()` test, check that the result **truly equals** the total of the input values, not just a hardcoded number.

The `unittest` framework offers a wide variety of assertion methods to check values, types, and other properties in your tests. Here is a comprehensive list of all available **assertion methods**:

### Equality and Value Assertions

| Method | Equivalent to | Description |
|--------|---------------|-------------|
| `.assertEqual(a, b)` | `a == b` | Check if two values are equal |
| `.assertNotEqual(a, b)` | `a != b` | Check if two values are not equal |
| `.assertAlmostEqual(a, b, places=7)` | `round(a-b, places) == 0` | Check if two numbers are approximately equal |
| `.assertNotAlmostEqual(a, b, places=7)` | `round(a-b, places) != 0` | Check if two numbers are not approximately equal |
| `.assertGreater(a, b)` | `a > b` | Check if a is greater than b |
| `.assertGreaterEqual(a, b)` | `a >= b` | Check if a is greater than or equal to b |
| `.assertLess(a, b)` | `a < b` | Check if a is less than b |
| `.assertLessEqual(a, b)` | `a <= b` | Check if a is less than or equal to b |

### Boolean and None Assertions

| Method | Equivalent to | Description |
|--------|---------------|-------------|
| `.assertTrue(x)` | `bool(x) is True` | Check if value is True |
| `.assertFalse(x)` | `bool(x) is False` | Check if value is False |
| `.assertIsNone(x)` | `x is None` | Check if value is None |
| `.assertIsNotNone(x)` | `x is not None` | Check if value is not None |

### Identity Assertions

| Method | Equivalent to | Description |
|--------|---------------|-------------|
| `.assertIs(a, b)` | `a is b` | Check if a and b refer to the same object |
| `.assertIsNot(a, b)` | `a is not b` | Check if a and b do not refer to the same object |

### Membership Assertions

| Method | Equivalent to | Description |
|--------|---------------|-------------|
| `.assertIn(a, b)` | `a in b` | Check if a is in b |
| `.assertNotIn(a, b)` | `a not in b` | Check if a is not in b |

### Type Assertions

| Method | Equivalent to | Description |
|--------|---------------|-------------|
| `.assertIsInstance(a, b)` | `isinstance(a, b)` | Check if a is an instance of class b |
| `.assertNotIsInstance(a, b)` | `not isinstance(a, b)` | Check if a is not an instance of class b |

### String Assertions

| Method | Description |
|--------|-------------|
| `.assertMultiLineEqual(a, b)` | Compare multi-line strings with detailed diff output |
| `.assertRegex(text, regex)` | Check if regex pattern matches text |
| `.assertNotRegex(text, regex)` | Check if regex pattern does not match text |

### Sequence Assertions

| Method | Description |
|--------|-------------|
| `.assertSequenceEqual(a, b)` | Compare sequences (lists, tuples, etc.) |
| `.assertListEqual(a, b)` | Compare lists |
| `.assertTupleEqual(a, b)` | Compare tuples |
| `.assertSetEqual(a, b)` | Compare sets |
| `.assertDictEqual(a, b)` | Compare dictionaries |

### Exception Assertions

| Method | Description |
|--------|-------------|
| `.assertRaises(exception, callable, *args, **kwargs)` | Check if a specific exception is raised |
| `.assertRaisesRegex(exception, regex, callable, *args, **kwargs)` | Check if exception is raised and message matches regex |
| `.assertWarns(warning, callable, *args, **kwargs)` | Check if a specific warning is issued |
| `.assertWarnsRegex(warning, regex, callable, *args, **kwargs)` | Check if warning is issued and message matches regex |

### Other Assertions

| Method | Description |
|--------|-------------|
| `.fail(msg=None)` | Unconditionally fail the test with optional message |
| `.skipTest(reason)` | Skip the test with given reason |
| `.subTest(msg=None, **params)` | Create a sub-test context for multiple related assertions |

### Example Usage of Common Assertions

[common_assertions - examples](src/common_assertions.py)
