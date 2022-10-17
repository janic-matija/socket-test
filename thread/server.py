import socket
import threading

SERVER_HOST = "0.0.0.0"  # any
SERVER_PORT = 5001
ADDR = (SERVER_HOST, SERVER_PORT)
UTF = "utf-8"
BUFFER_SIZE = 5
filename = "../recv/text"


def handle_client(conn, addr, thr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the File Server.".encode(UTF))

    with open(filename + str(thr), "wb") as f:
        bytes_read = conn.recv(BUFFER_SIZE)
        if bytes_read:
            f.write(bytes_read)
        f.close()


def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_HOST}:{SERVER_PORT}.")

    thr = 0
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, thr))
        thread.start()
        thr += 1
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    main()
