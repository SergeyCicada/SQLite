import sqlite3
"""Эти функции вычисляют одно "Собирающее" значение для заданных групп
Например:
посчитать количество строк с разбивкой по жанру фильма или просто посчитать количество строк
Их всего 5

GROUP BY - ключевое слово для агрегации данных
COUNT() - считает количество записей
SUM() - считает сумму всех значений
AVG() - считает среднее арифметическое значение столбца
MIN() и MAX() - определяют минимальное и максимальное значение
AS - присваивает псевдоним для функций, например для сортировки
HAVING - ставится после GROUP BY для проверки значений (так же как WHERE) 
можно применять те же конструкции"""

with sqlite3.connect("../movie.db") as connection:
    cursor = connection.cursor()
    query = """
               SELECT country, SUM(rating) AS AVG_RATING
               FROM movie 
               WHERE genre = 'Драма'
               AND country != ''
               GROUP BY country
               HAVING  AVG_RATING > 5
               ORDER BY AVG_RATING
    """
    cursor.execute(query)

    for cinema in cursor.fetchall():  # получение результата из запроса
        print(cinema)


"""
Считает количество строк в таблице

               SELECT count()
               FROM movie 

    """

"""
Количество фильмов сгруппированных по жанрам
              
               SELECT COUNT(*), genre
               FROM movie 
               GROUP BY genre
    """

"""
Самый первый год выпуска фильма и самый последний

               SELECT MIN(release_year), MAX(release_year)
               FROM movie 
               
    """

"""
Средний рейтинг фильмов по страннам

               SELECT country, AVG(rating)
               FROM movie 
               GROUP BY country

    """