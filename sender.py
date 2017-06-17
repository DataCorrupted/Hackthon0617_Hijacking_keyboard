
import evdev
from evdev import *
import os
from socket import *



def send(event):
	host = "192.168.18.219" # set to IP address of target computer
	port = 13000
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	data=(str(event.code)+" "+str(event.value)).encode("UTF-8")
	UDPSock.sendto(data, addr)
	UDPSock.close()
	print(event);
	"""Inj = UInput()
	Inj.write_event(event)
	Inj.syn()"""

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
devices.reverse();
device = devices[3]
print(device)
print();
grabbed = False
last = -1
ui = UInput()

for event in device.read_loop():
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
