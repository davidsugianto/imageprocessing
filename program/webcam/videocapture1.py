import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame					
	_,frame = cap.read()
	
	cv2.imshow('video',frame)
	
