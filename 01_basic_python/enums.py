"""
it is very important concept in python. which allow us to define the constant value.
for example: a lamp has 2 states.On or Off. so we must have to create those 2 states
manually. either it will be turned_On or turned_Off
"""

from enum import Enum


class LampState(Enum):
    """an example of state."""

    On = 1
    Off = 0


class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


if __name__ == "__main__":
    # lamp1: LampState = LampState(1)
    # print(lamp1)
    # lamp2: LampState = LampState(0)
    # print(lamp2)

    color = Color.GREEN

    if color == Color.RED:
        print(f"Color is {color.value}")
    elif color == Color.BLUE:
        print(f"Color is {color.value}")
    else:
        print(f"Color is {color.value}")
