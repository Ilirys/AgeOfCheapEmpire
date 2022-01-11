import pygame
import random
import game.definitions as definitions
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from ..definitions import *
from math import *
from game.deplacement import lerp
from ..villager import Villager


class VillagerIA(Villager):
    def __init__(self,tile, world, camera, IA, pv=2000, team="red"):
        super().__init__(tile, world, camera, pv, team)
        self.IA = IA
        self.IA.villagers[self.tile["grid"][0]][self.tile["grid"][1]] = self
        self.IA.ressource_manager.apply_cost_to_resource(self.name)
        self.IA.ressource_manager.population += 1
        self.busy = False 

        #Farm
        self.storage_tile = self.IA.towncenter




    #Override
    def update(self):
        # Updating mouse position and action and the grid_pos
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], self.camera.scroll)
        # Animation update
        self.update_sprite()             

        if self.dest_tile == self.tile:
            if self.attack:
                self.movestraight_animation = False
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
                self.movestraight_animation = False
                #self.attack_ani = True
                self.cible.pv -= self.dmg
                if self.cible.pv <= 0:
                    self.attack = False
                    self.attack_ani = False
            elif self.farm:
                self.farmer_cases_autour()

            elif self.construire:
                self.construire_batiment(self.batiment_tile, self.batiment_pv)

            elif self.transfer_resources_bool:
                self.transfer_resources()  

            else: 
                self.busy = False
                try:
                    self.IA.farmers.remove(self)
                except: pass    


        if self.path_index <= len(self.path) - 1:
            if self.dest_tile != self.tile:
                self.movestraight_animation = True

            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.progression < 1:
                self.progression += (1 / 135) * definitions.DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]
                self.progression = round(self.progression, 4)
            else:
                self.progression = 1
            self.pos_x = round(lerp(self.render_pos_x, new_real_pos[0], self.progression), 3)
            self.pos_y = round(lerp(self.render_pos_y, new_real_pos[1], self.progression), 3)

            if self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]:  # now - self.move_timer > 1000:  # update position in the world
                self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
                self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False
                self.change_tile(new_pos)
                self.progression = 0

        else:
            self.movestraight_animation = False



    #override
    def change_tile(self, new_tile):
        if not self.world.world[new_tile[0]][new_tile[1]]["collision"]:
            self.IA.villagers[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.IA.villagers[new_tile[0]][new_tile[1]] = self
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[new_tile[0]][new_tile[1]] = self

            self.tile = self.world.world[new_tile[0]][new_tile[1]]
            self.render_pos_x = self.tile["render_pos"][0]
            self.render_pos_y = self.tile["render_pos"][1]

            # collision matrix (for pathfinding and buildings)
            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
            self.path_index += 1
        else: 
            self.create_path(self.dest_tile["grid"][0], self.dest_tile["grid"][1])
            self.render_pos_x = self.pos_x
            self.render_pos_y = self.pos_y

    #Override
    def transfer_resources(self): #Si la capacité a atteint son max, on transfere les ressources du villageois, au compteur de ressources
        if self.nb_ressource_Transp >= self.max_ressources:
            self.IA.ressource_manager.resources[self.ressource_Transp] += self.nb_ressource_Transp
            self.nb_ressource_Transp = 0
            self.ressource_Transp = "" 
            self.busy = False 
            self.IA.farmers.remove(self)
            self.transfer_resources_bool = False
            
            

    #Override
    def farmer_cases_autour(self): 
        if (self.world.world[self.cible["grid"][0]][self.cible["grid"][1]]["tile"].ressource.nbRessources > 0):
            self.farmer_cases(self.cible)  
        else: 
            self.IA.farmers.remove(self)          
            self.farm = False    
            self.busy = False   
        