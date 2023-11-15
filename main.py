import socket

# Get the hostname of the local machine
hostname = socket.gethostname()

# Get the IP address of the local machine
ip_address = socket.gethostbyname(hostname)

# Print the IP address
print(f"The IP address of this machine is {ip_address}")
