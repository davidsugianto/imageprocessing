import cv2.cv as cv
import time

cv.NamedWindow("pict",1)
capture = cv.CaptureFromCAM(0)
while True:
	img = cv.imgread(capture)
	cv.imshow('pict', img)
print img
if cv.WaitKey(10) == 27:
	break
