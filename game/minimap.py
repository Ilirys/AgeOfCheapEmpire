import pygame
from .definitions import * 
from .utils import *

class Minimap:

    def __init__(self, width, height):

            self.width = width
            self.height = height
            self.GreenLight=(75,128,75,200)
            self.Green=(20,100,20,235)
            self.Grey=(128,128,128)
            self.Gold=(200,200,128)
            self.Brown=(70,33, 0)
            self.Red=(175,0,0)
            self.Blue=(0,128,255)

            # minimap hud (Bottom left)
            self.create_minimap_hud()
            self.tab_minimap=self.create_tab_minimap()
            

    def draw(self, screen):

        # minimap hud
        pygame.draw.rect(self.minimap_surface, self.GreenLight, (2, 2, 450, 450))
        for i in range (MAP_SIZE):
            for j in range (MAP_SIZE):
                if self.tab_minimap[i][j] != self.GreenLight:
                    pygame.draw.rect(self.minimap_surface, self.tab_minimap[i][j], (2+9*i, 2+9*j, 9, 9))
                #pygame.draw.rect(self.minimap_surface, self.tab_minimap[i][j], (2+9*i, 2+9*j, 9, 9))
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.minimap_surface, -45), (454, 220)) , (600, self.height-225))   # avant : 500 , *0.21
    
    def create_minimap_hud(self):
        self.minimap_surface = pygame.Surface((454, 454), pygame.SRCALPHA) # avant : *0.32 et *0.21
        self.minimap_rect = self.minimap_surface.get_rect(topleft=(500, self.height * 0.79))
        #self.minimap_surface.fill((0 , 0, 0, 175))
         

    def create_tab_minimap(self):
        tab_minimap = [[self.GreenLight for x in range(MAP_SIZE)] for y in range(MAP_SIZE)]    
        return tab_minimap
        

    def update(self, world):
        for i in range (MAP_SIZE):
            for j in range (MAP_SIZE):
                if world.world[i][j]["tile"].nomElement == "tree":
                    self.tab_minimap[i][j] = self.Green
                elif world.world[i][j]["tile"].nomElement == "stone":
                    self.tab_minimap[i][j] = self.Grey
                elif world.world[i][j]["tile"].nomElement == "gold":
                    self.tab_minimap[i][j] = self.Gold
                elif world.world[i][j]["tile"].nomElement == "food":
                    self.tab_minimap[i][j] = self.Brown
                elif world.world[i][j]["collision"] == True:
                    self.tab_minimap[i][j] = self.Red
                else:
                    self.tab_minimap[i][j] = self.GreenLight

    def cart_to_iso(self, x, y): # Coordonées rectangulaires en isométriques
        iso_x = x - y 
        iso_y = (x + y)/2
        return iso_x, iso_y