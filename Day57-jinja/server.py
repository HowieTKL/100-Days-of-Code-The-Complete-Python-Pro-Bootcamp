import datetime
import random
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    rand = random.randint(1, 10)
    return render_template('index.html', num=rand, year=datetime.datetime.now().year)


@app.route('/blog/<int:num>')
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    return render_template("blog.html", posts=response.json(), num=num)


if __name__ == '__main__':
    app.run()
