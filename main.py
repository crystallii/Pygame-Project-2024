# LAVA FALL game
# Crystal Li
# Block B computer programming
# June 4 2024

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Raining Lava")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player size

player_width = 20
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - 100

# Lava size and speed

lava_width = 10
lava_height = 50
lava_speed = 15

# Lava 

lava_list = []
lava_spawn_timer = 0
lava_spawn_interval = 8

# Displaying hearts (used chatgpt)
heart_image = pygame.image.load('images/pixel-heart-2779422_1280.webp')
heart_image = pygame.transform.scale(heart_image, (40, 40))

heart_list = [1, 1, 1, 1, 1]
game_over = False

def display_hearts():
    for i in range(len(heart_list)):
        screen.blit(heart_image, (10 + i * 40, 10))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Event handling (used chatgpt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 7
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += 7

    # Spawn lava (used chatgpt)

    if not game_over:
        lava_spawn_timer += 1
        if lava_spawn_timer == lava_spawn_interval:
            lava_x = random.randint(0, screen_width - lava_width)
            lava_list.append([lava_x, 0])
            lava_spawn_timer = 0

        # Move lava
        for lava in lava_list:
            lava[1] += lava_speed

        # Check collision with player (used chatgpt)
        for lava in lava_list:
            if player_x < lava[0] + lava_width and player_x + player_width > lava[0] and \
                    player_y < lava[1] + lava_height and player_y + player_height > lava[1]:
                if len(heart_list) > 0:
                    heart_list.pop()
                    if len(heart_list) == 0:
                        game_over = True
                lava_list.remove(lava)

        # Remove lava if it goes out of the screen
        for lava in lava_list:
            if lava[1] > screen_height:
                lava_list.remove(lava)

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Draw lava
    for lava in lava_list:
        pygame.draw.rect(screen, RED, (lava[0], lava[1], lava_width, lava_height))

    # Display hearts
    display_hearts()

    # Game over screen
    if game_over:
        font = pygame.font.Font(None, 100)
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - 180, screen_height // 2 - 25))

    # Update display
    pygame.display.flip()

    # Cap the frame rate (used chat-gpt)
    clock.tick(60)

# Quit Pygame
pygame.quit()