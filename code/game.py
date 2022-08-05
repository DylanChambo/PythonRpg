import pygame, sys
from settings import *
from level import Level

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
        self.level = Level()
    
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
                
            self.screen.fill('black')
            # Updates the level
            self.level.run()
            # Updates display
            pygame.display.update()
            self.clock.tick(FPS)
