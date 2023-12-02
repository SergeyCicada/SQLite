import sqlite3

"""SELECT, FROM, LIMIT, OFFSET"""
with sqlite3.connect("../movie.db") as connection:
    cursor = connection.cursor()
    query = """
               SELECT title, release_year
               FROM movie 
               WHERE genre = 'Фантастика'
               AND rating > 6 

    """
    cursor.execute(query)

    for cinema in cursor.fetchall(): # получение результата из запроса
        print(cinema)


"""
Запрос для проверки вхождения нескольких значений IN
и вывод первых 10 результатов с пропуском в 10 строк

               SELECT title, country
               FROM movie 
               WHERE genre IN ('Фантастика', 'Детектив')
               LIMIT 10
               OFFSET 10
    """

"""
Запрос для проверки вхождения каких либо совпадений по буквам и т.д. LIKE
Типо регулярные выражения

               SELECT title, country
               FROM movie 
               WHERE genre LIKE 'R%' - совпадения с началом R
            
    """

"""
Выборка числовых значений BETWEEN - между

               SELECT title, country
               FROM movie 
               WHERE rating  BETWEEN 6 AND 8

    """

"""
Выборка пустых значений '' тоже значение, IS NOT NULL вообще нет значений

               SELECT title, country
               FROM movie 
               WHERE director != '' AND director IS NOT NULL

    """