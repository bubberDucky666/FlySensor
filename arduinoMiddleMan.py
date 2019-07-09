import serial
import time
import vidTrack5
import screenMonitor as sM
import struct

prtName = "/dev/cu.usbmodem14201"
baud    = 9600

threshold = 180
maxVal    = 225
minArea   = 4000
maxArea   = 10000

Port = serial.Serial(prtName, baud, timeout=.1)
time.sleep(.5)

Tracker = sM.Tracker(threshold, maxVal, minArea, maxArea)

nC = sM.cal(Tracker)

# input("Send thing") 
# while True:
#      Port.write(1)


#You can possibly integrate a timed aspect to things, but maybe not
while True:
    c = sM.check(Tracker, nC, Tracker.minArea, maxArea)

    time.sleep(2)

    msg     = Port.read()
    #oC      = subject

    # if msg:
    #     print(msg)
    
    # print("___________________")
    # print("Ard:")
    # print(msg)
    # print("___________________")
   

    if c not in nC and c > nC[1]:
        Port.write(1)
        print("Detected")
        time.sleep(.08)
        
        while True:
            c = sM.check(Tracker, nC, Tracker.minArea, Tracker.maxArea)
            if c < nC:
                break
        