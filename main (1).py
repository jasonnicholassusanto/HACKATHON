import pygame

# Static variables
nil = 0

# To create/initialize the screen of the game
pygame.init()

# Setting the screen size (width, height)
width = 1200
height = 640
screen = pygame.display.set_mode((width, height))

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
w      w                  w      w           w          w   ww   w        w
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

# Initializing player coordinates
player_x = 800
player_y = 300
player_x_displacement = nil
player_y_displacement = nil
speed = 0.5


# blit means to draw an image of the player onto the screen
def player(x, y):
    screen.blit(player_image, (x, y))


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

#class Player():
    #def __init__(self, x, y, width, height, color):
        #self.x = x
        #self.y = y
        #self.width = width
        #self.height = height

# Running the game screen, until player chooses to close the window
# Game loop which stops the window from closing down. Closing the window by clicking the exit window
running = True
while running:
    # Background color (R,G,B) - 0 to 255 intensity
    R = G = B = 255
    screen.fill((R, G, B))

    map(background_map)

    # An event is anything that is happening inside our game window
    # Any kind of input control is also an event such as pressing a key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If a keystroke is pressed, check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x_displacement = -speed
            if event.key == pygame.K_d:
                player_x_displacement = speed
            if event.key == pygame.K_w:
                player_y_displacement = speed
            if event.key == pygame.K_s:
                player_y_displacement = -speed

        # To stop the movement of the egg
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_x_displacement = nil
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_y_displacement = nil

    # This is for the changing of the player movement
    player_x += player_x_displacement
    player_y -= player_y_displacement

    # Screen Boundaries excluding the walls
    if player_x <= nil+13:
        player_x = nil+13
    elif player_x >= (width - player_pixel - 13):
        player_x = (width - player_pixel-13)
    elif player_y <= 30:
        player_y = 30
    elif player_y >= (height - player_pixel - 16):
        player_y = (height - player_pixel-16)


    # Wall/obstacles boundaries


    # Calling the player method
    player(player_x, player_y)

    # To update the changes made
    pygame.display.update()
