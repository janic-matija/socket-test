import os
import socket

IPs = os.popen('ip a')
line = IPs.readline()
ip = ""
while line:
    if line.__contains__("inet ") and line.__contains__("vm"):
        ip += line[line.index("inet ")+5:line.index("/")] + "\n"
    line = IPs.readline()
print(ip)

s = socket.socket()
