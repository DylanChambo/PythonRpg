import pygame
from settings.settings import Globals

class Player():
    def __init__(self, game, pos):
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load('../graphics/player.png').convert_alpha(), ( Globals.TILESIZE, 2 * Globals.TILESIZE))
        self.pos = pos
        self.hitbox = self.image.get_rect()
        self.hitbox.center = pos
        self.direction = pygame.math.Vector2()
        self.speed = 0.1

    def draw(self, camera):
        self.game.screen.blit(self.image, camera.ajust(self.pos))

    def update(self):
        self.image = pygame.transform.scale(pygame.image.load('../graphics/player.png').convert_alpha(), ( Globals.TILESIZE, 2 * Globals.TILESIZE))
        self.move(self.speed)

    def move(self, speed):

        self.direction.x, self.direction.y = (0, 0)

        if self.game.controls.controls["UP"]:
            self.direction.y -= 1
        if self.game.controls.controls["DOWN"]:
            self.direction.y += 1
        if self.game.controls.controls["LEFT"]:
            self.direction.x -= 1
        if self.game.controls.controls["RIGHT"]:
            self.direction.x += 1

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.pos += speed * self.direction
        self.hitbox.center = Globals.TILESIZE * self.pos

        
