import os, time
while(1):
    # delete previous file
    try:
        os.unlink("./image.png")
    except:
        pass

    # download the file
    os.system("curl 192.168.9.20/image.png > ./image.png")

    # sleep
    time.sleep(0.5)
