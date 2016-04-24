from flask import Flask
from flask_restful import Api
from services.beacon import BeaconList, Beacon, GetSingleBeacon
from services.venues import GetVenues

app = Flask(__name__)
api = Api(app)

api.add_resource(BeaconList, '/beacons')
api.add_resource(Beacon, '/beacon/update')
api.add_resource(GetVenues, '/venues')
api.add_resource(GetSingleBeacon, '/beacon/<string:id>')

if __name__ == "__main__":
    app.run()

