INSERT INTO genres (name)
VALUES ('Horror'), ('Sci-Fi');

INSERT INTO author (name)
VALUES ('Author1'), ('Author2'), ('Author3');

INSERT INTO books (name, genre_id)
VALUES ('Book1', 1), ('Book2', 2), ('Book3', 2);

INSERT INTO book_author (book_id, author_id)
VALUES (1, 1), (2, 3), (2, 2);
