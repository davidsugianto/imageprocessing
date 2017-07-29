import cv2
import numpy as np
cap = cv2.VideoCapture(1)

cap.set(3,320)
cap.set(4,240)
cap.set(15,0.1)
while True :
    _,video = cap.read()
	video = cv2.flip(video,1)
	data = np.array([0,0,0])
	hsv = cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
	low_orange = np.array([0,50,150])
	up_orange = np.array([20,255,255])
	orange=[0,140,255]
	kernel = np.ones((10,10),np.uint8)
	mask=cv2.inRange(hsv,low_orange,up_orange)
	mask=cv2.dilate(mask,kernel,iterations=10)
	cnts= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	if len(cnts)>0:
		c = max(cnts, key=cv2.contourArea)
		((x,y),radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center=(int (M["m10"]/M["m00"] ),int (M["m01"]/M[ "m00"]))
		#if radius >=0:
		cv2.circle(video, (int (x),int (y)), int (radius),orange,4)
		data=np.array([int(x),int(y),int(radius)])
	else:
		data = np.array([0,0,0])
	cv2.imshow('video',video)
cap.release()
cv2.destroyAllWindows()
