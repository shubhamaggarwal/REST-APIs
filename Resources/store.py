from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.models.store import StoreModel


class Store(Resource):

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"store": store.json()}, 200
        return {"message": "Store Not Found"}, 404

    @jwt_required()
    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"Message": "A store with the same name already exists."}, 400
        store = StoreModel(name=name)
        store.save_to_db()
        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            print(store)
            store.delete_from_db()
        return {"Message": "Store Deleted"}, 200


class Stores(Resource):

    @jwt_required()
    def get(self):
        stores = StoreModel.query.all()
        stores_json_list = list(map(lambda store: store.json(), stores))
        return {"stores": stores_json_list}, 200