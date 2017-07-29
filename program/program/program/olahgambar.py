import numpy as np
import cv2 as cv
from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep as delay
camera = PiCamera()
camera.resolution=(100,100)
rawCapture=PiRGBArray(camera, size=(100,100))
delay(5)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
gray = cv.cvtColor(hsv,cv.COLOR_BGR2GRAY)
_,treshold =cv.threshold(gray, 127, 255,cv.THRESH_BINARY)
print image
cv.imshow("image",image)
cv.imshow("grayscale",gray)
cv.imshow("hsv",hsv)
cv.imshow("threshold",treshold)
cv.waitKey(0)
