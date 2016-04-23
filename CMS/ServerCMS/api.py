from flask import Flask
from flask_restful import Resource, Api
import requests
import json

app = Flask(__name__)
api = Api(app)


class KontaktApiGetDevices(Resource):
    def get(self):
        url = "https://api.kontakt.io/device"
        headers = {
            'api-key': "SCfoAPpNWQQBQGIpvLRciZNajCRjfeor",
            'accept': "application/vnd.com.kontakt+json;version=7",
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'postman-token': "34ed6af9-8904-f0bf-7d30-77f360df6088"
        }
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)


class KontaktApiUpdateDevice(Resource):
    def get(self):
        url = "https://api.kontakt.io/device/update"
        ## Aqui van los datos a modificar
        payload = "alias=Third%20Beacon&uniqueId=MCKf&deviceType=beacon"
        headers = {
            'api-key': "SCfoAPpNWQQBQGIpvLRciZNajCRjfeor",
            'accept': "application/vnd.com.kontakt+json; version=7",
            'conte': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'postman-token': "a71a0d73-f284-7b46-ec46-df8a8a3ab2f8",
            'content-type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return json.loads(response.text)

class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(KontaktApiGetDevices, '/kontakt/getDevice')
api.add_resource(KontaktApiUpdateDevice, '/kontakt/updateDevice')

if __name__ == '__main__':
    app.run(debug=True)
