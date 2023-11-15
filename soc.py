import socket

def find_available_port():
    # Create a temporary socket
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    temp_socket.bind(('localhost', 0))  # Bind to any available port on localhost
    _, port = temp_socket.getsockname()  # Get the allocated port
    temp_socket.close()  # Close the temporary socket
    return port

# Usage example
port = find_available_port()
if port:
    print(f"Found available port: {port}")
else:
    print("No available port found")
