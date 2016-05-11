from flask_restful import Resource, request, reqparse
from external_services.firebase.persistance.database import \
    get_campaign_data, put_campaign_data, post_campaign_data, delete_campaign_data


class Campaigns(Resource):
    def get(self, id_customer, id_campaign):
        return get_campaign_data(id_customer, id_campaign), 200

    def put(self, id_customer, id_campaign):
        return put_campaign_data(id_customer, id_campaign, request.json), 201

    def delete(self, id_customer, id_campaign):
        return delete_campaign_data(id_customer, id_campaign, request.json), 203


class Campaign(Resource):
    def post(self, id_customer):
        return post_campaign_data(id_customer, request.json), 202

