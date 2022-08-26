import pygame
from settings.common import *

class Player():
    def __init__(self, pos):
        self.image = pygame.transform.smoothscale(pygame.image.load('../graphics/player.png').convert_alpha(), ( TILESIZE, 2 * TILESIZE))
        self.rect = self.image.get_rect(left = pos[0], top = pos[1] - TILESIZE,)
        self.direction = pygame.math.Vector2()
        self.speed = 5
