import serial
import os
import time

ser = serial.Serial("COM12", 115200)

# if rate of radio-activities is below thresh 
# then social distancing is implemented 
thresh = 40 # found through experimentation

# hashmap to store unique mac addresses
macs = {}

x = ser.readline()
start = time.time()

while x :
	new_mac = str(x).split(" ")
	if new_mac[6] not in macs : # add unique mac address
		macs[new_mac[6]] = 1

	if (time.time() - start) >= 60 : # reset timer after every 60 seconds	
		rate = 60*len(macs)//(time.time() - start)
		print("Current Rate : ",rate)
		if rate >= thresh :
			print("Warning : Socail Distancing Violated !!")
		macs = {}
		start = time.time()
		print("rate updated after evry 60 seconds !!! ") 

	try:
		x = ser.readline()
	except:
		break
else :
	print("got Nothin !!")
print()
