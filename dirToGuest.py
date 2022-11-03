import sys
import time
import socket
import os
import paramiko

start = time.time()
BUFF = 1_000_000
HOST = "10.18.110.76"
SERVER_HOST = "0.0.0.0"  # any
PORT = 9990

if sys.argv[0] == '/home/matija/Projekti/socket-test/dirToGuest.py':  # server prima fajl

    os.makedirs('server', exist_ok=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', PORT))
    sock.listen(65535)
    print('Waiting for a client...')
    client, address = sock.accept()
    print(f'Client joined from {address}')
    with client, client.makefile('rb') as serverfile:
        while True:
            raw = serverfile.readline()
            if not raw:
                break
            filename = raw.strip().decode()
            length = int(serverfile.readline())
            print(f'Downloading {filename}...\n  Expecting {length:,} bytes...', end='', flush=True)

            path = os.path.join('server', filename)
            os.makedirs(os.path.dirname(path), exist_ok=True)

            with open(path, 'wb') as f:
                while length:
                    buf = min(length, BUFF)
                    data = serverfile.read(buf)
                    if not data: break
                    f.write(data)
                    length -= len(data)
                else:
                    print('Complete')
                    continue

            # socket was closed early.
            print('Incomplete')
            break
else:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    with open("IP/pw", 'r') as passFile:
        pw = passFile.readline()
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname='10.18.110.49', port=22, username='root',
                password=pw, timeout=3)

    ftp_client = ssh.open_sftp()
    ftp_client.put('/home/matija/Projects/socket-test/socket-test/dirToGuest.py', '/home/matija/Projekti/socket-test'
                                                                                  '/dirToGuest.py')
    ftp_client.close()
    stdin, stdout, stderr = ssh.exec_command("python3 /home/matija/Projekti/socket-test/dirToGuest.py")
    del ftp_client, stdin, stdout, stderr

    server.connect((HOST, PORT))

    while True:
        with server:
            for path, dirs, files in os.walk('data'):
                for file in files:
                    filename = os.path.join(path, file)
                    relpath = os.path.relpath(filename, 'data')
                    filesize = os.path.getsize(filename)

                    print(f'Sending {relpath}')

                    with open(filename, 'rb') as f:
                        server.sendall(relpath.encode() + b'\n')
                        server.sendall(str(filesize).encode() + b'\n')

                        while True:
                            data = f.read(BUFF)
                            if not data:
                                break
                            server.sendall(data)
            print('Done.')
            break
    server.close()

    print(time.time() - start)
