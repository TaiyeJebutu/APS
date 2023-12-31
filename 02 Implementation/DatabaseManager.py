import mysql.connector


class databaseManager:
    def __init__(self, Core):
        self.core = Core

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

            myCursor.execute(f"INSERT INTO asp_assignment.pay_details (EmployeeID, PaymentDate, AnnualSalary, TaxCode, MonthlySalary, Pension) "
                             f"SELECT EmployeeID, '{employeeData['PaymentDate']}', {employeeData['AnnualSalary']}, '{employeeData['TaxCode']}', {employeeData['MonthlySalary']}, {employeeData['Pension']} "
                             f"FROM asp_assignment.employee_info "
                             f"WHERE FullName='{employeeData['FullName']}' AND Level = {employeeData['Level']};")
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

    def getEmployeeInfo(self, employeeID):
        db = self.connect()
        myCursor = db.cursor()
        try:
            myCursor.execute(f"SELECT * from asp_assignment.employee_info e, asp_assignment.pay_details p where e.EmployeeID = {employeeID} and p.EmployeeID = {employeeID};")
            allInfo = myCursor.fetchone()
            myCursor.execute(f"SELECT * from asp_assignment.location_info where EmployeeID = {employeeID};")
            locationInfo = myCursor.fetchall()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return "An error occurred"

        return allInfo, locationInfo

    def updatePassword(self, newPassword, userID):
        db = self.connect()
        myCursor = db.cursor()
        try:
            myCursor.execute(f"UPDATE asp_assignment.employee_info SET Password = '{newPassword}' Where EmployeeID = {userID};")
            db.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return "An error occurred"

    def updateEmployeeInfo(self, employeeID, form_data):
        db = self.connect()
        myCursor = db.cursor()
        try:
            for key in form_data:
                if form_data[key] != '' and form_data[key] != None:
                    myCursor.execute(f"UPDATE asp_assignment.employee_info e, asp_assignment.pay_details p SET {key} = '{form_data[key]}' WHERE e.EmployeeID = {employeeID} AND p.EmployeeID = {employeeID};")

            db.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

            return "An error occurred"

    def addLocation(self, location, employeeID, datetime):
        db = self.connect()
        myCursor = db.cursor()
        try:
            self.checkAmountOfLocations(myCursor, employeeID)
            myCursor.execute(f"INSERT INTO asp_assignment.location_info (`EmployeeID`, `Datetime`, `Location`)"
                             f"VALUES ('{employeeID}', '{datetime}', '{location}');")
            db.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return "An error occurred"

    def checkAmountOfLocations(self, myCursor, employeeID):
        try:
            myCursor.execute(f"SELECT * from asp_assignment.location_info WHERE EmployeeID = {employeeID};")
            locations = myCursor.fetchall()
            if len(locations) >= 5:
                myCursor.execute(f"DELETE FROM asp_assignment.location_info WHERE EmployeeID = {employeeID} AND LocationID = {locations[0][0]}")

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return "An error occurred"

    def deleteUser(self, employeeID):
        db = self.connect()
        myCursor = db.cursor()
        try:
            myCursor.execute(f"DELETE FROM asp_assignment.pay_details where EmployeeID = {employeeID};")
            myCursor.execute(f"DELETE FROM asp_assignment.location_info where EmployeeID = {employeeID};")
            myCursor.execute(f"DELETE FROM asp_assignment.employee_info where EmployeeID = {employeeID};")
            db.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return "An error occurred"