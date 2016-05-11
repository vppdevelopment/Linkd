from flask_restful import Resource, request, reqparse
from external_services.firebase.persistance.database import \
    get_data_by_id, get_data, \
    update_data_by_id, update_data, \
    post_data, post_data_by_id


#TODO get this as an arg from the request
#GET is used to obtain elements
#POST is used to create new elements
#PUT is used to update existing elements

collection = 'users'


class FirebaseData(Resource):
    '''def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('collection', type=str, help='Collection to be searched' ,location='headers')
        args = parser.parse_args()
        return get_data(args['collection'])'''

    def get(self):
        return get_data(collection), 200

    def put(self):
        return update_data(collection, request.json), 201

    def post(self):
        return post_data(collection, request.json), 202


class FirebaseDataById(Resource):
    def get(self, id):
        return get_data_by_id(collection, id), 200

    def put(self, id):
        return update_data_by_id(collection, request.json, id), 201

    def post(self, id):
        return post_data_by_id(collection, request.json, id), 202

