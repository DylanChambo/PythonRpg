import pygame, sys
from settings.settings import Globals
from scripts.player import Player
from scripts.camera import Camera
from scripts.controls import Input

class Game:
    # Code runs when class is initialized. Only runs once 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT), pygame.RESIZABLE)
         # Sets Title of window
        pygame.display.set_caption("Pygame")
        # Sets window Icon
        # pygame.display.set_icon(Icon_name)
        self.clock = pygame.time.Clock()
        # initializes the game.
        self.player = Player(self, (0, 0))
        self.camera = Camera(self)
        self.controls = Input(self)
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

            self.update()
            self.draw()

            self.clock.tick(Globals.FPS)


    def update(self):
        Globals.update()
        self.controls.update()
        self.camera.update()
        self.player.update()

    def draw(self):
        self.camera.draw()