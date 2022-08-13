import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    img=np.zeros(frame.shape, np.uint8) 

    sm_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)

    img[:height//2, :width//2]=sm_frame  #top left
    img[height//2:, :width//2]=cv2.rotate(sm_frame,cv2.cv2.ROTATE_180)  #top right
    img[:height//2, width//2:]=sm_frame  #bottom left
    img[height//2:, width//2:]=sm_frame  #bottom right

    cv2.imshow('img',img)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()    
cv2.destroyAllWindows()
