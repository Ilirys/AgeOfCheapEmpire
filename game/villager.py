import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, TILE_SIZE, dicoBatiment
from math import *
from game.deplacement import lerp
from .workers import Worker


class Villager(Worker):

    def __init__(self, tile, world, camera, pv=2000, team="blue"):
        super().__init__(tile, world, camera, pv, team)

        #saves
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.villager[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None

        # Farm
        self.farm = False
        self.ressource_Transp = ""
        self.nb_ressource_Transp = 0
        self.max_ressources = 1000

        self.cibleFarm = 0
        self.efficiency = 5



    def create_path(self, x, y, farmReset=False):
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

                    self.construire = False

                    self.attack_bati = False

                    if farmReset: self.farm = False

                    searching_for_path = False
                elif self.world.unites[x][y] != None or self.world.batiment[x][y] or self.dest_tile["tile"].ressource.getNbRessources() != 0 or self.world.world[x][y]["tile"].tile_batiment != 0:
                    # Reinitialise la cible
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
                        self.farm = False
                        self.temp_tile_a = self.cible.tile
                        self.construire = False
                        self.attack_bati = False
                    elif self.dest_tile["tile"].ressource.getNbRessources() != 0:  # Condition de farm
                        self.cible = self.dest_tile
                        self.farm = True
                        self.construire = False
                        self.attack_bati = False
                    elif self.world.batiment[x][y]: #and self.team == self.world.batiment[x][y].team
                        self.cible = self.dest_tile
                        self.farm = False
                        if x == self.world.storage_tile["grid"][0] and y == self.world.storage_tile["grid"][1]:
                            self.transfer_resources()
                    elif self.world.world[x][y]["tile"].tile_batiment != 0:
                        self.cible =  self.world.batiment[self.world.world[x][y]["tile"].tile_batiment["grid"][0]][self.world.world[x][y]["tile"].tile_batiment["grid"][1]]#self.world.world[x][y]["tile"].tile_batiment

                        self.attack_bati = True


                    if self.temp_tile:  #Dans le cas ou on voulait aller a une case occupée, il faut remettre la collision de la case occupée a 1
                        self.world.world[self.temp_tile["grid"][0]][self.temp_tile["grid"][1]]["collision"] = True
                        self.world.collision_matrix[self.temp_tile["grid"][1]][self.temp_tile["grid"][0]] = 0   # 0 pour collision!
                        self.temp_tile = None    

                    self.dest_tile = self.world.world[self.path[-1][0]][self.path[-1][1]]  # La case destination est la dernière de la liste path

                    self.progression = 0

                    searching_for_path = False

                else:
                    searching_for_path = False

            else:
                searching_for_path = False

    #override
    def change_tile(self, new_tile):
        if not self.world.world[new_tile[0]][new_tile[1]]["collision"]:
            self.world.villager[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.villager[new_tile[0]][new_tile[1]] = self
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[new_tile[0]][new_tile[1]] = self

            self.tile = self.world.world[new_tile[0]][new_tile[1]]
            self.render_pos_x = self.tile["render_pos"][0]
            self.render_pos_y = self.tile["render_pos"][1]

            # collision matrix (for pathfinding and buildings)
            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
        else: 
            self.create_path(self.dest_tile["grid"][0], self.dest_tile["grid"][1])
            self.render_pos_x = self.pos_x
            self.render_pos_y = self.pos_y


    #override
    def update(self):

        # Updating mouse position and action and the grid_pos
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], self.camera.scroll)

        # Hitbox
        self.hitbox.update(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                               self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)

            # Selection polygon
        pos_poly = [self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                        self.pos_y - self.image.get_height() + self.camera.scroll.y + 50]
        self.iso_poly = [(pos_poly[0] - 10, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 29),
                             (pos_poly[0] + 40, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 59)]

        # Animation update
        self.update_sprite()

        if self.selected:
            if self.world.can_place_tile(grid_pos):
                if mouse_action[2]: #Clic droit
                    self.create_path(grid_pos[0], grid_pos[1], True) #Creer le chemin vers la case pointée par la souris
                    self.selected = False
                    self.world.hud.select_surface_empty = True  #Enlever le hud de l'unite
                    self.world.hud.display_building_icons = False   
            
                if mouse_action[0]:
                    if not self.world.hud.selected_tile : # Déselectionner seulement si on ne va pas poser de batiment
                        self.selected = False
                        self.world.hud.select_surface_empty = True
                        self.world.hud.display_building_icons = False             

        if self.dest_tile == self.tile:
            if self.attack:
                self.walkdown_animation = False
                self.cible.attacked = True
                self.cible.attacker = self
                #self.attack_ani = True
                self.cible.pv -= self.dmg
                if self.world.world[self.cible.tile["grid"][0]][self.cible.tile["grid"][1]] != self.world.world[self.temp_tile_a["grid"][0]][self.temp_tile_a["grid"][1]]:
                    if self.cible.dest_tile == self.cible.tile:
                        self.world.world[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]]["collision"] = True
                        self.world.unites[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]] == self.cible
                        self.create_path(self.cible.tile["grid"][0], self.cible.tile["grid"][1])
                if self.cible.pv <= 0:
                    self.attack = False
                    self.attack_ani = False
            elif self.attack_bati:
                self.walkdown_animation = False
                #self.attack_ani = True
                self.cible.pv -= self.dmg
                if self.cible.pv <= 0:
                    self.attack = False
                    self.attack_ani = False
            elif self.farm:
                self.farmer_cases_autour()

            elif self.construire:
                self.construire_batiment(self.batiment_tile, self.batiment_pv)     
   
        if self.hitbox.collidepoint(mouse_pos):
            if mouse_action[0]:
                self.selected = True
                self.sound.play()

        if self.path_index <= len(self.path) - 1:
            if self.dest_tile != self.tile:
                self.walkdown_animation = True

            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.progression < 1:
                self.progression += (1 / 135) * DISPLACEMENT_SPEED[CURRENT_SPEED]
                self.progression = round(self.progression, 4)
            else:
                self.progression = 1
            self.pos_x = round(lerp(self.render_pos_x, new_real_pos[0], self.progression), 3)
            self.pos_y = round(lerp(self.render_pos_y, new_real_pos[1], self.progression), 3)

            if self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]:  # now - self.move_timer > 1000:  # update position in the world
                self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
                self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False
                self.change_tile(new_pos)
                self.path_index += 1
                self.progression = 0

        else:
            self.walkdown_animation = False

    #override
    def update_sprite(self):
        if self.walkdown_animation == True:
            self.temp += 0.2
            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp = 0

        elif self.attack_ani == True:
            self.temp += 0.2
            self.image = self.animation_attack[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation_attack):
                self.temp = 0

        # elif self.farm_ani == True:
        #    self.temp += 0.2
        #    self.image = self.animation_farm[int(self.temp)]
        #   if self.temp + 0.2 >= len(self.animation_farm):
        #       self.temp = 0

        elif self.pv > 0:
            self.image = self.world.animation.villager_standby

    #override
    def delete(self):
        if self.temp + 0.1 < 11 :
            self.temp += 0.1
        self.image = self.animation_mort[int(self.temp)]
        if self.temp >= 10.9:

            self.world.entities.remove(self)

            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

            self.world.villager[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.selected = False
            self.temp = 0


    #override
    def farmer_cases(self, cible):  # Farme la cible
        self.ressource_Transp = cible["tile"].ressource.typeRessource
        self.nb_ressource_Transp += self.efficiency
        cible["tile"].ressource.nbRessources -= self.efficiency
        if cible["tile"].ressource.nbRessources <= 0:
            self.world.reset_tile(cible["grid"][0], cible["grid"][1])

        if self.nb_ressource_Transp >= self.max_ressources:
            self.create_path(self.world.storage_tile["grid"][0], self.world.storage_tile["grid"][1], True)    

    #override
    def farmer_cases_autour(self):  # Farme les cases autour de soit, si rien a farm alors on se déplace sur la dernière case farmée
        if (self.world.world[self.tile["grid"][0] + 1][self.tile["grid"][1] + 0]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] + 1][self.tile["grid"][1] + 0]
            self.farmer_cases(self.cible)

        elif (self.world.world[self.tile["grid"][0] + 0][self.tile["grid"][1] + 1]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] + 0][self.tile["grid"][1] + 1]
            self.farmer_cases(self.cible)

        elif (self.world.world[self.tile["grid"][0] + 1][self.tile["grid"][1] + 1]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] + 1][self.tile["grid"][1] + 1]
            self.farmer_cases(self.cible)

        elif (self.world.world[self.tile["grid"][0] - 1][self.tile["grid"][1] + 0]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] - 1][self.tile["grid"][1] + 0]
            self.farmer_cases(self.cible)

        elif (self.world.world[self.tile["grid"][0] + 0][self.tile["grid"][1] - 1]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] + 0][self.tile["grid"][1] - 1]
            self.farmer_cases(self.cible)

        elif (self.world.world[self.tile["grid"][0] - 1][self.tile["grid"][1] - 1]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] - 1][self.tile["grid"][1] - 1]
            self.farmer_cases(self.cible)

        elif (self.world.world[self.tile["grid"][0] - 1][self.tile["grid"][1] + 1]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] - 1][self.tile["grid"][1] + 1]
            self.farmer_cases(self.cible)

        elif (self.world.world[self.tile["grid"][0] + 1][self.tile["grid"][1] - 1]["tile"].ressource.nbRessources > 0):
            self.cible = self.world.world[self.tile["grid"][0] + 1][self.tile["grid"][1] - 1]
            self.farmer_cases(self.cible)

        else:
            if self.dest_tile == self.tile:
                self.create_path(self.cible["grid"][0], self.cible["grid"][1])


    def transfer_resources(self): #Si la capacité a atteint son max, on transfere les ressources du villageois, au compteur de ressources
        if self.nb_ressource_Transp >= self.max_ressources:
            self.world.resource_manager.resources[self.ressource_Transp] += self.nb_ressource_Transp
            self.nb_ressource_Transp = 0
            self.ressource_Transp = "" 

    def construire_batiment(self, batiment_tile, pvMaxDuBatiment): #Augmente les pv des batiments jusqua son max        
        
        if self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].pv < pvMaxDuBatiment :
           self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].pv += 1 
        else:
            self.construire = False
            self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].current_image = 2  

