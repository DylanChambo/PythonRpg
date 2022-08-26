import pygame, sys
from settings.settings import *
from settings.common import *
from scripts.player import Player
from scripts.camera import Camera

class Game:
    # Code runs when class is initialized. Only runs once 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
         # Sets Title of window
        pygame.display.set_caption("Pygame")
        # Sets window Icon
        # pygame.display.set_icon(Icon_name)
        self.clock = pygame.time.Clock()
        # initializes the game.
        self.player = Player(self, (0, 0))
        self.camera = Camera(self, (0, 0))
        # self.input = Input(self)
        # self.level = Level()
    
    # Run loop
    def run(self):
        # Loops till game exits
        while True:
            # Checks for events
            for event in pygame.event.get():
                # Checks for quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.camera.draw()
            self.clock.tick(FPS)

        

    def input(self):
        pass