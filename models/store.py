from src.db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')
    # lazy = dynamic : Don't create itemModel objects in the stores table
    # as soon as a table of stores is created

    def __init__(self, name):
        self.name = name

    @classmethod
    def find_by_name(cls, name):
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        find_query = 'SELECT * FROM stores WHERE name = ?'
        result = cursor.execute(find_query, (name,)).fetchone()
        connection.close()
        if result:
            return cls(*result) #
        """
        # SQLAlchemy Magic
        store = cls.query.filter_by(name=name).first()
        return store

    def save_to_db(self):
        # insert + update
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        insert_query = 'INSERT INTO stores VALUES(?)'
        cursor.execute(insert_query, (self.name))

        connection.commit()
        connection.close()
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}
        # self.items has become a query builder due to lazy = dynamic.
        # Until self.json() is called no ItemModel objects
        # are created for the function call.

