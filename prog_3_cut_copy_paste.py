import cv2

img=cv2.imread('acc.jpg')
#print(img.shape)
copy=img[67:117,100:150]
img[0:50,0:50]=copy

for i in range(67,117):
    for j in range(100,150):
        img[i][j]=[255,255,255]


cv2.imshow('Cut copy paste',img)
cv2.waitKey(0)
cv2.destroyAllWindows()