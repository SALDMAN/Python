import pygame
import socket
import pickle

def send_player_position(player_x):
    # Pickle and send the player's position to the server
    client.send(pickle.dumps(player_x))

def receive_server_data():
    # Receive and unpickle the server data containing enemy's position and score
    data = client.recv(1024)
    return pickle.loads(data)

# Set up the client
host = '127.0.0.1'
port = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# ... (Initialize pygame and other game-related setup)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            client.close()

    handle_player_input(player)
    move_enemy(enemy, player, score, screen_height)

    send_player_position(player.x)
    server_data = receive_server_data()

    # Update enemy's position and score
    enemy.x = server_data["enemy_x"]
    score[0] = server_data["score"]

    if check_collision(player_rect(player), enemy_rect(enemy)):
        pygame.quit()
        client.close()

    score_text = display_score(score, font)
    draw_objects(screen, player_rect(player), enemy_rect(enemy), score_text)

    clock.tick(60)
