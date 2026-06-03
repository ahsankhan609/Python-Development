"""it is very important concept in python. which allow us to define the constant value.

for example: a lamp has 2 states.On or Off.
so we must have to create those 2 states manually.
either it will be turned_On or turned_Off.
"""

# https://youtu.be/TAMbq0iRUsA
from enum import Enum


class LampState(Enum):
    """an example of state."""

    On = 1
    Off = 0


class Color(Enum):
    """Simple Color class."""

    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


if __name__ == "__main__":
    # lamp1: LampState = LampState(1) #noqa: ERA001
    # print(lamp1) # noqa: ERA001
    # lamp2: LampState = LampState(0) #noqa: ERA001
    # print(lamp2)  # noqa: ERA001

    color = Color.GREEN

    if color in (Color.RED, Color.BLUE):
        print(f"Color is {color.value}")
    else:
        print(f"Color is {color.value}")
