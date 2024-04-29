import cv2
import numpy as np

web = cv2.VideoCapture(0)
ker = np.ones((5, 5), np.uint8)

while True:
    success, frame = web.read()
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.GaussianBlur(frame, (7,7), 0)
    frame3 = cv2.Canny(frame, 100, 100)
    frame4 = cv2.dilate(frame3, ker, iterations=1)
    frame5 = cv2.erode(frame4, ker, iterations=1)


    cv2.imshow('Video', frame)
    cv2.imshow('Video1', frame1)
    cv2.imshow('Video2', frame2)
    cv2.imshow('Video3', frame3)
    cv2.imshow('Video4', frame4)
    cv2.imshow('Video5', frame5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break