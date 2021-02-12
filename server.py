
""" Opens a socket and starts listening to connections from clients
"""
import socket

PORT = 8000
MAX_CONNECTIONS = 999
IP = socket.gethostname()

SERVER_SOCKET = socket.socket()
SERVER_SOCKET.bind(('', PORT))
SERVER_SOCKET.listen(MAX_CONNECTIONS)
print('Server started listening at IP {} on port {} '.format(IP, PORT))

(CLIENT_SOCKET, ADDRESS) = SERVER_SOCKET.accept()
print('New connection made!')

while True:
    MESSAGE = CLIENT_SOCKET.recv(1024).decode()
    print(MESSAGE)
