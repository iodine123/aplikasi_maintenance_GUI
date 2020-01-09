from serial import *

availSerial=False

ser=Serial()
def connectSerial():
	global ser
	global availSerial
	baudRate=9600
	try:
		serialPort = "/dev/ttyUSB0"
		ser= Serial(serialPort,baudRate,timeout=0, writeTimeout=0)	
		print("serial 0")
		ready = 1
	
	except:
			serialPort = "/dev/ttyUSB1"
			ser= Serial(serialPort,baudRate,timeout=0, writeTimeout=0)	
			print("serial 1")
	


def enterMode():
	a = "c"
	try:
		ser.write(str.encode(a))
	except: 
		pass
	print(a)

def exitMode():
	a = "X"
	try:
		ser.write(str.encode(a))
	except: 
		pass
	print(a)

def motorWake():
	a = "mW"
	try:
		ser.write(str.encode(a))
	except: 
		pass
	print(a)

def motorSleep():
	a = "m4"
	try:
		ser.write(str.encode(a))
	except: 
		pass
	print(a)

def motorHome():
	a = "mH"
	try:
		ser.write(str.encode(a))
	except: 
		pass
	print(a)

def cekSensor():
	a = "s"
	try:
		ser.write(str.encode(a))
	except: 
		pass
	print(a)

def tes(lokasi, mode):
	a = "t" + lokasi + mode
	print(mode)
	print(a)
	try:
		ser.write(str.encode(a))
	except: 
		pass
	
