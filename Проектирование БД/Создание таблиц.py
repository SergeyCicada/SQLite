"""CREATE TABLE - команда для создания таблицы

Таблицы - books
Столбцы - name, author, description, genre, publication_date, pages_count, price
Первичный ключ - id
Индекс - name
Ограничений:
    - Обязательный name (NOT NULL)
    - pages_count > 0 (CONSTRAINT CHECK - проверка при вставке)
    - genre по умолчанию Undefined

Типы - bit, int, decimal, float, date, time, datetime, varchar

Первичный ключ - столбец, который уникально идентифицирует  строку в таблице

Модификатор AUTOINCREMENT - автоматическое увеличение значения последующей строки на 1

PRIMARY KEY - указывает на уникальность первичного ключа столбца id

Индекс - отсортированный список значений полей, предназначенный для ускорения поиска в базе данных.
Создается отдельно

"""

import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    query = """
            CREATE TABLE books(
            id integer PRIMARY KEY AUTOINCREMENT,
            name varchar(50) NOT NULL,
            author varchar(100),
            description varchar(255),
            genre varchar(20) CONSTRAINT df_genre DEFAULT 'Undefined',
            publication_date date,
            pages_count integer CONSTRAINT ck_pages_count CHECK ( pages_count > 0 ),
            price decimal
        )
    """

    index_query = """
            CREATE INDEX book_name_idx ON books (name)
    """

    cursor.execute(query)
    cursor.execute(index_query)



"""Изменение, добавление, добавление колонок в таблице

ALTER - добавление, изменение, удаление колонок типа данных
RENAME - переименовать"""

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()
    query = """
            ALTER TABLE books RENAME description TO text
    """

    cursor.execute(query)

""" Добавление столбца
 
            ALTER TABLE books 
            ADD publication_country varchar(100) 
               
    """

""" Удаление столбца (не работает в SQLite. Создаём новую таблицу и мигрируем туда данные)

           ALTER TABLE books DROP COLUMN publication_country
        
   """

""" Удаление таблиц

           DROP TABLE books;

   """

