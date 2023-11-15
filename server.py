import socket

# Define host and port
HOST = 'localhost'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# Initialize the client count to 0
client_count = 0

# Handle incoming connections
while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()

    # Increment the client count
    client_count += 1

    # Print the number of connected clients
    print(f"Client connected from {client_address}. Total clients: {client_count}")

    # Close the client socket
    client_socket.close()
