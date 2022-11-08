import time
import socket
import os

start = time.time()
BUFF = 1_000_000

os.makedirs('client', exist_ok=True)

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect(('192.168.122.17', 9000))
with sock, sock.makefile('rb') as clientfile:
    while True:
        raw = clientfile.readline()
        if not raw: break

        filename = raw.strip().decode()
        length = int(clientfile.readline())
        print(f'Downloading {filename}...\n  Expecting {length:,} bytes...', end='', flush=True)

        path = os.path.join('client', filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'wb') as f:
            while length:
                buf = min(length, BUFF)
                data = clientfile.read(buf)
                if not data: break
                f.write(data)
                length -= len(data)
            else:
                print('Complete')
                continue

        # socket closed
        print('Incomplete')
        break
print(time.time() - start)
