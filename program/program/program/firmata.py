from pyfirmata import Arduino
from time import sleep
board=Arduino('/dev/ttyACM0')
servo=board.get_pin('d:7:s')
while True:
	for i in range(255):
		print (i)
		servo.write(i)
		sleep(0.1)
	sleep(0.1)
