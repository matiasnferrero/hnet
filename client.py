

import socket

s = socket.socket()


server_ip = input("Please write the server IP: ")

port = input("Please write the port: ")


s.connect( ( server_ip , port  ))

running = True

while running:
    x = input("enter message: ")
    x_encoded = x.encode()
    s.send(x_encoded)