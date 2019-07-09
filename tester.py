import serial
import time

prtName = "/dev/cu.usbmodem14201"
baud    = 9600

Port = serial.Serial(prtName, baud, timeout=.1)

for i in range(300):
	time.sleep(.08)
	Port.write(1)

Port.reset_output_buffer()
Port.close()
