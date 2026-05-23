"""Store books titles in a sqlite3 database.

- lite weight, local database. It is a file based database.
- It is a part of python standard library.
- no separate server required
"""

import sqlite3
from pathlib import Path

# let's create a database named books.db and connect with it.
# If the database does not exist, it will be created automatically.
db_path: Path = Path(__file__).parent / "db" / "books.db"
sql_file: Path = Path(__file__).parent / "db" / "query.sql"

with sqlite3.connect(db_path) as connection:
    cursor: sqlite3.Cursor = connection.cursor()

    # executescript() runs all queries in the file at once
    cursor.executescript(sql_file.read_text())

    # Fetch and display results from SELECT query
    # cursor.execute("SELECT title FROM books WHERE published_year < 1950;")
    cursor.execute("SELECT title FROM books WHERE published_year > 1950;")
    records: list[tuple[str]] = cursor.fetchall()
    for record in records:
        print(record)
