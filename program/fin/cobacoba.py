from picamera import PiCamera
import cv2
import time

cv.NAmedWindow("camera",1)
capture = cv.captureFromCAM(0)
while True:
	img = cv.QueryFrame(capture)
	cv.ShowImage("camera",img)
	if cv.WaitKey(10) == 27:
			break

