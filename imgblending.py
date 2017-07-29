import cv2
import numpy as np

img1 = cv2.imread('bola.jpg')
img2 = cv2.imread('bola1.jpg')

hasil = cv2.addWeighted(img1,0.9,img2,0.5,0)

cv2.imshow('hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
