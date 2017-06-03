import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str,
                        required=True,
                        help='A username is required',
                        )
    parser.add_argument('password', type=str,
                        required=True,
                        help='A password is required'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return {"message": "User with the same username already exists"}, 400
        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return user.json(), 201
