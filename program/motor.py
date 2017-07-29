
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#maju
GPIO.output(15, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)

p = GPIO.PWM(14, 50)

try:
	p.start(50)
	while 1:
		for dc in range(0, 101, 5):
			#p.ChangDutyCycle(dc)
			#time.sleep(0.1)
		for dc in range(0, 1, 0):
			#p.ChangDutyCycle(dc)
			#time.sleep(0.1)
except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()
