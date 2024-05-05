import cv2
import numpy as np
from contour import contours

web = cv2.VideoCapture(0)
web.set(3, 640)
web.set(4, 480)

while True:
    ret, frame = web.read()
    imgc = frame.copy()
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.GaussianBlur(frame1, (7, 7), 0)
    frame3 = cv2.Canny(frame2, 50, 200)
    contours(frame3, imgc)

    cv2.imshow('frame', frame)
    cv2.imshow('can', imgc)
    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)
    cv2.imshow('frame3', frame3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
