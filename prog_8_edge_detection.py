from matplotlib.image import imread
import cv2
import numpy as np

img=cv2.imread('chess_board.jpg')
img=cv2.resize(img, (0,0), fx=0.5 ,fy=0.5)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray,100,0.1,50)
corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img, (x,y), 5, (255,0,0), 1)


cv2.imshow('corners',img)
cv2.imwrite('chess_board_corners.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()