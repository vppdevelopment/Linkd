import requests

from external_services.kontakt import kontakt_config


def get_beacons():
    response = requests.get(kontakt_config.URL_DEVICE, headers=kontakt_config.HEADER_BASE)
    return response.json()


def update_beacon(payload):
    response = requests.post(kontakt_config.URL_DEVICE_UPDATE, data=payload, headers=kontakt_config.HEADER_BASE)
    return response.json()


def get_single_beacon(device_id):
    response = requests.get(kontakt_config.URL_DEVICE_SINGLE.format(device_id), headers=kontakt_config.HEADER_BASE)
    return response.json()


def get_venues():
    response = requests.get(kontakt_config.URL_VENUES, headers=kontakt_config.HEADER_BASE)
    return response.json()


def get_single_venue(venue_id):
    response = requests.get(kontakt_config.URL_VENUES_SINGLE.format(venue_id), headers=kontakt_config.HEADER_BASE)
    return response.json()
