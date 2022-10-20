import os
import socket
import sys
import time

start_time = time.time()

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1000000
HOST = "10.18.110.49"
PORT = 5001
filename = "data/big3"

s = socket.socket()
print(f"[+] Connecting to {HOST}:{PORT}")
s.connect((HOST, PORT))
print("[+] Connected.")

with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        # print(sys.getsizeof(bytes_read))
s.close()

end_time = time.time()
print(str(end_time - start_time))
