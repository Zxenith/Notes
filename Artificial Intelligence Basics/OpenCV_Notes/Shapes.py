import cv2
import numpy as np

ker = np.ones((5,5), np.uint8)
web = cv2.VideoCapture(0)
web.set(3,1280)
web.set(4,720)


while True:
    success, img = web.read()
    # img = cv2.Canny(img, 100, 100)
    # img = cv2.dilate(img, ker, iterations=1)
    # img = cv2.erode(img, ker, iterations=1)
    cv2.line(img,(100,100),(img.shape[1], img.shape[0]),(0,0,255),5)
    cv2.rectangle(img, (0, 0), (250,300), (0,0,255), 2) #cv2.FILLED
    cv2.circle(img,(500,100),45,(0,250,255), 5)
    cv2.putText(img, "Hello World", (300,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 5)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# cv2.imshow('here', img)

# cv2.waitKey(0)