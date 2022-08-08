import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-32,-26)

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

        self.hitbox.x += speed * self.direction.x
        self.collision("horizontal")
        self.hitbox.y += speed * self.direction.y
        self.collision("vertical")
        self.rect.center = self.hitbox.center


    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Moving Right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Moving Down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Moving Up
                        self.hitbox.top = sprite.hitbox.bottom

    # Update Method Runs each gameloop
    def update(self):
        self.input()
        self.move(self.speed)