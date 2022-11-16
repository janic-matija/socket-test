import socket
import os

BUFF = 1_000_000_000
SERVER_HOST = "0.0.0.0"  # any
PORT = 9999


def recv_dir(folder, sock):
    from_client = sock
    os.makedirs(folder, exist_ok=True)
    with from_client, from_client.makefile('rb') as serverfile:
        while True:
            raw = serverfile.readline()
            if not raw:
                break
            filename = raw.strip().decode()
            length = int(serverfile.readline())

            path = os.path.join(folder, filename)
            os.makedirs(os.path.dirname(path), exist_ok=True)

            with open(path, 'wb') as f:
                while length:
                    buf = min(length, BUFF)
                    data = serverfile.read(buf)
                    if not data:
                        break
                    f.write(data)
                    length -= len(data)
                else:
                    continue
    from_client.close()

    # def main():


server_sock = socket.socket()
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_RCVBUF,
    BUFF)
server_sock.bind((SERVER_HOST, PORT))

server_sock.listen(65535)
client, address = server_sock.accept()
recv_dir('/tempdir/server', client)

server_sock.close()

# if __name__ == "__main__":
#   main()
