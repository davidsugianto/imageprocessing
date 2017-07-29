import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(1)
cap.set (3,320)
cap.set (4,240)
cap.set (15,0.1)
while True:
        Bool,video=cap.read()
        video=cv.flip(video,1)
        hsv = cv.cvtColor(video, cv.COLOR_BGR2HSV)
		lower_orange = np.array ([0,97,0])
		upper_orange = np.array ([255,38,255])
        kernel = np.ones((2,2),np.uint8)
        colors=(0,140,255)
        mask = cv.inRange(hsv, lower_orange, upper_orange)
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
        mask=cv.morphologyEx(mask, cv.MORPH_CLOSE,kernel)
        dilation = cv.dilate(mask,kernel,iterations = 1)
        cnts= cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
              
        center =None
        if len(cnts)>0:
               	c = max(cnts, key=cv.contourArea)
               	((x,y),radius) = cv.minEnclosingCircle(c)
               	M = cv.moments(c)
               	center=(int (M["m10"]/M["m00"]),int (M["m01"]/M["m00"]))
 
              	if radius > 0.5:
                        cv.circle(video, (int(x), int(y)), int(radius), colors,2)
        		#cv.circle(video, (160, 120),20, (0,0,0),5)
			cv.line(video,(160,120),(int(x),int(y)),(0,255,0),5)

	cv.imshow('video',video)
    #cv.imshow('gray',mask)
    #cv.imshow('hsv',hsv)
        if cv.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()

