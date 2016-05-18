import unittest
import requests
import json


class BeaconServices(unittest.TestCase):

    def test_get_beacons(self):
        url = 'http://localhost:5000/devices'
        result = requests.get(url)
        self.assertEqual(result.status_code, 200)

    def test_get_single_beacon(self):
        url = 'http://localhost:5000/devices/jx53'
        result = requests.get(url)
        self.assertEqual(result.status_code, 200)

    def test_get_single_beacon_not_found(self):
        url = 'http://localhost:5000/devices/zzzz'
        result = requests.get(url)
        self.assertEqual(result.status_code, 404)

    def temp_toUpdateBeacon(self):
        url = 'http://localhost:5000/devices/jx53'
        data = {'uniqueId': 'MCKf', 'alias': 'Third Beacon', 'deviceType': 'beacon'}
        data = json.dumps(data)
        response = requests.post(url, headers={'content-type': "application/json"}, data=data)
        print response.content
        self.assertEqual(response.content, '"Update successful."\n')

if __name__ == '__main__':
    unittest.main()
