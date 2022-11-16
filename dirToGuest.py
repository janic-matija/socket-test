import time
import socket
import os

start = time.time()
BUFF = 1_000_000_000
HOST = "192.168.122.17"
PORT = 9999


def send_dir(folder, sock):
    to_server = sock
    while True:
        print(f'Host conected to {HOST}:{PORT}')
        with to_server:
            for path, dirs, files in os.walk(folder):
                for file in files:
                    filename = os.path.join(path, file)
                    relpath = os.path.relpath(filename, folder)
                    filesize = os.path.getsize(filename)

                    print(f'Sending {relpath}')

                    with open(filename, 'rb') as f:
                        to_server.sendall(relpath.encode() + b'\n')
                        to_server.sendall(str(filesize).encode() + b'\n')

                        while True:
                            data = f.read(BUFF)
                            if not data:
                                break
                            to_server.sendall(data)
            print('Done.')
            break


client_sock = socket.socket()
client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_SNDBUF,
    BUFF)
print('connecting')
client_sock.connect((HOST, PORT))
print('connected')
send_dir('data', client_sock)
client_sock.close()

print(time.time() - start)
