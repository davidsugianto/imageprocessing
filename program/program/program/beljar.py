#library
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
from time import sleep
import cv2
#start take a video from pi camera
camera = PiCamera()
camera.resolution= (640,480)
camera.framerate =32
raw = PiRGBArray (camera ,size=(640,480))
sleep(1)
while(True):
	for frame in camera.capture_continuous(raw, format="bgr", use_video_port=True):
		image =frame.array
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		cv2.imshow("gambar",gray)
		if cv2.waitKey(1) & 0xFF==ord('q'):
			break
cap.release()
cv2.destroyAllWindows()
	
