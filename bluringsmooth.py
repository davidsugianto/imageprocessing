import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(1):
	__,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_red = np.array([150,50,50])
	upper_red = np.array([255,255,255])
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask=mask)
	kernel = np.ones((15,15),np.float32)/225
	smooth = cv2.filter2D(res,-1,kernel)
	cv2.imshow('original', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('averaging', smooth)
	x = cv2.waitKey(5) & 0xFF
	if x == 27 :
		break
cv2.destroyAllWindows()
cap.release()
	
