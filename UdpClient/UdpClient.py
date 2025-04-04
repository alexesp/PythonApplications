#UDP Clent Side
import socket


#Creat a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send som information via a connectionless protocol
client_socket.sendto("Hello server world!!!".encode("utf-8"), (socket.gethostbyname(socket.gethostname()), 23000))
