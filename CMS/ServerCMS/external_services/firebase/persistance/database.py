from firebase import firebase
from external_services.firebase.properties.firebase_conf import config as firebase_conf, routes as firebase_routes

firebase = firebase.FirebaseApplication(firebase_conf['firebase_url'], None)

## TODO POST method usage allows to CREATE a data set

def get_full_data(collection):
    result = firebase.get(firebase_routes[collection], None)
    return result


def set_data(collection, data):
    result = firebase.post(firebase_routes[collection], data)
    return result


def set_data_by_id(collection, data, id):
    result = firebase.post(firebase_routes[collection] + '/' + id, data)
    return result


def get_data(collection):
    result = firebase.get(firebase_routes[collection], None)
    return result


def get_data_by_id(collection, id):
    result = firebase.get(firebase_routes[collection] + '/' + id, None)
    return result

