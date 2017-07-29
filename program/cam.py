import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while True:
	bool,video = cap.read()
	cv.imshow('gambar',video)
	if cv.waitKey(1) & 0XFF ==ord('q'):
		break
cv.release()
cv.destroyAllWindows()
