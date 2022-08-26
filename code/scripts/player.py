import pygame
from settings.common import *

class Player():
    def __init__(self, game, pos):
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load('../graphics/player.png').convert_alpha(), ( TILESIZE, 2 * TILESIZE))
        self.pos = pos
        self.hitbox = self.image.get_rect(center = (pos[0], pos[1] - 1))
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def draw(self, screen, camera):
        screen.blit(self.image, camera.ajust(self.hitbox.center))