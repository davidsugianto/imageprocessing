import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	#cMap = cv2.flip(cv2.applyColorMap(frame, cv2.COLORMAP_HOT), 1)
	gray = cv2.cvtColor(frame, cv2.COreLOR_BGR2GRAY)
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
