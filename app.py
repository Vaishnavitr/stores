from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from sqlalcourse.security import authenticate, identity
from sqlalcourse.resources.user import UserRegister
from sqlalcourse.resources.item import ItemList, Item
from resources.store import StoreList, Store
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///data.db'
# turn off flask modification tracker which are not saved and doesnt turn of sqlalcourse tracker
app.secret_key = 'vaish'
api = Api(app)

# creating table data.db file for us, for this you need to import all the tables which should be created
@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1/student/Vaishnavi
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# if '__name__' == '__main__':
from db import db
db.init_app(app)
app.run(port=5000, debug=True)

