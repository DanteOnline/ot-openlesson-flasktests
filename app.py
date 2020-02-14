from flask import Flask, render_template
from database import db_session, init_db
from models import Category, Product

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True


# Create a user to test with
@app.before_first_request
def create_user():
    init_db()
    # Создаем 2 категории
    games = Category(name='Games')
    films = Category(name='Films')
    db_session.add_all([games, films])
    # Создаем товары
    SOME_TEXT = 'some_text'
    skyrim = Product(name='Skyrim', price=10.1, category=games, description=SOME_TEXT)
    fallout = Product(name='Fallout', price=5.5, category=games, description=SOME_TEXT)
    matrix = Product(name='Matrix', price=1.2, category=films, description=SOME_TEXT)
    db_session.add_all([skyrim, fallout, matrix])
    # commit
    db_session.commit()


# Views
@app.route('/')
def home():
    categories = db_session.query(Category).all()
    products = db_session.query(Product).all()
    return render_template('index.html', categories=categories, products=products)


if __name__ == '__main__':
    app.run()
