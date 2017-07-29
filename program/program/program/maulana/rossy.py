from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2 


camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
kernel = np.ones((5,5),np.uint8)

time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        image = frame.array
        vidio=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	
        cv2.imshow("image", image)
        cv2.imshow("vidio", vidio)
        

        key = cv2.waitKey(1) & 0xFF
	

        rawCapture.truncate(0)


        if key == ord("q"):
            break

