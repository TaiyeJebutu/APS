from flask import Flask, render_template, request
from flask.views import MethodView

app = Flask(__name__)

class gui(MethodView):
    def __init__(self, Core):
        self.core = Core
        app.add_url_rule("/form", "form", self.form)
        app.add_url_rule("/data/", "data", self.data, methods=['POST', 'GET'])
        app.add_url_rule("/photo" 'photo', self.photo)
        app.run(host='0.0.0.0', port=80)

    def form(self):
        return render_template('index.html')

    def data(self):
        # if request.method == 'GET':
        #     return f"The URL /data is accessed directly. Try going to '/form' to submit form"
        # if request.method == 'POST':
        #     form_data = {"ID" : request.form.get("ID"), "Password" : request.form.get("Password")}
        #     if self.core.CheckLoginInfo(form_data):
        #         return render_template('data.html',form_data = form_data)
        #     else:
        #         return "Incorrect Username or Password"
        location = self.core.getLocation()
        form_data = {"ID": request.form.get("ID"),
                     "Password": request.form.get("Password"),
                     "Location": location}

        return render_template('data.html', form_data=form_data)
