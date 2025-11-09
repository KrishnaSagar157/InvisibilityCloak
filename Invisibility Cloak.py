import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)
time.sleep(2)
background=None

while True:

    ret,frame=cap.read()
    if not ret:
        break

    frame=cv2.flip(frame,1)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red1=np.array([0,120,70])
    upper_red1=np.array([10,255,255])
    lower_red2=np.array([170,120,70])
    upper_red2=np.array([180,255,255])

    mask1=cv2.inRange(hsv,lower_red1,upper_red1)
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    mask=mask1 + mask2

    
    kernel=np.ones((3,3),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.dilate(mask,kernel,iterations=1)

    key =cv2.waitKey(1) & 0xFF
    if key == ord('b'):
        background=frame.copy()
        print("Background Captured")
        continue



    if background is not None:
        mask_inv=cv2.bitwise_not(mask)
        cloak_area=cv2.bitwise_and(background,background,mask=mask)
        person_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
        final = cv2.addWeighted(cloak_area, 1, person_area, 1, 0)
        cv2.imshow('Invisibility Cloak',final)
    
    else:
        cv2.putText(frame, "Press 'b' to capture background", (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.imshow('Invisibility Cloak', frame)

    
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()