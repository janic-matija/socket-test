import os
import socket
import sys
import time

BUFF = 1_000_000_000
HOST = "192.168.122.17"
SERVER_HOST = "0.0.0.0"  # any
PORT = 9999

start = time.time()

if sys.argv[0] == 'fromHost.py':  # server prima fajl

    print("if")
    server_sock = socket.socket()
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        BUFF)
    print("bind")
    server_sock.bind((SERVER_HOST, PORT))
    print("listen")
    server_sock.listen(65535)
    client, address = server_sock.accept()
    poruka = "poruka"
    client.send(bytes(poruka, "utf-8"))

    server_sock.close()
else:
    os.system("python3 fromHost.py")
    client_sock = socket.socket()
    client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        BUFF)
    # time.sleep(0)
    print("budan")
    client_sock.connect((HOST, PORT))
    poruka = client_sock.recv(4)
    print(poruka)
    client_sock.close()

    print(time.time() - start)
