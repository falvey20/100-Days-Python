from flask import Flask, render_template
import requests
from post import Post

all_posts = requests.get("https://api.npoint.io/d8b70129e3812ad83c47").json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["Title"], post["Subtitle"], post["Content"])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def read_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
