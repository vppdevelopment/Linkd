from flask_restful import Resource, request
from external_services.kontakt.api.kontakt_api import get_beacons, update_beacon, get_single_beacon


class BeaconList(Resource):
    def get(self):
        return get_beacons()


class Beacon(Resource):
    def post(self):
        payLoad = request.json
        return update_beacon(payLoad)


class GetSingleBeacon(Resource):
    def get(self, id):
        return get_single_beacon(id)


