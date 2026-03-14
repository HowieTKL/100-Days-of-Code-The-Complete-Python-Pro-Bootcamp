from flask import Flask

app = Flask(__name__)
print("__name__", __name__)

@app.route("/")
def hello():
    return ("<h1 style='text-align: center'>Hello!</h1>"
            "<p>Kitty pic...</p>"
            "<img src='https://media.tenor.com/9IsWdfGhlI0AAAAM/cute-cat.gif'/>")


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "<p>Bye!</p>"

@app.route("/greet/<name>")
def greet(name):
    return f"<p>Hi {name.title()}!</p>"

