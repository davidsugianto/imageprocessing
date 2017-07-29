import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0)
cap.set (3,320)
cap.set (4,240)
cap.set (15,0.1)
reg_x=(5,75,145,215,285)
reg_y=(20,60,100,140,180)
while True:
	Bool,video=cap.read()
	video=cv.flip(video,0)
	hsv = cv.cvtColor(video, cv.COLOR_BGR2HSV)
	lower=(0,0,196)
	upper=(178,30,234)
	lower1=(0,0,0)
	upper1=(0,0,70)
	kernel = np.ones((2,2),np.uint8)
	colors=(0,140,255)
	mask = cv.inRange(hsv, lower, upper)
	#print hsv
	mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
	mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
	mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
	mask=cv.morphologyEx(mask, cv.MORPH_CLOSE,kernel)
	mask= cv.dilate(mask,kernel,iterations = 2)
	#laplacian=cv.Laplacian(video,cv.CV_64F)
	cv.imshow('mask',mask)
	cnts= cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
	#for i in range(0,5):
		#for j in range(0,5):
			#cv.rectangle(video,(reg_x[i],reg_y[j]),(reg_x[i]+30,reg_y[j]+30),(255,0,0),2)
	center =None
	for c in cnts:		
		c = max(cnts, key=cv.contourArea)
		x,y,w,h = cv.boundingRect(c)
		cv.putText(video,'x,y',(int(x),int(y)), cv.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,255),2)
		cv.putText(video,'w,h',(int(x+w),int(y+h)), cv.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,255),2)
		cv.rectangle(video,(x,y),(x+w,y+h),(0,255,0),2)
		posisi_x=x+(w/2)
		posisi_y=y+(h/2)
		luas=w+h
		print '(%d,%d) dan panjang=%d dan lebar= %d ,luas=%d'%(posisi_x,posisi_y,w,h,luas),
		if y<30:
			print 'dekat',
		elif y>=30:
			print 'jauh',
		if posisi_x<110:
			print 'kanan'
		elif posisi_x>210:
			print 'kiri'
		else:
			print 'tengah'
		cv.circle(video, (int(posisi_x), int(posisi_y)), 1, (150,0,255), 20)
		print ' '
	cv.imshow('video',video)

	if cv.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

