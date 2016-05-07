from flask_restful import Resource, request
from external_services.firebase.persistance.database import set_data, get_data, set_data_by_id, get_data_by_id

#TODO get this as an arg from the request
collection = 'users'

class FirebaseData(Resource):

    def get(self):
        return get_data(collection)

    def put(self):
        return set_data(collection, request.json), 201


class FirebaseDataById(Resource):
    def get(self, id):
        return get_data_by_id(collection, id)

    def put(self, id):
        return set_data_by_id(collection, request.json, id), 202


