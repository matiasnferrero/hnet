

import socket
import time

listensocket = socket.socket()

port = 8000

maxConnections = 999

ip = socket.gethostname()

listensocket.bind(  (  '' , port  )  )

listensocket.listen ( maxConnections )

print(' Server started listening at IP {} on port {} '.format(ip,port) )

( clientsocket , adress ) = listensocket.accept()

print('new connection made!')

running = True 


while running:
  message = clientsocket.recv(1024) 
  message_decoded = message.decode()
  print(message)
  print(message_decoded)

  #if message_decoded != '':
   # print('now I sleep 5 seconds before printing your next message')
    #time.sleep(5)



