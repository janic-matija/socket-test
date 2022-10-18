import socket
import threading

SERVER_HOST = "10.18.110.76"
SERVER_PORT = 5001
ADDR = (SERVER_HOST, SERVER_PORT)
UTF = "utf-8"
BUFFER_SIZE = 4096
filename = "../data/big"


def main():
    to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[+] Connecting to {SERVER_HOST}:{SERVER_PORT}")
    to_server.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")

    thr = 0
    while True:
        thread = threading.Thread(target=send_to_server, args=(to_server, ADDR, thr))
        thread.start()
        thr += 1


def send_to_server(conn, addr, thr):
    print(thr*BUFFER_SIZE)
    # with open(filename, "rb") as f:
    #     f.seek(thr*BUFFER_SIZE)
    #     bytes_read = f.read(BUFFER_SIZE)
    #     if bytes_read:
    #         conn.sendall(bytes_read)
    # conn.close()


if __name__ == "__main__":
    main()


# Klijent nije dobro realizovan

