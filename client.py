

import socket

s = socket.socket()

### check in which host is running the client
hostname_client = socket.gethostname()

if hostname_client == "matias-TUF-Gaming-FX705GM-FX705GM":
    hostname_server = "matias-Precision-M6700"

else:
    hostname_server = "matias-TUF-Gaming-FX705GM-FX705GM"


port = 8000

s.connect( ( hostname_server , port  ))

running = True

while running:
    x = input("enter message: ")
    x_encoded = x.encode()
    s.send(x_encoded)