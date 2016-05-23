from flask_restful import Resource
from external_services.firebase.firebase_api import get_demo_message


class Demo(Resource):
    def get(self, id_device):
        return get_demo_message('demo', id_device), 200