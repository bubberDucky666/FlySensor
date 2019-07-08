import serial
import time
import vidTrack5
import screenMonitor as sM
import struct

prtName = "/dev/cu.usbmodem14201"
baud    = 9600

threshold = 90
maxVal    = 225
minArea   = 400
maxArea   = 4000

Port = serial.Serial(prtName, baud, timeout=.1)
#time.sleep(2)

Tracker = sM.Tracker(threshold, maxVal, minArea, maxArea)

nC = sM.cal(Tracker)

input("Send thing") 
while True:
     Port.write(1)


#You can possibly integrate a timed aspect to things, but maybe not
while True:
    subject = sM.check(Tracker, nC)
    # msg     = Port.readline()
    #oC      = subject

    # if msg:
    #     print(msg)
    
    #     print("___________________")
    #     print("Ard:")
    #     print(msg)
    #     print("___________________")

    if subject > nC:
        Port.write(1)
        
        while True:
            subject = sM.check(Tracker, subject)
            if subject < nC:
                break