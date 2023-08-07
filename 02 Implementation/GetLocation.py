import geocoder
from geopy.geocoders import Nominatim



class getLocation:

    geolocator = Nominatim(user_agent="geoapiExercises")
    def getCurrentLocation(self):
        latlong = geocoder.ip("me")
        return latlong.address



