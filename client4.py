import socket
import sys

UDP_IP = "10.18.110.76"
UDP_PORT = 5005

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
filename = "data/big"
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(4096)
        if not bytes_read:
            break
        sock.sendto(bytes_read, (UDP_IP, UDP_PORT))
        # print(sys.getsizeof(bytes_read))
