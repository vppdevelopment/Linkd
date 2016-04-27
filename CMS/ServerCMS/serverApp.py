from flask import Flask
from flask_restful import Api
from services.beacon import BeaconList, Beacon, GetSingleBeacon
from services.venues import GetVenues
from services.persistance import GetFirebaseData, GetUser, SetUserName

app = Flask(__name__)
api = Api(app)

api.add_resource(BeaconList, '/beacons')
api.add_resource(Beacon, '/beacon/update')
api.add_resource(GetVenues, '/venues')
api.add_resource(GetSingleBeacon, '/beacon/<string:id>')
api.add_resource(GetFirebaseData, '/data')
api.add_resource(GetUser, '/users')
api.add_resource(SetUserName, '/users2')

if __name__ == "__main__":
    app.run()

