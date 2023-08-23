from GetLocation import getLocation
from TakePhoto import takePhoto

class informationManager:
    def __init__(self, Core):
        self.core = Core
        self.location = getLocation()
        self.photo = takePhoto()

    def getGPS(self):
        g = self.location.getCurrentLocation()
        return g

    def takePhoto(self,userID):
        return self.photo.getPhoto(userID)