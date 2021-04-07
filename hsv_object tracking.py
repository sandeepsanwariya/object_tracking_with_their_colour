import cv2
import numpy as np
import imutils
cap=cv2.VideoCapture(0)

while True:

    success,img=cap.read()

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #red
    l_r = np.array([0, 50, 120])
    u_r = np.array([10, 255, 255])

    #yellow
    l_y = np.array([25, 70, 120])
    u_y = np.array([30, 255, 255])

    #green
    l_g = np.array([45, 181 , 29])
    u_g = np.array([179, 255, 227])

    #blue
    l_b = np.array([90, 60, 0])
    u_b = np.array([121, 255, 255])

    mask1 = cv2.inRange(hsv,l_y,u_y)
    mask2 = cv2.inRange(hsv, l_g, u_g)
    mask3 = cv2.inRange(hsv, l_r, u_r)
    mask4 = cv2.inRange(hsv, l_b, u_b)

    cnts1=cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts1 =imutils.grab_contours(cnts1)

    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)

    cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)

    for c in cnts1:
        area1=cv2.contourArea(c)
        if area1>5000:
            cv2.drawContours(img,[c],-1,(0,255,0),3)

            M=cv2.moments(c)

            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])

            cv2.circle(img,(cx,cy),7,(255,255,255),-1)
            cv2.putText(img,"yellow",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)

    for c in cnts2:
        area2=cv2.contourArea(c)
        if area2>5000:
            cv2.drawContours(img,[c],-1,(0,255,0),3)

            M=cv2.moments(c)

            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])

            cv2.circle(img,(cx,cy),7,(255,255,255),-1)
            cv2.putText(img,"grran",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)

    for c in cnts3:
        area3=cv2.contourArea(c)
        if area3>5000:
            cv2.drawContours(img,[c],-1,(0,255,0),3)

            M=cv2.moments(c)

            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])

            cv2.circle(img,(cx,cy),7,(255,255,255),-1)
            cv2.putText(img,"red",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)

    for c in cnts4:
        area4=cv2.contourArea(c)
        if area4>5000:
            cv2.drawContours(img,[c],-1,(0,255,0),3)

            M=cv2.moments(c)

            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])

            cv2.circle(img,(cx,cy),7,(255,255,255),-1)
            cv2.putText(img,"blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)





    cv2.imshow("tracking",img)
    if cv2.waitKey(5)  & 0xFF ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()