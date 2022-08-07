import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites


   
    def input(self):
        # Input Management
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

        self.rect.x += speed * self.direction.x
        self.collision("horizontal")
        self.rect.y += speed * self.direction.y
        self.collision("vertical")


    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # Moving Right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # Moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # Moving Down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # Moving Up
                        self.rect.top = sprite.rect.bottom

    # Update Method Runs each gameloop
    def update(self):
        self.input()
        self.move(self.speed)