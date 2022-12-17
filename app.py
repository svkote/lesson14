from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def page_by_title(title):
    film_json = get_film_by_title(title)
    return render_template('by_title.html', film=film_json)
    # return film_json


@app.route('/movie/<int:start>/to/<int:finish>')
def page_by_year(start, finish):
    films = get_films_by_realese_year_range(start, finish)
    return render_template('by_year.html', films=films)
    # return films


@app.route('/rating/<rating>')
def page_by_rating(rating):
    films = get_films_by_rating(rating)
    return render_template('by_rating.html', films=films)
    # return films


@app.route('/genre/<genre>')
def page_by_genre(genre):
    films = get_films_by_genre(genre)
    return render_template('by_genre.html', films=films)
    # return films


@app.errorhandler(404)
def route_not_found(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def internal_server_error(error):
    return f"На сервере произошла ошибка {error}", 500


if __name__ == '__main__':
    app.run(debug=True)
