import sqlite3

"""ORDER BY-ключевое слово для сортировки данных по конкретному столбцу
ASC - сортировка от меньшего к большему
DESC - сортировка от большего к меньшему"""

with sqlite3.connect("../movie.db") as connection:
    cursor = connection.cursor()
    query = """
               SELECT title, release_year
               FROM movie 
               ORDER BY release_year ASC
               LIMIT 5

    """
    cursor.execute(query)

    for cinema in cursor.fetchall():  # получение результата из запроса
        print(cinema)

""" Комбиинированная сортировка по нескольким столбцам
               SELECT title, release_year
               FROM movie 
               ORDER BY release_year ASC, rating ASC
               LIMIT 5

    """
