import cv2
import numpy as np

width, height = 640, 480

framewidth = 1000
frameheight = 500
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 100)

def preprocessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)
    imgcanny = cv2.Canny(imgBlur, 100, 200)
    
    ker = np.ones((5, 5), np.uint8)
    imgdial = cv2.dilate(imgcanny, ker, iterations=1)
    imgerode = cv2.erode(imgdial,ker,iterations=1)

    return imgerode

def contours(img, imgc):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area > 500:
            cv2.drawContours(imgc, cnt, -1, (0, 255, 0), 2)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(approx)

            cor = len(approx)

            x, y, w, h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (width, height))

    img3 = preprocessing(img)

    cv2.imshow("Video", img)
    cv2.imshow("New",img3)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
