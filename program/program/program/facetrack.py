from picamera.array import PiRGBArray 
from picamera import PiCamera
from imutils.video import VideoStream
import datetime
import imutils
import argparse
import numpy as np
from time import sleep
import cv2 as cv
camera = PiCamera()
camera.resolution=(320,240)
camera.framerate =32
rawCapture = PiRGBArray(camera, size=(320,240))
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	cv.imshow(image)
