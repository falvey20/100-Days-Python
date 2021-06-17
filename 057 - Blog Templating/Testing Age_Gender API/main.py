from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_num, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}").json()
    gender_response = requests.get(f"https://api.genderize.io?name={name}").json()
    age = age_response["age"]
    gender = gender_response["gender"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/d8b70129e3812ad83c47")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
