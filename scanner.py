#this program takes some time to scan everything, I recommend you to run it on a vps and wait until its finished.
#as this program isnt so fast, i would like you to give me some ideas to make it faster, thank you.
import socket
import sys
import os
def scan(port):
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
    t = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(t)
    if os.getuid() != 0:
        print("                You need to be root!")
        quit()
    os.system("ulimit -s 99999; ulimit -n 99999")
    os.system("sysctl -w fs.file-max=999999 1>/dev/null 2>/dev/null")
    os.system("ulimit 9999999; ulimit -H 99999999")
    try:
        port = int(sys.argv[1])
        outpf = sys.argv[2]
        if sys.argv[3] == "-t":
            sock.settimeout(sys.argv[4])
        else: pass

    except:
        print("Usage: python "+sys.argv[0]+" <PORT> <OUTPUT_FILE>\nYou can also use your own timeout, after the output file write: -t <SECONDS_TIMEOUT>")
        quit()
    f=open(outpf,"w+")
    print("INTERNET SCANNING STARTED WITH PORT: "+str(port))
    scan(port)
    f.close
    print("All the internet scanned!!")
