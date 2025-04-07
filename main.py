import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Obstacles")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Load images
bg_image = pygame.image.load("bg.png").convert()
fl_image = pygame.image.load("fl.png").convert_alpha()
enemy_image = pygame.image.load("en.png").convert_alpha()

# Get dimensions of images
fl_width, fl_height = fl_image.get_size()
enemy_width, enemy_height = enemy_image.get_size()

# Player parameters
fl_x, fl_y = 400, 300
fl_speed = 5
fl_angle = 0

# Enemy parameters
enemies = [
    {"x": 200, "y": 200, "direction": (0, 0), "speed": 3},
    {"x": 600, "y": 400, "direction": (0, 0), "speed": 4},
    {"x": 300, "y": 500, "direction": (0, 0), "speed": 3},
]

def get_rotated_image(angle: int) -> pygame.Surface:
    """Returns the rotated image of the car by the specified angle."""
    return pygame.transform.rotate(fl_image, angle)

def random_direction() -> tuple:
    """Returns a random direction for the enemy."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    return random.choice(directions)

# Main game loop
running = True
while running:
    # Draw background
    screen.blit(bg_image, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        fl_y -= fl_speed * 0.707
        fl_x -= fl_speed * 0.707
        fl_angle = -135
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        fl_y -= fl_speed * 0.707
        fl_x += fl_speed * 0.707
        fl_angle = 135
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        fl_y += fl_speed * 0.707
        fl_x -= fl_speed * 0.707
        fl_angle = -45
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        fl_y += fl_speed * 0.707
        fl_x += fl_speed * 0.707
        fl_angle = 45
    elif keys[pygame.K_UP]:
        fl_y -= fl_speed
        fl_angle = 180
    elif keys[pygame.K_DOWN]:
        fl_y += fl_speed
        fl_angle = 0
    elif keys[pygame.K_LEFT]:
        fl_x -= fl_speed
        fl_angle = -90
    elif keys[pygame.K_RIGHT]:
        fl_x += fl_speed
        fl_angle = 90

    # Prevent player from going out of bounds
    fl_x = max(0, min(fl_x, WIDTH))
    fl_y = max(0, min(fl_y, HEIGHT))

    # Update enemy movements
    for enemy in enemies:
        enemy["x"] += enemy["direction"][0] * enemy["speed"]
        enemy["y"] += enemy["direction"][1] * enemy["speed"]

        # Reverse direction when hitting boundaries
        if enemy["x"] < 0 or enemy["x"] > WIDTH - enemy_width:
            enemy["direction"] = (-enemy["direction"][0], enemy["direction"][1])
        if enemy["y"] < 0 or enemy["y"] > HEIGHT - enemy_height:
            enemy["direction"] = (enemy["direction"][0], -enemy["direction"][1])

        # Randomly change enemy direction
        if random.randint(0, 60) == 0:
            enemy["direction"] = random_direction()

    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy_image, (enemy["x"], enemy["y"]))

    # Draw the player (car)
    rotated_fl = get_rotated_image(fl_angle)
    rotated_rect = rotated_fl.get_rect(center=(fl_x, fl_y))
    screen.blit(rotated_fl, rotated_rect.topleft)

    # Collision detection
    fl_rect = rotated_fl.get_rect(center=(fl_x, fl_y))
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy["x"], enemy["y"], enemy_width, enemy_height)
        if fl_rect.colliderect(enemy_rect):
            print("Collision! Game Over.")
            running = False

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
