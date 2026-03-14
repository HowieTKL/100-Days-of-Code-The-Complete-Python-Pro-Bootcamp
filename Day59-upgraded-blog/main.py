import datetime
import requests
from flask import Flask, render_template

from blog import Blog

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/blog/<int:id>')
def blog(id):
    return render_template("post.html", id=id, blogs=blogs)

response = requests.get("https://api.npoint.io/5dd69790d2c5b1a235a9")
response.raise_for_status()
posts_json = response.json()
print(posts_json)
blogs = {}
for post in posts_json:
    blogs[post["id"]] = Blog(blog_id=post["id"], title=post["title"], subtitle=post["subtitle"], content=post["body"],
                             image_url=post["image_url"], author=post["author"], date=post["date"])
print(blogs)

@app.context_processor
def inject_current_time():
    return {"current_time": datetime.datetime.now()}

if __name__ == "__main__":
    app.run(debug=True)
