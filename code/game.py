import pygame, sys
from settings.settings import *
from settings.common import *
from scripts.player import Player

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
        self.player = Player((0, 0))
        #self.camera = Camera(self.player)
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
        
            self.draw()
            self.clock.tick(FPS)

    def draw(self):

        self.screen.fill('black')

        for i in range(20):
            for j in range(20):
                if (i % 2 == j % 2):
                    pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect( (i*TILESIZE) + WIDTH / 2 , (j*TILESIZE) + HEIGHT / 2, TILESIZE, TILESIZE))

        self.screen.blit(self.player.image, self.player.rect.topleft)
        pygame.display.update()

    def input(self):
        pass