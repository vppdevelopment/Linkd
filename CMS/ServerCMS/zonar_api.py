from flask import Flask
from flask_restful import Api

from services.database.core.persistance import FirebaseData, FirebaseDataById
from services.device.device import BeaconList, Beacon, Venue, VenueList
from services.resources.campaign import Campaigns, Campaign
from services.resources.customer import Customers, Customer
from services.resources.demo import Demo

app = Flask(__name__)
api = Api(app)

api.add_resource(BeaconList, '/devices/', endpoint='devices')
api.add_resource(Beacon, '/devices/<string:device_id>', endpoint='device')
api.add_resource(VenueList, '/device-customers/', endpoint='venue-list')
api.add_resource(Venue, '/device-customer/<string:venue_id>', endpoint='venues')


api.add_resource(Customer, '/customer/', endpoint='customers')
api.add_resource(Campaign, '/campaign/', endpoint='campaigns')
api.add_resource(Customers, '/customer/<string:id_customer>', endpoint='customer')
api.add_resource(Campaigns, '/campaign/<string:id_customer>/<string:id_campaign>', endpoint='campaign')


'''For internal demo'''
api.add_resource(Demo, '/message/<string:id_device>')


if __name__ == "__main__":
    app.run()

