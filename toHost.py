import socket
import sys
import os
import paramiko
import time

start_time = time.time()

BUFFER_SIZE = 1073741824
HOST = "10.18.110.49"
PORT = 9996
SERVER_HOST = "0.0.0.0"  # any
SERVER_PORT = 9996

stdin, stdout, stderr = "", "", ""

print(sys.argv[0])
if sys.argv[0] == "/home/matija/Projects/socket-test/socket-test/fromVM.py":  # prima fajl
    print("fromVM u if")

    file_recv = "/home/matija/Projects/socket-test/socket-test/recv/big100MB2"

    recv_file_socket = socket.socket()
    recv_file_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
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
    print(f"listening {time.time()-start_time}")
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
    print(f"ssh finished {time.time()-start_time}")
    # print(stdout.readlines())
    # print("izvrseno")

    client_socket, address = send_file_socket.accept()
    print(f"[+] {address} is connected.")
    filename = "data/big3"
    brojac = 0
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)
            if brojac == 0:
                print(time.time()-start_time)
                brojac = 1
    client_socket.close()
    send_file_socket.close()

    end_time = time.time()
    print(str(end_time - start_time))
