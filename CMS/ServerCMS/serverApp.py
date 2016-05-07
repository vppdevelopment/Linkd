from flask import Flask
from flask_restful import Api
from services.device.device import BeaconList, Beacon, Venue, VenueList
from services.database.persistance import FirebaseData


app = Flask(__name__)
api = Api(app)

api.add_resource(BeaconList, '/devices/')#, endpoint='devices')
api.add_resource(Beacon, '/devices/<string:device_id>')#, endpoint='device')
api.add_resource(VenueList, '/customers/')#, endpoint='customers')
api.add_resource(Venue, '/customer/<string:venue_id>')#, endpoint='venues')
api.add_resource(FirebaseData, '/data/')


if __name__ == "__main__":
    app.run()

