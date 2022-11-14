#!/usr/bin/env python3
import subprocess
import sys
import time
import socket
import os

import paramiko

start = time.time()
BUFF = 1_000_000_000
HOST = "192.168.122.17"
SERVER_HOST = ''  # any
PORT = 9999


def ssh_send(hn, p, u, pw):
    if os.path.isfile(pw):
        with open(pw, 'r') as passFile:
            pw = passFile.readline()
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=hn, port=p, username=u,
                password=pw, timeout=3)

    stdin, stdout, stderr = ssh.exec_command("mkdir -p /tempdir")
    this_dir = str(subprocess.check_output(['pwd']))[2:-3] + "/"
    this_file = this_dir + os.path.basename(__file__)
    print(this_file)

    ftp_client = ssh.open_sftp()

    ftp_client.put(this_file, '/tempdir/fromHost.py')
    ftp_client.close()
    stdin, stdout, stderr = ssh.exec_command("python3 /tempdir/fromHost.py")
    print(stdout.readlines())
    del ftp_client, stdin, stdout, stderr


def recv_dir(folder, sock):
    from_client = sock
    os.makedirs(folder, exist_ok=True)
    with from_client, from_client.makefile('rb') as serverfile:
        while True:
            raw = serverfile.readline()
            if not raw:
                break
            filename = raw.strip().decode()
            length = int(serverfile.readline())
            # print(f'Downloading {filename}...\n  Expecting {length:,} bytes...', end='', flush=True)

            path = os.path.join(folder, filename)
            os.makedirs(os.path.dirname(path), exist_ok=True)

            with open(path, 'wb') as f:
                while length:
                    buf = min(length, BUFF)
                    data = serverfile.read(buf)
                    if not data: break
                    f.write(data)
                    length -= len(data)
                else:
                    # print('Complete')
                    continue

            # interrupt
            # print('Incomplete')
    from_client.close()


def send_dir(folder, sock):
    to_server = sock.connect((HOST, PORT))
    while True:
        print(f'Client conected to {HOST}:{PORT}')
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


# def main():
if sys.argv[0] == '/tempdir/fromHost.py':  # server prima fajl

    guest_sock = socket.socket()
    guest_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    guest_sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        BUFF)
    print("connecting")
    guest_sock.connect(('10.18.110.76', PORT))
    print("connected")
    recv_dir('/tempdir/server', guest_sock)
    guest_sock.close()
else:

    host_sock = socket.socket()
    host_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host_sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        BUFF)

    print("binding")
    host_sock.bind(('0.0.0.0', PORT))
    print("listening")
    host_sock.listen(65535)
    ssh_send('192.168.122.17', 22, 'root', "IP/pw")
    print("accepting")
    guest, address = host_sock.accept()
    print("accepted")
    send_dir('data', guest)
    guest.close()
    host_sock.close()

    print(time.time() - start)

# if __name__ == "__main__":
#     main()
