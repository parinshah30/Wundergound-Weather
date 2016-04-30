"""
This function will give you the current weather condition given a latitude and longitude
You need to register with wunderground and get a key
"""
from pprint import pprint
import requests

# WUNDERGROUND_KEY = '<wunderground key>'


def current_weather_from_lat_long(latitude=37.33426850, longitude=-121.88618876):
    """
    This function will give you the current weather condition given a latitude and longitude
    :param latitude: latitude
    :param longitude: longitude
    :return: json with current weather conditions
    """
    url = 'http://api.wunderground.com/api/{key}/conditions/q/{lat},{long}.json'.format(key=WUNDERGROUND_KEY, lat=latitude, long=longitude)
    r = requests.get(url)
    # pprint(r.json()['current_observation']['weather'])
    pprint(r.json()['current_observation'])

if __name__ == '__main__':
    lat = 37.33426850
    long = -121.88618876
    current_weather_from_lat_long(lat, long)

