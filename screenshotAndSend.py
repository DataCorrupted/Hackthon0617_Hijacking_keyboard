

#!/usr/bin/env python
from socket import *
import pyscreenshot as ImageGrab
import time

host = "192.168.9.20" # set to IP address of targe
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
buf=1024
while(True):
    image = ImageGrab.grab();
    image.save("/var/www/html/image.png",format="png")
    time.sleep(5)


