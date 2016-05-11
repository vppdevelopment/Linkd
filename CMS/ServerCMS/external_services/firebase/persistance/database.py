import json
from firebase import firebase
from external_services.firebase.properties.firebase_conf import config as firebase_conf, routes as firebase_routes

firebase = firebase.FirebaseApplication(firebase_conf['firebase_url'], None)

##TODO Define an schema and normalize it ASAP

'''
GET: Route of existent item in the document with the 'collection' value
POST: New item in the document. Must be done with a PUT in Firebase
PUT: Edit an item in the document. The 'collection' item is where the change will be made
DELETE: Do I have to say something else?
'''

'''Customer'''


def get_customer_data(id_customer):
    result = firebase.get(firebase_routes['customer'] + '/' + id_customer, None)
    return result


def put_customer_data(id_customer, data):
    result = firebase.put(firebase_routes['customer'] + '/' + id_customer, id_customer, data)
    return result


def post_customer_data(data):
    result = firebase.put(firebase_routes['customer'], data['id'], data)
    return result


def delete_customer_data(id_customer):
    result = firebase.delete(firebase_routes['customer'], id_customer)
    return result


'''Campaign'''


def get_campaign_data(id_customer, id_campaign):
    result = firebase.get(firebase_routes['campaign'] + '/' + id_customer + '/' + id_campaign, None)
    return result


def put_campaign_data(id_customer, id_campaign, data):
    result = firebase.put(firebase_routes['campaign'] + '/' + id_customer + '/' + id_campaign, data)
    return result


def post_campaign_data(id_customer, data):
    result = firebase.put(firebase_routes['campaign'] + '/' + id_customer, data)
    return result


def delete_campaign_data(id_customer, id_campaign):
    result = firebase.delete(firebase_routes['campaign'] + '/' + id_customer, id_campaign)
    return result


'''Basic usage'''


def get_data(collection):
    result = firebase.get(firebase_routes[collection], None)
    return result


def get_data_by_id(collection, id):
    result = firebase.get(firebase_routes[collection] + '/' + id, None)
    return result


def post_data(collection, data):
    result = firebase.post(firebase_routes[collection], data)
    return result


def post_data_by_id(collection, data):
    result = firebase.post(firebase_routes[collection] + '/' + id, id, data)
    return result


def update_data(collection, data):
    result = firebase.put(firebase_routes[collection], data)
    return result


def update_data_by_id(collection, data, id):
    result = firebase.put(firebase_routes[collection] + '/' + id, id, data)
    return result



