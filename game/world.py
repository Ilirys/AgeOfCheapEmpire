import pygame
import random
import noise
from game.Ressource import Ressource
from .Tile import Tile
from .definitions import *
from .bouquet import Bouquet

class World:

    def __init__(self, hud, grid_length_x, grid_length_y, width, height):
        self.hud = hud
        self.grid_length_x = grid_length_x  #Taille MAP
        self.grid_length_y = grid_length_y
        self.width = width  #Taille écran
        self.height = height
        
        self.Bou = Bouquet() #Génération forets, ressources

        self.grass_tiles = pygame.Surface((grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
        self.tiles = self.load_images()
        self.world = self.create_world()
        self.temp_tile = None

        
    def update(self, camera):
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()

        self.temp_tile = None
        if self.hud.selected_tile is not None:

            grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera.scroll)

            if self.can_place_tile(grid_pos):
                img = self.hud.selected_tile["image"].copy()
                img.set_alpha(100)

                render_pos = self.world[grid_pos[0]][grid_pos[1]]["render_pos"]
                iso_poly = self.world[grid_pos[0]][grid_pos[1]]["iso_poly"]
                collision = self.world[grid_pos[0]][grid_pos[1]]["collision"]

                self.temp_tile = {
                    "image": img,
                    "render_pos": render_pos,
                    "iso_poly": iso_poly,
                    "collision": collision
                }

                if mouse_action[0] and not collision:
                    self.world[grid_pos[0]][grid_pos[1]]["tile"] = self.hud.selected_tile["name"]
                    self.world[grid_pos[0]][grid_pos[1]]["collision"] = True
                    self.hud.selected_tile = None

    def draw(self, screen, camera):
        screen.blit(self.grass_tiles,(camera.scroll.x, camera.scroll.y)) #Au lieu d'iterer pour tout les block de fond, ici herbe, on le fait une fois
        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                render_pos = self.world[x][y]["render_pos"]
                nomElement = self.world[x][y]["tile"].nomElement
                if nomElement != "":
                    screen.blit(self.tiles[nomElement],
                                (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x +40,
                                 render_pos[1] -  (self.tiles[nomElement].get_height() - TILE_SIZE + 30) + camera.scroll.y))
        if self.temp_tile is not None:
            iso_poly = self.temp_tile["iso_poly"]
            iso_poly = [(x + self.grass_tiles.get_width()/2 + camera.scroll.x, y + camera.scroll.y) for x, y in iso_poly]
            if self.temp_tile["collision"]:
                pygame.draw.polygon(screen, (255, 0, 0), iso_poly, 3)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), iso_poly, 3)
            render_pos = self.temp_tile["render_pos"]
            screen.blit(
                self.temp_tile["image"],
                (
                    render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                    render_pos[1] - (self.temp_tile["image"].get_height() - TILE_SIZE) + camera.scroll.y
                )
            )

    def create_world(self): #Génère la map
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
                    world[grid_x][grid_y]["tile"].nomElement = "stone"
                    world[grid_x][grid_y]["tile"].ressource.nbRessource = NB_RESSOURCES[3]
                    world[grid_x][grid_y]["tile"].ressource.typeRessource = "WOOD"  

        return world    


    def grid_to_world(self, grid_x, grid_y):    #Renvoit un dictionnaire avec notamment des coordonnées isométriques pour une vue 2.5D
        rien = Ressource(0,"")
        tile = Tile(grid_x,grid_y,0, rien ,0)
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
            "tile": tile,
            "collision": False if tile.nomElement == "" else True
        }
        return out


    def cart_to_iso(self,x,y): #Coordonées rectangulaires en isométriques
        iso_x = x-y 
        iso_y = (x + y)/2
        return iso_x, iso_y
    
    def mouse_to_grid(self, x, y, scroll):
        # transform to world position (removing camera scroll and offset)
        world_x = x - scroll.x - self.grass_tiles.get_width()/2
        world_y = y - scroll.y
        # transform to cart (inverse of cart_to_iso)
        cart_y = (2*world_y - world_x)/2
        cart_x = cart_y + world_x
        # transform to grid coordinates
        grid_x = int(cart_x // TILE_SIZE)
        grid_y = int(cart_y // TILE_SIZE)
        return grid_x, grid_y

    def générer_townhall(self):
        x=random.random()
        y= random.randint(-4,4)
        z= random.randint(-4,4)
         #if x<0.25:
            #townhall (7+y, 7+z)
         #elif x<0.5:
            #townhall (self.grid_length_x-7+y, 7+z)
         #elif x<0.75:
            #townhall (7+y, self.grid_length_y-7+z)
         #else:
            #townhall (self.grid_length_x-7+y, self.grid_length_y-7+z)
            

    def load_images(self): #Chargement des images, retourne le dictionnaire d'images

        Towncenter = pygame.image.load("assets/Towncenter.png").convert_alpha()
        grass = pygame.image.load("assets/grass.png").convert_alpha()
        tree = pygame.image.load("assets/tree.png").convert_alpha()
        stone = pygame.image.load("assets/stone.png").convert_alpha()
        gold = pygame.image.load("assets/gold.png").convert_alpha()
        fruit = pygame.image.load("assets/fruit.png").convert_alpha()

        images = {
            "Towncenter": Towncenter,
            "grass": grass,
            "tree": tree
        }

        return images

    def can_place_tile(self, grid_pos):
        mouse_on_panel = False
        for rect in [self.hud.resources_rect, self.hud.build_rect]:
            if rect.collidepoint(pygame.mouse.get_pos()):
                mouse_on_panel = True
        world_bounds = (0 <= grid_pos[0] <= self.grid_length_x) and (0 <= grid_pos[1] <= self.grid_length_x)

        if world_bounds and not mouse_on_panel:
            return True
        else:
            return False


        



