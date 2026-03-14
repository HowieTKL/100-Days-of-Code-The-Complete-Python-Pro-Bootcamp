import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
from datetime import datetime

IMAGE_BASE="https://image.tmdb.org/t/p/w500"
DATE_FORMAT="%Y-%m-%d"

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)

class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

    def __str__(self):
        return f'{self.title}'

# create table
# with app.app_context():
#     db.create_all()

# new_movie = Movies(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# second_movie = Movies(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

class EditForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Update')

class AddForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Search')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating.asc()))
    movies = result.scalars().all()
    for i in range(0, len(movies)):
        movies[i].ranking = len(movies) - i
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = db.get_or_404(Movies, movie_id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = float(form["rating"].data)
        movie.review = form["review"].data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("edit.html", movie=movie, form=EditForm())

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = db.get_or_404(Movies, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

def fetch_movies(title):
    parameters = {
        "query": f"{title}",
    }
    headers = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}",
    }
    response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters, headers=headers)
    response.raise_for_status()
    results = response.json()["results"]
    return results

@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        return redirect(url_for("select", title=form.title.data))
    return render_template("add.html", form=form)

@app.route('/select')
def select():
    movies = fetch_movies(request.args.get('title'))
    return render_template("select.html", movies=movies)

@app.route('/selected/<int:tmdb_id>')
def selected(tmdb_id):
    headers = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}",
    }
    parameters = {
        "language": "en-US",
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{tmdb_id}",
                            headers=headers, params=parameters)
    response.raise_for_status()
    movie = response.json()
    new_movie = Movies(
        title=movie["title"],
        year=datetime.strptime(movie['release_date'], DATE_FORMAT).year,
        description=movie["overview"],
        img_url=IMAGE_BASE + movie["poster_path"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", movie_id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
