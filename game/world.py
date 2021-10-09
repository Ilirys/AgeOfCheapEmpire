
import pygame
import random
import noise

from game.Ressource import Ressource
from .Tile import Tile
from .definitions import *
from .bouquet import Bouquet

class World:

    def __init__(self,grid_length_x,grid_length_y,width,height): 
        self.grid_length_x = grid_length_x  #Taille MAP
        self.grid_length_y = grid_length_y
        self.width = width  #Taille écran
        self.height = height
        
        self.Bou = Bouquet() #Génération forets, ressources

        self.grass_tiles = pygame.Surface((grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
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
                self.grass_tiles.blit(self.tiles["grass"],(render_pos[0] + (self.grass_tiles.get_width())/2 ,render_pos[1] ))

                if self.Bou.M1[grid_x][grid_y] == "wood": #Checking if our ressource matrice, M1, has set any ressource on the tile 
                    world[grid_x][grid_y]["tile"].nomElement = "tree"
                    world[grid_x][grid_y]["tile"].ressource.nbRessource = NB_RESSOURCES[0]
                    world[grid_x][grid_y]["tile"].ressource.typeRessource = "WOOD"
                
                if self.Bou.M1[grid_x][grid_y] == "gold":
                    world[grid_x][grid_y]["tile"].nomElement = "gold"
                    world[grid_x][grid_y]["tile"].ressource.nbRessource = NB_RESSOURCES[2]
                    world[grid_x][grid_y]["tile"].ressource.typeRessource = "WOOD"

                if self.Bou.M1[grid_x][grid_y] == "fruit":
                    world[grid_x][grid_y]["tile"].nomElement = "food"
                    world[grid_x][grid_y]["tile"].ressource.nbRessource = NB_RESSOURCES[1]
                    world[grid_x][grid_y]["tile"].ressource.typeRessource = "WOOD"

                if self.Bou.M1[grid_x][grid_y] == "stone":
                    world[grid_x][grid_y]["tile"].nomElement = "gold"
                    world[grid_x][grid_y]["tile"].ressource.nbRessource = NB_RESSOURCES[3]
                    world[grid_x][grid_y]["tile"].ressource.typeRessource = "WOOD"  

        return world    


    def grid_to_world(self, grid_x, grid_y):    #Renvoit un dictionnaire avec notamment des coordonnées isométriques pour une vue 2.5D
        rien = Ressource(0,"")
        tile1 = Tile(grid_x,grid_y,0, rien ,0)
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
        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx,miny],
            "tile": tile1
        }
        return out

    def cart_to_iso(self,x,y): #Coordonées rectangulaires en isométriques
        iso_x = x-y 
        iso_y = (x + y)/2
        return iso_x, iso_y    


    def load_images(self):

        Towncenter = pygame.image.load("assets/Towncenter.png").convert_alpha()
        grass = pygame.image.load("assets/grass.png").convert_alpha()
        tree = pygame.image.load("assets/tree.png").convert_alpha()
        rock = pygame.image.load("assets/rock.png").convert_alpha()
        gold = pygame.image.load("assets/gold.png").convert_alpha()
        fruit = pygame.image.load("assets/fruit.png").convert_alpha()
        return {"Towncenter": Towncenter, "grass": grass, "tree": tree, "rock": rock, "gold": gold, "food": fruit}
        



