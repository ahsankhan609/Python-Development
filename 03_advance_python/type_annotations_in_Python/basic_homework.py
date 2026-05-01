#Exercise1

text:str = 'Hello Python'
percent:float = 3.14
is_connected:bool = True
people:list[str] = ['mario', 'fuki',' japan']

print("=" * 50)

# Exercise 2
class Fruit:
    def __init__(self, fruit_name:str, fruit_weight_in_grams:float) -> None:
        self.fruit_name:str = fruit_name
        self.grams:float = fruit_weight_in_grams


def return_fruit_description(name:Fruit) -> str :
    return f'This {name.fruit_name} weighs {name.grams} grams.'

apple:Fruit = Fruit ('Apple', 50)
description:str = return_fruit_description(apple)
print(description)

print("=" * 50)

# Exercise 3
def get_user(user_id:int) -> str | None :
    users:dict[int, str] = {0: 'Mario', 1: 'Luigi'}
    return users.get(user_id)

first_user = get_user(0)
print(first_user )
print("=" * 50)
