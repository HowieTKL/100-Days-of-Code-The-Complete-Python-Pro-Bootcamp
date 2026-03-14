from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['name']
    password = request.form['password']
    print(username, password)
    return f"<h1>Name: {username}, Password: {password}</h1>"