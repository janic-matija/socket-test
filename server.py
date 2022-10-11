#!/usr/bin/python3           # This is server.py file
import socket

# create a socket object


# get local machine name
host = '0.0.0.0'

port = 9700

while port < 9750:
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serversocket.bind((host, port))

    serversocket.listen(50)

    clientsocket, addr = serversocket.accept()
    byte = clientsocket.recv(2)
    nesto = int.from_bytes(byte, 'big')
    print(nesto)

    port += 1
    clientsocket.close()
    serversocket.close()


