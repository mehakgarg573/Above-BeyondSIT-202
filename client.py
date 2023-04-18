#Mehak, 2110994772
#SIT-202 

import socket

# define host and port
host = '127.0.0.1'
port = 5000

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((host, port))

# send a message to the server
message = 'Hello'
client_socket.send(message.encode('utf-8'))
print(f"Sent message to server: {message}\n")

# receive the response from the server
data = client_socket.recv(1024)
response = data.decode('utf-8')
print(f"Received response from server: {response}\n")

# get the name from the user via the terminal
name = input("Enter your name: ")

# send the name to the server
client_socket.send(name.encode('utf-8'))
print(f"Sent name to server: {name}\n")

# receive the welcome message from the server
data = client_socket.recv(1024)
welcome_message = data.decode('utf-8')
print(f"Received welcome message from server: {welcome_message}\n")

# close the connection
client_socket.close()
