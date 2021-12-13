import pygame
import random
import noise
from DTO.batimentDTO import BarrackDTO, HouseDTO, TowncenterDTO
from game.horseman import Horseman
from game.soldier import Soldier
from game.workers import Worker
from game.villager import Villager
from game.archer import Archer
from .utils import *
from DTO.worldDTO import WorldDTO
from game.Ressource import Ressource
from .Tile import Tile
from .definitions import *
from .bouquet import Bouquet
from .batiment import *
from .animation import Animation
import pickle

class World:

    def __init__(self, resource_manager, entities, hud, grid_length_x, grid_length_y, width, height, camera):
        self.resource_manager = resource_manager
        self.entities = entities
        self.hud = hud
        self.grid_length_x = grid_length_x  #Taille MAP
        self.grid_length_y = grid_length_y
        self.width = width  #Taille écran
        self.height = height
        self.camera = camera
        
        self.Bou = Bouquet() #Génération forets, ressources

        self.grass_tiles = pygame.Surface((grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
        self.tiles = self.load_images()
        self.world = self.create_world()
        self.collision_matrix = self.create_collision_matrix()

        self.animation = Animation()
        
        #Units and their corresponding save
        self.unites = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]

        self.workers = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        self.workersDTO = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]

        self.villager = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        self.villagerDTO = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]

        self.soldier = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        self.soldierDTO = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]

        self.horseman = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        self.horsemanDTO = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]

        self.villager = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        self.villagerDTO = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
                                                                        
        self.archer = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        self.archerDTO = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]

        #Buildings
        self.batiment = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        self.batimentDTO = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]

        self.temp_tile = None
        self.examine_tile = None
        self.caserne_tile = None # Used to spawn units on the right tile
        self.house_tile = None # Used to drop resources of villager when full
        self.move_timer = pygame.time.get_ticks()
        
        #Save paths
        self.map_save_file_path = SAVED_GAME_FOLDER + "world"
        self.building_save_file_path = SAVED_GAME_FOLDER + "batiments"
        self.workers_save_file_path = SAVED_GAME_FOLDER + "worker"
        self.soldiers_save_file_path = SAVED_GAME_FOLDER + "soldiers"
        self.horseman_save_file_path = SAVED_GAME_FOLDER + "horseman"
        self.villager_save_file_path = SAVED_GAME_FOLDER + "villager"
        self.archer_save_file_path = SAVED_GAME_FOLDER + "archer"

        #init
        self.restore_save()
        if self.batiment == [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]: self.générerCamp = self.générer_camp()
   
    def update(self, camera):
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()

        if mouse_action[2]:
            self.examine_tile = None
            self.hud.examined_tile = None
            self.hud.select_surface_empty = True

        self.temp_tile = None
        if self.hud.selected_tile is not None:

            grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera.scroll)
            collision2 = collision3 = collision4 = True
            if self.hud.selected_tile["name"] == "House":
                taille = 1
            else: taille=2
            if self.can_place_tile(grid_pos):
                img = self.hud.selected_tile["image"].copy()
                img.set_alpha(100)
                render_pos = self.world[grid_pos[0]][grid_pos[1]]["render_pos"]
                iso_poly = self.world[grid_pos[0]][grid_pos[1]]["iso_poly"]
                collision = self.world[grid_pos[0]][grid_pos[1]]["collision"]

                if ((grid_pos[0]+1) < (self.grid_length_x-1)) and ((grid_pos[1]+1) < (self.grid_length_x-1)):  # détèce la collision pour la pose de batiment 2x2
                    collision2 = self.world[grid_pos[0]+1][grid_pos[1]]["collision"]
                    collision3 = self.world[grid_pos[0]][grid_pos[1]+1]["collision"]
                    collision4 = self.world[grid_pos[0]+1][grid_pos[1]+1]["collision"]


                self.temp_tile = {
                    "image": img,
                    "render_pos": render_pos,
                    "iso_poly": iso_poly,
                    "collision": collision,
                    "name" :  self.hud.selected_tile["name"]
                }
                
                if mouse_action[0] and not collision:
                    
                    if dicoBatiment[self.hud.selected_tile["name"]][1] == 1:
                        ent = Batiment(render_pos, self.hud.selected_tile["name"], self.resource_manager)
                        self.entities.append(ent)
                        self.batiment[grid_pos[0]][grid_pos[1]] = ent
                        self.world[grid_pos[0]][grid_pos[1]]["collision"] = True
                        self.collision_matrix[grid_pos[1]][grid_pos[0]] = 0 
                        self.hud.selected_tile = None

                    elif ((not collision2) and (not collision3) and (not collision4)):  # les 3 autres cases sont dispos
                        ent = Batiment(render_pos, self.hud.selected_tile["name"], self.resource_manager)
                        self.entities.append(ent)
                        self.batiment[grid_pos[0]][grid_pos[1]] = ent
                        for i in range (dicoBatiment[self.hud.selected_tile["name"]][1]):
                            for j in range (dicoBatiment[self.hud.selected_tile["name"]][1]):
                                self.world[grid_pos[0]+i][grid_pos[1]+j]["collision"] = True
                                self.collision_matrix[grid_pos[1]+j][grid_pos[0]+i] = 0 
                        self.hud.selected_tile = None
            
        elif self.hud.selected_unit_icon:  #Si les icones unités sont selectionées, le clic gauche fais spawn autour de la caserne
                now = pygame.time.get_ticks()
                if mouse_action[0]:
                    if now - self.move_timer > UNITS_SPAWN_TIME:
                        self.spawn_unit_autour_caserne(
                            self.hud.selected_unit_icon["name"], self.caserne_tile)
                        self.hud.selected_unit_icon = None

                        self.move_timer = now
                    else: self.hud.selected_unit_icon = None   

        else:

            grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera.scroll)

            if self.can_place_tile(grid_pos):
                batiment = self.batiment[grid_pos[0]][grid_pos[1]]
                if mouse_action[0] and (batiment is not None):
                    self.examine_tile = grid_pos
                    self.hud.examined_tile = batiment


    def create_collision_matrix(self):
        collision_matrix = [[1 for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]            
        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                if self.world[x][y]["collision"]:
                    collision_matrix[y][x] = 0

        return collision_matrix            

    def draw(self, screen, camera):
        screen.blit(self.grass_tiles,(camera.scroll.x, camera.scroll.y)) #Au lieu d'iterer pour tout les block de fond, ici herbe, on le fait une fois
        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                render_pos = self.world[x][y]["render_pos"]
                nomElement = self.world[x][y]["tile"].nomElement
                if nomElement != "":  #Si le nom de l'element sur la case n'est pas vide alors on affiche la ressource correspondante (arbre etc)
                        screen.blit(self.tiles[nomElement],
                                (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x +25,
                                 render_pos[1] -  (self.tiles[nomElement].get_height() - TILE_SIZE +15) + camera.scroll.y))
                
                #draw bâtiments    
                batiment = self.batiment[x][y]
                if batiment is not None:
                    screen.blit(batiment.image,
                                    (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x +25 - (batiment.image.get_width()*(dicoBatiment[batiment.name][1]-1))/4,
                                     render_pos[1] - (batiment.image.get_height()/dicoBatiment[batiment.name][1] - TILE_SIZE +15) + camera.scroll.y))
                    if self.examine_tile is not None:
                        if (x == self.examine_tile[0]) and (y == self.examine_tile[1]):
                            mask = pygame.mask.from_surface(batiment.image).outline()
                            # affiche le rectangle blanc autour du batiment
                            mask = [(x + render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x +25 - (batiment.image.get_width()*(dicoBatiment[batiment.name][1]-1))/4, y + render_pos[1] - (batiment.image.get_height()/dicoBatiment[batiment.name][1] - TILE_SIZE +15) + camera.scroll.y) for x, y in mask]
                            pygame.draw.polygon(screen, (255, 255, 255), mask, 2)
                            #affiche hud batiment
                            if (batiment.name=="Towncenter"):
                                self.hud.display_unit_icons = False 
                                self.hud.blit_hud("hudTowncenter", str(batiment.pv), screen)
                            elif (batiment.name=="House"):
                                self.hud.display_unit_icons = False 
                                self.hud.blit_hud("hudHouse", str(batiment.pv), screen)
                                self.house_tile = self.world[x][y] #Used to drop resources of villager when full
                            elif (batiment.name=="Barrack"):
                                self.hud.display_unit_icons = True
                                self.hud.blit_hud("hudCaserne", str(batiment.pv), screen)
                                self.caserne_tile = self.world[x][y] #Used to spawn units on the right tile
                    elif not self.examine_tile:
                        self.hud.display_unit_icons = False                

                # draw units
                unites = self.unites[x][y]
                if unites is not None:
                    if unites.pv > 0:
                                
                        if unites.name == "horseman":
                            if unites.selected:
                                self.hud.blit_hud("hudCavalier", str(unites.pv), screen)
                                pygame.draw.polygon(screen, (255, 255, 255), unites.iso_poly, 2)
                            screen.blit(unites.image, (unites.pos_x + self.grass_tiles.get_width() / 2 + camera.scroll.x + 22,
                            unites.pos_y - unites.image.get_height() + camera.scroll.y + 55))
                            
                        else:
                            if unites.selected:
                                self.hud.blit_hud("hud" + unites.name, str(unites.pv), screen, str(unites.nb_ressource_Transp), unites.ressource_Transp)
                                pygame.draw.polygon(screen, (255, 255, 255), unites.iso_poly, 2)

                                if unites.name == "Villageois":
                                    self.hud.display_building_icons = True

                            screen.blit(unites.image, (unites.pos_x + self.grass_tiles.get_width() / 2 + camera.scroll.x + 45,
                            unites.pos_y - unites.image.get_height() + camera.scroll.y + 50))
                            
                    else:
                        unites.delete()    
                        self.hud.select_surface_empty = True    

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
                    render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x +25 - (self.temp_tile["image"].get_width()*(dicoBatiment[self.temp_tile["name"]][1]-1))/4,
                    render_pos[1] - (self.temp_tile["image"].get_height()/dicoBatiment[self.temp_tile["name"]][1] - TILE_SIZE +15) + camera.scroll.y
                )
            )
        #ACTIVE LES COORDONNEES DU CURSEUR = -10FPS
        
        # mouse_pos = pygame.mouse.get_pos()
        # grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera.scroll)
        # txt = str(grid_pos)
        # draw_text(screen, txt, 20, WHITE, (mouse_pos[0], mouse_pos[1]+20))
        



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
                    world[grid_x][grid_y]["tile"].setRessource(Ressource(NB_RESSOURCES[0], LES_RESSOURCES[0]))
                    world[grid_x][grid_y]["collision"] = True

                    '''
                    world[grid_x][grid_y]["tile"].nomElement = "tree"
                    world[grid_x][grid_y]["tile"].ressource.nbRessource = NB_RESSOURCES[0]
                    world[grid_x][grid_y]["tile"].ressource.typeRessource = "wood"
                    world[grid_x][grid_y]["collision"] = True
                    '''

                if self.Bou.M1[grid_x][grid_y] == "fruit":
                    world[grid_x][grid_y]["tile"].nomElement = "food"
                    world[grid_x][grid_y]["tile"].setRessource(Ressource(NB_RESSOURCES[1], LES_RESSOURCES[1]))
                    world[grid_x][grid_y]["collision"] = True

                if self.Bou.M1[grid_x][grid_y] == "gold":

                    world[grid_x][grid_y]["tile"].nomElement = "gold"
                    world[grid_x][grid_y]["tile"].setRessource(Ressource(NB_RESSOURCES[2], LES_RESSOURCES[2]))
                    world[grid_x][grid_y]["collision"] = True

                if self.Bou.M1[grid_x][grid_y] == "stone":
                    world[grid_x][grid_y]["tile"].nomElement = "stone"
                    world[grid_x][grid_y]["tile"].setRessource(Ressource(NB_RESSOURCES[3], LES_RESSOURCES[3]))
                    world[grid_x][grid_y]["collision"] = True

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

    def cart_to_iso(self, x, y): #Coordonées rectangulaires en isométriques
        iso_x = x - y 
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

        if grid_x > 49: grid_x = 49
        if grid_x < 0: grid_x = 0
        if grid_y > 49: grid_y = 49
        if grid_y < 0: grid_y = 0

        return grid_x, grid_y

    def générer_camp(self):
        générateur = random.random()
        x = 7
        y = random.randint(-4,4)
        z = random.randint(-4,4)
        #print(générateur, "\t", y, "\t", z, "\n")
        if générateur<0.25:
            a = x+y
            b = x+z
        elif générateur<0.5:
            a = self.grid_length_x-x+y
            b = x+z
        elif générateur<0.75:
            a = x+y
            b = self.grid_length_y-x+z
        else:
            a = self.grid_length_x-x+y
            b = self.grid_length_y-x+z
        M2=self.Bou.creation_camp(a, b)
        for grid_x in range(self.grid_length_x): #On itère pour la taille de la map
            for grid_y in range(self.grid_length_y):
                if M2[grid_x][grid_y] == "wood": #Checking if our ressource matrice, M1, has set any ressource on the tile 
                    self.world[grid_x][grid_y]["tile"].nomElement = ""
                    self.world[grid_x][grid_y]["tile"].setRessource(Ressource(0,""))
                    self.world[grid_x][grid_y]["collision"] = False


        render_pos = self.world[a][b]["render_pos"]
        ent = Batiment(render_pos, "Towncenter", self.resource_manager) # (Towncenter(render_pos, self.resource_manager)
        self.entities.append(ent)
        self.batiment[a][b] = ent
        for i in range (3):
            for j in range (3):
                self.world[a+j][b+i]["collision"] = False
                self.world[a+j][b+i]["tile"].ressource.typeRessource = ""
                self.world[a+j][b+i]["tile"].ressource.nbRessource = 0
                self.collision_matrix[b+i][a+j] = 1
        for i in range (2):
            for j in range (2):
                self.world[a+j][b+i]["collision"] = True
                self.world[a+j][b+i]["tile"].setRessource(Ressource(0, ""))
                self.collision_matrix[b+i][a+j] = 0
        
    def load_images(self): #Chargement des images, retourne le dictionnaire d'images

        Towncenter = pygame.image.load("assets/towncenter.png").convert_alpha()
        House = pygame.image.load("assets/house.png").convert_alpha()
        Barrack = pygame.image.load("assets/barrack.png").convert_alpha()
        grass = pygame.image.load("assets/grass.png").convert_alpha()
        tree = pygame.image.load("assets/tree.png").convert_alpha()
        stone = pygame.image.load("assets/stone.png").convert_alpha()
        gold = pygame.image.load("assets/gold.png").convert_alpha()
        fruit = pygame.image.load("assets/fruit.png").convert_alpha()

        images = {
            "Towncenter": Towncenter,
            "House": House,
            "Barrack": Barrack,
            "grass": grass,
            "tree": tree,
            "gold": gold,
            "food": fruit,
            "stone": stone
        }

        return images

    def can_place_tile(self, grid_pos):
        mouse_on_panel = False
        for rect in [self.hud.resources_rect, self.hud.build_rect]:
            if rect.collidepoint(pygame.mouse.get_pos()):
                mouse_on_panel = True
        world_bounds = (0 <= grid_pos[0] <= (self.grid_length_x-1)) and (0 <= grid_pos[1] <= (self.grid_length_x-1))

        if world_bounds and not mouse_on_panel:
            return True
        else:
            return False

    def reset_tile(self, x, y): #On lui fournit des coordonnées de la case et il la reinitialise ainsi que toute les collisions
        self.world[x][y]["tile"].ressource.nbRessources == 0
        self.world[x][y]["tile"].nomElement=""
        self.world[x][y]["tile"].ressource.nbRessource = ""
        self.world[x][y]["tile"].ressource.typeRessource = ""
        self.world[x][y]["collision"] = False
        self.collision_matrix[y][x] = 1

    def spawn_unit_autour_caserne(self, unit_name, tile): #On lui fournit la case de la caserne ou batiment 2x2 et il s'occupe de spawn autour
        if not self.world[tile["grid"][0] ][tile["grid"][1] + 2]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] ][tile["grid"][1] + 2], self, self.camera) 
                Villager(self.world[tile["grid"][0] ][tile["grid"][1] + 2], self, self.camera) 
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] ][tile["grid"][1] + 2], self, self.camera) 
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] ][tile["grid"][1] + 2], self, self.camera) 
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] ][tile["grid"][1] + 2], self, self.camera) 
        
        elif not self.world[tile["grid"][0] -1 ][tile["grid"][1] + 2]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self, self.camera)    
                Villager(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self, self.camera)    
        
        elif not self.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self, self.camera)    
                Villager(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self, self.camera)    
        
        elif not self.world[tile["grid"][0] -1 ][tile["grid"][1] ]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] -1 ][tile["grid"][1] ], self, self.camera)    
                Villager(self.world[tile["grid"][0] -1 ][tile["grid"][1] ], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] -1 ][tile["grid"][1] ], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] -1 ][tile["grid"][1] ], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] -1 ][tile["grid"][1] ], self, self.camera)    
        
        elif not self.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self, self.camera)    
                Villager(self.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self, self.camera)    
        
        elif not self.world[tile["grid"][0] ][tile["grid"][1] - 1]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] ][tile["grid"][1] - 1], self, self.camera)    
                Villager(self.world[tile["grid"][0] ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] ][tile["grid"][1] - 1], self, self.camera)    
        
        elif not self.world[tile["grid"][0] +1 ][tile["grid"][1] - 1]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self, self.camera)    
                Villager(self.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self, self.camera)    
        
        elif not self.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self, self.camera)    
                Villager(self.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self, self.camera)    
        
        elif not self.world[tile["grid"][0] +2 ][tile["grid"][1] ]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] +2 ][tile["grid"][1] ], self, self.camera)    
                Villager(self.world[tile["grid"][0] +2 ][tile["grid"][1] ], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] +2 ][tile["grid"][1] ], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] +2 ][tile["grid"][1] ], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] +2 ][tile["grid"][1] ], self, self.camera)    
        
        elif not self.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self, self.camera)
                Villager(self.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self, self.camera)    
        
        elif not self.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self, self.camera)    
                Villager(self.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self, self.camera)    
        
        elif not self.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ]["collision"]:
            if unit_name == "Villageois":
                #Worker(self.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self, self.camera)    
                Villager(self.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self, self.camera)    
            if unit_name == "Soldier":
                Soldier(self.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self, self.camera)    
            if unit_name == "horseman":
                Horseman(self.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self, self.camera)    
            if unit_name == "Archer":
                Archer(self.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self, self.camera)    

    def restore_save(self):
        #Map restore
        try:    
            with open(self.map_save_file_path, "rb") as input:
                restore_world_dto = pickle.load(input)
                self.world = restore_world_dto.world
                self.collision_matrix = restore_world_dto.collision_matrix
                input.close()
        except: 
            print("Created map save file")

        #Buildings restore
        try:    
            with open(self.building_save_file_path, "rb") as input:
                restore_building_dto = pickle.load(input)
                self.batimentDTO = restore_building_dto
                input.close()

        except: 
            print("Created building save file")  

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                if self.batimentDTO[x][y] != None:
                    entDTO = self.batimentDTO[x][y]
                    ent = Batiment(entDTO.pos, entDTO.name, self.resource_manager)
                    for resource, cost in self.resource_manager.costs[entDTO.name].items(): #Giving back the resources spent reloading save
                        self.resource_manager.resources[resource] += cost  
                    self.entities.append(ent)
                    self.batiment[x][y] = ent
                    if entDTO.name == "House":
                        self.house_tile = self.world[x][y]



    def save(self):
        try:   #Map save
            with open(self.map_save_file_path, "wb") as output:
                worker_dto = WorldDTO(self.world,self.collision_matrix)
                pickle.dump(worker_dto,output)
                output.close()
        except: print("Couldnt dump map save in file")

        #Buildings save 
        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                if self.batiment[x][y] != None:
                    ent = self.batiment[x][y]
                    if ent.name == "Towncenter":
                        entDTO = TowncenterDTO(ent.pos)
                    if ent.name == "House":
                        entDTO = HouseDTO(ent.pos)
                    if ent.name == "Barrack":
                        entDTO = BarrackDTO(ent.pos)
                    self.batimentDTO[x][y] = entDTO

        try:   
            with open(self.building_save_file_path, "wb") as output:
                pickle.dump(self.batimentDTO,output)
                output.close()
        except: print("Couldnt dump building save in file") 

        



