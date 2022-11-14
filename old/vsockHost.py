import socket
import sys
import os
import paramiko
import time

start_time = time.time()

BUFFER_SIZE = 8192
# HOST = "10.18.110.49"
CID = socket.VMADDR_CID_ANY
PORT = 9949
# SERVER_HOST = "0.0.0.0"  # any

stdin, stdout, stderr = "", "", ""
print(sys.argv[0])
if sys.argv[0] == "/home/matija/Projects/socket-test/socket-test/vsockHost.py":  # prima fajl
    file_recv = "/home/matija/Projects/socket-test/socket-test/recv/big100M"

    CID_con = socket.VMADDR_CID_ANY
    recv_file_socket = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
    recv_file_socket.connect((CID_con, PORT))

    with open(file_recv, "wb") as fr:
        while True:
            bytes_read = recv_file_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            fr.write(bytes_read)
    recv_file_socket.close()

else:  # salje fajl
    send_file_socket = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
    send_file_socket.bind((CID, PORT))
    print(f"{CID}")
    send_file_socket.listen()

    with open("IP/pw", 'r') as passFile:
        pw = passFile.readline()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='10.18.110.76', port=22, username='root',
                password=pw, timeout=3)
    ftp_client = ssh.open_sftp()
    ftp_client.put('/home/matija/Projects/socket-test/vsock.py', '/home/matija/Projects/socket-test/socket-test'
                                                                 '/vsockHost.py')
    ftp_client.close()
    stdin, stdout, stderr = ssh.exec_command("python3 /home/matija/Projects/socket-test/socket-test/vsockHost.py")
    # print(stdout.readlines())

    # del ftp_client, stdin, stdout, stderr
    (client_socket, (cid, port)) = send_file_socket.accept()
    print(f"[+] {cid} is connected.")
    filename = "data/big5"
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
