import cv2

print(cv2.__version__)

img = cv2.imread("Resources\\puppy.jpg")

cv2.imshow("Output", img)

#Setting a delay, 0 means infinite
cv2.waitKey(0)

# cap = cv2.VideoCapture("Resources\\Testing video.mp4")
framewidth = 1000
frameheight = 500
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 100)


while True:
    success, frame = cap.read()
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
