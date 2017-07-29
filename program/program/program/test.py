from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
camera = PiCamera()
rawCapture =PiRGBArray(camera)
time.sleep(0.2)
camera.capture(rawCapture,format="bgr")
image = rawCapture.array
gambar=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GAMBAR GAUL",gambar)
cv2.waitKey(0)
