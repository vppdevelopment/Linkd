from flask_restful import Resource, request

from external_services.firebase.firebase_api import \
    get_customer_data, put_customer_data, post_customer_data, delete_customer_data


##TODO research the way is used the POST or PUT to create new elements
##TODO possibly I have to build a new logic to evaluate when its new and when it exists

class Customers(Resource):
    def get(self, id_customer):
        return get_customer_data(id_customer), 200

    def put(self, id_customer):
        return put_customer_data(id_customer, request.json), 201

    def delete(self, id_customer):
        return delete_customer_data(id_customer), 203


class Customer(Resource):
    def post(self):
        return post_customer_data(request.json), 202
