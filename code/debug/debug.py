import pygame
pygame.init()
font = pygame.font.Font(None, 30)

# Debug: Displays the inputed info on the top left corner of the screen
def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface,'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

def hitbox(display_surface, sprite, offset):
    # Display the hitboxs of all sprites with collisions
    hitbox = sprite.hitbox.copy()
    hitbox.center -= offset
    pygame.draw.rect(display_surface, (255, 0, 0), hitbox, 2)