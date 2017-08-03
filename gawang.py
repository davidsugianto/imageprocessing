import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(1)
cap.set(3,320)
cap.set(4,240)
cap.set(15,0.1)

while True:
	_,video = cap.read()
	video = cv2.flip(video,1)
	hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
	lower = np.array ([105,39,147])
	upper = np.array ([107,189,168])
	kernel = np.ones((5,5),np.uint8)
	colors = (0,140,255)
	mask = cv2.inRange(hsv, lower, upper)
	dilation = cv2.dilate(mask, kernel, iterations = 1)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	mask = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
	mask = cv2.GaussianBlur(mask,(5,5),0)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	
	if len(cnts) > 0 :
			c = max(cnts, key=cv2.contourArea)
			((x,y),radius) = cv2.minEnclosingCircle(c)
			#center = (int (M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
		
			if radius > 10:
				cv2.circle(video, (int(x), int(y)), int(radius), colors,2)
				cv2.line(video, (160,120), (int(x), int(y)), (0,255,0), 5)
				
	cv2.imshow('video', video)
	cv2.imshow('mask', mask)
			
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()	
