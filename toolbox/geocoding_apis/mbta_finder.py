"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key="
GMAPS_API_KEY = "AIzaSyAqswAJZEulRtIHPvMpyCEYMT8XpU8uCM4" 
MBTA_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def make_url(place):
    """
    Creates a properly formatted URL
    input: Place name
    output: url for place
    """
    base = GMAPS_BASE_URL #the beginning of the url, for all gmap calls
    url = base + urllib.urlencode([('address', place),('key', GMAPS_API_KEY)]) #specify place by calling urlencode
    return url 

def get_json(place):
    """
    Given a place name, return
    a Python JSON object containing the response to that request.
    Uses make_url function
    """
    url = make_url(place)
    f=urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    place_info = get_json(place_name)
    place_results = place_info['results']
    place_in_list = place_results[0]
    place_geometry= place_in_list['geometry']
    place_location = place_geometry['location']

    return (place_location['lat'], place_location['lng'])


def get_nearest_station((lat, lng)):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = MBTA_BASE_URL + MBTA_API_KEY + '&lat=' +str(lat) + '&lon=' +str(lng) + '&format=json'
    f=urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    stop_info= response_data['stop']
    stop_info_in_list = stop_info[0]
    return (stop_info_in_list['stop_name'],stop_info_in_list['distance'])



def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.

    Prints it in pretty format
    Also returns stop,distance as tuple just for shiggles
    """
    (lat,lng) = get_lat_long(place_name)
    (stop,distance) = get_nearest_station((lat,lng))
    print "Nearist stop is " + stop
    print "the distance to this stop is " + distance + " miles"
    return (stop,distance)

if __name__ == "__main__":
    find_stop_near("Fenway Park")