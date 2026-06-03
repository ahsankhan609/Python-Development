from typing import Any


def greet_people(*people: str) -> None:
    """
    This function greets people passed as arguments using *args.
    """
    print(people)  # people is a tuple
    print("*" * 25)
    for name in people:
        print(f'Hello {name}!')  # we can iterate over the tuple


def do_something(**kwargs: Any) -> None:
    """
    This function does something with the arguments passed as kwargs.
    """
    print(kwargs)  # kwargs is a dictionary
    print("*" * 25)
    for key, value in kwargs.items():  # we can iterate over the dictionary and print the key and value
        print(f'{key}: {value}')


def standard_arg(arg: Any) -> None:
    """
    This function prints the argument passed to it.
    """
    print(arg)


def pos_only_arg(arg1: Any, arg2: Any, /) -> None:
    """
    This function prints only the positional argument passed to it.
    Positional-only parameters are specified with a slash (/) before the parameter name.
    """
    print(arg1, arg2)


def kwd_only_arg(*, arg: Any) -> None:
    """
    This function prints only the keyword argument passed to it.

    Keyword-only parameters are specified with an asterisk (*) before the parameter name.
    Here, to access the argument, we need to explicitly use the keyword argument syntax.
    """
    print(arg)


def combined_example(pos_only: Any, /, standard: Any, *, kwd_only: Any) -> None:
    """
    This function prints the positional, standard, and keyword arguments passed to it.

    Positional-only parameters are specified with a slash (/) before the parameter name.

    Keyword-only parameters are specified with an asterisk (*) before the parameter name.

    Here, to access the argument, we need to explicitly use the keyword argument syntax.
    """
    print(pos_only, standard, kwd_only)


if __name__ == '__main__':

    # we can pass as many arguments as we want
    greet_people('Mario', 'Luigi', 'Peach', 'Toad', 'Bowser')

    # kwargs is a dictionary
    print(do_something(name='Mario', age=25, city='New York'))

    # standard argument
    standard_arg(10)

    # positional-only argument
    pos_only_arg(10, 20)

    # keyword-only argument
    kwd_only_arg(arg=10)

    # combined example
    combined_example(10, 20, kwd_only=40)
