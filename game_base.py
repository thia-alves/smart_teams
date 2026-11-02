
import pygame
import random
import math

# Initialise Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WASD Circle Movement")

# Colours (RGB)
GREEN = (0, 180, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Circle settings
x = WIDTH // 2
y = HEIGHT // 2
radius = 25
speed = 5

#making enimies
#settings
enemy_radius = 20
enemy_speed = 2

#3 enemies
enemies = []

for i in range(3):
    enemy_x = random.randint(20, WIDTH - 20)
    enemy_y = random.randint(20, HEIGHT - 20)

    enemies.append([enemy_x, enemy_y])


# Game clock
clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= speed  # Move up
    if keys[pygame.K_s]:
        y += speed  # Move down
    if keys[pygame.K_a]:
        x -= speed  # Move left
    if keys[pygame.K_d]:
        x += speed  # Move right

    # Keep the circle inside the window
    x = max(radius, min(WIDTH - radius, x))
    y = max(radius, min(HEIGHT - radius, y))

    # Draw the background
    screen.fill(GREEN)

    # Draw the circle
    pygame.draw.circle(screen, RED, (x, y), radius)

    #Enemy moving and stuff
    for enemy in enemies:
        dx = x - enemy[0]
        dy = y - enemy[1]
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:
            enemy[0] += (dx / distance) * enemy_speed
            enemy[1] += (dy / distance) * enemy_speed

        #circle for enimes
        pygame.draw.circle(
            screen,
            BLUE,
            (int(enemy[0]), int(enemy[1])),
            enemy_radius
        )
        #attacking
        if distance < radius + enemy_radius:
            print("GAME OVER!")
            running = False

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
