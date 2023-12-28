import socket
import pickle
import threading
import pygame
import random

# Set up the game variables
screen_width = 500
screen_height = 500

class GameObject:
    def __init__(self, size, x, y, speed):
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed

# Initial enemy position and score
enemy = GameObject(50, random.randint(0, screen_width - 50), 0, 10)
score = [0]

def handle_client(client_socket):
    global player_x

    while True:
        try:
            # Receive player's position from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Unpickle the received data
            player_x = pickle.loads(data)

            # Send enemy's position and score back to the client
            server_data = pickle.dumps({"enemy_x": enemy.x, "score": score[0]})
            client_socket.send(server_data)
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()

# Set up the server
host = '127.0.0.1'
port = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"Server listening on {host}:{port}")

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
