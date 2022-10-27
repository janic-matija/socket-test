import socket
import sys
import os
import paramiko
import time

start_time = time.time()

BUFFER_SIZE = 8192
HOST = "10.18.110.49"
PORT = 9999
SERVER_HOST = "0.0.0.0"  # any
SERVER_PORT = 9999

stdin, stdout, stderr = "", "", ""

print(sys.argv[0])
if sys.argv[0] == "/home/matija/Projects/socket-test/socket-test/fromVM.py":  # prima fajl
    print("fromVM u if")

    file_recv = "/home/matija/Projects/socket-test/socket-test/recv/big1G"

    recv_file_socket = socket.socket()
    print("kreiran socket")
    recv_file_socket.connect((HOST, PORT))

    print("konektovano?")

    with open(file_recv, "wb") as fr:
        while True:
            bytes_read = recv_file_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            fr.write(bytes_read)

    recv_file_socket.close()

else:  # salje fajl

    send_file_socket = socket.socket()

    send_file_socket.bind((SERVER_HOST, SERVER_PORT))

    send_file_socket.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    with open("IP/pw", 'r') as passFile:
        pw = passFile.readline()
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname='10.18.110.76', port=22, username='root',
                password=pw, timeout=3)

    ftp_client = ssh.open_sftp()
    ftp_client.put('/home/matija/Projects/socket-test/toHost.py', '/home/matija/Projects/socket-test/socket-test'
                                                                  '/fromVM.py')
    ftp_client.close()
    print("poslato")
    stdin, stdout, stderr = ssh.exec_command("python3 /home/matija/Projects/socket-test/socket-test/fromVM.py")
    del ftp_client, stdin, stdout, stderr
    # print(stdout.readlines())
    # print("izvrseno")

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
