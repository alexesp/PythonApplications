#Chat Server side
from email import message
import socket

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 23000
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(HOST_IP, HOST_IP)
server_socket.listen()

#Accept any incoming connection and let ht em know they are connected
print("Server is running...\n")
client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to the server..\n".encode(ENCODER))

#Send/recieve messages
while True:
    #Recieve information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
