import json
import sqlite3


def get_film_by_title(title):
    """Возвращает самый свежий фильм по названию"""
    with sqlite3.connect('netflix.db') as conn:
        cursor = conn.cursor()
        query = f'''SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title='{title}'
        ORDER BY release_year DESC
        LIMIT 1'''
        cursor.execute(query)
        res = cursor.fetchone()

    film = {"title": res[0], "country": res[1], "release_year": res[2], "genre": res[3], "description": res[4]}
    return json.dumps(film)


def get_films_by_realese_year_range(start, finish):
    """Возвращает список фильмов в указанном диапазоне дат выпуска"""
    with sqlite3.connect('netflix.db') as conn:
        cursor = conn.cursor()
        query = f'''SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {start} AND {finish}
        ORDER BY release_year DESC
        LIMIT 100'''
        cursor.execute(query)
        res = cursor.fetchall()

    films = []
    for row in res:
        film = {"title": row[0], "release_year": row[1]}
        films.append(film)

    return films


print(get_films_by_realese_year_range(1900, 2010))
