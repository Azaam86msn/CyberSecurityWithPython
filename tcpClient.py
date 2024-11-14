import socket

# Create the client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostbyname(socket.gethostname())
port = 444

# Connect to the server
clientSocket.connect((host, port))

# Receive the message from the server
message = clientSocket.recv(1024)

# Close the client connection
clientSocket.close()

# Print the received message
print(message.decode('utf-8'))
