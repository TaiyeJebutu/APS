import os

import cv2
import cv2 as cv
import datetime


class takePhoto:
    camera = cv2.VideoCapture(0)
    p = None
    frame = None

    def getPhoto(self,userID):
        global out, capture, rec_frame, image

        while True:
            success, frame = self.camera.read()
            if success:

                capture = 0
                now = datetime.date.today()
                p = os.path.sep.join(['shots', "EmployeeID_{}_Date_{}.png".format(userID,str(now))])  # pic name
                takePhoto.p = p
                takePhoto.frame = frame

                try:
                    ret, buffer = cv2.imencode('hello.jpg', cv2.flip(frame, 1))
                    frame = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                except Exception as e:
                    pass

    @classmethod
    def savePhoto(cls):
        try:
            cv2.imwrite(cls.p, cls.frame)
        except Exception as e:
            pass


