import socket
import sys
try:
    port = sys.argv[1]
    outpf = sys.argv[2]
except:
    print("Usage: python "+sys.argv[0]+" <PORT> <OUTPUT_FILE>")
    quit()
f=open(outpf,"w+")
for i in range(254):
    i += 1
    if i == 10 or i == 127:
        pass
    else:
        for o in range(256):
            if i == 192 and o == 168 or i == 172 and o >= 16 and o <= 31 or i == 169 and o == 254:
                pass
            else:
                for p in range(256):
                    for u in range(256):
                        ip=str(i)+"."+str(o)+"."+str(p)+"."+str(u)
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex((ip, port))
                        if result == 0:
                            f.write("[OPEN] "+ip+"\n")
                            print("[OPEN] "+ip+"\n")
                        sock.close()
f.close
print("All the internet scanned!!")
