import cv2
import cv2.cv as cv
import numpy as np

cv2.namedWindow('tracking')
cap = cv2.VideoCapture(1)
cap.set(3,320)
cap.set(4,240)


while True:
	buzz = 0
	_, frame = cap.read()
	frame = cv2.flip(frame,1)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower = np.array([30,150,50])
	upper = np.array([255,255,255])
	kernel = np.ones((5,5),np.uint8)
	mask = cv2.inRange(hsv, lower, upper)
	tracking = cv2.bitwise_and(frame, frame, mask = mask)
	dilation = cv2.dilate(tracking,kernel,iterations=1)
	closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
	closing = cv2.GaussianBlur(closing,(5,5),0)
	circles = cv2.HoughCircles(closing, cv.CV_HOUGH_GRADIENT,2,120,param1=120,param2=50,minRadius=10,maxRadius=0)
	if circles is not None:
		for i in circles[0,:]:
			if int(round(i[2])) < 30:
				cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,255,0),5)
				cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,255,0),10)
			elif int (round(i[2])) > 35:
				cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,255,0),5)
				cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,255,0),10)
				buzz = 1				
	
	cv2.imshow('frame', frame)
	cv2.imshow('closing', closing)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()
cap.release()
