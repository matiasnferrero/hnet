"""Run (on the client side) after the server started listening to connections.
"""
import socket

MY_SOCKET = socket.socket()
SERVER_IP = input("Please write the server IP: ")
PORT = input("Please write the port: ")
MY_SOCKET.connect((SERVER_IP, PORT))

while True:
    MY_SOCKET.send(input("Enter message: ").encode())
