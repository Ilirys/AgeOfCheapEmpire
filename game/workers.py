import json
import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, SAVED_GAME_FOLDER, TILE_SIZE
from game.deplacement import lerp
import pickle
import DTO.workerDTO

class Worker:

    def __init__(self,tile,world,camera,pv=2000, team="blue"):
        self.world = world
        self.world.entities.append(self)
        self.camera = camera
        self.tile = tile
        self.pv = pv
        self.team = team

        #Visual and audio effects
        self.name = "Villageois"
        self.image = pygame.image.load('assets/sprites/villager/Villager.png').convert_alpha()
        self.temp = 0
        self.animation = self.world.animation.villager_walk
        self.animation_mort = self.world.animation.villager_mort
        self.movestraight_animation = False
        self.sound = pygame.mixer.Sound('Sounds/villager_select4.WAV')
        self.attack_ani = False
        self.farm_ani = False
        self.animation_attack = self.world.animation.villager_attack
        self.animation_farm = self.world.animation.villager_farm

        # pathfinding
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = self
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]
        self.render_pos_x = self.tile["render_pos"][0]
        self.render_pos_y = self.tile["render_pos"][1]
        self.temp_tile = None       #Utilisé pour enlever et remettre la collision de la case d'une unite lors du pathfinding de l'attaque

        #selection
        self.selected = False
        self.hitbox = pygame.Rect(self.pos_x  + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)
        iso_poly = self.tile["iso_poly"]
        self.iso_poly = None
        self.cible = self
        self.dest_tile = self.tile
        
        #Attaque
        self.attack = False
        self.attack_bati = False
        self.dmg = 1
        self.range = 2
        self.temp_tile_a = self.tile


        #Farm
        self.farm = False
        self.ressource_Transp = ""
        self.nb_ressource_Transp = 0
        self.cibleFarm = 0
        self.efficiency = 3

        #Construction
        self.construire = False #Pour savoir si il doit faire un chemin vers le batiment a construire
        self.batiment_tile = None   #Case où aller construire
        self.batiment_pv = 0

        #init
        self.world.resource_manager.apply_cost_to_resource(self.name)
        self.path_index = 0
        self.path = []
        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
        self.mouse_to_grid(0,0,self.camera.scroll)
        
    def create_path(self, x, y):
        searching_for_path = True
        self.attack = False
        while searching_for_path:
            self.dest_tile = self.world.world[x][y]
            if self.dest_tile != self.tile:
                if not self.dest_tile["collision"]:  # Condition de déplacement normal, sans rien sur la case cible
                    self.grid = Grid(matrix=self.world.collision_matrix)
                    self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
                    self.end = self.grid.node(x, y)
                    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                    self.path_index = 0

                    self.path, runs = finder.find_path(self.start, self.end, self.grid)

                    self.progression = 0
                    self.attack = False

                    searching_for_path = False
                elif self.world.unites[x][y] != None or self.world.world[x][y]["tile"].tile_batiment != 0 :
                    # Reinitialise la derniere case de destination et la cible
                    self.cible = None

                    # Si la case contient une unitées ou du farm,
                    # On enleve la collision de la case du soldat (Or else can't get find_path to work)

                    self.temp_tile = self.world.world[x][y]
                    self.world.world[x][y]["collision"] = False
                    self.world.collision_matrix[y][x] = 1

                    self.grid = Grid(matrix=self.world.collision_matrix)
                    self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
                    self.end = self.grid.node(x, y)
                    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                    self.path_index = 0
                    self.path, runs = finder.find_path(self.start, self.end, self.grid)

                    # On enleve le dernier element de la liste (Pour ne pas aller SUR l'unité) et soit on attaque soit on farm
                    if self.path: self.path.pop()

                    if self.world.unites[x][y] != None:  # Condition d'attaque
                        self.cible = self.world.unites[x][y]
                        self.attack = True
                        self.temp_tile_a = self.cible.tile

                    elif self.world.world[x][y]["tile"].tile_batiment != 0:
                        self.cible =   self.world.batiment[[self.world.world[x][y]["tile"].tile_batiment][0]][[self.world.world[x][y]["tile"].tile_batiment][1]]  #self.world.world[x][y]["tile"].tile_batiment
                        self.attack_bati = True


                    self.dest_tile = self.world.world[self.path[-1][0]][self.path[-1][1]]  # La case destination est la dernière de la liste path

                    if self.temp_tile:  #Dans le cas ou on voulait aller a une case occupée, il faut remettre la collision de la case occupée a 1
                        self.world.world[self.temp_tile["grid"][0]][self.temp_tile["grid"][1]]["collision"] = True
                        self.world.collision_matrix[self.temp_tile["grid"][1]][self.temp_tile["grid"][0]] = 0
                        self.temp_tile = None

                    self.progression = 0

                    searching_for_path = False
            else:
                break


    def change_tile(self,new_tile):
        if not self.world.world[new_tile[0]][new_tile[1]]["collision"]:
            #Updates worker and unit matrices
            self.world.workers[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.workers[new_tile[0]][new_tile[1]] = self
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[new_tile[0]][new_tile[1]] = self

            self.tile = self.world.world[new_tile[0]][new_tile[1]]  #Change tile
            self.render_pos_x = self.tile["render_pos"][0]
            self.render_pos_y = self.tile["render_pos"][1]

            #collision matrix (for pathfinding and buildings): Active collision for the current tile 
            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
        else: 
            self.create_path(self.dest_tile["grid"][0], self.dest_tile["grid"][1])
            self.render_pos_x = self.pos_x
            self.render_pos_y = self.pos_y    

    def mouse_to_grid(self, x, y, scroll):
        # transform to world position (removing camera scroll and offset)
        world_x = x - scroll.x - self.world.grass_tiles.get_width()/2
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

    def update(self):


        #Updating mouse position and action and the grid_pos
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mouse_pos[0],mouse_pos[1],self.camera.scroll)

        #Hitbox
        self.hitbox.update(self.pos_x  + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)

        #Selection polygon
        pos_poly = [self.pos_x + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50]
        self.iso_poly = [(pos_poly[0] - 10, pos_poly[1] +44), (pos_poly[0] + 15, pos_poly[1] + 29), (pos_poly[0] + 40, pos_poly[1] + 44), (pos_poly[0] + 15 , pos_poly[1] + 59)]

        #Animation update
        self.update_sprite()


        if self.selected:
            if self.world.can_place_tile(grid_pos):
                if mouse_action[2]: #Clic droit
                    self.create_path(grid_pos[0], grid_pos[1]) #Creer le chemin vers la case pointée par la souris
                    self.selected = False
                    self.world.hud.select_surface_empty = True  #Afficher le hud de l'unite
                    self.world.hud.display_building_icons = False   
                    
                if mouse_action[0]: #Clic gauche
                    self.selected = False   #unselect
                    self.world.hud.select_surface_empty = True  #Afficher son hud
                    self.world.hud.display_building_icons = False   #Ne plus afficher les icones de constructions

        if self.dest_tile == self.tile:
            if self.attack:
                self.cible.attacked = True
                self.cible.attacker = self
                self.attack_ani = True
                self.cible.pv -= self.dmg
                #self.cible.create_path(self.tile["grid"][0],self.tile["grid"][1])
                if self.world.world[self.cible.tile["grid"][0]][self.cible.tile["grid"][1]] != self.world.world[self.temp_tile_a["grid"][0]][self.temp_tile_a["grid"][1]]:
                    if self.cible.dest_tile == self.cible.tile:
                        self.world.world[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]]["collision"] = True
                        self.world.unites[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]] == self.cible
                        self.create_path(self.cible.tile["grid"][0],self.cible.tile["grid"][1])
                if self.cible.pv <= 0:
                    self.attack = False
                    self.attack_ani = False
            elif self.attack_bati:
                self.movestraight_animation = False
                #self.attack_ani = True
                self.cible.pv -= self.dmg
                if self.cible.pv <= 0:
                    self.attack = False
                    self.attack_ani = False


        if self.hitbox.collidepoint(mouse_pos):
            if mouse_action[0]:
                self.selected = True
                self.sound.play()

        if self.path_index <= len(self.path) - 1:
            if self.dest_tile != self.tile:
                self.movestraight_animation = True

            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.progression < 1:
                self.progression += (1/135) * DISPLACEMENT_SPEED[CURRENT_SPEED]
                self.progression = round(self.progression,4)
            else:
                self.progression = 1    
            self.pos_x = round(lerp(self.render_pos_x, new_real_pos[0], self.progression),3)
            self.pos_y = round(lerp(self.render_pos_y, new_real_pos[1], self.progression),3)
            

            if  self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]: #now - self.move_timer > 1000:  # update position in the world          
                self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1 #Free the last tile from collision
                self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False
                self.change_tile(new_pos)
                self.path_index += 1
                self.progression = 0

        else:
            self.movestraight_animation = False
        
                

    def update_sprite(self):
        if self.movestraight_animation == True:
            self.temp +=0.2
            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp= 0

        elif self.attack_ani == True:
            self.temp += 0.2
            self.image = self.animation_attack[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation_attack):
                self.temp = 0
        elif self.pv > 0:
            self.image = self.world.animation.villager_standby

    def delete(self):
        self.temp += 0.1
        self.image = self.animation_mort[int(self.temp)]
        if self.temp >= 11:

            self.world.entities.remove(self)

            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1 #Free the last tile from collision
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

            self.world.workers[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.selected = False
            self.temp = 0


