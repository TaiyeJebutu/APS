from GUI import gui
from DatabaseManager import databaseManager
from InformationManager import informationManager

class Core:
    def __init__(self):
        self.DM = databaseManager(self)
        self.IM = informationManager(self)
        self.Gui = gui(self)

    def getLocation(self):
        self.IM.getGPS()

    def getPhoto(self):
        self.IM.takePhoto()

    def CheckLoginInfo(self, data):
        return self.DM.CheckLoginInfo(data)

    def getAdminIDs(self):
        return self.DM.getAdminIDs()

    def addEmployeeToDatabase(self, employeeData):
        self.DM.addEmployeeToDatabase(employeeData)

    def getEmployees(self, userLevel):
        return self.DM.getEmployees(userLevel)

    def getEmployeeInfo(self, employeeID):
        return self.DM.getEmployeeInfo(employeeID)

    def updatePassword(self, newPassword, userID):
        self.DM.updatePassword(newPassword, userID)
        


entryPoint = Core()
entryPoint.getLocation()

