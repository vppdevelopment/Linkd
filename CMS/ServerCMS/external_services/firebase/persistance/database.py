from firebase import firebase
from external_services.firebase.properties.firebase_conf import config as firebase_conf, routes as firebase_routes

firebase = firebase.FirebaseApplication(firebase_conf['firebase_url'], None)


def get_full_data():
    result = firebase.get(firebase_routes['full_zonar'], None)
    return result


def set_user_data(data):
    result = firebase.post(firebase_routes['users'], data)
    return result


def set_user_data_by_id(data, id):
    result = firebase.post(firebase_routes['users'] + '/' + id, data)
    return result


def get_user_data():
    result = firebase.get(firebase_routes['users'], None)
    return result


def get_user_data_by_id(id):
    result = firebase.get(firebase_routes['users'] + '/' + id, None)
    return result

