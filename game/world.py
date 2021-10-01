import pygame
import random
from .definitions import *

class World:

    def __init__(self,grid_length_x,grid_length_y,width,height): 
        self.grid_length_x = grid_length_x  #Taille MAP
        self.grid_length_y = grid_length_y
        self.width = width  #Taille écran
        self.height = height

        self.grass_tiles = pygame.Surface((width, height))
        self.tiles = self.load_images()
        self.world = self.create_world()
        

    def create_world(self):
        world = []
        for grid_x in range(self.grid_length_x): #On itère pour la taille de la map
            world.append([])                     #On fait une liste avec chaque indice
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x,grid_y)
                world[grid_x].append(world_tile)

                render_pos = world_tile["render_pos"] #Position de rendu pour coller les cases ensembles
                self.grass_tiles.blit(self.tiles["grass"],(render_pos[0] + self.width/2 ,render_pos[1] + self.height/4))
        return world    


    def grid_to_world(self, grid_x, grid_y):    #Renvoit un dictionnaire avec notamment des coordonnées isométriques pour une vue 2.5D
        
        #Matrice avec coordonées carthésiennes
        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)

        ]
        
        iso_poly = [self.cart_to_iso(x,y) for x,y in rect]

        minx = min([x for x,y in iso_poly])
        miny = min([y for x, y in iso_poly])

        r = random.randint(1,100) #Generation aléatoire d'arbres ou autre
        if r <= 20:
            tile = "tree"
        else:
            tile = ""    

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx,miny],
            "tile": tile
        }
        return out

    def cart_to_iso(self,x,y): #Coordonées rectangulaires en isométriques
        iso_x = x-y 
        iso_y = (x + y)/2
        return iso_x, iso_y    


    def load_images(self):
        
        Towncenter = pygame.image.load("assets/Towncenter.png")
        grass = pygame.image.load("assets/grass.png")
        tree = pygame.image.load("assets/tree.png")
        return {"Towncenter": Towncenter, "grass": grass, "tree": tree}
        



