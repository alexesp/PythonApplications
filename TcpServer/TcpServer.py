from http import client
import socket

#Create a server side socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostname()) #hostname
print(socket.gethostbyname(socket.gethostname()))  #if of the given hostname

#Bind our new socket to a tuple (IP Address, Port Address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 23000))

#Put the socket into listening mode to listen for any possible connections
server_socket.listen()

#Listen forever to accept any connection
while True:
    #Accept every single connection
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)

    print(f"Connected to {client_address}!\n")

    #Send a message to the client
    client_socket.send("You are connected!".encode("utf-8"))

    #Close the connection
    server_socket.close()
    break



