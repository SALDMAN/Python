import pygame
import sys
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Multiplayer Game")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player attributes
player_radius = 30
player1_pos = [screen_width // 4, screen_height // 2]
player2_pos = [3 * screen_width // 4, screen_height // 2]
player1_color = RED
player2_color = BLUE
player_speed = 5

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player1_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player1_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player1_pos[1] += player_speed

    if keys[pygame.K_a]:
        player2_pos[0] -= player_speed
    if keys[pygame.K_d]:
        player2_pos[0] += player_speed
    if keys[pygame.K_w]:
        player2_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player2_pos[1] += player_speed

    # Collision detection
    if (
        abs(player1_pos[0] - player2_pos[0]) < player_radius * 2
        and abs(player1_pos[1] - player2_pos[1]) < player_radius * 2
    ):
        # Collision occurred
        player1_color, player2_color = player2_color, player1_color

    # Clear the screen
    screen.fill(BLACK)

    # Draw players
    pygame.draw.circle(screen, player1_color, player1_pos, player_radius)
    pygame.draw.circle(screen, player2_color, player2_pos, player_radius)

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
