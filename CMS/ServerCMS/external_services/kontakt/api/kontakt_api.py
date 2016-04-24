import requests

from external_services.kontakt.properties.kontakt_conf import kontakt_url as url, headers_base as header


def get_beacons():
    url_complete = url['url_base']+ url['url_device']
    response = requests.get(url_complete, headers=header)
    return response.json()


def update_beacon(payload):
    url_complete = url['url_base'] + url['url_device_update']
    print(url_complete)
    response = requests.post(url_complete, data=payload, headers=header)
    return response.json()

