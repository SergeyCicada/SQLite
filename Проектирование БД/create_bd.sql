CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) not null
        );

CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) not null,
            genre_id INTEGER,
            FOREIGN KEY(genre_id) REFERENCES genres(id) ON DELETE SET NULL ON UPDATE CASCADE
        );

CREATE TABLE author (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) not null
        );

CREATE TABLE book_author (
            book_id INTEGER,
            author_id INTEGER,
            PRIMARY KEY (book_id, author_id),
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (author_id) REFERENCES author(id)
        );