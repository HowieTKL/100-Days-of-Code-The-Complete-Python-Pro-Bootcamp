import requests
from flask import Flask, render_template
import markupsafe

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello!</h1>"

@app.route("/guess/<user>")
def guess(user):
    response = requests.get(f'https://api.agify.io/?name={user}')
    response.raise_for_status()
    agify = response.json()
    print(agify)
    response = requests.get(f'https://api.genderize.io/?name={user}')
    response.raise_for_status()
    gender = response.json()
    print(gender)
    print(markupsafe.escape(user.title()))
    return render_template('guess.html', name=markupsafe.escape(user.title()), gender=gender["gender"], age=agify["age"])


if __name__ == '__main__':
    app.run()
