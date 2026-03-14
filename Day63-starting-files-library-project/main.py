from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

    def __str__(self):
        return f'{self.title}'

# create table
# with app.app_context():
#     db.create_all()

# with app.app_context():
#     new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.0)
#     db.session.add(new_book)
#     db.session.commit()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book))
        books = result.scalars().all()
        # for book in books:
        #     print(book.title, book.author, book.rating)
    return render_template('index.html', books=books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    if request.method == 'POST':
        with app.app_context():
            book = db.get_or_404(Book, book_id)
            book.rating = request.form['rating']
            db.session.commit()
            return redirect(url_for('home'))
    else:
        with app.app_context():
            book = db.get_or_404(Book, book_id)
            return render_template('edit.html', book=book)

@app.route("/delete/<int:book_id>", methods=['GET'])
def delete(book_id):
    print(request.args.get('id'))
    with app.app_context():
        book = db.get_or_404(Book, book_id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

