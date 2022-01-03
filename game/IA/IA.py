from pygame import *
import pygame
from itertools import count, cycle
from game.batiment import Batiment
from ..Ressource import *
from .soldierIA import SoldierIA
from .horsemanIA import HorsemanIA
from.archerIA import ArcherIA
from .villagerIA import VillagerIA
from ..world import World
from ..definitions import IA_DECISION_TIME


class IA:

    def __init__(self,world, ressource_manager, team="red"):
        self.team = team
        self.world = world
        self.towncenter = self.world.towncenterIA_tile
        self.player_towncenter = self.world.towncenter_tile
        self.ressource_manager = ressource_manager

        #Units
        self.warriors = []
        self.farmers = []
        self.villagers = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.soldiers = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.horsemen = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.archers = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]

        self.attacking = False

        #Build
        self.switch_iterator = cycle([-1,1])
        self.build_position_x = self.towncenter["grid"][0]
        self.build_position_y = self.towncenter["grid"][1]
        self.count_x = 0
        self.count_y = 0

        #Events
        self.take_decision_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.take_decision_event, IA_DECISION_TIME)

    def events(self, e):    #Remplace l'update de l'IA, cette boucle est effectuée chaque X seconde pour limiter la perte d'fps
        if e.type == self.take_decision_event:
            # self.attack_villagers()
            self.find_and_place_building("House")
            

    def attack_villagers(self):
        if self.attacking == False:
            for villager_x in self.world.villager:
                for villager in villager_x:
                    for w in self.warriors:
                        if villager is not None and w is not None:
                            if villager.team != w.team:
                                w.create_path(villager.tile["grid"][0],villager.tile["grid"][1])
                                self.attacking = True          # pour attaquer unités une par une sans appeller create path en boucle
                                if villager.pv < 0 or w.dest_tile == w.tile:
                                    self.attacking = False

    def find_and_place_building(self, name_of_building):  #Cherche ou poser autour du Towncenter, le batiment en parametre
        next_val = next(self.switch_iterator)
        print(self.count_x, self.count_y, next_val)
        
        if  (self.build_position_x + self.count_x * next_val) in range(self.world.grid_length_x) and  (self.build_position_y + self.count_y * next_val) in range(self.world.grid_length_y)  and  not self.world.world[self.build_position_x + self.count_x * next_val ][self.build_position_y + self.count_y * next_val]["collision"]:
            self.build_position_x += self.count_x * next_val 
            self.build_position_y += self.count_y * next_val 
            self.build(name_of_building)
        elif self.count_x < self.count_y:
            self.count_x += 1   
        elif self.count_y < self.count_x:
            self.count_y += 1
        else:
            self.count_x += 1     


    def build(self, name_of_building):  #Placer le batiment

        if dicoBatiment[name_of_building][1] == 1: #Pour taille de batiment 1x1
            ent = Batiment(self.world.world[self.build_position_x][self.build_position_y]["render_pos"], name_of_building, self.ressource_manager)
            self.world.entities.append(ent)
            ent.current_image = 1   #Petite image ruine pour construction
            self.world.batiment[self.build_position_x][self.build_position_y] = ent
            self.world.world[self.build_position_x][self.build_position_y]["collision"] = True
            self.world.collision_matrix[self.build_position_y][self.build_position_x] = 0
            self.world.world[self.build_position_x][self.build_position_y]["tile"].tile_batiment = self.world.world[self.build_position_x][self.build_position_y]
            self.ordre_de_construction_villageois(self.build_position_x, self.build_position_y)
            print(name_of_building, " has been built successfuly")
            
    def ordre_de_construction_villageois(self, grid_pos_x, grid_pos_y): #Ordonner a un villageois de construire
       for villager_x in self.villagers:  # Pour que le villageois construise un batiment, on trouve le villageois selectionné
           for villager in villager_x:
               if (villager != None and not villager.busy):
                   villager.batiment_pv = dicoBatiment[self.hud.selected_tile["name"]][2]
                   villager.batiment_tile = self.world[grid_pos_x][grid_pos_y]   #Case ou se trouve le batiment
                   villager.create_path(villager.batiment_tile["grid"][0], villager.batiment_tile["grid"][1] , True)
                   villager.construire = True
                   villager.busy = True
                   break                                  