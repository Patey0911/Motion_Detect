import cv2
import numpy as np
###k=cv2.VideoCapture(0)
#while(True):
 #   _,video=k.read()
  #  cv2.imshow('Camera',video)
   # y=cv2.waitKey(30) & 0xff
    #if(y==27):
     #   break

#events=[i for i in dir(cv2) if 'EVENT' in i]

cap=cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while(cap.isOpened()):
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur= cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh=cv2.threshold(blur, 20, 225, cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=10)
    contours, _=cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, w, h)=cv2.boundingRect(contour)
        if(cv2.contourArea(contour)<5000):
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h), (0,255,0), 2)
        cv2.putText(frame1,"Status: {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    
    cv2.imshow("frame",frame1)
    frame1=frame2
    ret, frame2=cap.read()

    if(cv2.waitKey(40)==27):
        break

cv2.destroyAllWindows()
cap.release()