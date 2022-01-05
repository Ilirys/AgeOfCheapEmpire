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
        self.switch_iterator = cycle([1,1,-1,-1])
        self.switch_iterator_2 = cycle([-1,1])
        self.odd_even = cycle([4,5])
        self.a = 4
        self.next_val = next(self.switch_iterator)
        self.next_val_2 = -1
        self.build_position_x = self.towncenter["grid"][0]
        self.build_position_y = self.towncenter["grid"][1]
        self.count = 0
        self.count_x = 0
        self.count_y = 0

        #Events
        self.take_decision_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.take_decision_event, IA_DECISION_TIME)

    def events(self, e):    #Remplace l'update de l'IA, cette boucle est effectuée chaque X seconde pour limiter la perte d'fps
        if e.type == self.take_decision_event:
            # self.attack_villagers()
            self.find_and_place_building("Barrack")
            

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
        
        if self.count == self.a:
            self.count_x += 1
            self.count = 0
            self.a = next(self.odd_even)

        if  (self.build_position_x + self.count_x * self.next_val) in range(self.world.grid_length_x) and  (self.build_position_y + self.count_y * self.next_val * self.next_val_2) in range(self.world.grid_length_y)  and  not self.world.world[self.build_position_x + self.count_x * self.next_val ][self.build_position_y + self.count_y * self.next_val * self.next_val_2]["collision"]:
            
            build_save = [self.build_position_x, self.build_position_y]
            self.build_position_x += self.count_x * self.next_val 
            self.build_position_y += self.count_y * self.next_val * self.next_val_2 
            self.build(name_of_building)
            self.build_position_x, self.build_position_y = build_save[0], build_save[1]

        # print(self.count_x, self.count_y, self.next_val)
        self.count_x, self.count_y = self.count_y, self.count_x  #Switch
        self.next_val = next(self.switch_iterator)
        self.next_val_2 = next(self.switch_iterator_2)

        self.count += 1   


    def build(self, name_of_building):  #Placer le batiment
        if self.build_position_x != self.towncenter["grid"][0] and self.build_position_y != self.towncenter["grid"][1]:    
            
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

            elif self.build_position_x + 1 in range(self.world.grid_length_x) and self.build_position_y + 1 in range(self.world.grid_length_y):
                collision2 = self.world.world[self.build_position_x + 1][self.build_position_y]["collision"]
                collision3 = self.world.world[self.build_position_x + 1][self.build_position_y + 1]["collision"]
                collision4 = self.world.world[self.build_position_x ][self.build_position_y + 1]["collision"]
                if (self.build_position_x + 1 in range(self.world.grid_length_x) and self.build_position_y + 1 in range(self.world.grid_length_y) and (not collision2) and (not collision3) and (not collision4) ):  # les 3 autres cases sont dispos
                    ent = Batiment(self.world.world[self.build_position_x][self.build_position_y]["render_pos"], name_of_building, self.ressource_manager)
                    self.world.entities.append(ent)
                    self.world.batiment[self.build_position_x][self.build_position_y] = ent
                    for i in range (dicoBatiment[name_of_building][1]):
                        for j in range (dicoBatiment[name_of_building][1]):
                            self.world.world[self.build_position_x+i][self.build_position_y+j]["collision"] = True
                            self.world.collision_matrix[self.build_position_y+j][self.build_position_x+i] = 0
                            self.world.world[self.build_position_x + i][self.build_position_y + j]["tile"].tile_batiment = self.world.world[self.build_position_x][self.build_position_y]

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