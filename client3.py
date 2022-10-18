import socket

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
HOST = "10.18.110.76"
PORT = 5001
filename = "data/big"

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
s.close()
