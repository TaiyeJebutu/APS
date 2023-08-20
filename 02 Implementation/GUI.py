import datetime, time
import os

import cv2
from flask import Flask, render_template, request, Response
from flask.views import MethodView

from TakePhoto import takePhoto

app = Flask(__name__)

class gui(MethodView):
    camera = cv2.VideoCapture(0)
    image = None
    formData = None
    def __init__(self, Core):
        self.core = Core
        app.add_url_rule("/form", "form", self.form)
        app.add_url_rule("/data/", "data", self.data, methods=['POST', 'GET'])
        app.add_url_rule("/photoPage/", 'photoPage', self.photoPage, methods=['POST', 'GET'])
        app.add_url_rule("/savePhoto/", 'savePhoto', self.savePhoto, methods=['POST', 'GET'])
        app.add_url_rule("/video_feed/", 'video_feed', self.video_feed, methods=['POST', 'GET'])
        app.run(host='0.0.0.0', port=80)

    def form(self):
        return render_template('index.html')

    def data(self):

        if request.method == 'POST':
            location = self.core.getLocation()
            form_data = {"ID": request.form.get("ID"),
                         "Password": request.form.get("Password"),
                         "Location": location}
            gui.formData = form_data
            return render_template('data.html', form_data=form_data)
        else:
            return render_template('data.html', form_data=gui.formData)
    def photoPage(self):
        return render_template('photoPage.html')

    def savePhoto(self):
        takePhoto.savePhoto()
        return render_template('data.html', form_data= gui.formData)



    def video_feed(self):
        return Response(takePhoto().getPhoto(gui.formData["ID"]), mimetype='multipart/x-mixed-replace; boundary=frame')




