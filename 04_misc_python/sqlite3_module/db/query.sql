CREATE TABLE IF NOT EXISTS books (
    title_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    published_year INTEGER,
    author TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO books (title, published_year, author) VALUES
('The Hunger Games', 2008, 'Suzanne Collins'),
('The Great Gatsby', 1925, 'F. Scott Fitzgerald'),
('The Maze Runner', 2009, 'James Dashner'),
('The Lord of the Rings', 1954, 'J.R.R. Tolkien');

-- SELECT title FROM books WHERE published_year < 1950;

-- SELECT * FROM books;
