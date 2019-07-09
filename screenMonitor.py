from cv2 import cv2
import time
from PIL import ImageGrab as ig
import numpy as np
from vidTrack5 import Tracker
import serial

dur         = 1
threshold 	= 90
maxVal		= 100
minArea 	= 1000
maxArea     = 4000

# Initial calibration period
def cal(Tracker):
    input("Open camera software but do not add fly to video")
    print("Calibration starting")

    var    = True
    while var:
        neutAr = []
        for i in range(3):
            img = ig.grab()
            img = np.array(img)

            val = Tracker.getContours(img)
            neutAr.append(val)
            #cv2.imshow("ye", img )
        c0 = len(neutAr[0])
        c1 = len(neutAr[1])
        c2 = len(neutAr[2])

        print(c0, c1, c2)

        if c0 == c1 and c1 ==c2:
            nC  = neutAr[1]
            var = False

    print("Calibration compleate")
    input("Hit enter/space, then start recording. Hit same button to end.")
    return len(nC)

def check(Tracker, nC, minArea, max):
    
    img   = ig.grab()
    #img.show()
    #print("shown")
    frame = np.array(img)
    c     = 0

    contours = Tracker.getContours(frame)

    time.sleep(2)

    for i in range(len(contours)):
        #------ Basic Declarations ---------------------

        p         = contours[i]
        #desired area
        area      = cv2.contourArea(p)
        
        #-------------------------------------------------
        
        #------- Contour Calculations --------------------
            
        if area >= minArea and maxArea <= maxArea:
            
            c = c +1

            # #make rotating boxes around points
            # rect = cv2.minAreaRect(p)
            # box	 = cv2.boxPoints(rect)
            # box  = np.int0(box)

            # #put the box onto the original frame
            # cv2.drawContours(frame, [box], 0, (0,255,0), 2)

            # cv2.imshow("message", frame)
            # if cv2.waitKey(1) == 27:
            #    input()
    
    print(c)
    return c




