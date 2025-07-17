import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Block")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Game clock
clock = pygame.time.Clock()
FPS = 120

# Paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - 40
paddle_speed = 7

# Block properties
BLOCK_SIZE = 30
block_x = random.randint(0, WIDTH - BLOCK_SIZE)
block_y = -BLOCK_SIZE
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    """Utility function to draw text"""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Game loop
running = True
while running:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_speed

    # Move the block
    block_y += block_speed

    # Reset block if caught or missed
    if block_y + BLOCK_SIZE >= paddle_y and paddle_x < block_x + BLOCK_SIZE and paddle_x + PADDLE_WIDTH > block_x:
        score += 1
        block_x = random.randint(0, WIDTH - BLOCK_SIZE)
        block_y = -BLOCK_SIZE
    elif block_y > HEIGHT:
        draw_text("Game Over!", font, RED, SCREEN, WIDTH // 2 - 80, HEIGHT // 2)
        draw_text(f"Final Score: {score}", font, BLACK, SCREEN, WIDTH // 2 - 80, HEIGHT // 2 + 40)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Draw paddle and block
    pygame.draw.rect(SCREEN, BLUE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(SCREEN, RED, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))

    # Draw score
    draw_text(f"Score: {score}", font, BLACK, SCREEN, 10, 10)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

