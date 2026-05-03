from typing import Callable

# LAMBDA Function:
'''
Explanation:
# from typing import Callable
Callable[[int, int], int]: This tells Python that add is a function that takes two int arguments and returns an int.
'''

add: Callable[[int, int], int] = lambda a, b: a + b

if __name__ == "__main__":
    print(add(10, 20))  # usage of lambda function
    print((lambda a, b: a * b)(4, 5))  # another way to use lambda
