from flask_restful import Resource, request, abort, reqparse
from external_services.kontakt.api.kontakt_api import get_beacons, update_beacon, get_single_beacon, get_venues, get_single_venue


def validate_in_collection(id, element, elementType):
    print element
    if element is None:
        abort(404, message="{} {} doesn't exist".format(elementType, id))
    else:
        return element


class Beacon(Resource):
    def get(self, device_id):
        return validate_in_collection(device_id, get_single_beacon(device_id), "Beacon")


class Venue(Resource):
    def get(self, venue_id):
        return validate_in_collection(venue_id, get_single_venue(venue_id), "Venue")


class BeaconList(Resource):
    def get(self):
        return get_beacons()


class VenueList(Resource):
    def get(self):
        return get_venues()


