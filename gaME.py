import pygame
import random

def initialize():
    pygame.init()
    return pygame.display.set_mode((500, 500)), pygame.font.Font(None, 30)

def draw_objects(screen, player, enemy, score_text):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (0, 0, 0), player)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

def handle_player_input(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player.size:
        player.x += player.speed

def move_enemy(enemy, player, score, screen_height):
    enemy.y += enemy.speed
    if enemy.y > screen_height:
        enemy.x = random.randint(0, screen_width - enemy.size)
        enemy.y = 0
        score[0] += 1
        enemy.speed += 0.1

def check_collision(player, enemy):
    return player.colliderect(enemy)

def display_score(score, font):
    return font.render("Score: " + str(score[0]), True, (0, 0, 0))

def main():
    global screen_width
    screen, font = initialize()

    screen_width = 500
    screen_height = 500

    class GameObject:
        def __init__(self, size, x, y, speed):
            self.size = size
            self.x = x
            self.y = y
            self.speed = speed

    player = GameObject(50, (screen_width - 50) / 2, screen_height - 50, 5)
    enemy = GameObject(50, random.randint(0, screen_width - 50), 0, 10)

    score = [0]
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        handle_player_input(player)
        move_enemy(enemy, player, score, screen_height)

        if check_collision(player_rect(player), enemy_rect(enemy)):
            pygame.quit()
            return

        score_text = display_score(score, font)
        draw_objects(screen, player_rect(player), enemy_rect(enemy), score_text)

        clock.tick(60)

def player_rect(player):
    return pygame.Rect(player.x, player.y, player.size, player.size)

def enemy_rect(enemy):
    return pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)

if __name__ == "__main__":
    main()


