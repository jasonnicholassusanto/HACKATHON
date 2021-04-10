import socket
from _thread import *
import sys

server = "192.168.0.104"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind our server and port to the socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Opens the port
MAXIMUM_PLAYERS = 10
s.listen(MAXIMUM_PLAYERS)

print("Waiting for a connection, Server Started")

def threaded_client(connection):
    connection.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            connection.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    connection.close()

# Continuously look for connections
while True:
    connection, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (connection, ))

