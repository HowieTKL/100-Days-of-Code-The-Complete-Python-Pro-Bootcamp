import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

#db = sqlite3.connect('books-collection.db')
#cursor = db.cursor()
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#db.commit()

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
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
#with app.app_context():
#    db.create_all()

# insert row
# with app.app_context():
#     new_book = Book(title="Harry Potter and the Chamber of Secrets", author="J. K. Rowling", rating=9.0)
#     db.session.add(new_book)
#     db.session.commit()

#read
with app.app_context():
    result = db.session.execute(db.select(Book))
    books = result.scalars()
    for book in books:
        print(book.title, book.author, book.rating)

#update
with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.id == 1))
    the_book = result.scalar()
    the_book.rating = 9.3
    db.session.commit()

# delete
with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.id == 2))
    the_book = result.scalar()
#    db.session.delete(the_book)
#    db.session.commit()

