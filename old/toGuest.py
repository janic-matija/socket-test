import socket
import socketserver
import sys
import os
import paramiko
import time

start_time = time.time()

BUFFER_SIZE = 1000000000
HOST = "10.18.110.76"
SERVER_HOST = "0.0.0.0"  # any
PORT = 9990

if sys.argv[0] == '/home/matija/paramiko/fromHost.py':  # prima fajl
    os.system("mkdir -p /home/matija/from_host \n ")

    file_recv = "/home/matija/from_host/big100"

    recv_file_socket = socket.socket()
    recv_file_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    recv_file_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    recv_file_socket.connect((HOST, PORT))

    with open(file_recv, "wb") as fr:
        # bytes_read = recv_file_socket.recv(BUFFER_SIZE)
        # fr.write(bytes_read)
        while True:
            # fr.write(recv_file_socket.recv(BUFFER_SIZE))
            bytes_read = recv_file_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            fr.write(bytes_read)
        # recv_file_socket.recv_into(fr)

    recv_file_socket.close()

else:  # salje fajl

    send_file_socket = socket.socket()

    send_file_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # send_file_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    send_file_socket.bind((SERVER_HOST, PORT))

    send_file_socket.listen(65535)
    print(f"[*] Listening as {SERVER_HOST}:{PORT}")
    print(f"listening {time.time()-start_time}")
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
    print(f"ssh finished {time.time() - start_time}")
    client_socket, address = send_file_socket.accept()
    # client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    print(f"[+] {address} is connected.")
    filename = "data/bigM"
    brojac = 0
    with open(filename, "rb") as f:
        client_socket.sendfile(f, 0)
        # while True:
        #     bytes_read = f.read(BUFFER_SIZE)
        #     if not bytes_read:
        #         break
        #     client_socket.sendall(bytes_read)
        #     if brojac == 0:
        #         print(f"first loop {time.time() - start_time}")
        #         brojac = 1
    client_socket.close()
    send_file_socket.close()

    end_time = time.time()
    print(str(end_time - start_time))
