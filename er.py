import pygame
import random

# Initialize pygame
pygame.init()
# Set up the screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the player
player_size = 50
player_x = (screen_width - player_size) / 2
player_y = screen_height - player_size
player_speed = 5

# Set up the enemy
enemy_size = 50
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = 0
enemy_speed = 10

# Set up the score
score = 0
font = pygame.font.Font(None, 30)

# Set up the game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = 0
        score += 1
        enemy_speed += 0.1

    # Check for collision
    if (player_x < enemy_x + enemy_size and player_x + player_size > enemy_x
            and player_y < enemy_y + enemy_size and player_y + player_size > enemy_y):
        game_over = True

    # Draw the screen
    screen.fill(white)
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
