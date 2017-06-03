import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        """
        MADE OBSOLETE BY SQLALCHEMY
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        select_by_username = 'SELECT * FROM users WHERE username = ?'
        # user = next(cursor.execute(select_by_username, (username,)))
        result = cursor.execute(select_by_username, (username,)).fetchone()
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        MADE OBSOLETE BY SQLALCHEMY
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        select_by_id = 'SELECT * FROM users WHERE id = ?'
        # user = next(cursor.execute(select_by_username, (username,)))
        result = cursor.execute(select_by_id, (_id,)).fetchone()
        if result:
            user = cls(*result)
        else:
            user = None
        connection.close()
        """
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"username": self.username, "password": self.password}
