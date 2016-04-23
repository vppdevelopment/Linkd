from flask_restful import Resource, request
from external_services.kontakt import get_beacons, update_beacon


class BeaconList(Resource):
    def get(self):
        return get_beacons()


class Beacon(Resource):
    def post(self):
        payLoad = request.json
        return update_beacon(payLoad)