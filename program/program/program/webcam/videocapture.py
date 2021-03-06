import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pins=[14,15,17,18,27,22,23,24,25,20,21]
for i in Pins:
	GPIO.setup(i,GPIO.OUT)
pwm = GPIO.PWM(17,100)
pwm1 = GPIO.PWM(18,100)
pwm2 = GPIO.PWM(25,100)
pwm3=GPIO.PWM(21,100)
pwm.start(0)
pwm1.start(0)
pwm2.start(0)
Low = GPIO.LOW
High =GPIO.HIGH

def motor_ka(cw,ccw,pwm_ka):
	GPIO.output(15,cw)
	GPIO.output(14,ccw)
	pwm.ChangeDutyCycle(pwm_ka)

def motor_be(cw,ccw,pwm_be):
	GPIO.output(22,cw)
	GPIO.output(27,ccw)
	pwm1.ChangeDutyCycle(pwm_be)
def motor_ki(cw,ccw,pwm_ki):
	GPIO.output(23,cw)
	GPIO.output(24,ccw)
	pwm2.ChangeDutyCycle(pwm_ki)
#def giring(cw,ccw,pwm1):
 #   GPIO.output(16,cw)
	#GPIO.output(20,ccw)
	#pwm3.ChangeDutyCycle(pwm1)
	
def maju():
	motor_ki(1,0,100)
	motor_be(0,0,100)
	motor_ka(1,0,100)
def mundur():
	motor_ki(0,1,100)
	motor_be(0,0,100)
	motor_ka(0,1,100)
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


def stop():
	motor_ki(0,0,20)
	motor_be(0,0,20)
	motor_ka(0,0,20)
def belok_ki():
	motor_ki(0,1,50)
	motor_be(0,1,50)
	motor_ka(1,0,50)
#	sleep(1)
#	stop()
def belok_ka():
	motor_ki(1,0,50)
	motor_be(1,0,50)
	motor_ka(0,1,50)
#	sleep(1)
#	stop()
def geser_ka():
	motor_ki(1,0,15)
	motor_be(0,1,45)
	motor_ka(0,1,30)
def geser_ki() :
	motor_ki(0,1,30)
	motor_be(1,0,45)
	motor_ka(1,0,15)
def strategi():
	maju()
	sleep(2)
	belok_ki()
	sleep(2)
	geser_ka()
	sleep(2)
	stop()
def tendang():
	motor_be(0,1,100);
def main():
	while True:
		data = raw_input("masukkan data:")
		if data =='f':
			maju()
		elif data == 'b' :
			mundur()
		elif data == 'd' :
			belok_ka()
		elif data == 's' :
			belok_ki()			
		elif data == 'c' :
			geser_ka()
		elif data == 'x':
			geser_ki()
		elif data =='q':
			tendang()
		elif data=='1':
			motor_ka(1,0,100)
		elif data == '2' :
			motor_ka(0,1,100)
		elif data == '3' :
			motor_ki(1,0,100)
		elif data == '4' :
			motor_ki (0,1,100)
		elif data == '5' :
			motor_be(1,0,100)
		elif data == '6' :
			motor_be(0,1,100)
		elif data == 't':
			shoot()
			
		else :
			stop()
		
if __name__=='__main__':
	main()
	
