from flask_restful import Resource, request
from external_services.firebase.persistance.database import get_data, set_user_data, get_user


class GetFirebaseData(Resource):
    def get(self):
        return get_data()

'''
class GetUsers(Resource):
    def get(self):
        return get_users()
'''

class GetUser(Resource):
    def get(self, id):
        return get_user(id)


class SetUserName(Resource):
    def post(self, data):
        return set_user_data(data)

