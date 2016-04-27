from flask_restful import Resource, request
from external_services.kontakt.api.kontakt_api import get_venues


class GetVenues(Resource):
    def get(self):
        return get_venues()

