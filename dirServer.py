import socket
import os

BUFF = 1_000_000_000

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 1)
# sock.setsockopt(socket.SOL_TCP, socket., b'reno')
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_MAXSEG, 10000)
# print(sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_MAXSEG))
sock.bind(('', 9000))
sock.listen(65535)

while True:
    print('Waiting for a client...')
    client, address = sock.accept()
    print(f'Client joined from {address}')
    with client:
        for path, dirs, files in os.walk('data'):
            for file in files:
                filename = os.path.join(path, file)
                relpath = os.path.relpath(filename, 'data')
                filesize = os.path.getsize(filename)

                print(f'Sending {relpath}')

                with open(filename, 'rb') as f:
                    client.sendall(relpath.encode() + b'\n')
                    client.sendall(str(filesize).encode() + b'\n')

                    while True:
                        data = f.read(BUFF)
                        if not data: break
                        client.sendall(data)
        print('Done.')
        break
sock.close()
