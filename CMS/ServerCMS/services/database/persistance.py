from flask_restful import Resource, request
from external_services.firebase.persistance.database import get_data, set_user_data, get_user



class FirebaseData(Resource):
    def get(self):
        return get_data()

    def put(self):
        print request.json
        return set_user_data(request.json), 201




class GetUser(Resource):
    def get(self, id):
        return get_user(id)


class SetUserName(Resource):
    def post(self, data):
        return set_user_data(data)


class Todo(Resource):
    def get(self, todo_id):
        #abort_if_todo_doesnt_exist(todo_id)
        return get_data(todo_id)

    '''def delete(self, todo_id):
        #abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204'''

    def put(self, todo_id):
        #args = parser.parse_args()
        task = {'task': 'insert'}
        set_user_data(task)
        return task, 201

