import socket

# Define the server's IP address and port
server_ip = '10.0.0.11'  # Replace with the server's IP address
server_port = 8080  # Replace with the server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Send data to the server
message = 'Hello, server!'
client_socket.sendall(message.encode())

# Receive data from the server
data = client_socket.recv(1024).decode()
print('Received from server:', data)

# Close the socket
client_socket.close()
