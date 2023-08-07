import cv2 as cv
from datetime import datetime

class takePhoto:

    def getPhoto(self):
        cam_port = 0
        cam = cv.VideoCapture(cam_port)

        result, image = cam.read()

        photoName = datetime.now().strftime("%d/%m/%Y%H:%M:%S") + ".png"

        if result:
            cv.imshow("Photo", image)

            cv.imwrite(photoName, image)

            cv.waitKey(0)
            cv.destroyWindow("Photo")

        else:
            print("No image detected. Please try again")




test = takePhoto().getPhoto()