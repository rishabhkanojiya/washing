from flask import Flask
from flask_restful import Resource, Api
from resources.store import Store, StoreItems

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'rishabh'
api = Api(app)


api.add_resource(Store, '/info/<string:name>')
api.add_resource(StoreItems, '/Allinfo')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
