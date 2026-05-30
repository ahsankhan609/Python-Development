"""introduced in Python 3.11"""

from typing import Self


class Fruits:
    """Fruit class"""

    def __init__(self, name: str) -> None:
        self.name: str = name

    @classmethod
    def super_fruit(cls, name: str, calories: int) -> Self:
        """

        :param name:
        :param calories:
        :return:
        """
        super_fruit = f"{name}{'!' * calories}"
        return cls(super_fruit)


if __name__ == "__main__":
    fruit: Fruits = Fruits.super_fruit("Apple", 10)
    print(fruit.name)
