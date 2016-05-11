from flask import Flask
from flask_restful import Api

from services.database.core.persistance import FirebaseData, FirebaseDataById
from services.device.device import BeaconList, Beacon, Venue, VenueList
from services.resources.campaign import Campaign
from services.resources.customer import Customers

app = Flask(__name__)
api = Api(app)

api.add_resource(BeaconList, '/devices/', endpoint='devices')
api.add_resource(Beacon, '/devices/<string:device_id>', endpoint='device')
api.add_resource(VenueList, '/customers/', endpoint='customers')
api.add_resource(Venue, '/customer/<string:venue_id>', endpoint='venues')

## TODO These are test routes
api.add_resource(FirebaseData, '/data/', endpoint='data')
api.add_resource(FirebaseDataById, '/data/<string:id>', endpoint='data-single')

##TODO These are the new routes for Customers and Campaigns
api.add_resource(Customers, '/customers/<string:id_customer>')
api.add_resource(Campaign, '/campaign/<string:id_customer>/<string:id_campaign>')

if __name__ == "__main__":
    app.run()

