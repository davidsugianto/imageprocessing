from picamera import PiCamera
from time import sleep
camera= PiCamera()
camera.resolution=(640,480)
camera.start_preview()
sleep(5)
camera.capture('/home/pi/program/gambar.png')
sleep(3)
camera.stop_preview()
