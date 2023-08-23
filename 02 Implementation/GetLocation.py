import requests
import socket
import json
class getLocation:

    def get_ip(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    def getCurrentLocation(self):

        ip_address = self.get_ip()
        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result = json.loads(result)
        # response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        # location_data = {
        #     "ip": ip_address,
        #     "city": response.get("city"),
        #     "region": response.get("region"),
        #     "country": response.get("country_name")
        # }
        return "location_data"


