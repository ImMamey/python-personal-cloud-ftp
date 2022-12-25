import os
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 4466
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the file server".encode(FORMAT))
def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()

if __name__=="__main__":
    main()
