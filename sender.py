
import evdev
from evdev import *
import os
from socket import *

print ("enter ifconig -a to find out your ip (inet addr)")
host = "192.168.9.52" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
def send(event):
	# make sure all events are keyboard.
	if event.type != 1:
		return
	data=(str(event.code)+" "+str(event.value)).encode("UTF-8")
	UDPSock.sendto(data, addr)
	print(event, "sent");

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
devices.reverse();
for device in devices:
	if "keyboard" in device.name:
		break;
print(device)	
print();
grabbed = False
last = -1
ui = UInput()

for event in device.read_loop():
	#print(categorize(event))
	if grabbed:
		send(event)
	# Trace keyboard only.
	if event.type != evdev.ecodes.EV_KEY:
		continue;
	# Only trace when left the key
	if event.value == 1:
		continue;
	if not grabbed and event.code == 2 and last == 56:
		device.grab();
		grabbed = not grabbed;
		print("grab")
	if grabbed and event.code == 3 and last == 56:
		device.ungrab();
		grabbed = not grabbed;
		print("ungrab")
	last = event.code;
