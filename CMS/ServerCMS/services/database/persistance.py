from flask_restful import Resource, request
from external_services.firebase.persistance.database import set_user_data, get_user_data, set_user_data_by_id, get_user_data_by_id


class FirebaseData(Resource):
    def get(self):
        return get_user_data()

    def put(self):
        return set_user_data(request.json), 201


class FirebaseDataById(Resource):
    def get(self, id):
        return get_user_data_by_id(id)

    def put(self, id):
        return set_user_data_by_id(request.json, id), 202


