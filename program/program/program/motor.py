import cv2 as cv

image=cv.imread('ball.jpg')
blur=cv.GaussianBlur(image,(11,11),0)
cv.imwrite('image',image)
cv.imshow('blur',blur)
cv.waitKey()	
