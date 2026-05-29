# NOTE: https://www.geeksforgeeks.org/python/python-docstrings/
# NOTE: Example of Google Style Docstring: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
# NOTE : https://realpython.com/how-to-write-docstrings-in-python/
# NOTE: https://realpython.com/documenting-python-code/
# NOTE: https://note.nkmk.me/en/python-docstring/
# NOTE: type checking for python code - https://www.youtube.com/watch?v=2xWhaALHTvU
# NOTE: Document Python Code with ChatGPT - https://realpython.com/document-python-code-with-chatgpt/

# INFO: Follow conventions for one-line and multiline docstrings described in PEP 257
# INFO: According to PEP 8, comments should have a maximum length of 72 characters.
# INFO: Type hinting was added to Python 3.5 and is an additional form to help the readers of your code

# NOTE: reST(Restructured Text) is a lightweight markup language used for writing plain text.
# It's the default formatting style for inline documentation in Python, as outlined in PEP 287, and is used with tools like Sphinx to generate documentation.

# TODO: Run following command in terminal to see the docstring of the module:
# """uv run -m pydoc write_better_docstrings.py"""

"""
    Docstrings (Documentation Strings) are special strings used to document Python code. They provide a description of what a module, class, function or method does.

    Declared using triple quotes (' ' ' or " " ").
    Written just below the definition of a function, class, or module.
    Unlike comments (#), docstring can be accessed at runtime using __doc__ or help().
"""


def greet(name: str) -> str:
    """
    This function greets the user by their name. It returns a greeting message.

    Args:
        name (str) - The name of the user.

    Returns:
        str - A greeting message for the user.
    """
    return f"Hello, {name}!"


"""
    Google Style Docstring:

    Google style docstrings follow a specific format and are inspired by Google's documentation style guide. They provide a structured way to document Python code, including parameters, return values and descriptions.
"""


def multiply(a: int, b: int) -> int:
    """
    Multiply two given numbers and return the product.

    Args:
        a (int) - first number.
        b (int) - second number.

    Returns:
        int - product of a and b.
    """
    return a * b


"""
    Numpydoc Style Docstrings:
    
    Numpydoc-style docstrings are widely used particularly for documenting functions and classes related to numerical computations and data manipulation. It is an extension of Google-style docstrings, with some additional conventions for documenting parameters and return values.
"""


def divide_two_numbers(a: float, b: float) -> float:
    """
    Divide two given numbers and return the quotient.

    Parameters
    ----------
    a : float - dividend.
    b : float - divisor.

    Returns
    -------
    float - quotient of division of a by b.
    """
    if b == 0:
        raise ValueError("Division by zero not allowed.")
    return a / b


"""
    Docstrings for Functions:
    
    Functions are common in most codebases, so writing clear and informative docstrings for them is essential. A good function docstring should provide a summary of what the function does, along with details about its parameters, return values, and exceptions, if any. Here’s an example:
"""


def enchant_wand(wand_type: str, level: int = 1) -> str:
    """
    Enhance a wand with magical properties.

    Args:
        wand_type (str) - The type of wand to enchant.
        level (int, optional) - The enchantment level. Defaults to 1.

    Returns:
        str - A message confirming the enchantment.

    Raises:
        ValueError: If the enchantment level is invalid.
    """
    if level < 1:
        raise ValueError("Enchantment level must be at least 1.")
    return f"{wand_type.capitalize()} enchanted to level {level}!"


def func() -> None:
    """
    This function does nothing. 

    Returns:
        None - This function returns nothing.
    """
    pass


if __name__ == "__main__":
    print("using __doc__: ", greet.__doc__)
    print("using help(): ", help(greet))
    print("using docstring: ", greet.__doc__)

    """
    Explanation:
    greet.__doc__: Directly prints the docstring text.
    help(greet): Displays docstring in a structured help format.
    """

    print(f"Result of {3} * {5} : {multiply(3, 5)}")
    print(f"Result of {6} / {2} : {divide_two_numbers(6, 2)}")

    print(f"Result of enchanting wand: {enchant_wand('oak', 30)}")
