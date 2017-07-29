#This program for image image processing
#**learning : by python programming**
#
#
#
#this Program write by: Muhammad fadlullah
#you can send me massage at my gmail : Muhammadfadlullah9@gmail.com
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#------------**************-----****************------------------********--------------*******----********-------
#-----------**************-----********************--------------********-------------********----********--------
#--------------------------__********-------********-----------********-------------********----********----------
#------------********-----__********----------******----------********-------------********----********-----------
#-----------********-------********---------********---------****************-----********----********------------
#----------********-------********------********------------*******************-----****************--------------
#---------********-------********----********--------------*********----*******------**************---------------
#--------********-------********------********-------------*********----*******-------- --********----------------
#-------********-------********--------********------------*********----*******----------********-----------------
#----************-----********----------********------------******************----------********------------------
#---************-----********------------********-------------**************-----------********-------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

import RPi.GPIO as GPIO
import numpy as np
import cv2
import socket

#import serial
import struct
import sys
from time import sleep
#compas
import smbus
import time
#bus = smbus.SMBus(1)
#address = 0x60
#GPIO setmode

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#socket networking
#robot = socket.socket()
#robot.connect(('192.168.1.102', 1500))
#pin mode GPIO RASPBERRY PI
Pins=[14,15,16,17,18,27,22,23,24,25,10,9,11,20,21]
for i in Pins:
	GPIO.setup(i,GPIO.OUT)
pwm = GPIO.PWM(17,255)
pwm1 = GPIO.PWM(27,255)
pwm2 = GPIO.PWM(23,255)
pwm3 = GPIO.PWM(11,255)
pwm.start(0)
pwm1.start(0)
pwm2.start(0)
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
cap.set(15,0.1)
#arduino=serial.Serial('/dev/ttyACM0',9600)
x=0
y=0
radius=0
Pid=0
error=0
last_error=0
Kp=0.2
Kd=0.5
Ki=0.02
Ts=1
fast_ka=float(70)
fast_ki=float(70)
fast_be=0
max_speed=100 
min_speed=0
pwm_be=0
set_point=150
#
compas=0
data=0
control=0
kondisi=0
con_scan=0
#networking
recaive=0	
def motor_ka(cw,ccw,pwm_ka):
	GPIO.output(14,cw)
	GPIO.output(15,ccw)
	pwm.ChangeDutyCycle(pwm_ka)

def motor_be(cw,ccw,pwm_be):
	GPIO.output(22,cw)
	GPIO.output(27,ccw)
	pwm1.ChangeDutyCycle(pwm_be)
def motor_ki(cw,ccw,pwm_ki):
	GPIO.output(24,cw)
	GPIO.output(23,ccw)
	pwm2.ChangeDutyCycle(pwm_ki)

def giring(cw,ccw,pwm_gi):
        GPIO.output(20,cw)
        GPIO.output(16,ccw)
        pwm3.ChangeDutyCycle(pwm_gi)

	
def hand_left(cw,ccw,pwm_l):
	GPIO.output(9,cw)
	GPIO.output(11,ccw)
	pwm3.ChangeDutyCycle(pwm_l)
def mundur():
	motor_ka(0,1,25)
	motor_ki(0,1,25)
	motor_be(0,0,0)

def maju():
	motor_ka(1,0,50)
	motor_ki(1,0,50)
	motor_be(0,0,0)
def stop():
	motor_ka(0,0,0)
	motor_ki(0,0,0)
	motor_be(0,0,0)
def putar_kanan ():
    motor_ka(0,1,15)
    motor_ki(1,0,15)
    motor_be(1,0,15)

def putar_kiri ():
	motor_ka(1,0,30)
	motor_ki(0,1,30)
	motor_be(0,1,30)

def slid_kanan():
	motor_ka(0,1,25)
	motor_be(0,1,30)
	motor_ki(1,0,20)
def slid_kiri():
	motor_ka(1,0,20)
	motor_be(1,0,30)
	motor_ki(0,1,25)


def kipper(data_x):
	if data_x ==0:
		stop()
	if data_x > 170 :
		slid_kanan()
	elif data_x < 150:
		slid_kiri()
	else:
		stop()
def shoot():
        GPIO.output(21,0)
        GPIO.output(20,1)
        sleep(0.3)
        GPIO.output(21,1)
        GPIO.output(20,0)
        sleep(0.3)
        GPIO.output(21,0)
        GPIO.output(20,0)
        sleep(0.3)
#compas sensor
def bearing():
        bear = bus.read_byte_data(address, 1)
	
        return bear
def pid(pv):	
		global error,last_error
		error=pv-set_point
 		hasil_PID=float(((Kp*error) +((Ki/10)*(error+last_error)*Ts)+((Kd/Ts)*(error-last_error))))
		last_error=error
		print hasil_PID
#function for image_processing
def __tracking__():	
	_,video = cap.read()
	video =cv2.flip(video,0)
	data=np.array([0,0,0])
	hsv = cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
	low_orange = np.array([0,50,180])
	up_orange = np.array([20,255,255])
	orange=[0,140,255]
	kernel = np.ones((9,9),np.uint8)
	mask=cv2.inRange(hsv,low_orange,up_orange)
	mask=cv2.dilate(mask,kernel,iterations=1)
	cnts= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center =None
	if len(cnts)>0:
		c = max(cnts, key=cv2.contourArea)
		((x,y),radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center=(int (M["m10"]/M["m00"] ),int (M["m01"]/M[ "m00"]))
		#if radius >=0:
		cv2.circle(video, (int (x),int (y)), int (radius),orange,4)
		data=np.array([int(x),int(y),int(radius)])
	#cv2.imshow('video',video)
	return data
def black():	
	_,video = cap.read()
	video =cv2.flip(video,0)
	data=np.array([0,0,0])
	hsv = cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
	low_orange = np.array([0,0,0])
	up_orange = np.array([0,20,70])
	#orange=[0,140,255]
	kernel = np.ones((9,9),np.uint8)
	mask=cv2.inRange(hsv,low_orange,up_orange)
	mask=cv2.dilate(mask,kernel,iterations=1)
	cnts= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center =None
	if len(cnts)>0:
		c = max(cnts, key=cv2.contourArea)
		((x1,y1),radius1) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center=(int (M["m10"]/M["m00"] ),int (M["m01"]/M[ "m00"]))
		#if radius >=0:
		#cv2.circle(video, (int (x),int (y)), int (radius),orange,4)
		#data1=np.array([int(x1),int(y1),int(radius1)])
	#cv2.imshow('video',video)
	else:
		x1=0
		y2=0
		radius1=0
	print 'kordinat(%d , %d ) diameter %d'%(x1,y1,radius1)

def _go_(_x_):
	Pid =_x_
	pwm_ka=fast_ka+Pid
	pwm_ki=fast_ki-Pid
	if (pwm_ka > max_speed):
		pwm_ka=max_speed
	elif(pwm_ka < min_speed):
		pwm_ka=min_speed
	if (pwm_ki > max_speed):
		pwm_ki=max_speed
	elif(pwm_ki < min_speed):
		pwm_ki=min_speed
	if pwm_ki >=70:
		motor_be(1,0,20)
	elif pwm_ka >=70:
		motor_be(0,1,20)
	else:
		motor_be(0,0,0)
	#if far >150:
		#pwm_ka=pwm_ka-5
		#pwm_ki=pwm_ki-5
	motor_ka(1,0,pwm_ka)
	motor_ki(1,0,pwm_ki)
	print '(%d , %d)'%(int(pwm_ka),int(pwm_ki))

def main():
	global kondisi,con_scan
        _simpan_=__tracking__()
        n_x=_simpan_[0]
        n_y=_simpan_[1]
        n_z=_simpan_[2]
        print 'kordinat(%d , %d ) diameter %d nilai Pid =%d'%(n_x,n_y,n_z,Pid)
        #if n_y >=200:
        #       mundur()
        #elif n_y >=190:
        #       motor_ka(0,0,0)
        #       motor_ki(0,0,0)
        #       motor_be(0,1,80)
        if n_z == 0:
           scanning()
        #elif kondisi ==1:
        #       stop()
                #print 'kiri'
        #else:
	elif n_y >220:
                giring(1,0,100)
                if con_scan == 0:
                        stop()
                        sleep(0.2)
                        maju()
                        con_scan=1
                        sleep(0.5)
                if con_scan ==1:
                        arah()
                        shoot()
        elif n_z >0:    #print 'maju'
                global Pid
                con_scan=0
                giring(0,0,0)
                Pid=pid(n_x)
                _go_(Pid)
	
while True:
	#refbox = robot.recv(1024)
	main()
	#black()	
