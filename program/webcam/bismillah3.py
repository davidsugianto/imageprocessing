import cv2
import numpy as np
from time import sleep

cap=cv2.cv2.VideoCapture(0)
while True:
	ret,video=cap.read()
	cv2.imshow('video',video)
	if (cv2.waitKey(1) & 0xFF ==ord('q')):
		break
cap.release()
cv2.destroyAllWindows()
