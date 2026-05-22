# single line comment
# always give a space after # sign for comments

"""
this is an example of multiline comments
"""

'''
this is another example of multiline comments
'''
print('this is example of print statement.')

print("####" * 35)

# creating variables

name: str = "John"
print(name)

print("####" * 35)

# python is case-sensitive language
x: int = 10
X: int = 11
print(x)  # it is different from X
print(X)  # it is different from x
print("####" * 35)


# CONSTANT variables in python
"""python is explainability no way to announce CONSTANT variables, so developers use CAPITAL name for variables,
 when they need to define any CONSTANT variable."""
PI = 3.1415
# we can change it anytime, but we should follow naming convention and don't change it
API_KEY = "hdsfas2439387eoiyqyr326975"

print("####" * 35)

# Data Types

text: str = "this is a text, example of string in python"
positive_number: int = 10  # positing integer
negative_number: int = -10  # negative integer
zero_number: int = 0  # zero integer
# when printed, it is ignored by interpreter
formated_big_number: int = 1_000_000
decimal_number: float = 10.25  # float integer
com_number: complex = 4+8j  # complex number
people_names: list[str] = ["John", "Smith",
                           "Mario", "kuigi"]  # list of strings
cart: list[int] = [10, 20, 30, 40, 50]  # list of integers
another_cart: list[int | float] = [10, 20.25, 30,
                                   40.45, 50, 60.65]  # list of integers and float
lotto_numbers: tuple = (1, 2, 3, 4, 5, 6)  # Tuple
set_of_numbers: set[int] = {1, 2, 3, 4, 5, 6, 6, 5, 9, 1, 2, 3, 8}
frozen_set: frozenset[int] = frozenset({1, 2, 3, 4, 5, 6, 6, 5, 9, 1, 2, 3, 8})

# when we print it in terminal, it will only print unique values if there are same values. and don't keep the order in which we give it data
print(
    f"List of set with unique numbers :{set_of_numbers}. \n List of frozen set with unique numbers :{set_of_numbers}")
range_of_numbers = range(1, 10)  # return a range object of numbers from 1-9
for range_of_number in range_of_numbers:
    print(range_of_number)
dictionary_of_users: dict[str, str] = {
    'user1': "John",
    'user2': "Smith",
    'user3': "Mario",
}  # first way to write dictionary
dict_of_users: dict[str, str] = dict(
    user1="John", user2="Smith", user3="Mario")  # another way to write dictionary
print(dict_of_users['user2'])  # access the value by key

is_connected: bool = True
is_online: bool = False
is_empty = None

#################################################################################################################
print("####" * 35)
print("basic arithmatic operations")
# basic arithmatic operation
num_1: int = 10
num_2: int = 5

add_nums: int = num_1 + num_2
print(add_nums)

subtract_nums: int = num_1 - num_2
print(subtract_nums)

multiply_nums: int = num_1 * num_2
print(multiply_nums)

divide_nums: float | int = num_1 / num_2
print(divide_nums)

# it means when we divide one number to other, what will be remaindered
modulo_nums: int = num_1 % num_2
print(modulo_nums)

exponent_nums: int = num_1 ** num_2
print(f"{exponent_nums:,}")

flow_division_nums: int = num_1 // num_2
print(f"{flow_division_nums:,}")
#################################################################################################################
print("####" * 35)
print("basic comparison operations")
print(id(num_1))
print(id(num_2))

print(num_1 == num_2)  # false, it compares the values of the variables
print(num_1 != num_2)  # true
print(num_1 > num_2)  # true
print(num_1 >= num_2)  # true
print(num_1 < num_2)  # false
print(num_1 <= num_2)  # false
print(num_1 is num_2)  # false, it compares the memory address
#################################################################################################################
print("####" * 35)
print("basic membership operations")
print(another_cart)
print(1 in another_cart)  # returns bool
print(20.25 in another_cart)  # returns bool
print(1 not in another_cart)  # returns bool
print(20.25 not in another_cart)  # returns bool
