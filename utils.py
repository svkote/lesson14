import json
import sqlite3


def sql_connect(query):
    """подключение к БД"""
    with sqlite3.connect('netflix.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
    return res


def get_film_by_title(title):
    """Возвращает самый свежий фильм по названию"""

    query = f'''SELECT title, country, release_year, listed_in, description
    FROM netflix
    WHERE title='{title}'
    ORDER BY release_year DESC
    LIMIT 1'''
    res = sql_connect(query)

    films = []
    for row in res:
        film = {"title": row[0], "country": row[1], "release_year": row[2], "genre": row[3], "description": row[4]}
        films.append(film)
    return films


def get_films_by_realese_year_range(start, finish):
    """Возвращает список фильмов в указанном диапазоне дат выпуска"""
    query = f'''SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN {start} AND {finish}
    ORDER BY release_year DESC
    LIMIT 100'''
    res = sql_connect(query)

    films = []
    for row in res:
        film = {"title": row[0], "release_year": row[1]}
        films.append(film)

    return films


def get_films_by_rating(ratings):
    """Возвращает список фильмов в указанных рейтингах"""
    if ratings == 'family':
        query = f'''SELECT title, rating, description
        FROM netflix
        WHERE rating IN ('G', 'PG', 'PG-13')
        ORDER BY release_year DESC
        LIMIT 100'''
    elif ratings == 'children':
        query = f'''SELECT title, rating, description
        FROM netflix
        WHERE rating='G'
        ORDER BY release_year DESC
        LIMIT 100'''
    else:
        query = f'''SELECT title, rating, description
        FROM netflix
        WHERE rating IN ('R', 'NC-17')
        ORDER BY release_year DESC
        LIMIT 100'''

    res = sql_connect(query)

    films = []
    for row in res:
        film = {"title": row[0], "rating": row[1], "description": row[2]}
        films.append(film)

    return films


def get_films_by_genre(genre):
    """Возвращает список фильмов в указанном жанре"""
    query = f'''SELECT title, description
    FROM netflix
    WHERE listed_in LIKE '%{genre}%'
    ORDER BY release_year DESC
    LIMIT 10'''
    res = sql_connect(query)

    films = []
    for row in res:
        film = {"title": row[0], "description": row[1]}
        films.append(film)

    return films


def get_films_by_type_release_year_genre(type_film, release_year, genre):
    """Возвращает список фильмов в указанном жанре, годе выпуска и типа"""
    query = f'''SELECT title, description
    FROM netflix
    WHERE netflix.type='{type_film}' 
    AND release_year={release_year}
    AND listed_in LIKE '%{genre}%'
    ORDER BY release_year DESC
    LIMIT 100'''
    res = sql_connect(query)

    films = []
    for row in res:
        film = {"title": row[0], "description": row[1]}
        films.append(film)

    return films


# print(get_films_by_type_release_year_genre('TV Show', 2020, 'TV Comedies'))
