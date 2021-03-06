
import evdev
from evdev import *
import os
from socket import *
import  gtk ,gobject
import time
buf=1024
host = "192.168.43.130:8888"
def receive():
	# Receive data anytime. If no data, sleep / wait / do anything but return.
	(data, addr) = UDPSock.recvfrom(buf)
	return data

#!/usr/bin/env python
# fullScreenScale.py - Show image scaled to full screen

def fitRect(thing, box): 
# scale 2
	scaleX=float(box.width)/thing.width
	scaleY=float(box.height)/thing.height
	scale=min(scaleY, scaleX) 
	thing.width=scale*thing.width 
	thing.height=scale*thing.height
# center 5
	thing.x=box.width/2-thing.width/2
	thing.y=box.height/2-thing.height/2 
	return thing 

def scaleToBg(pix, bg): 
	fit=fitRect( 
		gtk.gdk.Rectangle(0,0, pix.get_width(), pix.get_height()),
		gtk.gdk.Rectangle(0,0, bg.get_width(), bg.get_height())
		)
	scaled=pix.scale_simple(fit.width, fit.height, gtk.gdk.INTERP_BILINEAR)
	ret=bg.copy() 
	scaled.copy_area(
		src_x=0, src_y=0,
		width=fit.width, height=fit.height, 
		dest_pixbuf=ret, 
		dest_x=fit.x, dest_y=fit.y) 
	return ret 

def newPix(width, height, color=0x000000ff): 
	pix=gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, width , height) 
	pix.fill(color) 
	return pix 

def getScreenShot():
	image = ImageGrab.grab();
	image.show();

port = 13000
buf = 1024
addr = ("", port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

path="./image.jpg"
def receiveAndSaveImage():
	data=receive()
	f=open("image.jpg","w")
	try:
		while(data):
			f.write(data);
			UDPSock.settimeout(2)
			data=receive()
	except timeout:
		f.close()
		print "done\n\n\n" 
cnt=0


def setup():
	global err_cnt
	try:
		pix=gtk.gdk.pixbuf_new_from_file(os.path.join("./image0.png")) 
		window = gtk.Window()
		window.connect("destroy", gtk.main_quit)
		window.fullscreen() 
		bg=newPix(gtk.gdk.screen_width(), gtk.gdk.screen_height())
		pixFitted=scaleToBg(pix, bg) 
		image=gtk.image_new_from_pixbuf(pixFitted) 
		window.add(image)
		window.show_all()
	except:
		err_cnt += 1
		print(err_cnt)
		update()
		setup()

def update():
	global cnt, window, err_cnt
	while(1):
		a = os.system("curl %s/image.png > ./image.png"%(host,))
		if (a == 0):
			# cnt+=1
                        if(os.system("diff ./image.png ./image0.png")):
			    os.system("cp ./image.png  ./image0.png")
                            break
                        
			# os.system("mv ./image.png  ./image1.png")
		time.sleep(1/60.0)
		err_cnt += 1
		print(err_cnt)

def callback():
	global cnt,window
       
	# update the image
	update()
	# download the file
	

	# path="./image%s.png"%(cnt%2)
	#receiveAndSaveImage() 
	gtk.main_quit()
	setup()


	# pix=gtk.gdk.pixbuf_new_from_file(os.path.join(path)) 
	# bg=newPix(gtk.gdk.screen_width(), gtk.gdk.screen_height())
	# pixFitted=scaleToBg(pix, bg) 
	# image=gtk.image_new_from_pixbuf(pixFitted) 
	# window.clear()
	# window.add(image)
	# window.show_all()
	gobject.timeout_add(100,callback)
	gtk.main()

def main(): 
	global err_cnt
	err_cnt = 0
	setup()

	gobject.timeout_add(1,callback)
	gtk.main()

if __name__ == "__main__":
	main()

