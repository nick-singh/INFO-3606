import os

from flask import Flask
from flask import request, jsonify

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


from app.models.books import Book

@app.route("/")
def home():
    return "My flask app"

@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == 'GET':
        books = Book.query.all()
        return jsonify([book.toJSON() for book in books])
    if request.method == 'POST':
        print(request.json)
        data = request.json['data']
        book = Book(**data)
        db.session.add(book)
        db.session.commit()
        return jsonify({"status":302})
