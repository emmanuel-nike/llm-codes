import requests

def get_geocode(address):
    GOOGLE_MAPS_API_KEY = 'AIzaSyDppVwzKibbos6ayH7PBNlLP9rQvQFtKJ4'
    GEOCODING_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': address,
        'key': GOOGLE_MAPS_API_KEY
    }
    response = requests.get(GEOCODING_URL, params=params)
    if response.status_code == 200:
        return response.json()['results'][0]['geometry']['location']
    else:
        return None

print(get_geocode('1600 Amphitheatre Parkway, Mountain View, CA'))