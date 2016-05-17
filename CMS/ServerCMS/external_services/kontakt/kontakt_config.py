URL_BASE = 'https://api.kontakt.io/'
URL_DEVICE = URL_BASE + 'device/'
URL_DEVICE_SINGLE = URL_BASE + 'device/{}/'
URL_DEVICE_UPDATE = URL_BASE + 'device/update/'
URL_VENUES = URL_BASE + 'venue/'
URL_VENUES_SINGLE = URL_BASE + 'venue/{}/'
URL_VENUES_UPDATE = URL_BASE + 'venue/update/'
# TODO We strongly suggest that you supply a value for the User-Agent in the header.
HEADER_BASE = {
    'accept': "application/vnd.com.kontakt+json; version=7",
    'api-key': "SCfoAPpNWQQBQGIpvLRciZNajCRjfeor",
    'content-type': "application/x-www-form-urlencoded",
}
