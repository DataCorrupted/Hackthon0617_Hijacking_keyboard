import evdev
from evdev import *
import os
from socket import *

host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

def receive():
	# Receive data anytime. If no data, sleep / wait / do anything but return.
	(data, addr) = UDPSock.recvfrom(buf)
	data=data.split()
        print data
	code=data[0]
	value=data[1]
	return (int(code), int(value))

while True:
	(code, value) = receive()
	Inj = UInput()
	Inj.write(ecodes.EV_KEY, code, value)
	Inj.syn();
