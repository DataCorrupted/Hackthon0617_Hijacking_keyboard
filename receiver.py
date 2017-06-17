import evdev
from evdev import *
import os
from socket import *

def receive():
	# Receive data anytime. If no data, sleep / wait / do anything but return.
		
	host = ""
	port = 13000
	buf = 1024
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.bind(addr)
	(data, addr) = UDPSock.recvfrom(buf)
	data=data.split()
	code=data[0]
	value=data[1]
	UDPSock.close()
	return (int(code), int(value))

while True:
	(code, value) = receive()
	Inj = UInput()
	Inj.write(ecodes.EV_KEY, code, value)
	Inj.syn();