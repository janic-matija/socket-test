import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((socket.gethostname(), 9998))

msg = s.recv(1024)
print(msg.decode("utf-8"))
