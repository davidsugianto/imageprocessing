import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(1):
	__,frame = cap.read()
	#konversi bgr to hsv
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#data range warna biru
	lower = np.array([0,97,0])
	upper = np.array([255,38,255])
	
	mask = cv2.inRange(hsv, lower, upper)
	res = cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	x = cv2.waitKey(5) & 0xFF
	if x == 27 :
		break
cv2.destroyAllWindows()
	
