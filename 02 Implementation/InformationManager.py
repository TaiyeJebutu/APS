from GetLocation import getLocation
from TakePhoto import takePhoto
import time, threading


class informationManager:
    def __init__(self, Core):
        self.core = Core
        self.photo = takePhoto()
        self.location = getLocation()
        self.locationThread = None
        self.exit_event = threading.Event()

    def createLocationThread(self):
        self.locationThread = threading.Thread(target=self.startLocationThread, daemon=True)
        self.locationThread.start()

    def startLocationThread(self):
        while True:
            if self.exit_event.is_set():
                self.exit_event.clear()
                break
            location = self.location.getCurrentLocation()
            print(location)
            time.sleep(10)

    def stopLocationThread(self):
        self.exit_event.set()
        #self.locationThread.join()

    def takePhoto(self,userID):
        return self.photo.getPhoto(userID)