from socket import *

serverPort = 12000  # Defining the port number where the server will listen
serverSocket = socket(AF_INET, SOCK_STREAM)  # Creating a TCP server socket
serverSocket.bind(('', serverPort))  # Binding the server socket to the port so it can receive connections
serverSocket.listen(1)  # Listening for incoming client connections (only 1 in this case)

print('The server is ready to receive')  # Server status message

while True:  # Infinite loop to keep the server running and accepting connections
    connectionSocket, addr = serverSocket.accept()  # Accepts an incoming connection request
    sentence = connectionSocket.recv(1024).decode()  # Receives data from the client (max 1024 bytes)
    capitalizedSentence = sentence.upper()  # Converts the received string to uppercase
    connectionSocket.send(capitalizedSentence.encode())  # Sends the modified string back to the client
    connectionSocket.close()  # Closes the connection with the client
