#this program takes some time to scan everything, I recommend you to run it on a vps and wait until its finished.
#as this program isnt so fast, i would like you to give me some ideas to make it faster, thank you.

import socket
import sys
import os
import _thread
import time

def scan(port, ip, t):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[SCANNING] "+ip+"\n")
    sock.settimeout(t)
    result = sock.connect_ex((ip, port))    #sends packets and waits for a response
    if result == 0:
    	f.write(ip+"\n")
    	print("[OPEN] "+ip+"\n")
    else: print("[CLOSED] "+ip+"\n")
    sock.close()
    
if __name__ == '__main__':
    if os.getuid() != 0:
        print("                You need to be root!")
        quit()
    os.system("ulimit -s 99999; ulimit -n 99999")
    os.system("sysctl -w fs.file-max=999999 1>/dev/null 2>/dev/null")
    os.system("ulimit 9999999; ulimit -H 99999999")
    #this will let you send more packets at the same time, btw, use linux, but the new windows terminal seems pretty good, havent tried yet...
    
    try:
        port = int(sys.argv[1])
        outpf = sys.argv[2]
        t = int(sys.argv[3])
        #checks for the inputs while starting the program
    except:
        print("Usage: python "+sys.argv[0]+" <PORT> <OUTPUT_FILE> <SECONDS_TIMEOUT>")
        quit()
    f=open(outpf, "w+")
    print("INTERNET SCANNING STARTED WITH PORT: "+str(port)+"\n")
    
    for i in range(254): 
        i += 1
        s=0
        if i != 10 or i != 127:
            for o in range(256):
                if i != 192 and o != 168 or i != 172 and o < 16 and o > 31 or i != 169 and o != 254:
                    for p in range(256):
                        for u in range(256):
                            ip=str(i)+"."+str(o)+"."+str(p)+"."+str(u)
                            #declares the ip that is going to be used
                            t = _thread.start_new_thread (scan, (port, ip, t, ))
                            s += 0
                            if s == 500:
                                time.sleep(35)
                                s = 0
                            #to do multiple threads
    
    f.close
    print("All the internet scanned!!")
