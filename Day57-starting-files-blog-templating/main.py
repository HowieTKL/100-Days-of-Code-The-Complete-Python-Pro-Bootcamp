import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)

def get_blog_posts():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    ps = response.json()
    posts = {}
    for p in ps:
        post = Post(p['id'], p['title'], p['subtitle'], p['body'])
        posts[p['id']] = post
    print(posts)
    return posts

@app.route('/blog/<int:num>')
def blog(num):
    return render_template("post.html", post=blog_posts[num])

blog_posts = get_blog_posts()

if __name__ == "__main__":
    app.run(debug=True)
