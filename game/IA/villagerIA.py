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
        self.animation = self.world.animation.villagerIA_walk
        self.animation_attack = self.world.animation.villagerIA_farm
        self.animation_attack_up = self.world.animation.villagerIA_farm_up
        self.animation_attack_ldown = self.world.animation.villagerIA_farm_ldown
        self.animation_attack_left = self.world.animation.villagerIA_farm_left
        self.animation_attack_uleft = self.world.animation.villagerIA_farm_uleft
        self.animation_attack_right = self.world.animation.villagerIA_farm_right
        self.animation_attack_uright = self.world.animation.villagerIA_farm_uright
        self.animation_attack_rdown = self.world.animation.villagerIA_farm_rdown
        self.image_standby = pygame.image.load('assets/villagerIA/Villagerwalk001V2.png').convert_alpha()
        self.image = pygame.image.load('assets/villagerIA/Villagerwalk001V2.png').convert_alpha()

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
                self.walkdown_animation = False
                self.cible.attacked = True
                self.cible.attacker = self
                if self.cible != 0 and self.cible is not None:
                    self.cible.pv -= self.dmg
                if self.world.world[self.cible.tile["grid"][0]][self.cible.tile["grid"][1]] != self.world.world[self.temp_tile_a["grid"][0]][self.temp_tile_a["grid"][1]]:
                    if self.cible.dest_tile == self.cible.tile:
                        self.world.world[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]]["collision"] = True
                        self.world.unites[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]] == self.cible
                        self.create_path(self.cible.tile["grid"][0], self.cible.tile["grid"][1])
                if self.cible.pv <= 0:
                    self.attack = False
                    self.attack_ani = False
                    self.cible = 0
            elif self.attack_bati:
                self.walkdown_animation = False
                if self.cible is not None and self.cible != 0:
                    self.cible.pv -= self.dmg
                    if self.cible.pv <= 0:
                        self.attack = False
                        self.attack_ani = False
            elif self.farm:
                self.farm_ani = True
                self.farmer_cases_autour()


            elif self.construire:
                self.construire_batiment(self.batiment_tile, self.batiment_pv)

            elif self.transfer_resources_bool:
                self.transfer_resources()  
            else:
                self.busy = False
                if self in self.IA.farmers: self.IA.farmers.remove(self)     
 


        if self.path_index <= len(self.path) - 1:
            if self.dest_tile != self.tile:
                self.walkdown_animation = True

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
            self.walkdown_animation = False
            self.dest_tile = self.tile
        # print("Tile", self.tile["grid"][0], self.tile["grid"][1], "Pos", self.pos_x, self.pos_y)
        # print(" busy", self.busy, "farm ", self.farm, "cono", self.construire, "attack ", self.attack, "attabat", self.attack_bati)


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
            self.IA.ressource_manager.resources[self.ressource_Transp] += int(self.nb_ressource_Transp)
            self.nb_ressource_Transp = 0
            self.ressource_Transp = "" 
            self.busy = False 
            self.IA.farmers.remove(self)
            self.transfer_resources_bool = False
            
            

    #Override
    def farmer_cases_autour(self): 
        # print("                                         busy : ", self.busy, "farm", self.farm, "ressource", self.world.world[self.cible["grid"][0]][self.cible["grid"][1]]["tile"].ressource.nbRessources, "x et y", self.cible["grid"][0], self.cible["grid"][1], "type ",self.cible["tile"].ressource.typeRessource)
        if self.world.world[self.cible["grid"][0]][self.cible["grid"][1]]["tile"].ressource.nbRessources and self.world.world[self.cible["grid"][0]][self.cible["grid"][1]]["tile"].ressource.typeRessource == "": 
            self.world.reset_tile(self.cible["grid"][0], self.cible["grid"][1])
            self.busy = False
            self.farm = False
            if self in self.IA.farmers: self.IA.farmers.remove(self)
        if (self.world.world[self.cible["grid"][0]][self.cible["grid"][1]]["tile"].ressource.nbRessources > 0):
            self.farmer_cases(self.cible)  
        else: 
            if self in self.IA.farmers: self.IA.farmers.remove(self)          
            self.farm = False    
            self.busy = False  

    def construire_batiment(self, batiment_tile, pvMaxDuBatiment): #Augmente les pv des batiments jusqua son max        
        
        if self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].pv < pvMaxDuBatiment :
           self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].pv += 1*definitions.EFFICIENCY*int(DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]/5)
           if self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].pv > pvMaxDuBatiment:
               self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].pv = pvMaxDuBatiment
        else:
            self.construire = False
            self.busy = False
            self.IA.action_faite = 1
            self.world.batiment[batiment_tile["grid"][0]][batiment_tile["grid"][1]].current_image = 2

    def delete(self):
        
        
        self.IA.ressource_manager.population -= 1  

        self.world.entities.remove(self)

        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

        self.IA.villagers[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.selected = False
        self.temp = 0       
        