import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pins=[14,15,17,18,27,22,23,24,25]
for i in Pins:
	GPIO.setup(i,GPIO.OUT)
pwm = GPIO.PWM(17,100)
pwm1 = GPIO.PWM(27,100)
pwm2 = GPIO.PWM(23,100)
pwm.start(0)
pwm1.start(0)
pwm2.start(0)
Low = GPIO.LOW

High =GPIO.HIGH
def motor_ka(cw,ccw,pwm_ka):
	GPIO.output(14,cw)
	GPIO.output(15,ccw)
	pwm.ChangeDutyCycle(pwm_ka)

def motor_be(cw,ccw,pwm_be):
	GPIO.output(22,cw)
	GPIO.output(18,ccw)
	pwm1.ChangeDutyCycle(pwm_be)
def motor_ki(cw,ccw,pwm_ki):
	GPIO.output(25,cw)
	GPIO.output(24,ccw)
	pwm2.ChangeDutyCycle(pwm_ki)
	
def maju():
	motor_ki(1,0,30)
	motor_be(0,0,30)
	motor_ka(1,0,30)
def mundur():
	motor_ki(0,1,30)
	motor_be(0,0,30)
	motor_ka(0,1,30)
def stop():
	motor_ki(0,0,20)
	motor_be(0,0,20)
	motor_ka(0,0,20)
def belok_ki():
	motor_ki(0,1,10)
	motor_be(0,1,10)
	motor_ka(1,0,10)
	sleep(1)
	stop()
def belok_ka():
	motor_ki(1,0,10)
	motor_be(1,0,10)
	motor_ka(0,1,10)
	sleep(1)
	stop()
def geser_ka():
	motor_ki(1,0,15)
	motor_be(0,1,45)
	motor_ka(0,1,30)
def geser_ki() :
	motor_ki(0,1,30)
	motor_be(1,0,45)
	motor_ka(1,0,15)

def main():
	maju()
	sleep(2)
	belok_ki()
	sleep(2)
	geser_ka()
	sleep(2)
	stop()
	
		
if __name__=='__main__':
	main()
	
