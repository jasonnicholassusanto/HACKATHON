import pygame
import random

# Static variables
NIL = 0
FPS = 80
BLUE = (0, 0, 108)

# To create/initialize the screen of the game
pygame.init()
clock = pygame.time.Clock()

# Setting the screen size (width, height)
width = 1200
height = 640
screen = pygame.display.set_mode((width, height))

bg = pygame.image.load('background.png')

def welcome():
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    font = pygame.font.SysFont(None, 64, True)
    img = font.render('Welcome to Hard Boiled Eggs: The Game!', True, BLUE)
    screen.blit(img, (70, 350))
    font1 = pygame.font.SysFont(None, 30, True)
    img1 = font1.render('TO START: PRESS THE SPACE BAR', True, BLUE)
    screen.blit(img1, (400, 500))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

# Initializing map
background_map ="""
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
ww                 www w    ww     w                                     ww
ww                  w  w                                                 ww
wwwww    wwwwwww    w  w                      w      w   www  wwwwwww    ww
wwwww    w     w       wwwwwww     w          w      w   www  w     w    ww
ww       w             w     w     w      wwwww      wwwwwww  w     w    ww
ww       w             w     w     w      wwww       w     w  w           w    
w        w     w       w     ww   ww      www        w     w  w           w    
w        w    ww   w   w     ww           ww         w              wwwwwww    
ww       w   www   w   w     w           ww          ww             w     w  
wwwww    w   www   w   w              wwww     w      www    ww     w     w   
wwwwww       www       w           wwwwww    wwwww     ww    ww           w    
wwwwwww      www       w     w    wwwwww     w   w      w                 w 
wwwwwwww     wwwwwwwwwww     w   ww  ww     ww   ww     w           wwwwwww
w      w     w    w    w     w   ww  ww     ww   ww     w    ww     w     w   
w      w     w    w    w     w              w     w          ww     w     w
w                 w          w                               ww           w
w                 w          w                               ww           w
www  wwwwwwwww    w    wwwwwww                               ww           w
ww    ww     w    w    w         wwwwwwwwwwwwwwwwwwwwwwww    wwwwwwww     w
ww    ww     w    w    w         w                      w           w     w  
w      w                         w                      w           w     w
w      w                         w                      w           w     w
w      w                                                                  w
w                 w                                                       w
w                 w                          w                            w
w                 w                          w                            w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           w          wwwwwwwwwwww  wwwww
w      w                  w      w           w          w    w   w        w
w      w                  w      w          www        ww    w   w        w
w      w        www       w      w          wwww      www    w   w        w
w              wwwww      w                 wwwww    wwww                 w
w               www       w                 wwww      www                 w
w                w        w      w          www        ww        w        w
w      wwwwww         wwwww      wwwww      ww     w    w        w        w      
w                      wwwww   www   wwwwwwww      w             www    www 
w                                                                        ww
w                                                                         w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

"""



walls = background_map
background_map = background_map.splitlines()

# Setting the game's title and icon
pygame.display.set_caption("Hard boiled eggs")
icon = pygame.image.load('logoimage.png')
pygame.display.set_icon(icon)

# Loading player image (the egg image)
player_image = pygame.image.load('player_image.png')
player_pixel = 32

player2_image = pygame.image.load('player_image.png')
player2_pixel = 32

# Initializing player coordinates
player_x = 18
player_y = 624
player2_x = 500
player2_y = 1100
player_x_displacement = NIL
player2_x_displacement = NIL
player_y_displacement = NIL
player2_y_displacement = NIL
SPEED = 1

gameover = pygame.image.load('cracked_egg.png')

# blit means to draw an image of the player onto the screen
def player(x, y):
    screen.blit(player_image, (x, y))

def player2(x, y):
    screen.blit(player2_image, (x, y))

def gameOver(x, y):
    screen.blit(gameover, (x, y))

# Initializing the display of the walls
tile = pygame.image.load("wall.png")

# Initializing the game screen
def init_display():
    global screen, tile
    screen = pygame.display.set_mode((1200, 640))


# Creating the background map for the eggs to run around
def map(background_map):
    global tile
    for y, line in enumerate(background_map):
        for x, c in enumerate(line):
            if c == "w":
                screen.blit(tile, (x * 16, y * 16))


def show_go_screen():
    font = pygame.font.SysFont(None, 64, True)
    img = font.render('Game Over!', True, (204,204,0))
    screen.blit(img, (450, 350))
    gameOver(536, 200)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYDOWN:
                waiting = False


# Running the game screen, until player chooses to close the window
# Game loop which stops the window from closing down. Closing the window by clicking the exit window
game_over = False
welcome_page = True
running = True

#font = pygame.font.SysFont(None, 64, True)
#img = font.render('Welcome to Hard Boiled Eggs: The Game!', True, (204, 204, 0))
#screen.blit(img, (450, 350))

while running:
    if welcome_page:
        welcome()
        welcome_page = False

    WHITE = (255, 255, 255)
    screen.fill(WHITE)

    map(background_map)

    if game_over:
        show_go_screen()
        game_over = False
        player_x = 18
        player_y = 624
        player2_x = 500
        player2_y = 500
        player_x_displacement = NIL
        player2_x_displacement = NIL
        player_y_displacement = NIL
        player2_y_displacement = NIL
        if welcome_page:
            welcome()
            welcome_page = False
            player_x = 18
            player_y = 624
            player2_x = 500
            player2_y = 500
            player_x_displacement = NIL
            player2_x_displacement = NIL
            player_y_displacement = NIL
            player2_y_displacement = NIL


    # An event is anything that is happening inside our game window
    # Any kind of input control is also an event such as pressing a key
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If a keystroke is pressed, check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x_displacement = -SPEED
            if event.key == pygame.K_d:
                player_x_displacement = SPEED
            if event.key == pygame.K_w:
                player_y_displacement = SPEED
            if event.key == pygame.K_s:
                player_y_displacement = -SPEED

        # To stop the movement of the egg
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_x_displacement = NIL
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_y_displacement = NIL

    # This is for the changing of the player movement
    player_x += player_x_displacement
    player_y -= player_y_displacement

    # Screen Boundaries excluding the walls
    if player_x <= 13:
        player_x = 13
    elif player_x >= (width - player_pixel - 13):
        player_x = (width - player_pixel-13)
    elif player_y <= 30:
        player_y = 30
    elif player_y >= (height - player_pixel - 16):
        player_y = (height - player_pixel-16)


        # If a keystroke is pressed, check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2_x_displacement = -SPEED
            if event.key == pygame.K_RIGHT:
                player2_x_displacement = SPEED
            if event.key == pygame.K_UP:
                player2_y_displacement = SPEED
            if event.key == pygame.K_DOWN:
                player2_y_displacement = -SPEED

        # To stop the movement of the egg
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2_x_displacement = NIL
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_y_displacement = NIL

    # This is for the changing of the player movement
    player2_x += player2_x_displacement
    player2_y -= player2_y_displacement

    # Screen Boundaries excluding the walls
    if player2_x <= 13:
        player2_x = 13
    elif player2_x >= (width - player2_pixel - 13):
        player2_x = (width - player2_pixel-13)
    elif player2_y <= 30:
        player2_y = 30
    elif player2_y >= (height - player2_pixel - 16):
        player2_y = (height - player2_pixel-16)

    if player_x == player2_x:
        game_over = True


    # Calling the player method
    player(player_x, player_y)
    player2(player2_x, player2_y)

    # To update the changes made
    pygame.display.update()
