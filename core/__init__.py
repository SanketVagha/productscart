from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// productcart.sqlite3'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

from core.model.product import Product
from core.model.cart import CartItem
from core.model.cartDetails import CartDetails

db.init_app(app)
with app.app_context():
    db.create_all()