import cv2
import numpy as np

img = cv2.imread('Resources\\King Cards.jpg')

width, height = 250, 350
pts1 = np.float32([[419, 92], [590, 111], [400, 328], [585, 348]])
pts2 = np.float32([[0, 0],[width, 0],[0, height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(img, matrix, (width, height))

print(pts1)
print(pts2)
cv2.imshow('img',warped)
cv2.imshow('warped',img)

cv2.waitKey(0)