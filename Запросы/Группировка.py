import sqlite3

"""GROUP BY - объединение повторяющихся значений в группы
SELECT DISTINCT type FROM netflix - вывод уникальных значений"""

with sqlite3.connect("../movie.db") as connection:
    cursor = connection.cursor()
    query = """
               SELECT genre
               FROM movie 
               GROUP BY genre
               
    """
    cursor.execute(query)

    for cinema in cursor.fetchall():  # получение результата из запроса
        print(cinema)


""" Группировка по нескольким значениям

               SELECT genre, country
               FROM movie 
               GROUP BY genre, country
    """

""" Группировка по нескольким значениям с исключением пустого значения

               SELECT genre, country
               FROM movie 
               WHERE  country != ''
               GROUP BY genre, country
    """