#import sqlite3
from db import db
from models.store import StoreModel


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price):
        # when we are creating this object
        # we give only two args n not id(id is auto included)
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))

        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)
        """

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT into items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))
        connection.commit()
        connection.close()
        """

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? where name=?"
        cursor.execute(query, (self.price, self.name))
        connection.commit()
        connection.close()
        """