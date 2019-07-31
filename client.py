

import socket

s = socket.socket()


server_ip = input("Please write the server IP")


port = 8000

s.connect( ( server_ip , port  ))

running = True

while running:
    x = input("enter message: ")
    x_encoded = x.encode()
    s.send(x_encoded)