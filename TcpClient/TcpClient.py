from email import message
import socket


#Create a client side
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Cpnnect the socket to a server
client_socket.connect((socket.gethostbyname(socket.gethostname()), 23000))

#Recieve a message from the server...
message = client_socket.recv(1024)
print(message.decode("utf-8"))
print(type(message))



#Close the client socket
client_socket.close()


