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
	data=map(int, data.split())
	code=data[0]
	value=data[1]
	return (code, value)

Inj = UInput()
while True:
	(code, value) = receive()
	Inj.write(ecodes.EV_KEY, code, value)
	Inj.syn();
