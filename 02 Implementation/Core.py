from GUI import gui
from DatabaseManager import databaseManager
from InformationManager import informationManager

class Core:
    def __init__(self):
        self.DM = databaseManager(self)
        self.IM = informationManager(self)
        self.Gui = gui(self)

    def getLocation(self, employeeID):
        self.IM.createLocationThread(employeeID)

    def stopLocation(self):
        self.IM.stopLocationThread()

    def getPhoto(self, userID):
        return self.IM.takePhoto(userID)

    def savePhoto(self):
        self.IM.savePhoto()

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

    def updateEmployeeInfo(self, employeeID, form_data):
        self.DM.updateEmployeeInfo(employeeID, form_data)

    def addLocation(self, location, datetime, employeeID):
        self.DM.addLocation(location, employeeID, datetime)


entryPoint = Core()

