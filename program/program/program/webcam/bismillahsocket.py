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
#import serial
import struct
import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.connect(('192.168.20.5', 1500))
socket.connect(('192.168.1.101', 1500))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pins=[14,15,17,18,27,22,23,24,25,10,9,11]
for i in Pins:
	GPIO.setup(i,GPIO.OUT)
pwm = GPIO.PWM(17,255)
pwm1 = GPIO.PWM(27,255)
pwm2 = GPIO.PWM(23,255)
pwm3 = GPIO.PWM(11,255)
pwm.start(0)
pwm1.start(0)
pwm2.start(0)
Low = GPIO.LOW
High =GPIO.HIGH
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
Kp=0.2
Kd=0
Ki=0.1
Ts=1
fast_ka=20
fast_ki=20
#error1=0
error2=0
max_sped=50
min_sped=10
set_point=160
def control_Pid(pv):
	error=pv-set_point
	P=Kp*error
	#Max=error+error2
	#Min=error-error2
	#I=(Ki/10)*Max*Ts
	#D=(Kd/Ts)*Min
	hasil_PID= P
	#error1=error
	return hasil_PID

def motor_ki(cw,ccw,pwm_ki):
	GPIO.output(15,cw)
	GPIO.output(14,ccw)
	pwm.ChangeDutyCycle(pwm_ki)

def motor_be(cw,ccw,pwm_be):
	GPIO.output(18,cw)
	GPIO.output(22,ccw)
	pwm1.ChangeDutyCycle(pwm_be)
def motor_ka(cw,ccw,pwm_ka):
	GPIO.output(25,cw)
	GPIO.output(24,ccw)
	pwm2.ChangeDutyCycle(pwm_ka)

def hand_left(cw,ccw,pwm_l):
	GPIO.output(9,cw)
	GPIO.output(11,ccw)
	pwm3.ChangeDutyCycle(pwm_l)
def mundur():
	motor_ka(0,1,20)
	motor_ki(0,1,20)
	motor_be(0,0,0)

def maju():
	motor_ka(1,0,50)
	motor_ki(1,0,50)
	motor_be(0,0,0)
def stop():
	motor_ka(0,0,0)
	motor_ki(0,0,0)
	motor_be(0,0,0)
def scanning ():
	motor_ka(1,0,10)
	motor_ki(0,1,10)
	motor_be(0,1,10)

def forward(data_x):
	read_pid=control_Pid(data_x)
	pwm_ka=fast_ka-read_pid
	pwm_ki=fast_ki+read_pid
	if pwm_ka > max_sped:
		pwm_ka=max_sped
	elif pwm_ka < min_sped:
		pwm_ka=min_sped
	if pwm_ki > max_sped:
		pwm_ki=max_sped
	elif pwm_ki < min_sped:
		pwm_ki=min_sped
	if pwm_ki <=15 and pwm_ka > 24:
		motor_be(0,1,10)
	elif pwm_ka <= 15 and pwm_ki >24:
		motor_be(1,0,10)
	else:
		motor_be(0,0,0)
	print 'hasil pid = %d pwm ka = %d , pwm ki = %d' %(read_pid,pwm_ka,pwm_ki)
	motor_ka(1,0,pwm_ka)
	motor_ki(1,0,pwm_ki)

def go(data_radius,data_x):
	if data_radius ==0 :
		Stop()
	elif data_radius >60 :
		mundur()
	elif data_radius >=48 :
		hand_left(1,0,50)
		stop()
	elif data_radius <48 :
		forward(data_x)

while(True):
        datastring = socket.recv(1024)
        socket.send('siap kapten')
        #print('%s' %datastring)
        if datastring == "maju":
                maju()
                print("Robot Maju")
        elif datastring == "stop":
                print("Robot Stop")
                stop()
        elif datastring == "mundur":
                print("Robot Mundur")
                mundur()
        elif datastring == "kanan":
                print("Robot Ke kanan")
                motor_ka()
        elif datastring == 'kiri':
                print('Robot ke kiri')
                motor_ki()
        if not datastring:
            break
