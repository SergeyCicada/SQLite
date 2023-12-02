"""JOIN - специальная операция для объединения данных из двух таблиц
INNER JOIN - данные которые есть в обеих таблицах по связи.
LEFT JOIN - всё из основной таблицы и данные по связи.
RIGHT JOIN - данные приорет которых меняется согласно LEFT.
OUTER JOIN - выводим все данные.
"""

import sqlite3

with sqlite3.connect('book_db_2.db') as connection:
    cursor = connection.cursor()

    query = """
            SELECT books.name as 'book_name', genres.name as 'genre_name', author.name, book_author.*
            FROM books
            INNER JOIN genres ON books.genre_id = genres.id
            LEFT JOIN book_author ON books.id = book_author.book_id
            LEFT JOIN author ON book_author.author_id = author.id
     """

    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)
