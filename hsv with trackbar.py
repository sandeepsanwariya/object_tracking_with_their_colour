import numpy as np
import cv2
import random
import time
cap=cv2.VideoCapture(0)



def empty():
    psss
cv2.namedWindow("tb")
cv2.resizeWindow("tb",640,240)
cv2.createTrackbar("hue_min","tb",0,179,empty)
cv2.createTrackbar("hue_max","tb",0,179,empty)
cv2.createTrackbar("sat_min","tb",0,255,empty)
cv2.createTrackbar("sat_max","tb",255,255,empty)
cv2.createTrackbar("val_min","tb",0,255,empty)
cv2.createTrackbar("val_max","tb",255,255,empty)


while True:
    success, img = cap.read()
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("hue_min","tb")
    hmax = cv2.getTrackbarPos("hue_max","tb")
    smin = cv2.getTrackbarPos("sat_min","tb")
    smax = cv2.getTrackbarPos("sat_max","tb")
    vmin = cv2.getTrackbarPos("val_min","tb")
    vmax = cv2.getTrackbarPos("val_max","tb")

    lower=np.array([hmin,smin,vmin])

    upper=np.array([hmax,smax,vmax])
    print("lower-", lower,'upper-',upper)
    mask=cv2.inRange(imghsv,lower,upper)
    print(type(mask))

    imgr=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow(" image",img)
    cv2.imshow(" image2",imghsv)
    cv2.imshow(" image3", mask)
    #cv2.imshow(" image4q", imgr)
    cv2.waitKey(1)
    if cv2.waitKey(1)  & 0xFF ==ord("q"):
        break
