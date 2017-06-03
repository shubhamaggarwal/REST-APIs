from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,
                        required=True,
                        help="The price field must not be left blank")
    parser.add_argument('store_id', type=int,
                        required=True,
                        help="The store_id field must not be left blank")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'item': item.json()}, 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {"message": "Item with a same name already exists"}
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"Message": "An error occurred."}, 500 # Internal Server Error
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        """
        MADE OBSOLETE BY SQLALCHEMY

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        delete_query = 'DELETE FROM items WHERE name = ?'
        cursor.execute(delete_query, (name,))
        connection.commit()
        connection.close()
        """
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"Message": "Item deleted"}, 200

    def put(self, name):
        request_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, request_data['price'], request_data['store_id'])
        else:
            item.price = request_data['price']
        item.save_to_db()
        return item.json()


class Items(Resource):
    @jwt_required()
    def get(self):
        """
        MADE OBSOLETE BY SQLALCHEMY
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM items'
        items = []
        for row in cursor.execute(query):
            items.append({'name': row[0], 'price': row[1]})
        """
        items = ItemModel.query.all()
        # items_json_list = [item.json() for item in items]
        items_json_list = list(map(lambda item: item.json(), items))
        return {"items": items_json_list}, 200