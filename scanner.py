#this program takes some time to scan everything, I recommend you to run it on a vps and wait until its finished.
#as this program isnt so fast, i would like you to give me some ideas to make it faster, thank you.
import socket
import sys
import os
from threading import Thread
x=0
def scan(port, x):
    z = -1
    for i in range(254): 
        i += 1 
        if i != 10 or i != 127: 
            for o in range(256): 
                if i != 192 and o != 168 or i != 172 and o < 16 and o > 31 or i != 169 and o != 254: 
                    for p in range(256): 
                        for u in range(256): 
                            ip=str(i)+"."+str(o)+"."+str(p)+"."+str(u)
                            z+=1
                            if x == z:
                                print("[SCANNING] "+ip)
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                result = sock.connect_ex((ip, port))
                                if result == 0:
                                    f.write("[OPEN] "+ip)
                                    print("[OPEN] "+ip)
                                else: print("[CLOSED] "+ip)
                                sock.close()
                                return
if __name__ == '__main__':
    if os.getuid() != 0:
        print("                You need to be root!")
        quit()
    os.system("ulimit -s 99999; ulimit -n 99999")
    os.system("sysctl -w fs.file-max=999999 1>/dev/null 2>/dev/null")
    os.system("ulimit 9999999; ulimit -H 99999999")
    try:
        port = int(sys.argv[1])
        outpf = sys.argv[2]
    except:
        print("Usage: python "+sys.argv[0]+" <PORT> <OUTPUT_FILE>")
        quit()
    f=open(outpf,"w+")
    print("INTERNET SCANNING STARTED WITH PORT: "+str(port))
    while x < 4228507922:
        Thread(target = scan(port, x)).start()
        x+=1
    f.close
    print("All the internet scanned!!")
