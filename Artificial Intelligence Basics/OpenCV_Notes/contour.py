import cv2
import numpy as np

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

            if cor == 3: objt = 'Triangle'
            elif cor == 4:
                if w == h:
                    objt = 'Square'
                else:
                    objt = 'Rectangle'

            elif cor == 5: objt = 'Pentagon'
            elif cor == 6: objt = 'Hexagon'
            else: objt = 'Circle'


            cv2.rectangle(imgc, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(imgc, objt, (x + (w//2), y + (h//2)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)




path = 'Resources\\shapes.png'

img = cv2.imread(path)
imgc = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)
canny = cv2.Canny(blur, 50, 50)
here = np.hstack((canny, blur))

contours(canny, imgc)
# cv2.imshow('Original', img)
here2 = np.hstack((img, imgc))

cv2.imshow('Both', here2)
cv2.imshow('Gray', gray)
cv2.imshow('Blur', here)

cv2.waitKey(0)