from socket import *

serverName = "127.0.0.1"  # The server's IP address (localhost in this case)
serverPort = 12000  # The port on which the server is listening

clientSocket = socket(AF_INET, SOCK_STREAM)  # Creating a TCP client socket
clientSocket.connect((serverName, serverPort))  # Initiating the TCP connection to the server

sentence = input('Input lowercase sentence: ') # Custom message to send to the server
clientSocket.send(sentence.encode()) # Encoding and sending the string to the server

modifiedSentence = clientSocket.recv(1024)  # Receiving the response from the server
print('From Server:', modifiedSentence.decode())  # Decoding and printing the received uppercase string

clientSocket.close()  # Closing the client socket after communication
