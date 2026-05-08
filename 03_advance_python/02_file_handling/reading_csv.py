import csv
from collections import namedtuple

with open("employees.csv", mode="r", encoding="utf-8") as csv_file:
    reader: _reader = csv.reader(csv_file)
    Employee: type[Employee] = namedtuple(
        "Employee", next(reader), rename=True)
    for row in reader:
        employee = Employee(*row)
        print(employee)

# Employee(name='Linda', job='Technical Lead', email='linda@example.com')
# Employee(name='Joe', job='Senior Web Developer', email='joe@example.com')
# Employee(name='Lara', job='Project Manager', email='lara@example.com')
# Employee(name='David', job='Data Analyst', email='david@example.com')
# Employee(name='Jane', job='Senior Python Developer', email='jane@example.com')
