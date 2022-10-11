import os
import socket
os.system("mkdir -p data")
os.system("mkdir -p recv")
os.system("head -c 3G </dev/urandom >data/big")

