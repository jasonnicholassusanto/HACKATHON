import pygame

class WallSprite(pygame.sprite.Sprite):
    """ A stationary sprite"""
    def __init__( self, position, image ):
        pygame.sprite.Sprite.__init__( self )
        self.image        = image
        self.rect         = self.image.get_rect()
        self.rect.topleft = position

    def udpate( self ):
        # does not move
        pass

def enviroment():
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

    return background_map

# initate wall in map (put in main??)
# wall_image = pygame.image.load("brick_32.png").convert_alpha()
# wall_sprites = pygame.sprite.Group()   # a group for all the wall sprites
# for i in range(20):
#     # create a wall at a random position
#     new_wall = WallSprite( ( random.randrange( 0, WINDOW_WIDTH ), random.randrange( 0, WINDOW_HEIGHT ) ), wall_image )
#     wall_sprites.add( new_wall )  # put into the sprite group


# collision with wall algorithm
# if ( len( pygame.sprite.spritecollide( player_sprite, wall_sprites, False ) ) > 0 ):
#     player_sprite.stop_moving()

# collision with other player algorithm
# if len( pygame.sprite.spritecollide( self.player , self.other_player, True) ) > 0:
#     player.change_to_rotten()
#     self_other.change_to_rotten()

# collision with other player fire
# if len( pygame.sprite.spritecollide( self.player , fire_sprites, True) ) > 0:
#     self.player.change_to_raw()
#     self.fire.gone()