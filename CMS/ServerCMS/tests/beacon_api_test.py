import unittest
import requests
import json


class BeaconServices(unittest.TestCase):
    def test_update_beacon(self):
        url = 'http://127.0.0.1:5000/beacon/update'
        data = {'uniqueId': 'MCKf', 'alias': 'Third Beacon', 'deviceType': 'beacon'}
        data = json.dumps(data)
        response = requests.post(url, headers={'content-type': "application/json"}, data=data)
        print response.content
        self.assertEqual(response.content, '"Update successful."\n')


if __name__ == '__main__':
    unittest.main()
