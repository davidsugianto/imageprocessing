import cv2 
import numpy as np
cap=cv2.VideoCapture(1)
while 1:
	_,video = cap.read()
	video =cv2.flip(video,1)
	data=np.array([0,0,0])
	hsv = cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
	low_orange = np.array([0,90,98])
	up_orange = np.array([56,255,255])
	low_green=np.array([66, 122, 129])
	up_green=np.array([86,255,255])
	orange=[0,140,255]
	green=[0,255,0]
	kernel = np.ones((2,2),np.uint8)
	masking=cv2.inRange(hsv,low_green,up_green)
	masking=cv2.morphologyEx(masking,cv2.MORPH_OPEN,kernel)
	masking=cv2.dilate(masking,kernel,iterations=5)
	mask=cv2.inRange(hsv,low_orange,up_orange)
	mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
	mask=cv2.dilate(mask,kernel,iterations=5)
	cnts= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	cntsgreen= cv2.findContours(masking.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	if len(cntsgreen)>0:
		c1= max(cntsgreen,key=cv2.contourArea)
		x1,y1,w,h = cv2.boundingRect(c1)
		cv2.rectangle(video,(x1,y1),(x1+w,y1+h),(0,255,0),2)
	#if len(cnts):
		#c = max(cnts, key=cv2.contourArea)
	for c in cnts:
		((x,y),radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center=(int (M["m10"]/M["m00"] ),int (M["m01"]/M[ "m00"]))
		if x>x1 and y>y1 and x<(x1+w) and y<(y1+h):
			cv2.circle(video, (int (x),int (y)), int (radius),orange,4)
			data=np.array([int(x),int(y),int(radius)])
		else:
			data=np.array([0,0,0])
	cv2.imshow('video',video)
	cv2.imshow('mask',mask)
	cv2.imshow('masking',masking)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
