import socket

# Create the server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostbyname(socket.gethostname())
port = 444

# Bind the socket to the host and port
serverSocket.bind((host, port))

# Listen for incoming connections, with a maximum of 3 queued connections
serverSocket.listen(3)

print(f"Server listening on {host}:{port}...")

while True:
    # Accept a connection from a client
    clientSocket, address = serverSocket.accept()
    
    print("Received connection from %s" % str(address))

    # Send a welcome message to the client
    message = "Hello! Thank you for connecting to the server.\r\n"
    clientSocket.send(message.encode('utf-8'))

    # Close the client connection
    clientSocket.close()
