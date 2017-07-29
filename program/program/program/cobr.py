from picamera import PiCamera as a
from time import sleep as delay

camera = a()

camera.start_preview()
delay(10)
camera.stop_preview()
