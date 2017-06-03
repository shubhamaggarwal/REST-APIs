from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Resources.item import Item, Items
from Resources.store import Store, Stores
from Resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Shubham"
api = Api(app)
jwt = JWT(app, authenticate, identity)
# creates /auth


# Resource is anything that API creates in Database or sends back upon API call
# Every Resource is represented as a class in REST APIs
# No need to jsonify while using Flask-RESTful

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
