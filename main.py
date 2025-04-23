import json
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template


app = Flask(__name__)
Bootstrap5(app)

with open('database/ironman_suits_data.json', 'r') as f:
    suit_data = json.load(f)

with open('database/marvel_movies.json', 'r') as f:
    movies = json.load(f)

with open('database/marvel_tv_series.json', 'r') as f:
    tv_series = json.load(f)

with open('database/characters.json', 'r') as f:
    characters = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/suits')
def suits():
    return render_template('suits.html', data=suit_data)


@app.route('/detail_suit/<int:id>')
def detail_suit(id):
    id = id
    return render_template('detail_suit.html', data=suit_data, id=id)


@app.route('/marvel_phases')
def marvel_phases():
    return render_template('marvel_phases.html', movies=movies)


@app.route('/marvel_movies/<int:id>')
def marvel_movies(id):
    id=id
    return render_template('marvel_movies.html', id=id, movies=movies)


@app.route('/marvel_tv_series')
def marvel_tv_series():
    return render_template('marvel_tv_series.html', tv_series=tv_series)


@app.route('/marvel_characters')
def marvel_characters():
    return render_template('marvel_characters.html', characters=characters)

if __name__ == '__main__':
    app.run(debug=True)