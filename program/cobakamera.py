from picamera.array import PIRGBArray
from picamera import PiCamera
import cv2
from time import sleep

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PIRGBArray(camera,size=(640,480))

time.sleep(0.1)


		image= frame.array
		cv2.imshow("Frame", image)
		key= cv2.waitKey(1) & 0xff
		rawCapture.truncate(0)

	if key == ord("q"):
		break
