"""База данных создается на локальном диске при первом обращении к ней"""
import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()
