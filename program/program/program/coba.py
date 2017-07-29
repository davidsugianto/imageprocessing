from picamera.array import PiRGBArray 
from picamera import PiCamera
from imutils.video import VideoStream
import RPi.GPIO as IO
import datetime
import datetime
import imutils
import argparse
import numpy as np
from time import sleep
import cv2 as cv

#function for servo position

set_point=6.0

error=0
def servo (position):
	sudut = float((position/360)*11)
	return sudut


#function for follow ball
def follow(ball):
	A=6.0
	if 5.5>=ball <=6.5 :
		A=ball
	elif ball<5:
		A=int(ball+0.2)
	elif ball>6.5:
		A=float(ball-0.2)
	return A
	
			
#this function for inisilizer picamera
def main():
	camera = PiCamera()
	camera.rotation=180
	camera.resolution=(320,240)
	camera.framerate =32
	rawCapture = PiRGBArray(camera, size=(320,240))
	GPIO.setwarnings(False)
    #    GPIO.setmode(GPIO.BOARD)
    #    GPIO.setup(18, GPIO.OUT)
    #   p = GPIO.PWM(18, 50)
	
	IO.setmode(IO.BCM)
	IO.setup(19,IO.OUT)
	pwm=IO.PWM(19,50)
	pwm.start(6.0)
	
	while True:
		for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
			image = frame.array	
			blur = cv.GaussianBlur(image,(11,11),0)
			hsv = cv.cvtColor(blur,cv.COLOR_BGR2HSV)
			low_orange = np.array([0,50,80],dtype=np.uint8)
			up_orange = np.array([20,255,255],dtype=np.uint8)
			orange=[20,255,255]
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
				center=(int(M["m10"]/M["m00"]),int (M["m01"]/M["m00"]))
				if radius > 0.5:
					cv.circle(image, (int (x),int (y)), int (radius),orange,2)
					Servo = float(servo(x))
					PWM=follow(Servo)
					PWM.ChangeDutyCycle(PWM)
					print 'radius:%2.f koordinat:(%2.f,%2.f) sudut:%f Pid =%f'%(radius,x,y,Servo,PWM)
			cv.imshow("tracking",image)
			key=cv.waitKey(1) & 0xFF
			rawCapture.truncate(0)
			

if __name__=='__main__':
		main()
