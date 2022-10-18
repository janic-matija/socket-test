import os

output = os.popen('ip a').readlines()
os.system("mkdir -p data")
os.system("mkdir -p recv")
# os.system("head -c 3G </dev/urandom >data/big")
print(output)
