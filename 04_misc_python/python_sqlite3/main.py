"""
Store books titles in a sqlite3 database.
"""
import sqlite3

# lite weight, local database. It is a file based database.
# It is a part of python standard library.
# no separate server required

# to store titles in database, we will create a list of tuples.
# Each tuple will contain id and title of the book.
titles: list[tuple[int, str]] = [
    (1, "Quran"),
    (2, "The Hunger Games"),
    (3, "The Great Gatsby"),
    (4, "The Maze Runner"),
    (5, "The Lord of Rings"),
]

# let's create a database named books.db and connect with it.
# If the database does not exist, it will be created automatically.

with sqlite3.connect("books.db") as connection:
    cursor: sqlite3.Cursor = connection.cursor()

    # execute() method is used to execute sql commands and queries.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT
    )
    """)

    # insert data into the books table
    # Use executemany to insert all rows at once and keep operations inside the
    # connection context so the transaction is committed on exit.
    cursor.executemany(
        "INSERT OR IGNORE INTO books (book_id, title) VALUES (?, ?)", titles
    )
