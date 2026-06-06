import math
import random
import sqlite3

math.sqrt(10)
random.random()
sqlite3.connect("abc.db")
# NOQA: E401, F401
# NOQA: F401 is used to ignore the error of the importing un-used imports
# NOQA stands for "No QA" which is a code comment to ignore the error of the importing all statements at once.
