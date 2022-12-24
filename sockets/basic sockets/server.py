import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
#^ conectarse al local  host, puerto 1234
s.listen(5)

while True:
    clientsocket, address = s.accept()
    #^ accept connection
    print(f'Connection from {address} has been establisdhed.')
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))

