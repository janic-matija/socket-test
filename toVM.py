import socket
import socketserver
import sys
import os
import paramiko
import time

start_time = time.time()

BUFFER_SIZE = 1000000000000
HOST = "10.18.110.49"
SERVER_HOST = "0.0.0.0"  # any
PORT = 9999

if sys.argv[0] == '/home/matija/paramiko/toVM.py':  # prima fajl
    os.system("mkdir -p /home/matija/from_host \n ")

    file_recv = "/home/matija/from_host/big100"

    recv_file_socket = socket.socket()
    recv_file_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    recv_file_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    recv_file_socket.bind((SERVER_HOST, PORT))

    recv_file_socket.listen(65535)

    client_socket, address = recv_file_socket.accept()
    # client_socket.setblocking(0)
    with open(file_recv, "wb") as fr:
        # bytes_read = recv_file_socket.recv(BUFFER_SIZE)
        # fr.write(bytes_read)
        while True:
            # fr.write(recv_file_socket.recv(BUFFER_SIZE))
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            fr.write(bytes_read)
        # recv_file_socket.recv_into(fr)
    client_socket.close()
    recv_file_socket.close()

else:  # salje fajl

    with open("IP/pw", 'r') as passFile:
        pw = passFile.readline()
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname='10.18.110.49', port=22, username='root',
                password=pw, timeout=3)

    ftp_client = ssh.open_sftp()
    ftp_client.put('/home/matija/Projects/socket-test/socket-test/toVM.py', '/home/matija/paramiko/toVM.py')
    ftp_client.close()
    stdin, stdout, stderr = ssh.exec_command("python3 /home/matija/paramiko/toVM.py")
    del ftp_client, stdin, stdout, stderr
    print(f"ssh finished {time.time() - start_time}")

    send_file_socket = socket.socket()

    send_file_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # send_file_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    send_file_socket.connect((HOST, PORT))

    filename = "data/bigM"
    with open(filename, "rb") as f:
        send_file_socket.sendfile(f, 0)

    send_file_socket.close()

    end_time = time.time()
    print(str(end_time - start_time))
