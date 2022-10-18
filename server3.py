import socket

SERVER_HOST = "0.0.0.0"  # any
SERVER_PORT = 5001
BUFFER_SIZE = 4096
s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = s.accept()
print(f"[+] {address} is connected.")
filename = "big"  # os.path.basename(filename)
filename = "recv/" + filename

with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)

client_socket.close()
s.close()
