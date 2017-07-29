from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2
camera = PiCamera()
raw = PiRGBArray(camera)
time.sleep(1)
camera.capture(raw,format="png")
image = raw.array
gambar = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
coba1=np.array([50,100,100])
coba2=np.array([70,255,255])
hasil=cv2.inRange(hsv,coba1,coba2)
cv2.imshow('gambar',hasil)
cv2.waitkey(0)
