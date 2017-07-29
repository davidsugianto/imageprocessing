import cv2
import numpy as np
import RPI.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#pin raspberry
GPIO.setup(13,GPIO.IN)
#Pins=[12,10,9,4,13,5,6,13,14,15,16,17,18,27,22,23,24,25,10,9,11,20,21,19,26]
for i in Pins:
	GPIO.setup(i,GPIO.OUT)
pwm  = GPIO.PWM(17,255)
pwm.start(0)
cap.VideoCapture(1)
cap.set(3,320)
cap.set(4,240)
cap.set(15,0.1)
#pid control
#
def motor_ka(cw,ccw,pwm_ka):
	GPIO.output(15,cw)
	GPIO.output(14,ccw)
	pwm.ChangeDutyCycle(pwm_ka)
def maju():
	motor_ka(1,0,30)
	motor_ki(1,0,30)
	motor_be(0,0,0)
