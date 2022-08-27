import pygame
from settings.settings import Keys
class Input:

    def __init__(self, game):

        self.controls = {"UP" : False,
                         "DOWN" :False,
                         "LEFT" :False,
                         "RIGHT" :False}

    def __getitem__(self, key):
        return self.controls[key]

    def update(self):
        keys = pygame.key.get_pressed()
        self.controls["UP"] = keys[Keys.UP]
        self.controls["DOWN"] = keys[Keys.DOWN]
        self.controls["LEFT"] = keys[Keys.LEFT]
        self.controls["RIGHT"] = keys[Keys.RIGHT]

        if keys[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))