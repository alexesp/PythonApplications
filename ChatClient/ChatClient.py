#Chat Client side

from email import message
import socket

#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 23000
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


#Send/Recieve messages
while True:
    #Recieve information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #Quit if the connected server wants to quit, else keep sending messeges
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat...goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))


#Close the client socket
client_socket.close()