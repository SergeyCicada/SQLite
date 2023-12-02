"""Нормальная форма - требования, которые должна выполнять БД, чтобы свести к минимуму ошибки в результатах
выборки или изменения данных
Может проводится в 3 или 6 операций

1НМ
Не должно быть наборов значений в одной строке
Решение
Делим данные на несколько таблиц

2НМ
Все атрибуты должны зависеть от заголовка
Ищем дополнительные связи между столбцами и выделяем их в отдельную таблицу

3НМ
Не должно быть повторяющихся значений, применимых к нескольким записям (повторы по вертикали в столбце)
Ищем повторы и выделяем в отдельную таблицу"""



"""Исходная таблица


CREATE TABLE movies
(   
    snow_id text,
    type text,
    title text,
    director text,
    cast text,
    country text,
    date_added datetime,
    release_year int,
    rating text,
    duration int,
    duration_type text,
    listed_in text,
    description text  
);
    
"""

"""__________________________________________________________________________________"""

""" 1 - нормальная форма

    CREATE TABLE directors
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) not null       
);   

    CREATE TABLE actors
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) not null       
);  

    CREATE TABLE categories
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) not null       
);    

    CREATE TABLE shows
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type text,
    title text, 
    country text,
    date_added datetime,
    release_year int,
    rating text,
    duration int,
    duration_type text,
    description text
);

    CREATE TABLE snow_director
(
    show_id INTEGER,
    director_id INTEGER, 
    FOREIGN KEY (show id) REFERENCES shows(id)  
    FOREIGN KEY (director_id) REFERENCES directors(id)        
); 

    CREATE TABLE snow_actor
(
    show_id INTEGER,
    actor_id INTEGER, 
    FOREIGN KEY (show id) REFERENCES shows(id)  
    FOREIGN KEY (actor_id) REFERENCES actors(id)        
);  

    CREATE TABLE snow_category
(
    show_id INTEGER,
    category_id INTEGER, 
    FOREIGN KEY (show id) REFERENCES shows(id)  
    FOREIGN KEY (category_id) REFERENCES categories(id)        
);        
    
"""
"""__________________________________________________________________________________"""

"""2 НМ, таблица которая осталась от 1НМ

   CREATE TABLE show_duration
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type varchar(100),
    duration integer not null
);


    CREATE TABLE shows
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type text,
    title text, 
    country text,
    date_added datetime,
    release_year int,
    rating text,
    duration_id INTEGER,
    description text,
    FOREIGN KEY (duration_id) REFERENCES shows_duration(id)
);

"""

"""__________________________________________________________________________________"""

"""3 НМ, таблица которая осталась от 2НМ

  CREATE TABLE duration_type
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(100)
);


   CREATE TABLE show_duration
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    duration integer not null,
    FOREIGN KEY (type_id) REFERENCES duration_type(id)
);

  CREATE TABLE show_type
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(100)
);

  CREATE TABLE shows
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    title text, 
    country text,
    date_added datetime,
    release_year int,
    rating text,
    duration_id INTEGER,
    description text,
    FOREIGN KEY (duration_id) REFERENCES shows_duration(id)
    FOREIGN KEY (type_id) REFERENCES shows_type(id)
);

"""