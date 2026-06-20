"""JSON.

JSON :- JavaScript Object Notation. Data format for storing & exchanging
some information.

- It is inspired by JavaScript. It has same data structure as Numpy.
- All applications use this format to exchange data between client and server.
- It is a text format that is completely language independent.
- It is easy to read and write for humans. It is easy to parse and generate
for machines.
- Every language has its own library to parse and generate JSON data.
- Python has a built-in package called json, which can be used to work
with JSON data.

It is based on two structures:
1. A collection of name/value pairs. In various languages, this is realized
as an object, record, struct, dictionary, hash table, keyed list,
or associative array.
2. An ordered list of values. In most languages, this is realized as an
array, vector, list, or sequence.
3. Use for fetching data from online APIs.
4. It is used in web application.
5. data is saved in .json file format.

Example:
JSON format is like python dictionary
JSON contained a key-value pair
Keys are always enclosed in double quotes
[] is called javascript array in JSON. It is used to store multiple values in a
single variable.
None = null

"""

import json
from pathlib import Path

d = {"name": "shantanu", "age": 22, "is_married": False, "insurance": None}
name = "shantanu"
age = "22"
data = ["shantanu", 22, False, None]
data1 = ("shantanu", 22, False, None)
var = None

json_file: Path = Path(__file__).parent / "data.json"

existing: list[dict] = []
if json_file.exists() and json_file.stat().st_size > 0:
    with json_file.open("r") as f:
        loaded = json.load(f)
    existing = loaded if isinstance(loaded, list) else [loaded]

existing.append(d)

with json_file.open("w") as f:
    json.dump(existing, f, indent=4)
