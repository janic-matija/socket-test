import os

# output = os.popen('ip a').readlines()
os.system("mkdir -p ../data")
# os.system("mkdir -p recv")
# os.system("head -c 3G </dev/urandom >data/big")
# os.system("head -c 30G </dev/urandom >../data/big")
# os.system("head -c 12G </dev/urandom >data/big12")
# os.system("head -c 3G </dev/urandom >../data/big3")
os.system("head -c 1G </dev/urandom >../data/big1")
# os.system("head -c 100M </dev/urandom >../data/big5")
# print(output)
