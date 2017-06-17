
import evdev
from evdev import *

def send(event):
	print(event);
	Inj = UInput()
	Inj.write_event(event)
	Inj.syn()

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
devices.reverse();
device = devices[3]
print(device)
print();
grabbed = False
last = -1
ui = UInput()

for event in device.read_loop():
	print(categorize(event))
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
