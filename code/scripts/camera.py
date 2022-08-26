import pygame
from settings.settings import Globals

XOFFSET = Globals.WIDTH / 2 - Globals.TILESIZE / 2
YOFFSET = Globals.HEIGHT / 2 - Globals.TILESIZE / 2

class Camera():
    def __init__(self, game, pos):
        self.game = game
        self.pos = pygame.math.Vector2(pos)

    def ajust(self, pos):
        return ((pos[0] - self.pos[0]) * Globals.TILESIZE + XOFFSET, (pos[1] - self.pos[1]) * Globals.TILESIZE + YOFFSET)

    def draw(self):
        self.game.screen.fill('black')

        for i in range(-5, 6):
            for j in range(-5, 6):
                if (i % 2 == j % 2):
                    x, y = self.ajust((i, j))
                    pygame.draw.rect(self.game.screen, (0, 255, 0), pygame.Rect( x, y, Globals.TILESIZE, Globals.TILESIZE))

        self.game.player.draw(self)

        pygame.display.update()

