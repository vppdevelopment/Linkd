import unittest
import requests


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


if __name__ == '__main__':
    unittest.main()
