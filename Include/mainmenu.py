import playerclass
import pygame

player_1 = playerclass.Player()
player_2 = playerclass.Player()

# To create/initialize the screen of the game
pygame.init()

# Setting the screen size (width, height)
width = 1200
height = 640
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Hard boiled eggs")
icon = pygame.image.load('logoimage.png')
pygame.display.set_icon(icon)

player_image = pygame.image.load("player_image.png")
def player(x, y):
    screen.blit(player_image, (x, y))

running = True
while running:
    # Background color (R,G,B) - 0 to 255 intensity
    WHITE = (255, 255, 255)
    screen.fill(WHITE)

    # An event is anything that is happening inside our game window
    # Any kind of input control is also an event such as pressing a key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




