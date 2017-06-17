import evdev
from evdev import *

def receiver():
	# Receive data anytime. If no data, sleep / wait / do anything but return.

while True:
	event = receive()
	Inj = UInput()
	Inj.write_event(event)
	Inj.syn();