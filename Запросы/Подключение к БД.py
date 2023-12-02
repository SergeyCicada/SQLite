import sqlite3

"""Открытие и закрытие сессии"""

connection = sqlite3.connect("../movie.db")  # соединение с БД
cursor = connection.cursor()  # передача команд от приложения в БД
sqlite_create_table_query = """ 
                              SELECT *
                              FROM netflix
                              LIMIT 10
                            """  # запрос
cursor.execute(sqlite_create_table_query)  # выполняем запрос
print(cursor.fetchall())  # выводим результат запроса
connection.close()  # закрываем соединение

"""Через оператор with"""

with sqlite3.connect("../movie.db") as connection:
    cursor = connection.cursor()
    cursor.execute("Команды")


