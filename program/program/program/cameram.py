from picamera import PiCamera as a
from time import sleep as delay
import cv2
import numpy as np

camera = a()
cap = cv2.VideoCapture(0)
camera.start_preview()
while True:
    Bol,video=cap.read()
    cv2.imshow("vidio",video)
    if cv2.waitkey(1) & Oxff == ord('q'):
        break
camera.stop_preview()
