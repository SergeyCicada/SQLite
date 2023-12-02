import sqlite3

"""Добавление новых значений (Одиночное, множественное)"""

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    query = """
           INSERT INTO books (name, pages_count)
           VALUES ('New book2', 40), ('New book3', 45), ('New book4', 50)

     """

    cursor.execute(query)


"""Обновление данных"""

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    query = """
        UPDATE books
        SET genre = 'None'
        WHERE id=1

     """

    cursor.execute(query)

"""Удаление данных"""

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    query = """
        DELETE FROM books
        WHERE id = 6

     """

    cursor.execute(query)
