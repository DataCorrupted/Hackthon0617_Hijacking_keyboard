import os, time
while(1):
    # delete previous file
    try:
        os.unlink("./image1.png")
    except:
        pass

    # download the file
    a = os.system("curl 192.168.9.20/image.png > ./image1.png")
    print(a)
    if (a == 0):
    	os.system("mv ./image1.png ./image.png")

    exit(0)

    # sleep
    time.sleep(0.1)
