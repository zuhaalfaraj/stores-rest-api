from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.get_by_name(name)
        if store:
            return store.json()
        return {'message': "store not found"}, 404

    def post(self,name):
        if StoreModel.get_by_name(name):
            return {'message': "A store with name {} already exists".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred while creating the store, if that keeps happeining, contact with our technical team" }, 500
        return store.json()

    def delete(self, name):
        store =StoreModel.get_by_name(name)
        if store:
            store.delete_from_db()

        return {"message": "Store deleted"}



class StoreList(Resource):
    def get(self):
        return {"Stores": [store.json() for store in StoreModel.query.all()]}
