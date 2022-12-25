import os
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4466
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode("utf-8")
        cmd, msg = data.split("@")

        if cmd == "OK":
            print(f"{msg}")

if __name__ == '__main__':
    main()


