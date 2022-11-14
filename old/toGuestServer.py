import socket
import sys
import os
import paramiko
import time

start_time = time.time()

BUFFER_SIZE = 1000000
HOST = "10.18.110.76"
PORT = 9999
SERVER_HOST = "0.0.0.0"  # any
SERVER_PORT = 9999

send_file_socket = socket.socket()

send_file_socket.bind((SERVER_HOST, SERVER_PORT))

send_file_socket.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = send_file_socket.accept()
print(f"[+] {address} is connected.")
filename = "data/big3"
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        client_socket.sendall(bytes_read)
client_socket.close()
send_file_socket.close()

end_time = time.time()
print(str(end_time - start_time))
