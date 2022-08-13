import cv2
import random as r
#opencv uses BGR

img=cv2.imread('acc.jpg')
print(img.shape)

for i in range(int(img.shape[0]/2)):
    for j in range(int(img.shape[1]/2)):
        img[i][j]=[r.randrange(255),r.randrange(255),r.randrange(255)]

img=cv2.resize(img,(0,0),fx=3,fy=3)
cv2.imwrite('randomcolor.jpg',img)
cv2.imshow('Customized',img)
cv2.waitKey(0)
cv2.destroyAllWindows()