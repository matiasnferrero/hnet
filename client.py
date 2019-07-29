

import socket

s = socket.socket()

hostname = "matias-Precision-M6700"

port = 8000

s.connect( ( hostname , port  ))

running = True

while running:
    x = raw_input("enter message: ")
    x_encoded = x.encode()
    s.send(x)