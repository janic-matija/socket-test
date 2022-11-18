import time
import socket
import os
import subprocess

start = time.time()
BUFF = 1_000_000_000
HOST = "192.168.122.17"
HOST2 = "192.168.100.231"
PORT = 9990


def active_ips():
    addresses = []
    command = 'virsh list --name'
    vms = str(subprocess.check_output(command.split()).decode("utf-8")).splitlines()
    for i in range(0, len(vms) - 1):
        command = 'virsh domifaddr ' + str(vms[i])
        info = (str(subprocess.check_output(command.split()).decode("utf-8"))).splitlines()
        for i in range(2, len(info) - 1):
            addresses.append(info[i].split()[3].split('/')[0])
    return addresses


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


send_to = active_ips()
print(send_to)
for ip in send_to:
    client_sock = socket.socket()
    client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        BUFF)

    client_sock.connect((ip, PORT))
    send_dir('data', client_sock)
    client_sock.close()

print(time.time() - start)
