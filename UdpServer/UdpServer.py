
#UDP Server side

import socket

#Create a server sid socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bindo our new socket to a tuple (Ip address, port address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 23000))

#We are not listening or accepting connections since UDP is a conectionless protocol

message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)