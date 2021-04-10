import pygame


SPEED = 0.5
class Player(pygame.sprite.Sprite):
    WIDTH, HEIGHT = 1200, 640

    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # load player image
        self.image = pygame.image.load("player_image.png")
        self.rect = self.image.get_rect()
        x_coor, y_coor = self.rect.topleft # needs correction, should be random


    def motion(self):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If a keystroke is pressed, check whether is right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_coor = -SPEED
                if event.key == pygame.K_d:
                    x_coor = SPEED
                if event.key == pygame.K_w:
                    y_coor = SPEED
                if event.key == pygame.K_s:
                    y_coor = -SPEED

            # To stop the movement of the egg
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_coor = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_coor = 0





