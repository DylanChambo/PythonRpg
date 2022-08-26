import pygame
from debug.debug import hitbox

class Camera():
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
