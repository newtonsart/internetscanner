#this program takes some time to scan everything, I recommend you to run it on a vps and wait until its finished.
#as this program isnt so fast, i would like you to give me some ideas to make it faster, thank you.
import socket
import sys
import os
def scan(port, t):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(t)
    for i in range(254): 
        i += 1 
        if i != 10 or i != 127: 
            for o in range(256): 
                if i != 192 and o != 168 or i != 172 and o < 16 and o > 31 or i != 169 and o != 254: 
                    for p in range(256): 
                        for u in range(256): 
                            ip=str(i)+"."+str(o)+"."+str(p)+"."+str(u)
                            print("[SCANNING] "+ip)
                            result = sock.connect_ex((ip, port))
                            if result == 0:
                                f.write(ip)
                                print("[OPEN] "+ip)
                            else: print("[CLOSED] "+ip)
                            sock.close()
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
        outpf = sys.argv[2]
        t = int(sys.argv[3])
    except:
        print("Usage: python "+sys.argv[0]+" <PORT> <OUTPUT_FILE> <SECONDS_TIMEOUT>")
        quit()
    f=open(outpf,"w+")
    print("INTERNET SCANNING STARTED WITH PORT: "+str(port))
    scan(port, t)
    f.close
    print("All the internet scanned!!")
