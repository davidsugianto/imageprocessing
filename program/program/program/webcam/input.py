import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.IN)
while True:
	sensor=GPIO.input(14)
	print sensor
