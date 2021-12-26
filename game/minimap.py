import pygame
from .definitions import * 
from .utils import *

class Minimap:

    def __init__(self, width, height):

            self.width = width
            self.height = height

            # minimap hud (Bottom left)
            self.create_minimap_hud()
            self.tab_minimap=self.create_tab_minimap()
            

    def draw(self, screen):
        # minimap hud
        # pygame.draw.rect(self.minimap_surface, GreenLight, (2, 2, 450, 450))
        # for i in range (MAP_SIZE):
        #     for j in range (MAP_SIZE):
        #         if self.tab_minimap[i][j] != GreenLight:
        #             pygame.draw.rect(self.minimap_surface, self.tab_minimap[i][j], (2+9*i, 2+9*j, 9, 9))
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.minimap_surface, -45), (454, 220)) , (600, self.height-222))
    
    def create_minimap_hud(self):
        self.minimap_surface = pygame.Surface((454, 454), pygame.SRCALPHA)
        self.minimap_rect = self.minimap_surface.get_rect(topleft=(500, self.height * 0.79))
        #self.minimap_surface.fill((0 , 0, 0, 175))
         

    def create_tab_minimap(self):
        tab_minimap = [[GreenLight for x in range(MAP_SIZE)] for y in range(MAP_SIZE)]    
        return tab_minimap
        

    # def update(self, world):
    #     for i in range (MAP_SIZE):
    #         for j in range (MAP_SIZE):
    #             if world.world[i][j]["tile"].nomElement == "tree":
    #                 self.tab_minimap[i][j] = Green
    #             elif world.world[i][j]["tile"].nomElement == "stone":
    #                 self.tab_minimap[i][j] = Grey
    #             elif world.world[i][j]["tile"].nomElement == "gold":
    #                 self.tab_minimap[i][j] = Gold
    #             elif world.world[i][j]["tile"].nomElement == "food":
    #                 self.tab_minimap[i][j] = Brown
    #             elif world.world[i][j]["collision"] == True:
    #                 self.tab_minimap[i][j] = Red
    #             else:
    #                 self.tab_minimap[i][j] = GreenLight
