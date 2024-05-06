import cv2
import numpy as np

facecascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

web = cv2.VideoCapture(0)

while True:
    _, frame = web.read()
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces1 = facecascade.detectMultiScale(frame, 1.3, 5)
    faces2 = facecascade.detectMultiScale(frame2, 1.3, 5)

    for (x, y, w, h) in faces1:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x, y, w, h) in faces2:
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Chaman', (x, y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


    cv2.imshow('Video', frame)
    cv2.imshow('Face Detection', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break