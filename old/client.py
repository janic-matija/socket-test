#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object


# get local machine name
host = "10.18.110.76"

port = 9700

# connection to hostname on the port.

while port < 9750:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(host + " " + str(port))
    s.connect((host, port))
    # Receive no more than 1024 bytes
    byte = port.to_bytes(2, 'big')
    print(port - 9700)
    msg = s.send(byte)
    port += 1

    s.close()

