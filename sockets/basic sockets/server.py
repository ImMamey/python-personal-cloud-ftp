import socket
import pickle




HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
#^ conectarse al local  host, puerto 1234
s.listen(5)

while True:
    clientsocket, address = s.accept()
    #^ accept connection
    print(f'Connection from {address} has been establisdhed.')

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(bytes(msg))

