from datetime import datetime
from application import db
from logger import logger
from serializer import Serializer


class Users(db.Model):
    """
    This class represents the user table in the database
    which contains the details of the logged in user
    """
    try:
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(256), unique=True, nullable=False)
        mobilenum = db.Column(db.String(10), unique=True, nullable=False)
        password = db.Column(db.String(256), nullable=False)
        email = db.Column(db.String(256), unique=True, nullable=False)
        cart = db.relationship('Cart', backref='cart', lazy=True)
        wishlist = db.relationship('Wishlist', backref='wishlist', lazy=True)
        order = db.relationship('Order', backref='order', lazy=True)
    except Exception as e:
        logger.exception(e)

    def __init__(self, username, mobilenum, password, email):
        self.username = username
        self.mobilenum = mobilenum
        self.password = password
        self.email = email


class Books(db.Model, Serializer):
    """
    This class represents the table in the database
    which contains the books details to be sold online.
    """
    try:
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        book_id = db.Column(db.Integer, nullable=False)
        author = db.Column(db.String(1024), nullable=False)
        title = db.Column(db.String(1024), nullable=False)
        image = db.Column(db.Text)
        quantity = db.Column(db.Integer, nullable=False)
        price = db.Column(db.Integer, nullable=False)
        description = db.Column(db.Text, nullable=False)
        cart = db.relationship('Cart', lazy=True)
        wishlist = db.relationship('Wishlist', lazy=True)
    except Exception as e:
        logger.exception(e)

    def __init__(self, book_id, author, title, image, quantity, price, description):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.image = image
        self.quantity = quantity
        self.price = price
        self.description = description

    def serialize(self):
        d = Serializer.serialize(self)
        del d['cart']
        del d['wishlist']
        return d


class Cart(db.Model, Serializer):
    """
    This class represents the cart for a user,
    where the user can store products which the user wants to buy.
    """
    try:
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
        quantity = db.Column(db.Integer, default=1)
    except Exception as e:
        logger.exception(e)

    def __init__(self, user_id, book_id, quantity):
        self.user_id = user_id
        self.book_id = book_id
        self.quantity = quantity

    def serialize(self):
        d = Serializer.serialize(self)
        return d


class Order(db.Model):
    """
    This class represents the books which are to be ordered
    """
    try:
        __tablename__ = 'customer_order'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        total_amount = db.Column(db.Integer, nullable=False)
        is_delivered = db.Column(db.Boolean, default=False, nullable=False)
        order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    except Exception as e:
        logger.exception(e)

    def __init__(self, user_id, total_amount):
        self.user_id = user_id
        self.total_amount = total_amount

    def serialize(self):
        d = Serializer.serialize(self)
        return d


class Wishlist(db.Model):
    """
    This class represents the books which the user wishes to order later
    """
    try:
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    except Exception as e:
        logger.exception(e)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def serialize(self):
        d = Serializer.serialize(self)
        return d


class Orderbook(db.Model):
    """
    This class contains the book_id of the ordered book with user_id
    """
    try:
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    except Exception as e:
        logger.exception(e)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def serialize(self):
        d = Serializer.serialize(self)
        return d
