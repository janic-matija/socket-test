import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(("10.18.110.76", 9998))
#10.18.110.49
msg = s.recv(1024)
print(msg.decode("utf-8"))
