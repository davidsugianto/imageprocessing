import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
        Bool,video=cap.read()
	video=cv2.flip(video,0)
	cv2.imshow('video',video)
	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
cap.release()
cv2.destroyAllWindows()


