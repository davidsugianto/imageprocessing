import cv2 as cv
import numpy as np
image=cv.imread('/home/pi/program/gambar.png')
process = cv.cvtColor(image,cv.COLOR_BGR2HSV)
g1=process[:,:,0]
g2=process[:,:,1]
g3=process[:,:,2]
cv.imshow('image',g1)
cv.imshow('image1',g2)
cv.imshow('image2',g3)

cv.waitKey()
