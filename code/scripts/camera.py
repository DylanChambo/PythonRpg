import pygame
from settings.settings import Globals

class Camera():
    def __init__(self, game):
        self.game = game
        self.pos = self.game.player.pos

    def ajust(self, pos):
        return ((pos[0] - self.pos[0]) * Globals.TILESIZE + Globals.XOFFSET, (pos[1] - self.pos[1]) * Globals.TILESIZE + Globals.YOFFSET)

    def draw(self):
        self.game.screen.fill('black')
        x, y = self.ajust((0, 0))
        pygame.draw.rect(self.game.screen, (0, 255, 0), pygame.Rect( x, y, Globals.TILESIZE, Globals.TILESIZE))

        self.game.player.draw(self)

        pygame.display.update()

    def update(self):
        self.move()

    def move(self):
        self.pos = self.game.player.pos
    