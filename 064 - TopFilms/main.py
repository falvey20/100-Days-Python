from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '#########'
Bootstrap(app)

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///films.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Movie DB
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_API_KEY = "########"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"



class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

# Create Table
# db.create_all()

# After adding the new_movie this code is commented out.
# new_film = Film(
#     title="There Will Be Blood",
#     year=2007,
#     description="A story of family, religion, hatred, oil and madness, focusing on a turn-of-the-century prospector in the early days of the business.",
#     rating=8.2,
#     ranking=1,
#     review="What is there left to say about this absolute masterpiece? Are there actually words to describe how good this film was? I think there aren't. All I have to say is that this experience was something beyond special. From the first 15 minutes of silent cinema, to the amazing adventures the main character had to go through, this film kept me at the edge of my seat. Daniel Day-Lewis is magnificent as Daniel Plainview. No one could've done a better job. His accent, his voice, his presence and everything else made us 'live' with the character. All i gotta say is that this was 2 and a half hours of art and pure cinema. Hats off to P.T. Anderson for sculpting such an amazing story and for putting his entire heart in the film!",
#     img_url="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/fa0RDkAlCec0STeMNAhPaF89q6U.jpg"
# )
# db.session.add(new_film)
# db.session.commit()

@app.route("/")
def home():
    all_films = Film.query.order_by(Film.rating).all()
    for i in range(len(all_films)):
        all_films[i].ranking = len(all_films) - i
    db.session.commit()
    return render_template("index.html", films=all_films)


class EditFilmForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/edit", methods=['GET', 'POST'])
def edit_film():
    form = EditFilmForm()
    film_id = request.args.get('id')
    film = Film.query.get(film_id)

    if form.validate_on_submit():
        film.rating = float(form.rating.data)
        film.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", film=film, form=form)


@app.route("/delete")
def delete_film():
    film_id = request.args.get('id')
    film_to_delete = Film.query.get(film_id)
    db.session.delete(film_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


class FindFilmForm(FlaskForm):
    title = StringField("Film Title", validators=[DataRequired()])
    submit = SubmitField("Add Film")


@app.route("/add_film", methods=['GET', 'POST'])
def add_film():
    form = FindFilmForm()
    if form.validate_on_submit():
        film_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": film_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template('add.html', form=form)


@app.route("/find_film")
def find_film():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_film = Film(
            title=data["title"],
            # The data in release_date includes month and day, get just year.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for('edit_film', id=new_film.id))

if __name__ == '__main__':
    app.run(debug=True)
