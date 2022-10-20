import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('10.18.110.76', 9998))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len: ", msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        print(f"full message length: {msglen}")
        full_msg += msg.decode("utf-8")

        print(len(full_msg))
        if len(full_msg) - HEADERSIZE == msglen:
            print("full message received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
