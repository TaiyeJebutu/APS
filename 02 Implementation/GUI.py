from flask import Flask, render_template, request, redirect
from flask.views import MethodView

app = Flask(__name__)

class gui(MethodView):
    def __init__(self, Core):
        self.core = Core
        app.add_url_rule("/form", "form", self.form, methods=['POST', 'GET'])
        app.add_url_rule("/test", "test", self.test)
        app.add_url_rule("/data/", "data", self.data, methods=['POST', 'GET'])
        app.add_url_rule("/CreateEmployee/", "CreateEmployee", self.createEmployee, methods=['POST', 'GET'])
        app.add_url_rule("/EmployeeInfo/", "EmployeeInfo", self.employeeInfo, methods=['POST', 'GET'])
        app.add_url_rule("/ChangePassword/", "ChangePassword", self.changePassword, methods=['POST', 'GET'])
        app.run(host='0.0.0.0', port=80)
        self.loggedIn = False
        self.userLevel = 0
        self.userID = 0

    def form(self):
        if request.method == "POST":
            form_data = {"ID": request.form.get("ID"), "Password": request.form.get("Password")}
            self.userID = form_data['ID']
            PasswordAndLevel = self.core.CheckLoginInfo(form_data)
            self.userLevel = PasswordAndLevel[1]
            if PasswordAndLevel[0]:
                self.loggedIn = True
                if self.userLevel <= 1:
                    return redirect("/test")
                else:
                    return redirect('/data')
            else:
                return "Incorrect Username or Password"
        else:
            return render_template('index.html')

    def test(self):
        return render_template('test.html')

    def data(self):
        selectedableEmployees = self.core.getEmployees(self.userLevel)
        return render_template("data.html", employees = selectedableEmployees)


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
        employeeID = request.form.get("Employee")
        allInfo = self.core.getEmployeeInfo(employeeID[1])
        return render_template("EmployeeInfo.html", info=allInfo)

    def changePassword(self):
        if request.method == "POST":
            newPassword = request.form.get("NewPassword")
            self.core.updatePassword(newPassword, self.userID)
            return redirect("/data")
        else:
            return render_template("ChangePassword.html")


