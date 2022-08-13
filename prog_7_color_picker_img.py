import cv2
import numpy as np

arr = cv2.imread('D:\code\Others\opencv_trial\color_pallete.png')


hsv = cv2.cvtColor(arr, cv2.COLOR_BGR2HSV)
lower = np.array([0, 0, 0])
upper = np.array([10, 10, 10])
msk = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(arr, arr, mask=msk)
cv2.imshow('hsv', res)
cv2.waitKey(0)  # holds the window until a key is pressed
cv2.destroyAllWindows()  # destroys the windows
