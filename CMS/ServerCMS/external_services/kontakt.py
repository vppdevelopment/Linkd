import requests

url_base = "https://api.kontakt.io"
url_device = "/device"
url_device_update = "/device/update"

#We strongly suggest that you supply a value for the User-Agent in the header.
headers_base = {
    'accept': "application/vnd.com.kontakt+json; version=7",
    'api-key': "SCfoAPpNWQQBQGIpvLRciZNajCRjfeor",
    'content-type': "application/x-www-form-urlencoded",
}


def get_beacons():
    url = url_base+url_device
    response = requests.get(url, headers=headers_base)
    return response.json()


def update_beacon(payload):
    url = url_base+url_device_update
    response = requests.post(url, data=payload, headers=headers_base)
    return response.json()

