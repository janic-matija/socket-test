import time
import os

start = time.time()
os.system("rsync -a ~/Projects/socket-test/data root@192.168.122.216:/tempdir")
print(time.time() - start)
