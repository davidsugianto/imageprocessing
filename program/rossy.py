Python 2.7.9 (default, Sep 17 2016, 20:26:04) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> #import modul time
#import modul RPi.GPIO
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

#maju
try:
while 1:
GPIO.output(10, GPIO.LOW)
GPIO.output(12, GPIO.HIGH)

except KeyboardInterrupt:
		list = (12,10)
		GPIO.cleanup(list)
