import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
#cap.set(15,0.1)

def track():
	_,video = cap.read()
	video = cv2.flip(video, 0)
	hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
	#data = np.array([0,0,0])
	lower = np.array([0,97,0])
	upper = np.array([255,38,255])
	colors = (0,140,255)
	kernel = np.ones((2,2),np.uint8)
	mask = cv2.inRange(hsv, lower, upper)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	dilation = cv2.dilate(mask, kernel, iterations = 1)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	
	if len(values)>0:
		a = mask(values, key=cv2.contourArea)
		((x,y),radius) = cv2.minEnclosingCircle(a)
		data = np.array([int(x),int(y),int(radius)])
	else:
		data = np.array([0,0,0])
	cv2.imshow('video',video)


if __name__ == 'track':
    track()
		
	
	
