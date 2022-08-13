import cv2

img=cv2.imread('acc.jpg',0) #reads image

img=cv2.resize(img, (0,0), fx=3,fy=3) #resize image

img=cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) #rotates image

#cv2.imwrite('code_image_1.jpg',img) #saves image

cv2.imshow('Accident zone',img) #displays image
cv2.waitKey(0) #holds the window until a key is pressed
cv2.destroyAllWindows() #destroys the windows
