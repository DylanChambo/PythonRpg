import pygame
from settings.common import *
from settings.settings import *

XOFFSET = WIDTH / 2 - TILESIZE / 2
YOFFSET = HEIGHT / 2 - TILESIZE / 2

class Camera():
    def __init__(self, game, pos):
        self.game = game
        self.pos = pygame.math.Vector2(pos)

    def ajust(self, pos):
        return (pos[0] * TILESIZE + XOFFSET, pos[1] * TILESIZE + YOFFSET)

    def draw(self):
        self.game.screen.fill('black')

        for i in range(-12, 12):
            for j in range(-12, 12):
                if (i % 2 == j % 2):
                    x, y = self.ajust((i, j))
                    pygame.draw.rect(self.game.screen, (0, 255, 0), pygame.Rect( x, y, TILESIZE, TILESIZE))

        self.game.player.draw(self.game.screen, self)

        pygame.display.update()

