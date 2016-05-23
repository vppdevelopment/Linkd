from flask_restful import Resource, abort
from flask import request

from external_services.kontakt.kontakt_api import get_beacons, get_single_beacon, update_beacon, get_venues, get_single_venue


def validate_response(id, element, elementType):
    if element['status'] == 404:
        return abort(404, message="{} {} doesn't exist".format(elementType, id))
    else:
        return element


class Beacon(Resource):
    def get(self, device_id):
        return validate_response(device_id, get_single_beacon(device_id), "Beacon")

    def post(self, device_id):
        return validate_response(device_id, update_beacon(request.json), "Beacon")


class Venue(Resource):
    def get(self, venue_id):
        return validate_response(venue_id, get_single_venue(venue_id), "Venue")


class BeaconList(Resource):
    def get(self):
        return get_beacons()


class VenueList(Resource):
    def get(self):
        return get_venues()


