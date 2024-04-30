import cv2
import numpy as np

img = cv2.imread('Resources\\puppy.jpg')
print(img.shape)
# cv2.resize

imgnew = img[0:200, 100:400]

cv2.imshow('Puppy', img)
cv2.imshow('Puppy new', imgnew)


cv2.waitKey(0)