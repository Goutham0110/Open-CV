import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([100, 50, 20])
    upper = np.array([255, 100, 150])

    msk = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=msk)

    cv2.imshow('hsv', res)
    if(cv2.waitKey(1) == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()