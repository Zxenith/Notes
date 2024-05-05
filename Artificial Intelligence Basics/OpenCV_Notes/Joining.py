import cv2
import numpy as np

path = 'Resources\\King Cards.jpg'

def empty(a):
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 640, 480)
cv2.createTrackbar('Hue1', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('Hue2', 'Trackbars', 255, 255, empty)
cv2.createTrackbar('Saturation1', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('Saturation2', 'Trackbars', 255, 255, empty)
cv2.createTrackbar('Value1', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('Value2', 'Trackbars', 255, 255, empty)

while True:
    img = cv2.imread(path)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_lower = cv2.getTrackbarPos('Hue1', 'Trackbars')
    h_upper = cv2.getTrackbarPos('Hue2', 'Trackbars')
    s_lower = cv2.getTrackbarPos('Saturation1', 'Trackbars')
    s_upper = cv2.getTrackbarPos('Saturation2', 'Trackbars')
    v_lower = cv2.getTrackbarPos('Value1', 'Trackbars')
    v_upper = cv2.getTrackbarPos('Value2', 'Trackbars')
    print(h_lower,h_upper,s_lower,s_upper,v_lower,v_upper)

    lower = np.array([h_lower, s_lower, v_lower])
    upper = np.array([h_upper, s_upper, v_upper])
    mask = cv2.inRange(img, lower, upper)
    final = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('King', img)
    cv2.imshow('img', img2)
    cv2.imshow('mask', mask)
    cv2.imshow('final', final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break