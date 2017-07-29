import cv2
import numpy as np

img = cv2.imread('bola1.jpg')
retval, threshold =cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 =cv2.threshold(grayscaled, 220, 255, cv2.THRESH_BINARY)
cv2.imshow('ori', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()
