import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    # Input Management
    def input(self):
        keys = pygame.key.get_pressed()

        # Y direction movement
        self.direction.y = 0
        if keys[pygame.K_UP]:
            self.direction.y -= 1
        if keys[pygame.K_DOWN]:
            self.direction.y += 1
            
        # X direction movement
        self.direction.x = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x += 1
        if keys[pygame.K_LEFT]:
            self.direction.x -= 1
    
    def move(self, speed):
        # Normalises the Vector so you dont go 1.41x Faster when moving diagonally.
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += speed * self.direction

    # Update Method Runs each gameloop
    def update(self):
        self.input()
        self.move(self.speed)