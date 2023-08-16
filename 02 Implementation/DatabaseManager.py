import mysql.connector


class databaseManager:
    def __init__(self, Core):
        core = Core
        #db = self.connect()
        #self.myCursor = db.cursor()
        #self.Querie()

    def connect(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mclarenf1@"
        )
        return db

    def CheckLoginInfo(self, data):
        db = self.connect()
        myCursor = db.cursor()
        try:
            myCursor.execute(f"SELECT Password, level FROM asp_assignment.employee_info WHERE EmployeeID = {data['ID']};")

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

        info = myCursor.fetchone()
        if info[0] == data["Password"]:
            return [True, info[1]]
        return [False, info[1]]

    def getAdminIDs(self):
        db = self.connect()
        myCursor = db.cursor()
        try:
            myCursor.execute(f"SELECT EmployeeID, FullName FROM asp_assignment.employee_info Where Level > 1;")

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

        return myCursor.fetchall()

    def addEmployeeToDatabase(self, employeeData):
        db = self.connect()
        myCursor = db.cursor()
        try:
            myCursor.execute(f"INSERT INTO `asp_assignment`.`employee_info` (`FullName`, `Address`, `Postcode`, `Email`, `Telephone`, `DateOfBirth`, `StartDate`, `AdminID`, `Level`, `Password`) "
                             f"VALUES ('{employeeData['FullName']}', '{employeeData['Address']}', '{employeeData['Postcode']}', '{employeeData['Email']}', '{employeeData['PhoneNo']}', '{employeeData['DoB']}', "
                             f"'{employeeData['StartDate']}', '{employeeData['AdminID']}', '{employeeData['Level']}', 'Password');")
            db.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

    def getEmployees(self, userLevel):
        db = self.connect()
        myCursor = db.cursor()
        try:
            myCursor.execute(f"SELECT EmployeeID, FullName FROM asp_assignment.employee_info Where Level < {userLevel};")

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return "An error occurred"

        return myCursor.fetchall()
