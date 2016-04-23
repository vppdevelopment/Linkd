from flask import Flask
from flask_restful import Api
from services.beacon import BeaconList, Beacon

app = Flask(__name__)
api = Api(app)

api.add_resource(BeaconList, '/beacons')
api.add_resource(Beacon, '/beacon/update')

if __name__ == "__main__":
    app.run()

