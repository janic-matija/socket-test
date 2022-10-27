import socket
import socketserver
import sys
import os
import paramiko
import time

start_time = time.time()

BUFFER_SIZE = 10737418240
HOST = "10.18.110.76"
SERVER_HOST = "0.0.0.0"  # any
PORT = 9990
# socketserver.TCPServer.request_queue_size = 100
# print(socketserver.TCPServer.request_queue_size)

if sys.argv[0] == '/home/matija/paramiko/fromHost.py':  # prima fajl
    os.system("mkdir -p /home/matija/from_host \n ")

    file_recv = "/home/matija/from_host/big1G"

    recv_file_socket = socket.socket()
    # print(socket.TCP_MAXSEG)
    # recv_file_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_MAXSEG, 400)
    # print(socket.TCP_MAXSEG)
    recv_file_socket.connect((HOST, PORT))

    with open(file_recv, "wb") as fr:
        while True:
            bytes_read = recv_file_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            fr.write(bytes_read)

    recv_file_socket.close()

else:  # salje fajl

    send_file_socket = socket.socket()
    # send_file_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_MAXSEG, 400)

    send_file_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    send_file_socket.bind((SERVER_HOST, PORT))

    send_file_socket.listen(65535)
    print(f"[*] Listening as {SERVER_HOST}:{PORT}")

    with open("IP/pw", 'r') as passFile:
        pw = passFile.readline()
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname='10.18.110.49', port=22, username='root',
                password=pw, timeout=3)

    ftp_client = ssh.open_sftp()
    ftp_client.put('/home/matija/Projects/socket-test/socket-test/toGuest.py', '/home/matija/paramiko/fromHost.py')
    ftp_client.close()
    stdin, stdout, stderr = ssh.exec_command("python3 /home/matija/paramiko/fromHost.py")
    del ftp_client, stdin, stdout, stderr
    client_socket, address = send_file_socket.accept()
    print(f"[+] {address} is connected.")
    filename = "data/big1"
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)
    client_socket.close()
    send_file_socket.close()

    end_time = time.time()
    print(str(end_time - start_time))
