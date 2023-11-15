import pygame
import random
import socket
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Multiplayer Tetris")
# Define Tetris grid dimensions
grid_size = 20
grid_width = width // grid_size
grid_height = height // grid_size

# Define Tetris piece shapes
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    # Add more shapes as desired
]

# Define player positions
player_x = grid_width // 2
player_y = 0

# Generate a random piece for the player
player_piece = random.choice(shapes)

# Handle player controls
def handle_player_controls():
    global player_x, player_y, player_piece
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 1
    if keys[pygame.K_RIGHT]:
        player_x += 1
    if keys[pygame.K_DOWN]:
        player_y += 1
    if keys[pygame.K_SPACE]:
        # Rotate the player piece
        player_piece = list(zip(*player_piece[::-1]))

# Update player position and handle collisions
def update_player():
    global player_x, player_y, player_piece
    player_y += 1
    if player_y + len(player_piece) > grid_height:
        # Player reached the bottom, reset position and generate a new piece
        player_x = grid_width // 2
        player_y = 0
        player_piece = random.choice(shapes)

# Render the player piece and grid
def render():
    screen.fill((0, 0, 0))  # Clear the screen
    # Render player piece
    for y, row in enumerate(player_piece):
        for x, val in enumerate(row):
            if val:
                pygame.draw.rect(screen, (255, 255, 255), (player_x * grid_size + x * grid_size, player_y * grid_size + y * grid_size, grid_size, grid_size))
    # Render grid
    for y in range(grid_height):
        for x in range(grid_width):
            pygame.draw.rect(screen, (128, 128, 128), (x * grid_size, y * grid_size, grid_size, grid_size), 1)
    pygame.display.flip()  # Update the screen
# Set up the game loop
clock = pygame.time.Clock()
running = True

# Set up the game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_player_controls()
    update_player()
    render()

    clock.tick(30)  # Limit the frame rate to 30 FPS

pygame.quit()

