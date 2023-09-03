import json
from urllib.request import urlopen
from geopy.geocoders import Nominatim
from geopy.location import Location


class getLocation:
    def getLatLogn(self):
        urlopen("http://ipinfo.io/json")
        data = json.load(urlopen("http://ipinfo.io/json"))
        lat = data['loc'].split(',')[0]
        long = data['loc'].split(',')[1]
        return(lat,long)

    def getCurrentLocation(self):

        latLong = self.getLatLogn()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location: Location = geolocator.geocode(latLong[0] + "," + latLong[1])
        location_data = location.address

        return location_data


