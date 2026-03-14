import random

from flask import Flask

app = Flask(__name__)
print("__name__", __name__)

target_num = random.randint(0, 9)

@app.route("/")
def hello():
    global target_num
    target_num = random.randint(0, 9)
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />")


@app.route('/<int:guess>')
def guess(num):
    if num == target_num:
        return ("<h1 style='color: green'>You got it!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />")
    elif num < target_num:
        return ("<h1 style='color: blue'>Too low!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />")
    else:
        return ("<h1 style='color: red'>Too high!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")

