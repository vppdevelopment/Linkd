from firebase import firebase
from external_services.firebase.properties.firebase_conf import config as firebase_conf, routes as firebase_routes

firebase = firebase.FirebaseApplication(firebase_conf['firebase_url'], None)


def get_data():
    result = firebase.get(firebase_routes['full_zonar'], None)
    return result


def set_user_data(data):
    result = firebase.post(firebase_routes['users'], data, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
    return result


def get_user(data):
    result = firebase.get(firebase_routes['users'], data)
    return result

