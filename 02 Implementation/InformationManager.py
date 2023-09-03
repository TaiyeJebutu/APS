from GetLocation import getLocation
from TakePhoto import takePhoto
from datetime import datetime
import time, threading


class informationManager:
    def __init__(self, Core):
        self.core = Core
        self.photo = takePhoto()
        self.location = getLocation()
        self.locationThread = None
        self.exit_event = threading.Event()

    def createLocationThread(self, employeeID):
        self.locationThread = threading.Thread(target=self.startLocationThread, daemon=True, args=(employeeID,))
        self.locationThread.setName("Location_thread")
        self.locationThread.start()

    def startLocationThread(self, employeeID):
        while True:
            if self.exit_event.is_set():
                self.exit_event.clear()
                break
            location = self.location.getCurrentLocation()
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.core.addLocation(location, dt, employeeID)
            time.sleep(10)

    def stopLocationThread(self):
        self.exit_event.set()

    def takePhoto(self,userID):
        return self.photo.getPhoto(userID)