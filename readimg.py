import cv2
import numpy as np
#import matplotlib.pyplot as plt

# Load an color image in grayscale
img = cv2.imread('bola1.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
