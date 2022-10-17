import socket
import threading

import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = "10.18.110.76"
port = 5001
filename = "../data/big"


def send_to_server(conn, addr):
    threading.current_thread().ident
    print(f"[+] Connecting to {host}:{port}")
    # conn.connect(addr)
    print("[+] Connected.")

    with open(filename, "rb") as f:
        bytes_read = f.read(BUFFER_SIZE)
        if bytes_read:
            bytes_read
            # conn.sendall(bytes_read)
    f.close()
    conn.close()


def main():
    to_server = socket.socket()
    addr = (host, port)
    while True:
        thread = threading.Thread(target=send_to_server, args=(to_server, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    main()
