from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from services.device import Device, DeviceList
app = Flask(__name__)
api = Api(app)

api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/devices/<string:device_id>')


if __name__ == '__main__':
    app.run(debug=True)