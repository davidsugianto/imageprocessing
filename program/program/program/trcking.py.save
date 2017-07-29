import numpy as np
import cv2 as cv
from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep as delay

#configuration picamera array to get RGB value
camera = PiCamera()
camera.resolution=(640,480)
rawCapture=PiRGBArray(camera, size=(640,480))
delay(4)
#camera capture
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
tresholding = cv.threshold(gray,127,255,cv.THRESH_BINARY)[1]
low_red=np.array([6,237,150])
high_red=np.array([6,237,90])
track = cv.inRange(image,low_red,high_red)
#track = cv.bitwise_and(image, image, treshold= treshold)

cv.imshow("image",image)
cv.imshow("hsv",hsv)
cv.imshow("gray",gray)
cv.imshow("thresholding",tresholding)
cv.imshow("tracking",track)
cv.waitKey(0)

