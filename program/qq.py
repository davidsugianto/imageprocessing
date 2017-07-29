Python 2.7.9 (default, Sep 17 2016, 20:26:04) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pins = [27,14,15]
for a in Pins:
    GPIO.setup(a,GPIO.OUT)
pwm = GPIO.PWM(27, 100)
pwm.start(0)
Low = GPIO.LOW
High = GPIO.HIGH

def morse(nilai):
	banyaksimbol = nilai.split()
	for simbol in banyaksimbol:
		if (simbol == "a")
			muter_s()
		else:
			muter_we()
			

def motor_s(cw,ccw,pwm1):
    GPIO.output(14,cw)
    GPIO.output(15,ccw)
    pwm.ChangeDutyCycle(pwm1)
    
def muter_e():
    motor_s(0,1,40)    
    
def muter_we():
    motor_s(1,0,50)
    


