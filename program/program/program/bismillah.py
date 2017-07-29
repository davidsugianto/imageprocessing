from picamera.array import PiRGBArray 
from picamera import PiCamera
#from imutils.video import VideoStream
import datetime
#import imutils
import argparse
import numpy as np
from time import sleep
import cv2 as cv
#import serial
import struct
setpoint=160
error=0
pv=0
a=125
#function for follow ball with control tunning Pid

def main():
	camera = PiCamera()
	#camera.rotation=180
	camera.resolution=(320,240)
	camera.framerate =32
	rawCapture = PiRGBArray(camera, size=(320,240))
	#arduino=serial.Serial('/dev/ttyACM0',9600)

	last_error=0
	sudut=10
	
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		image = frame.array	
		blur =cv.GaussianBlur(image,(11,11),0)
		hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
		low_orange = np.array([0,50,100],dtype=np.uint8)
		up_orange = np.array([20,255,255],dtype=np.uint8)
		orange=[0,140,255]
		kernel = np.ones((9,9),np.uint8)
		mask=cv.inRange(hsv,low_orange,up_orange)
		mask=cv.morphologyEx(mask, cv.MORPH_OPEN,kernel)
		mask=cv.morphologyEx(mask, cv.MORPH_CLOSE,kernel)
		cnts= cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
		center =None
		if len(cnts)>0:
			c = max(cnts, key=cv.contourArea)
			((x,y),radius) = cv.minEnclosingCircle(c)
			M = cv.moments(c)
			center=(int (M["m10"]/M["m00"]),int (M["m01"]/M["m00"]))
			if radius > 0.5:
				cv.circle(image, (int (x),int (y)), int (radius),orange,4)
				cv.putText(image,'ball',(int(x-radius),int(y-radius)),cv.FONT_HERSHEY_SIMPLEX,0.6,orange,2)
				data_radius=radius/1
				data_x=(x/320)*200
				data_y=(y/240)*200	
				#arduino.write(struct.pack('>B',radius))			
				#arduino.write(struct.pack('>BBB',data_radius,data_x,data_y))
				print 'radius:%2.f koordinat:(%d,%d)'%(radius,data_x,data_y)
		else:
			print 'tidak ada bola ' 
			#arduino.write(struct.pack('>BBB',0,0,0))
		cv.imshow("tracking",image)
		rawCapture.truncate(0)
		#cv.imshow("mask",mask)
		#cv.imshow('hsv',hsv)
		#cv.imshow('blur',blur)
		key = cv.waitKey(1) & 0xFF
		if key == ord("q"):
			arduino.close()
			break
	
if __name__=='__main__':
	main()



	
