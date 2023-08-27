import cv2, threading
from flask import Flask, render_template, request, redirect, Response

from flask.views import MethodView

from TakePhoto import takePhoto

app = Flask(__name__)

class gui(MethodView):
    camera = cv2.VideoCapture(0)
    image = None
    formData = None
    def __init__(self, Core):
        self.core = Core
        self.loggedIn = False
        self.userLevel = 0
        self.loggedInUserID = 0
        self.selectedEmployeeID = 0
        self.startGui()

    def startGui(self):
        app.add_url_rule("/form", "form", self.form, methods=['POST', 'GET'])
        app.add_url_rule("/test", "test", self.test)
        app.add_url_rule("/data/", "data", self.data, methods=['POST', 'GET'])
        app.add_url_rule("/CreateEmployee/", "CreateEmployee", self.createEmployee, methods=['POST', 'GET'])
        app.add_url_rule("/EmployeeInfo/", "EmployeeInfo", self.employeeInfo, methods=['POST', 'GET'])
        app.add_url_rule("/ChangePassword/", "ChangePassword", self.changePassword, methods=['POST', 'GET'])
        app.add_url_rule("/EditEmployeeInfo", "EditEmployeeInfo", self.editEmployeeInfo, methods=['POST', 'GET'])
        app.add_url_rule("/UserEmployeeInfo/", "UserEmployeeInfo", self.userEmployeeInfo, methods=['POST', 'GET'])
        app.add_url_rule("/photoPage/", 'photoPage', self.photoPage, methods=['POST', 'GET'])
        app.add_url_rule("/savePhoto/", 'savePhoto', self.savePhoto, methods=['POST', 'GET'])
        app.add_url_rule("/video_feed/", 'video_feed', self.video_feed, methods=['POST', 'GET'])
        app.run(host='0.0.0.0', port=80)

    def form(self):
        if request.method == "POST":
            form_data = {"ID": request.form.get("ID"), "Password": request.form.get("Password")}
            self.loggedInUserID = form_data['ID']
            PasswordAndLevel = self.core.CheckLoginInfo(form_data)
            self.userLevel = PasswordAndLevel[1]
            if PasswordAndLevel[0]:
                self.loggedIn = True
                self.core.getLocation(self.loggedInUserID)
                if self.userLevel <= 1:
                    try:
                        return redirect("/UserEmployeeInfo")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        return redirect("/UserEmployeeInfo")
                else:
                    return redirect('/data')
            else:
                return "Incorrect Username or Password"
        else:
            if self.loggedIn:
                self.loggedIn = False
                self.core.stopLocation()
            return render_template('index.html')

    def test(self):
        return render_template('test.html')

    def data(self):
        selectedableEmployees = self.core.getEmployees(self.userLevel)
        return render_template("data.html", employees=selectedableEmployees)

    def photoPage(self):
        if self.userLevel <= 1:
            userAccessibleTabs = [["Home", "/UserEmployeeInfo"], ["Change Password", "/ChangePassword"]]
            return render_template('PhotoPageV2.html', tabs=userAccessibleTabs)
        else:
            userAccessibleTabs = [["Home", "/data"], ["Change Password", "/ChangePassword"], ["Create Employee", "/CreateEmployee"]]
            return render_template('PhotoPageV2.html', tabs=userAccessibleTabs)

    def savePhoto(self):
        takePhoto.savePhoto()
        return redirect('/data')

    def video_feed(self):
        return Response(takePhoto().getPhoto(self.loggedInUserID), mimetype='multipart/x-mixed-replace; boundary=frame')


    def createEmployee(self):
        if not self.loggedIn:
            return redirect("/form")

        if request.method == "POST":
            form_data = {"FullName" : request.form.get("FullName"), "Address": request.form.get("Address"), "Postcode": request.form.get("Postcode"), "Email": request.form.get("Email"),
                         "PhoneNo": request.form.get("PhoneNo"), "DoB": request.form.get("DoB"), "StartDate": request.form.get("StartDate"), "AdminID": request.form.get("AdminID"),
                         "Level": request.form.get("Level"), "PaymentDate": request.form.get("PaymentDate"), "AnnualSalary": request.form.get("AnnualSalary"), "TaxCode": request.form.get("TaxCode"),
                         "MonthlySalary": request.form.get("MonthlySalary"), "Pension": request.form.get("Pension")}
            self.core.addEmployeeToDatabase(form_data)
            return redirect("/data")
        else:
            AdminIDs = self.core.getAdminIDs()
            return render_template("CreateEmployee.html", AdminIDs=AdminIDs)

    def employeeInfo(self):
        if not self.loggedIn:
            return redirect("/form")
        try:
            employeeID = request.form.get("Employee")
            self.selectedEmployeeID = employeeID[1]
            allInfo = self.core.getEmployeeInfo(employeeID[1])

            return render_template("EmployeeInfo.html", info=allInfo)
        except Exception as e:
            print(f"An error occurred {e}")
            return redirect("/data")

    def userEmployeeInfo(self):
        allInfo = {"db_info": self.core.getEmployeeInfo(self.loggedInUserID), "location": "Location_data"}
        return render_template("UserEmployeeInfoV2.html", info=allInfo)

    def changePassword(self):
        if request.method == "POST":
            newPassword = request.form.get("NewPassword")
            self.core.updatePassword(newPassword, self.loggedInUserID)
            if self.userLevel <= 1:
                return redirect("/UserEmployeeInfo")
            else:
                return redirect("/data")
        else:
            if self.userLevel <= 1:
                usersAccessibleTabs = [["Home", "/UserEmployeeInfo"], ["Take Photo", "/photoPage"]]
                return render_template("ChangePassword.html", tabs=usersAccessibleTabs)
            else:
                usersAccessibleTabs = [["Home", "/data"], ["Take Photo", "/photoPage"], ["Create Employee", "/CreateEmployee"]]
                return render_template("ChangePassword.html", tabs=usersAccessibleTabs)

    def editEmployeeInfo(self):
        if not self.loggedIn:
            return redirect("/form")

        if request.method == "POST":
            form_data = {"FullName": request.form.get("FullName"), "Address": request.form.get("Address"),
                         "Postcode": request.form.get("Postcode"), "Email": request.form.get("Email"),
                         "PhoneNo": request.form.get("Telephone"), "DateOfBirth": request.form.get("DoB"),
                         "StartDate": request.form.get("StartDate"), "AdminID": request.form.get("AdminID"),
                         "Level": request.form.get("Level"), "PaymentDate": request.form.get("PaymentDate"),
                         "AnnualSalary": request.form.get("AnnualSalary"), "TaxCode": request.form.get("TaxCode"),
                         "MonthlySalary": request.form.get("MonthlySalary"), "Pension": request.form.get("Pension")}
            self.core.updateEmployeeInfo(self.selectedEmployeeID, form_data)
            return redirect("/data")
        else:
            AdminIDs = self.core.getAdminIDs()
            return render_template("/EditEmployeeInfo.html", AdminIDs=AdminIDs)


