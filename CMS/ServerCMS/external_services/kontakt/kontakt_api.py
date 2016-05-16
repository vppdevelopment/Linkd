import requests

from external_services.kontakt.kontakt_configuration import kontakt_url as url, headers_base as header


def get_beacons():
    url_complete = url['url_base']+ url['url_device']
    response = requests.get(url_complete, headers=header)
    return response.json()


def update_beacon(payload):
    url_complete = url['url_base'] + url['url_device_update']
    print(url_complete)
    response = requests.post(url_complete, data=payload, headers=header)
    return response.json()


def get_single_beacon(id):
    url_complete = url['url_base']+ url['url_device'] + id
    response = requests.get(url_complete, headers=header)
    return response.json()


def get_venues():
    url_complete = url['url_base'] + url['url_venues']
    response = requests.get(url_complete, headers=header)
    return response.json()


def get_single_venue(venue_id):
    url_complete = url['url_base'] + url['url_venues'] + venue_id
    response = requests.get(url_complete, headers=header)
    return response.json()
