import imp


import pygame
# Game Settings

class Globals(object):
    FPS = 60
    WIDTH = 1280
    HEIGHT = 720
    TILESIZE = WIDTH // 20
    XOFFSET = WIDTH / 2 - TILESIZE / 2
    YOFFSET = HEIGHT / 2 - TILESIZE / 2

    
    @classmethod
    def update(cls):
        cls.WIDTH, cls.HEIGHT = pygame.display.get_window_size()
        if 16 * cls.WIDTH > 9 * cls.HEIGHT:
            pass
        else:
            pass
        cls.TILESIZE = cls.WIDTH // 20
        cls.XOFFSET = cls.WIDTH / 2 - cls.TILESIZE / 2
        cls.YOFFSET = cls.HEIGHT / 2 - cls.TILESIZE / 2

class Keys():
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d