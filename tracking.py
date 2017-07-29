import cv2
import numpy as np

WINDOW_NAME = 'orangeBallTracker'

def tracking(image):
	blur = cv2.GaussianBlur(image, (5,5),0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	lower_orange = np.array ([40,70,70])
	upper_orange = np.array ([80,200,200])
	mask = cv2.inRange(hsv, lower_orange, upper_orange)
	bmask = cv2.GaussianBlur(mask, (5,5),0)
	#ambil data centroid
	moments = cv2.moments(bmask)
	m00 = moments['m00']
	centroid_x, centroid_y = None, None
	if m00 !=0:
		centroid_x = int(moments['m00']/m00)
		centroid_y = int(moments['m00']/m00)
		
	ctr= (-1,-1)
	#jika data centroid sudah ada
	if centroid_x != None and centroid_y != None:
		ctr = (centroid_x, centroid_y)
		#meletakkan lingkaran hitam
		cv2.circle(image, ctr,4, (0,0,0))
	#menamplakan RGB
	cv2.imshow(WINDOW_NAME, image)
	if cv2.waitKey(1) & 0xFF == 27:
		ctr = None
	return ctr
	
#input camera
if __name__ == '__main__':
	capture = cv2.VideoCapture(0)
	while True:
		done, image = capture.read()
		if done :
			if not tracking(image):
				break
			if cv2.waitKey(1) & 0xFF == 27:
				break
		else :
			print('capture failed')
			break
