import pygame

FPS = 60

class Player():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player_image.png")

    def move(self):
        speed = 0.5
        if main.event.type == pygame.KEYDOWN:
            if main.event.key == pygame.K_a:
                player_x_displacement = -speed
            if main.event.key == pygame.K_d:
                player_x_displacement = speed
            if main.event.key == pygame.K_w:
                player_y_displacement = speed
            if main.event.key == pygame.K_s:
                player_y_displacement = -speed

        # To stop the movement of the egg
        if main.event.type == pygame.KEYUP:
            if main.event.key == pygame.K_a or event.key == pygame.K_d:
                player_x_displacement = NIL
            if main.event.key == pygame.K_w or event.key == pygame.K_s:
                player_y_displacement = NIL

        # This is for the changing of the player movement

    player_x += player_x_displacement
    player_y -= player_y_displacement

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        WHITE = (255, 255, 255)
        screen.fill(WHITE)

        map(background_map)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


