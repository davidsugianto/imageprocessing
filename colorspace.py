import cv2
import numpy as np
img = np.zeros((300,10,3), np.uint8)
cv2.namedWindow('image')

def nothing(x):
	pass
#create trackbar
cv2.createTrackbar('h','image',0,255,nothing)
cv2.createTrackbar('s','image',0,255,nothing)
cv2.createTrackbar('v','image',0,255,nothing)
cv2.createTrackbar('H','image',0,255,nothing)
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)
cv2.createTrackbar('kernel','image',2,20,nothing)
cap = cv2.VideoCapture(1)
cap.set(3,320)
cap.set(4,240)
cap.set(15,0.1)
while True:
	_,video = cap.read()
	video = cv2.flip(video,1)
	hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
	h = cv2.getTrackbarPos('h','image')
	s = cv2.getTrackbarPos('s','image')
	v = cv2.getTrackbarPos('v','image')
	H = cv2.getTrackbarPos('H','image')
	S = cv2.getTrackbarPos('S','image')
	V = cv2.getTrackbarPos('V','image')
	ker = cv2.getTrackbarPos('kernel','image')
	low = (h,s,v)
	up = (H,S,V)
	kernel = np.ones((ker,ker), np.uint8)
	mask = cv2.inRange(hsv,low,up)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	mask = cv2.dilate(mask,kernel,iterations = 20)
	constant = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	cv2.imshow('image', mask)
	cv2.imshow('video', video)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
