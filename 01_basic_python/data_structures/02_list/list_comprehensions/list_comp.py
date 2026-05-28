people: list[str] = ['Mario', 'Luigi', 'Peach']

cap_people: list[str] = [person.upper() for person in people]
print(cap_people)