import pygame
from pygame import *
import sys

WIDTH = 600
HEIGHT = 480
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 7, HEIGHT / 7)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
pygame.key.set_repeat(True)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
sprite_block = pygame.sprite.Group()
obstacle = Obstacle()
sprite_obstacle.add(obstacle)

# Game loop
while True:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Moving sprites with arrow keys or WASD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == K_w:
                player.rect.centery -= 5
            elif event.key == pygame.K_DOWN or event.key == K_s:
                player.rect.centery += 5
            elif event.key == pygame.K_LEFT or event.key == K_a:
                player.rect.left -= 5
            elif event.key == pygame.K_RIGHT or event.key == K_d:
                player.rect.right += 5

    # Update
    all_sprites.update()
    sprite_block.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    sprite_block.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()