from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('token',
                        type=int,
                        required=True,
                        help='token field cannot be empty'
                        )
    parser.add_argument('rfid_code',
                        required=True,
                        help='water_usage field cannot be empty'
                        )

    parser.add_argument('water_usage',
                        type=float,
                        required=True,
                        help='water_usage field cannot be empty'
                        )

    def get(self, name):

        item = StoreModel.find_by_name(name)
        #data = Store.parser.parse_args(1)

        if item:
            return item.json(), 201
        return {'Message': 'User Dosent Exist'}, 404

    def post(self, name):

        if StoreModel.find_by_name(name):
            return {'Message': 'User already exist'}, 400

        data = Store.parser.parse_args()
        store = StoreModel(name, **data)

        try:
            store.save_to_db()

        except:
            return {'Message': 'An error occured while inserting an object'}, 404

        return store.json(), 201

    def put(self, name):

        data = Store.parser.parse_args()

        store = StoreModel.find_by_name(name)

        if store is None:

            store = StoreModel(name, **data)
        else:
            store.token = data['token']
            store.rfid_code = data['rfid_code']
            store.water_usage = data['water_usage']

        store.save_to_db()
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'Message': 'item deleted'}


class StoreItems(Resource):

    def get(self):

        return {'Info': list(map(lambda x: x.json(), StoreModel.query.all()))}
