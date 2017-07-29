import cv2
import numpy as np
import cv2.cv as cv

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

def nothing(x):
	pass

cv2.namedWindow('H')
cv2.namedWindow('S')
cv2.namedWindow('V')
cv2.namedWindow('closing')
cv2.namedWindow('tracking')

cv2.createTrackbar('hmin', 'H',12,179,nothing)
cv2.createTrackbar('hmax', 'H',37,179,nothing)

cv2.createTrackbar('smin', 'S',96,255,nothing)
cv2.createTrackbar('smax', 'S',255,255,nothing)

cv2.createTrackbar('vmin', 'V',186,255,nothing)
cv2.createTrackbar('vmax', 'V',255,255,nothing)

while(1):
	bismillah = 0
	__, frame = cap.read()
	#convert to hsv
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	hue,sat,val = cv2.split(hsv)
	#trackbar
	hmn = cv2.getTrackbarPos('hmin','H')
	hmx = cv2.getTrackbarPos('hmax','H')
	
	smn = cv2.getTrackbarPos('smin','S')
	smx = cv2.getTrackbarPos('smix','S')
	
	vmn = cv2.getTrackbarPos('vmin','V')
	vmx = cv2.getTrackbarPos('vmax','V')
	
	# thresholding
    hthresh = cv2.inRange(np.array(hue),np.array(hmn),np.array(hmx))
    sthresh = cv2.inRange(np.array(sat),np.array(smn),np.array(smx))
    vthresh = cv2.inRange(np.array(val),np.array(vmn),np.array(vmx))

    # bitwise and h s and v
    tracking = cv2.bitwise_and(hthresh,cv2.bitwise_and(sthresh,vthresh))

    # filter morfologi
    dilation = cv2.dilate(tracking,kernel,iterations = 1)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
    closing = cv2.GaussianBlur(closing,(5,5),0)

    # deteksi garis lingkaran
    circles = cv2.HoughCircles(closing,cv.CV_HOUGH_GRADIENT,2,120,param1=120,param2=50,minRadius=10,maxRadius=0)
    
    #menggambar lingkaran
	 if circles is not None:
            for i in circles[0,:]:
                if int(round(i[2])) < 30:
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,255,0),5)
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,255,0),10)
                elif int(round(i[2])) > 35:
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,0,255),5)
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,0,255),10)
                    bismillah = 1
	 cv2.imshow('H',hthresh)
	 cv2.imshow('S',sthresh)
	 cv2.imshow('V',vthresh)
	 cv2.imshow('closing',closing)
	 cv2.imshow('tracking',frame)
	 
	 a = cv2.waitKey(5) & 0xFF
	 if a == 27:
		 break

cap.release()
cv2.destroyAllWindows()
	 


