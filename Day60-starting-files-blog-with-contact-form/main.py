import os
import smtplib
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

load_dotenv()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)

        msg = f"Subject: contact\n\n{name}\n{email}\n{phone}\n{message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("elari.purple@gmail.com", os.getenv("SMTP_PASSWORD"))
            connection.sendmail("elari.purple@gmail.com", "praecognita@gmail.com", msg)

        return render_template("contact.html")
    else:
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(name, email, phone, message)
    return "Ok"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
