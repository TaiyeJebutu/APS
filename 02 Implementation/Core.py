from GUI import gui
from DatabaseManager import databaseManager
from InformationManager import informationManager


class Core:
    def __init__(self):
        self.DM = databaseManager(self)
        self.IM = informationManager(self)
        self.Gui = gui(self)

    def getLocation(self):
        location = self.IM.getGPS()
        return location

    def getPhoto(self):
        self.IM.takePhoto()

    def CheckLoginInfo(self, data):
        return self.DM.CheckLoginInfo(data)


entryPoint = Core()
entryPoint.getLocation()
entryPoint.getPhoto()
