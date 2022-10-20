import socket
import sys

UDP_IP = ""
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

filename = "recv/big"
with open(filename, "wb") as f:
    while True:
        bytes_read = sock.recvfrom(4096)
        if not bytes_read:
            break
        f.write(bytes_read[0])
        # print(sys.getsizeof(bytes_read))
