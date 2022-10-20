import socket
import sys
import os
import paramiko
import time

BUFFER_SIZE = 1000000
HOST = "10.18.110.76"
PORT = 9999

file_recv = "/home/matija/from_host/big3"

recv_file_socket = socket.socket()
recv_file_socket.connect((HOST, PORT))

with open(file_recv, "wb") as fr:
    while True:
        bytes_read = recv_file_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        fr.write(bytes_read)

recv_file_socket.close()
