from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
#camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
kernel = np.ones((5,5),np.uint8)
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
   	 # grab the raw NumPy array representing the image, then initialize the timestamp
    		# and occupied/unoccupied text
    image = frame.array
    video=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    video1=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    low_red = np.array([156,87,111], dtype=np.uint8)
    up_red = np.array([200,255,255], dtype=np.uint8) 
    red = cv2.inRange(video1, low_red, up_red)
    red = cv2.morphologyEx(red,cv2.MORPH_CLOSE,kernel)
    red = cv2.morphologyEx(red,cv2.MORPH_OPEN,kernel)
    red = cv2.dilate(red,kernel) 
    res = cv2.bitwise_and(image,image, mask= red)       
    hitam=cv2.threshold(red, 127, 255, cv2.THRESH_BINARY_INV)[1]
	# show the frame
    #(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #for plc, contour in enumerate(contours):
	#area = cv2.contourArea(contour)
	#if (area>300):
	 #  x,y,w,h = cv2.boundingRect(contour)
	  # image =cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
	   #cv2.putText(img,"Orange Color",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))
    print video1    
    cv2.imshow("tracking",res)
    cv2.imshow("video" ,video)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
