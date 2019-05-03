import socket
import sys
import os
from threading import Thread

def scanback(port):
    for i in range(127):
        if i != 10 or i != 127: 
            for o in range(256):
                if i != 192 and o != 168 or i != 172 and o < 16 and o > 31 or i != 169 and o != 254: 
                    for p in range(256): 
                        for u in range(256):
                            i-=127
                            o-=255
                            p-=255
                            u-=255
                            ipb=str(abs(i))+"."+str(abs(o))+"."+str(abs(p))+"."+str(abs(u))
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            result = sock.connect_ex((ipb, port))
                            print(ip)
                            if result == 0:
                                f.write("[OPEN] "+ipb)
                                print("[OPEN] "+ipb)
                            sock.close()

def scan(port):
    for i in range(127): 
        i += 1 
        if i != 10 or i != 127: 
            for o in range(256): 
                if i != 192 and o != 168 or i != 172 and o < 16 and o > 31 or i != 169 and o != 254: 
                    for p in range(256): 
                        for u in range(256): 
                            ip=str(i)+"."+str(o)+"."+str(p)+"."+str(u)
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            result = sock.connect_ex((ip, port))
                            print(ip)
                            if result == 0:
                                f.write("[OPEN] "+ip)
                                print("[OPEN] "+ip)
                            sock.close()
                        
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
    Thread(target = scan(port)).start()
    Thread(target = scanback(port)).start()
    f.close
    print("All the internet scanned!!")