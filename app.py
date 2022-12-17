from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def route_not_found(title):
    film_json = get_film_by_title(title)
    return render_template('by_title.html', film=film_json)


@app.errorhandler(404)
def route_not_found(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def internal_server_error(error):
    return f"На сервере произошла ошибка {error}", 500


if __name__ == '__main__':
    app.run(debug=True)
