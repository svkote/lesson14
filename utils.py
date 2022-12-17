import json
import sqlite3


def get_film_by_title(title):
    """Возвращает самый свежий фильм по названию"""
    with sqlite3.connect('netflix.db') as conn:
        cursor = conn.cursor()
        query = f'''SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title='{title}'
        ORDER BY release_year DESC'''
        cursor.execute(query)
        res = cursor.fetchone()

    film = {"title": res[0], "country": res[1], "release_year": res[2], "genre": res[3], "description": res[4]}
    return json.dumps(film)


print(get_film_by_title('42 Grams'))
