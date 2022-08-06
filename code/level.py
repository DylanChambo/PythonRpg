from lib2to3.pgen2.token import NEWLINE
import pygame
from settings import *
from player import Player
from tile import Tile
from debug import debug

class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obsticle_sprites = pygame.sprite.Group()
        # creates map:
        self.create_map()

    def create_map(self):
        # Generates the map from the array.
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                # x and y are the ajusted coordinate to pixel szie
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x,y), [self.visible_sprites, self.obsticle_sprites])
                elif col == "p":
                    self.player = Player((x,y), [self.visible_sprites])
                

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)