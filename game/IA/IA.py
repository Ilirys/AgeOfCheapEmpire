from time import process_time_ns
from pygame import *
import pygame
from itertools import count, cycle
from DTO.IADTO import IADTO
from DTO.archerDTO import archerDTO
from DTO.horsemanDTO import horsemanDTO
from DTO.soldierDTO import soldierDTO
from DTO.villagerDTO import villagerDTO
from game.batiment import Batiment
from ..Ressource import *
from .soldierIA import SoldierIA
from .horsemanIA import HorsemanIA
from.archerIA import ArcherIA
from .villagerIA import VillagerIA
from ..world import World
from ..definitions import IA_DECISION_TIME
from ..villager import Villager


class IA:

    def __init__(self,world, ressource_manager, camera, clock, team="red", strategy="attaque"):
        self.team = team
        self.world = world
        self.camera = camera
        self.towncenter = self.world.towncenterIA_tile
        self.player_towncenter = self.world.towncenter_tile
        self.ressource_manager = ressource_manager
        self.strategy=strategy
        self.evolution = 0
        self.action_faite = 0
        self.pop_vague = 0
        self.attaque_valide = 0
        self.demande_valide = 0
        self.attaque_en_cours = 0
        self.barrack_x = None
        self.barrack_y = None
        self.clock = clock 

        #Units
        self.warriors = []
        self.farmers = []
        self.villagers = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.soldiers = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.horsemen = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.archers = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]

        self.position_defense = self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy]
        self.attacking = False
        self.defending = False

        #Build
        self.number_of_buildings = 0    #Le nombre de batiments construits, qui sera réinitialisé quand on aura atteint le nombre désiré 
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
        self.number_of_buildings = 0
        self.tile = self.towncenter
        self.compteur_construction_bat = 0

        
        # SoldierIA(self.world.world[0][0], self.world,self.camera, self)
        # VillagerIA(self.world.world[1][0], self.world,self.camera, self)
        # VillagerIA(self.world.world[1+1][0], self.world,self.camera, self)
        # HorsemanIA(self.world.world[1][1], self.world,self.camera, self)
        # ArcherIA(self.world.world[2][2], self.world,self.camera, self)

        #Farm
        self.world.world[self.build_position_x][self.build_position_y]["visited"] = True
        self.x = self.build_position_x
        self.y = self.build_position_y + 1
        self.directions =cycle(["x_forwards", "y_backwards", "x_backwards", "y_forwards"])
        self.current_direction = next(self.directions)
        self.number_of_villagers_farming = 0
        self.i = 0
        self.j = 0
        self.wood_list = [] #La liste des cases arbres les plus proches du towncenter IA, trié. (Premier element c'est la case de world qui contient l'arbre le plus proche)
        self.food_list = []
        self.stone_list = []
        self.gold_list = []
        self.wood_list_iterator = iter(self.wood_list)  #Pour parcourir les cases où envoyer les villageois farm
        self.food_list_iterator = iter(self.food_list)
        self.stone_list_iterator = iter(self.stone_list)
        self.gold_list_iterator = iter(self.gold_list)
        self.init_list_ressource()

        if self.strategy=="vague": 
            self.ressource_manager.max_population += 15
            self.pop_vague = 1
            self.attaque_valide = 0
            self.demande_valide = 0
            self.attaque_en_cours = 0
            self.ressource_manager.resources["food"] = 0
        else:
            self.pop_vague = 3
    
        self.attaque_en_cours = 0
        #Events
        self.take_decision_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.take_decision_event, IA_DECISION_TIME)
        self.i = 0

        #Save
        self.villagersDTO = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.soldiersDTO = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.horsemenDTO = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.archersDTO = [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)]
        self.soldiers_save_file_path = definitions.SAVED_GAME_FOLDER + "soldiersIA"
        self.horseman_save_file_path = definitions.SAVED_GAME_FOLDER + "horsemanIA"
        self.villager_save_file_path = definitions.SAVED_GAME_FOLDER + "villagerIA"
        self.archer_save_file_path = definitions.SAVED_GAME_FOLDER + "archerIA"
        self.IA_save_file_path = definitions.SAVED_GAME_FOLDER + "IA"

        #Init
        self.restore()
        if self.villagers == [[None for x in range(self.world.grid_length_x)] for y in range(self.world.grid_length_y)] and self.strategy != "vague": VillagerIA(self.world.world[self.build_position_x - 1][self.build_position_y], self.world,self.camera, self)


    def events(self, e):    #Remplace l'update de l'IA, cette boucle est effectuée chaque X seconde pour limiter la perte d'fps
        if e.type == self.take_decision_event:
            print("Strategy", definitions.strat, "[ Wood : ", self.ressource_manager.resources["wood"], " Food : ", self.ressource_manager.resources["food"], " Gold : ", self.ressource_manager.resources["gold"],
            " ] --> evolution ", self.evolution, " <--")
            
            if self.strategy == "attaque":  
                match self.evolution:
                    
                    case 0: # 3 Villageois
                        if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                            self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                        else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        if self.get_number_of_units_IA("Villageois") >= 3:
                            self.number_of_buildings = 0
                            self.evolution += 1
                            
                    case 1: # Caserne
                        if self.get_number_of_units_IA("Villageois") < 3:
                            if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                                self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                            else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        elif self.ressource_manager.resources["wood"]>self.ressource_manager.costs["Barrack"]["wood"]and self.number_of_buildings < 1:
                            self.find_and_place_building("Barrack", 1)
                        else: self.farm(self.wood_list_iterator, self.get_number_of_units_IA("Villageois"))
                        self.compteur_construction_bat += 1 * round(self.clock.get_fps() * IA_DECISION_TIME / 1000) * definitions.EFFICIENCY*int(DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]/5)
                        if (self.action_faite == 1) and (self.compteur_construction_bat >= (dicoBatiment["Barrack"][2] + 100)):
                            self.compteur_construction_bat = 0
                            self.action_faite = 0
                            self.number_of_buildings = 0
                            self.evolution += 1

                    case 2: # 3 fermes
                        if self.get_number_of_units_IA("Villageois") < 3:
                            if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                                self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                            else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        elif self.ressource_manager.resources["wood"]>self.ressource_manager.costs["Farm"]["wood"] and self.number_of_buildings < 3:
                            self.find_and_place_building("Farm", 1)
                        else: self.farm(self.wood_list_iterator, self.get_number_of_units_IA("Villageois"))
                        self.compteur_construction_bat += 1 * round(self.clock.get_fps() * IA_DECISION_TIME / 1000) * definitions.EFFICIENCY*int(DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]/5)
                        if (self.action_faite == 1) and (self.compteur_construction_bat >= (dicoBatiment["Farm"][2] + 100)):
                            self.action_faite = 0
                            self.compteur_construction_bat = 0
                            if self.number_of_buildings >= 3:
                                self.number_of_buildings = 0
                                self.evolution += 1

                    case 3: # 3 maisons
                        if self.get_number_of_units_IA("Villageois") < 3:
                            if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                                self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                            else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        elif self.ressource_manager.resources["wood"]>self.ressource_manager.costs["House"]["wood"] and self.number_of_buildings < 3:
                            self.find_and_place_building("House", 1)
                        else: self.farm(self.wood_list_iterator, self.get_number_of_units_IA("Villageois"))
                        self.compteur_construction_bat += 1 * round(self.clock.get_fps() * IA_DECISION_TIME / 1000) * definitions.EFFICIENCY*int(DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]/5)
                        if (self.action_faite == 1) and (self.compteur_construction_bat >= (dicoBatiment["House"][2] + 200)):
                            self.action_faite = 0
                            self.compteur_construction_bat = 0
                            if self.number_of_buildings >= 3:
                                self.number_of_buildings = 0
                                self.evolution += 1

                    case 4: # 5 soldats
                        if self.get_number_of_units_IA("Villageois") < 3:
                            if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                                self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                            else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        elif self.ressource_manager.resources["food"]>self.ressource_manager.costs["Soldier"]["food"]:
                            self.spawn_unit_autour_caserne("Soldier", self.world.world[self.barrack_x][self.barrack_y])
                        else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        if self.get_number_of_units_IA("Soldier") >= 5:
                            self.number_of_buildings = 0
                            self.evolution += 1
                    
                    case 5: # récolte or pour passage age
                        if self.get_number_of_units_IA("Villageois") < 3:
                            if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                                self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                            else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        elif self.ressource_manager.resources["gold"]>=self.ressource_manager.costs["Passage_Age"]["gold"]:
                            self.passage_age_IA()
                            self.evolution +=1
                        else: self.farm(self.gold_list_iterator, self.get_number_of_units_IA("Villageois"))

                    case 6: # attaque
                        if self.get_number_of_units_IA("Villageois") < 3:
                            if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                                self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                            else: self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        elif self.get_number_of_units_IA("Soldier") >= 5 and self.get_number_of_units_IA("Horseman") >= 2:
                            if (self.get_number_of_units_joueur("Soldier") + self.get_number_of_units_joueur("horseman") + self.get_number_of_units_joueur("Archer")) !=0 :
                                self.attack_player_warriors()
                            elif self.get_number_of_units_joueur("Villageois") != 0 :
                                self.attack_villagers()
                            else: self.attack_town_center()
                            if self.ressource_manager.resources["wood"]>self.ressource_manager.costs["Farm"]["wood"]:
                                self.find_and_place_building("Farm", self.get_number_of_units_IA("Villageois"))
                            self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois")-1)
                            self.farm(self.wood_list_iterator, 1)
                        elif self.get_number_of_units_IA("Soldier") < 5 and self.ressource_manager.resources["food"]>self.ressource_manager.costs["Soldier"]["food"]:
                            self.spawn_unit_autour_caserne("Soldier", self.world.world[self.barrack_x][self.barrack_y])
                        elif self.get_number_of_units_IA("Horseman") < 2 and self.ressource_manager.resources["food"]>self.ressource_manager.costs["horseman"]["food"]:
                            self.spawn_unit_autour_caserne("horseman", self.world.world[self.barrack_x][self.barrack_y])
                        else:
                            self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))



            elif self.strategy == "blitz": 
                 match self.evolution:
                    
                    case 0:
                        if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                            self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                            self.number_of_buildings += 1
                        else: self.farm(self.food_list_iterator, 1+self.number_of_buildings)
                        if self.number_of_buildings >= 2:
                            self.number_of_buildings = 0
                            self.set_defense_pos()
                            self.evolution += 1
                            
                    case 1:
                        if self.ressource_manager.resources["wood"]>self.ressource_manager.costs["Barrack"]["wood"]and self.number_of_buildings < 1:
                            self.find_and_place_building("Barrack", 1)
                        else: self.farm(self.wood_list_iterator, 1)
                        self.compteur_construction_bat += 1 * round(self.clock.get_fps() * IA_DECISION_TIME / 1000) * definitions.EFFICIENCY*int(DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]/5)
                        if (self.action_faite == 1) and (self.compteur_construction_bat >= (dicoBatiment["Barrack"][2] + 100)):
                            self.compteur_construction_bat = 0
                            self.action_faite = 0
                            self.number_of_buildings = 0
                            self.evolution += 1

                    case 2:
                        if self.ressource_manager.resources["wood"]>self.ressource_manager.costs["House"]["wood"] and self.number_of_buildings < 3:
                            self.find_and_place_building("House", 1)
                        else: self.farm(self.wood_list_iterator, 1+self.number_of_buildings)
                        self.compteur_construction_bat += 1 * round(self.clock.get_fps() * IA_DECISION_TIME / 1000) * definitions.EFFICIENCY*int(DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]/5)
                        if (self.action_faite == 1) and (self.compteur_construction_bat >= (dicoBatiment["House"][2] + 200)):
                            self.action_faite = 0
                            self.compteur_construction_bat = 0
                            if self.number_of_buildings >= 3:
                                self.number_of_buildings = 0
                                self.evolution += 1
                    
                    case 3:
                        if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Soldier"]["food"]:
                            self.spawn_unit_autour_caserne("Soldier", self.world.world[self.barrack_x][self.barrack_y])
                        else:
                            self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        if self.get_number_of_units_IA("Villageois") < 3 and self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                            self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                        if self.get_number_of_units_IA("Soldier") >= 3:
                            self.number_of_buildings = 0
                            self.evolution += 1
                            

                    case 4:
                        self.attack_town_center()
                        if self.ressource_manager.resources["wood"]>=self.ressource_manager.costs["Farm"]["wood"]:
                            self.find_and_place_building("Farm", 1)
                        else : self.farm(self.wood_list_iterator, self.get_number_of_units_IA("Villageois"))
                        if self.get_number_of_units_IA("Soldier") == 0:
                            self.evolution +=1
                    
                    case 3:
                        if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Soldier"]["food"] and self.get_number_of_units_IA("Soldier")<self.pop_vague:
                            self.spawn_unit_autour_caserne("Soldier", self.world.world[self.barrack_x][self.barrack_y])
                        else:
                            self.farm(self.food_list_iterator, self.get_number_of_units_IA("Villageois"))
                        if self.get_number_of_units_IA("Villageois") < 3 and self.ressource_manager.resources["food"]>self.ressource_manager.costs["Villageois"]["food"]:
                            self.spawn_unit_autour_caserne("Villageois", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                        if self.get_number_of_units_IA("Soldier") >= self.pop_vague:
                                self.attaque_en_cours = 1
                                if (self.get_number_of_units_joueur("Soldier") + self.get_number_of_units_joueur("horseman") + self.get_number_of_units_joueur("Archer")) !=0 :
                                    self.attack_player_warriors()
                                elif self.get_number_of_units_joueur("Villageois") != 0 :
                                    self.attack_villagers()
                                else: self.attack_town_center()
                        if self.attaque_en_cours ==1 and self.get_number_of_units_IA("Soldier") == 0:
                            self.attaque_en_cours = 0
                            self.pop_vague += 1
                            if self.pop_vague > 8:
                                self.pop_vague = 8

            elif self.strategy == "vague":
                if self.ressource_manager.resources["food"]>self.ressource_manager.costs["Soldier"]["food"] and self.ressource_manager.population < self.pop_vague and self.attaque_en_cours == 0:
                    self.spawn_unit_autour_caserne("Soldier", self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy])
                if self.get_number_of_units_IA("Soldier") >= self.pop_vague:
                        self.attaque_en_cours = 1
                        if (self.get_number_of_units_joueur("Soldier") + self.get_number_of_units_joueur("horseman") + self.get_number_of_units_joueur("Archer")) !=0 :
                            self.attack_player_warriors()
                            print("Attaque soldat")
                        elif self.get_number_of_units_joueur("Villageois") != 0 :
                            self.attack_villagers()
                            print("Attaque Villageois")
                        else:
                            self.attack_town_center()
                            print("Attaque Forum")
                elif self.get_number_of_units_IA("Soldier") == 0 and self.attaque_en_cours == 1: 
                    self.attaque_en_cours = 0
                    if self.pop_vague < 8: self.pop_vague += 1
                    else : self.ressource_manager.resources["food"] += 60
                else: self.ressource_manager.resources["food"] += 4 + self.pop_vague
                            


     
            
            


    def find_and_place_building(self, name_of_building, number_of_buildings_to_build = 1):  #Cherche ou poser autour du Towncenter, le batiment en parametre, le nombre de batiment a poser.
        if self.get_number_of_free_units(self.villagers) != 0:  #Si le nombre de batiments qu'on a construit est inférieur au nombre désiré et si on a des villageois libre
            if self.count == self.a:
                self.count_x += 1
                self.count = 0
                self.a = next(self.odd_even)

            if  ((self.build_position_x + self.count_x * self.next_val) in range(self.world.grid_length_x) 
                    and  (self.build_position_y + self.count_y * self.next_val * self.next_val_2) in range(self.world.grid_length_y)
                    and  not self.world.world[self.build_position_x + self.count_x * self.next_val ][self.build_position_y 
                    + self.count_y * self.next_val * self.next_val_2]["collision"]
                    and (self.build_position_x + dicoBatiment[name_of_building][1])<MAP_SIZE
                    and (self.build_position_y + dicoBatiment[name_of_building][1])<MAP_SIZE):
                
                build_save = [self.build_position_x, self.build_position_y]
                self.build_position_x += self.count_x * self.next_val 
                self.build_position_y += self.count_y * self.next_val * self.next_val_2 
                self.build(name_of_building)
                self.build_position_x, self.build_position_y = build_save[0], build_save[1]

            self.count_x, self.count_y = self.count_y, self.count_x  #Switch
            self.next_val = next(self.switch_iterator)
            self.next_val_2 = next(self.switch_iterator_2)

            self.count += 1


    def build(self, name_of_building):  #Placer le batiment
        if self.build_position_x != self.towncenter["grid"][0] and self.build_position_y != self.towncenter["grid"][1] :    
            
            if dicoBatiment[name_of_building][1] == 1: #Pour taille de batiment 1x1
                ent = Batiment(self.world.world[self.build_position_x][self.build_position_y]["render_pos"], name_of_building, self.ressource_manager, team = self.team, age = self.ressource_manager.age)
                self.world.entities.append(ent)
                ent.current_image = 1   #Petite image ruine pour construction
                self.world.batiment[self.build_position_x][self.build_position_y] = ent
                self.world.world[self.build_position_x][self.build_position_y]["collision"] = True
                self.world.collision_matrix[self.build_position_y][self.build_position_x] = 0
                self.world.world[self.build_position_x][self.build_position_y]["tile"].tile_batiment = self.world.world[self.build_position_x][self.build_position_y]
                if name_of_building == "House": self.ressource_manager.max_population += 5
                self.ordre_de_construction_villageois(self.build_position_x, self.build_position_y, name_of_building)
                self.number_of_buildings += 1
                print("------------------------------------------------------------> ", name_of_building, " en construction")
                self.compteur_construction_bat = 0 # on remet à 0 le compteur pour qu'il puisse attendre le temps de construction du batiment
                

            elif self.build_position_x + 1 in range(self.world.grid_length_x) and self.build_position_y + 1 in range(self.world.grid_length_y):

                collision2 = self.world.world[self.build_position_x + 1][self.build_position_y]["collision"]
                collision3 = self.world.world[self.build_position_x + 1][self.build_position_y + 1]["collision"]
                collision4 = self.world.world[self.build_position_x ][self.build_position_y + 1]["collision"]
                if (self.build_position_x + 1 in range(self.world.grid_length_x) and self.build_position_y + 1 in range(self.world.grid_length_y) and (not collision2) and (not collision3) and (not collision4)):  # les 3 autres cases sont dispos
                    ent = Batiment(self.world.world[self.build_position_x][self.build_position_y]["render_pos"], name_of_building, self.ressource_manager, team= self.team, age = self.ressource_manager.age)
                    self.world.entities.append(ent)
                    self.world.batiment[self.build_position_x][self.build_position_y] = ent
                    for i in range (dicoBatiment[name_of_building][1]):
                        for j in range (dicoBatiment[name_of_building][1]):
                            self.world.world[self.build_position_x+i][self.build_position_y+j]["collision"] = True
                            self.world.collision_matrix[self.build_position_y+j][self.build_position_x+i] = 0
                            self.world.world[self.build_position_x + i][self.build_position_y + j]["tile"].tile_batiment = self.world.world[self.build_position_x][self.build_position_y]

                    self.ordre_de_construction_villageois(self.build_position_x, self.build_position_y, name_of_building)

                    if name_of_building == "Barrack":  # coordonnée caserne
                        self.barrack_x = self.build_position_x
                        self.barrack_y = self.build_position_y

                    self.number_of_buildings += 1
                    print("------------------------------------------------------------> ", name_of_building, " en construction")
                self.compteur_construction_bat = 0 # on remet à 0 le compteur pour qu'il puisse attendre le temps de construction du batiment
            
    def ordre_de_construction_villageois(self, grid_pos_x, grid_pos_y, nom_du_batiment): #Ordonner a un villageois de construire
        for villager_x in self.villagers:  # Pour que le villageois construise un batiment, on trouve le villageois selectionné
           for villager in villager_x:
               if (villager != None and not villager.busy):
                   villager.batiment_pv = dicoBatiment[nom_du_batiment][2]
                   villager.batiment_tile = self.world.world[grid_pos_x][grid_pos_y]   #Case ou se trouve le batiment
                   villager.create_path(villager.batiment_tile["grid"][0], villager.batiment_tile["grid"][1] , True)
                   villager.construire = True
                   villager.busy = True
                   return 0
        return 1       

    def get_number_of_free_units(self, unit_list):
        count = 0
        for unit_x in unit_list:
            for unit in unit_x:
                if unit != None and not unit.busy: count += 1
        return count

    def load_farm_list(self, ressource, ressource_list):      #Trouve en faisant le contour en spirale du towcenter les cases contenant les ressources spécifiées et les mets dans leur liste 
        self.cant_turn_anywhere = 0                             
        self.x = self.build_position_x
        self.y = self.build_position_y + 1
        self.directions =cycle(["x_forwards", "y_backwards", "x_backwards", "y_forwards"])
        self.current_direction = next(self.directions)
        while self.cant_turn_anywhere < 600:
            if self.x > self.world.grid_length_x: 
                self.x = self.world.grid_length_x - 1
                self.current_direction = next(self.directions)
            if self.y > self.world.grid_length_y: 
                self.y = self.world.grid_length_y - 1
                self.current_direction = next(self.directions)
            if self.y < 0 : 
                self.y = 0
                self.current_direction = next(self.directions)
            if self.x < 0 : 
                self.x = 0
                self.current_direction = next(self.directions)
                
            if self.x in range(0,self.world.grid_length_x) and self.y in range(0,self.world.grid_length_y):
                self.world.world[self.x][self.y]["visited"] = True

                if self.world.world[self.x][self.y ]["tile"].ressource.typeRessource == ressource:
                    if self.world.world[self.x][self.y] not in ressource_list: ressource_list.append(self.world.world[self.x][self.y])

            if self.current_direction == "x_forwards":
                if self.x + 1 in range(0,self.world.grid_length_x) and self.y -1 in range(0,self.world.grid_length_y) and not self.world.world[self.x][self.y -1]["visited"]:
                    self.current_direction = next(self.directions)
                    self.y -= 1
                    self.cant_turn_anywhere = 0 
                else: 
                    self.x += 1
                    self.cant_turn_anywhere += 1		

            elif self.current_direction == "y_backwards":
                if self.x - 1 in range(0,self.world.grid_length_x) and self.y - 1 in range(0,self.world.grid_length_y) and not self.world.world[self.x - 1][self.y ]["visited"]:
                    self.current_direction = next(self.directions)
                    self.x -= 1
                    self.cant_turn_anywhere = 0 
                else: 
                    self.y -= 1
                    self.cant_turn_anywhere += 1

            elif self.current_direction == "x_backwards":
                if self.x - 1 in range(0,self.world.grid_length_x) and self.y + 1 in range(0,self.world.grid_length_y) and not self.world.world[self.x ][self.y + 1 ]["visited"]:
                    self.current_direction = next(self.directions)
                    self.y += 1
                    self.cant_turn_anywhere = 0 
                else: 
                    self.x -= 1
                    self.cant_turn_anywhere += 1

            elif self.current_direction == "y_forwards":
                if self.x + 1 in range(0,self.world.grid_length_x) and self.y + 1 in range(0,self.world.grid_length_y) and not self.world.world[self.x + 1][self.y ]["visited"]:
                    self.current_direction = next(self.directions)
                    self.x += 1
                    self.cant_turn_anywhere = 0 
                else: 
                    self.y += 1
                    self.cant_turn_anywhere += 1

    def reset_world_visted_tiles(self):
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                self.world.world[x][y]["visited"] = False

    def init_list_ressource(self):
        self.reset_world_visted_tiles()
        self.load_farm_list("food", self.food_list) 
        self.reset_world_visted_tiles()
        self.load_farm_list("wood", self.wood_list)
        self.reset_world_visted_tiles()
        self.load_farm_list("stone", self.stone_list)
        self.reset_world_visted_tiles()
        self.load_farm_list("gold", self.gold_list)

    def farm(self, ressource_to_farm_iterator, number_of_villagers):  #Si on veut envoyer deux villageois farm du bois --> self.farm(self.wood_list_iterator, 2)    
        for villager_x in self.villagers:  # Pour que le villageois construise un batiment, on trouve le villageois selectionné
           for villager in villager_x:
               if (villager != None and not villager.busy and len(self.farmers) < number_of_villagers):
                    if self.tile["tile"].ressource.nbRessources <= 0:
                        self.tile = next(ressource_to_farm_iterator, -1)
                    if self.tile != -1:
                        # print("here",tile["grid"][0], tile["grid"][1] )
                        villager.create_path(self.tile["grid"][0], self.tile["grid"][1], True)
                        villager.busy = True
                        self.farmers.append(villager)

    def passage_age_IA(self):
        self.ressource_manager.age = "2"
        if self.ressource_manager.is_affordable("Passage_Age"):
            self.ressource_manager.apply_cost_to_resource("Passage_Age")
            for batiment in self.world.entities:
                if isinstance(batiment, Batiment):
                    print("Ageing up!")
                    if batiment.team == self.team:
                        batiment.load_Age2_images()                    

    def spawn_unit_autour_caserne(self, unit_name, tile): #On lui fournit la case de la caserne ou batiment 2x2 et il s'occupe de spawn autour
        if self.ressource_manager.population < self.ressource_manager.max_population:
            if (not self.world.world[tile["grid"][0] ][tile["grid"][1] + 2]["collision"]):
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] ][tile["grid"][1] + 2], self, self.camera, self) 
                    VillagerIA(self.world.world[tile["grid"][0] ][tile["grid"][1] + 2], self.world, self.camera, self) 
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] ][tile["grid"][1] + 2], self.world, self.camera, self) 
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] ][tile["grid"][1] + 2], self.world, self.camera)
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] ][tile["grid"][1] + 2], self.world, self.camera)
            
            elif (not self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 2]["collision"]):
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 2], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] + 1 ], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] -1 ][tile["grid"][1] ]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] ], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] ], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] ], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] ], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] -1 ][tile["grid"][1] ], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0]  -1 ][tile["grid"][1] - 1], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] ][tile["grid"][1] - 1]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] ][tile["grid"][1] - 1], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] ][tile["grid"][1] - 1], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] +1 ][tile["grid"][1] - 1]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] - 1], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] -1 ], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] +2 ][tile["grid"][1] ]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] ], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] ], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] ], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] ], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] ], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self, self.camera)
                    VillagerIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +1 ], self.world, self.camera)
            
            elif not self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] +2 ][tile["grid"][1] +2 ], self.world, self.camera)

            elif not self.world.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ]["collision"]:
                if unit_name == "Villageois":
                    #Worker(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self, self.camera, self)    
                    VillagerIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self.world, self.camera, self)    
                if unit_name == "Soldier":
                    SoldierIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self.world, self.camera, self)    
                if unit_name == "horseman":
                    HorsemanIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self.world, self.camera, self)    
                if unit_name == "Archer":
                    ArcherIA(self.world.world[tile["grid"][0] +1 ][tile["grid"][1] +2 ], self.world, self.camera)



    def attack_villagers(self):
        self.attacking = True
        self.defending = False
        for villager_x in self.world.villager:
            for villager in villager_x:
                for w in self.warriors:
                    if villager is not None and w is not None:
                        if w.attack == False :
                                w.create_path(villager.tile["grid"][0],villager.tile["grid"][1])
    
    def test_attack_villagers(self):
        a=0
        for villager_x in self.world.villager:
            for villager in villager_x:
                for w in self.warriors:
                    if villager is not None and w is not None:
                        self.demande_valide = 1
                        a=1
        if a == 0:
            self.demande_valide = 0
                        



    def attack_player_warriors(self):
            self.attacking = True
            self.defending = False
            for unit_x in self.world.unites:
                for unit in unit_x:
                    for w in self.warriors:
                        if unit is not None and w is not None and isinstance(unit,Villager) == False:
                            if w.attack == False: # pour attaquer unités une par une sans appeller create path en boucle
                                if unit.team == "blue":
                                    w.create_path(unit.tile["grid"][0], unit.tile["grid"][1]) # attaquer la premiere unités sachant que

    
    def test_attack_player_warriors(self):
        a=0
        for unit_x in self.world.unites:
            for unit in unit_x:
                for w in self.warriors:
                    if unit is not None and w is not None and isinstance(unit,Villager) == False:
                            if unit.team == "blue":
                                    self.demande_valide = 1
                                    a=1
        if a == 0:
            self.demande_valide = 0



    def attack_town_center(self):
        self.attacking = True
        self.defending = False
        for w in self.warriors:
            #print(1)
            if self.world.batiment[self.player_towncenter["grid"][0]][self.player_towncenter["grid"][1]] is not None and w is not None:
                #print(2)
                if self.world.batiment[self.player_towncenter["grid"][0]][self.player_towncenter["grid"][1]].pv > 0:
                    if self.world.batiment[self.player_towncenter["grid"][0]][self.player_towncenter["grid"][1]].team != w.team and w.attack_bati == False:
                        w.create_path(self.player_towncenter["grid"][0], self.player_towncenter["grid"][1])


    def attack_caserne(self):
        pass


    def attack_house(self):
        pass


    #def annul_attack(self):
        #for w in self.warriors:
            #if w.attack == True:
                #w.attack = False
                #self.attacking = False


    def defend_base(self):
        if self.defending == True:
            for x in range(self.world.grid_length_x):
                for y in range(self.world.grid_length_y):
                    if self.world.batiment[x][y] and self.world.batiment[x][y].team == self.team:
                        if dicoBatiment[self.world.batiment[x][y].name][1] == 2:
                            if self.world.unites[x+2][y] != None and self.world.unites[x+2][y].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+2][y] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+2][y].tile["grid"][0],self.world.unites[x+2][y].tile["grid"][1])

                            if self.world.unites[x+2][y+1] != None and self.world.unites[x+2][y+1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+2][y+1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+2][y+1].tile["grid"][0],self.world.unites[x+2][y+1].tile["grid"][1])

                            if self.world.unites[x+2][y+2] != None and self.world.unites[x+2][y+2].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+2][y+2] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+2][y+2].tile["grid"][0],self.world.unites[x+2][y+2].tile["grid"][1])

                            if self.world.unites[x+1][y+2] != None and self.world.unites[x+1][y+2].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+1][y+2] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+1][y+2].tile["grid"][0],self.world.unites[x+1][y+2].tile["grid"][1])

                            if self.world.unites[x][y+2] != None and self.world.unites[x][y+2].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x][y+2] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x][y+2].tile["grid"][0],self.world.unites[x][y+2].tile["grid"][1])

                            if self.world.unites[x-1][y+2] != None and self.world.unites[x-1][y+2].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x-1][y+2] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x-1][y+2].tile["grid"][0],self.world.unites[x-1][y+2].tile["grid"][1])

                            if self.world.unites[x-1][y+1] != None and self.world.unites[x-1][y+1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x-1][y+1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x-1][y+1].tile["grid"][0],self.world.unites[x-1][y+1].tile["grid"][1])

                            if self.world.unites[x-1][y] != None and self.world.unites[x-1][y].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x-1][y] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x-1][y].tile["grid"][0],self.world.unites[x-1][y].tile["grid"][1])

                            if self.world.unites[x-1][y-1] != None and self.world.unites[x-1][y-1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x-1][y-1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x-1][y-1].tile["grid"][0],self.world.unites[x-1][y-1].tile["grid"][1])


                            if self.world.unites[x][y-1] != None and self.world.unites[x][y-1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x][y-1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x][y-1].tile["grid"][0],self.world.unites[x][y-1].tile["grid"][1])

                            if self.world.unites[x+1][y-1] != None and self.world.unites[x+1][y-1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+1][y-1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+1][y-1].tile["grid"][0],self.world.unites[x+1][y-1].tile["grid"][1])

                            if self.world.unites[x+2][y-1] != None and self.world.unites[x+2][y-1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+2][y-1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+2][y-1].tile["grid"][0],self.world.unites[x+2][y-1].tile["grid"][1])

                        if dicoBatiment[self.world.batiment[x][y].name][1] == 2:
                            if self.world.unites[x+1][y] != None and self.world.unites[x+1][y].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+1][y] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+1][y].tile["grid"][0],self.world.unites[x+1][y].tile["grid"][1])

                            if self.world.unites[x+1][y+1] != None and self.world.unites[x+1][y+1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+1][y+1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+1][y+1].tile["grid"][0],self.world.unites[x+1][y+1].tile["grid"][1])

                            if self.world.unites[x][y+1] != None and self.world.unites[x ][y+1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x][y+1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x][y+1].tile["grid"][0],self.world.unites[x][y+1].tile["grid"][1])

                            if self.world.unites[x-1][y] != None and self.world.unites[x-1][y].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x-1][y] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x-1][y].tile["grid"][0],self.world.unites[x-1][y].tile["grid"][1])

                            if self.world.unites[x-1][y-1] != None and self.world.unites[x-1][y-1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x-1][y-1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x-1][y-1].tile["grid"][0],self.world.unites[x-1][y-1].tile["grid"][1])

                            if self.world.unites[x][y-1] != None and self.world.unites[x][y-1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x][y-1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x][y-1].tile["grid"][0],self.world.unites[x][y-1].tile["grid"][1])

                            if self.world.unites[x+1][y-1] != None and self.world.unites[x+1][y-1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+1][y-1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x+1][y-1].tile["grid"][0],self.world.unites[x+1][y-1].tile["grid"][1])

                            if self.world.unites[x-1][y+1] != None and self.world.unites[x-1][y+1].team != self.team:
                                for w in self.warriors:
                                    if self.world.unites[x+1][y+1] and w:
                                        if w.attack == False:  # pour attaquer unités une par une sans appeller create path en boucle
                                            w.create_path(self.world.unites[x-1][y+1].tile["grid"][0],self.world.unites[x-1][y+1].tile["grid"][1])

    def set_defense_pos(self): # Lilian remet i et j à 0 à chaque prochaine évolution stp
        self.attacking = False
        self.defending = True
        if self.world.towncenter_IA_posx < 25 and self.world.towncenter_IA_posy < 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx + 2][self.world.towncenter_IA_posy + 2]
            for w in self.warriors:
                if self.world.world[self.position_defense["grid"][0] + self.i][self.position_defense["grid"][1] + self.j]["collision"] == False:
                    if w.dest_tile == 0:
                        w.create_path(self.position_defense["grid"][0] + self.i,self.position_defense["grid"][1] + self.j)
                        self.j += 1
                        self.i += 1



        if self.world.towncenter_IA_posx > 25 and self.world.towncenter_IA_posy < 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx - 2 ][self.world.towncenter_IA_posy + 2]
            for w in self.warriors:
                if self.world.world[self.position_defense["grid"][0] - self.i][self.position_defense["grid"][1] + self.j]["collision"] == False:
                    if w.dest_tile == 0:
                        w.create_path(self.position_defense["grid"][0] - self.i,self.position_defense["grid"][1] + self.j)
                        self.j += 1
                        self.i += 1

        if self.world.towncenter_IA_posx < 25 and self.world.towncenter_IA_posy > 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx + 2][self.world.towncenter_IA_posy - 2]
            for w in self.warriors:
                if self.world.world[self.position_defense["grid"][0] + self.i][self.position_defense["grid"][1] - self.j]["collision"] == False:
                    if w.dest_tile == 0:
                        w.create_path(self.position_defense["grid"][0] + self.i,self.position_defense["grid"][1] - self.j)
                        self.j += 1
                        self.i += 1

        if self.world.towncenter_IA_posx > 25 and self.world.towncenter_IA_posy > 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx - 2][self.world.towncenter_IA_posy - 2]
            for w in self.warriors:
                if self.world.world[self.position_defense["grid"][0] - self.i][self.position_defense["grid"][1] - self.j]["collision"] == False:
                    if w.dest_tile == 0:
                        w.create_path(self.position_defense["grid"][0] - self.i,self.position_defense["grid"][1] -self.j)
                        self.j += 1
                        self.i += 1

    def get_number_of_units_joueur(self, unit_name):
        count = 0
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                if unit_name == "Villageois":
                    if self.world.villager[x][y] != None:
                        count += 1
                if unit_name == "Soldier":
                    if self.world.soldier[x][y] != None:
                        count += 1   
                if unit_name == "Horseman":
                    if self.world.horseman[x][y] != None:
                        count += 1   
                if unit_name == "Archer":
                    if self.world.archer[x][y] != None:
                        count += 1    
        return count    

    def get_number_of_units_IA(self, unit_name):
        count = 0
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                if unit_name == "Villageois":
                    if self.villagers[x][y] != None:
                        count += 1
                if unit_name == "Soldier":
                    if self.soldiers[x][y] != None:
                        count += 1   
                if unit_name == "Horseman":
                    if self.horsemen[x][y] != None:
                        count += 1   
                if unit_name == "Archer":
                    if self.archers[x][y] != None:
                        count += 1    
        return count                                 


    def save(self):
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
            
                if self.soldiers[x][y] != None:
                    currentsoldier = self.soldiers[x][y]
                    self.world.collision_matrix[currentsoldier.tile["grid"][1]][currentsoldier.tile["grid"][0]] = 1
                    self.world.world[currentsoldier.tile["grid"][0]][currentsoldier.tile["grid"][1]]["collision"] = False
                    self.soldiersDTO[x][y] = soldierDTO(currentsoldier.name,currentsoldier.pv,currentsoldier.range,currentsoldier.dmg,currentsoldier.tile)
                
                if self.horsemen[x][y] != None:
                    currenthorseman = self.horsemen[x][y]
                    self.world.collision_matrix[currenthorseman.tile["grid"][1]][currenthorseman.tile["grid"][0]] = 1
                    self.world.world[currenthorseman.tile["grid"][0]][currenthorseman.tile["grid"][1]]["collision"] = False
                    self.horsemenDTO[x][y] = horsemanDTO(currenthorseman.name,currenthorseman.pv,currenthorseman.range,currenthorseman.dmg,currenthorseman.tile)
                
                if self.villagers[x][y] != None:
                    currentvillager = self.villagers[x][y]
                    self.world.collision_matrix[currentvillager.tile["grid"][1]][currentvillager.tile["grid"][0]] = 1
                    self.world.world[currentvillager.tile["grid"][0]][currentvillager.tile["grid"][1]]["collision"] = False
                    self.villagersDTO[x][y] = villagerDTO(currentvillager.name,currentvillager.pv,currentvillager.range,currentvillager.dmg,currentvillager.tile)
                
                if self.archers[x][y] != None:
                    currentarcher = self.archers[x][y]
                    self.world.collision_matrix[currentarcher.tile["grid"][1]][currentarcher.tile["grid"][0]] = 1
                    self.world.world[currentarcher.tile["grid"][0]][currentarcher.tile["grid"][1]]["collision"] = False
                    self.archersDTO[x][y] = archerDTO(currentarcher.name,currentarcher.pv,currentarcher.range,currentarcher.dmg,currentarcher.tile) 

        try:   #IA save
            with open(self.IA_save_file_path, "wb") as output:
                IA_dto = IADTO(self.team, self.strategy, self.pop_vague, self.attaque_valide, self.demande_valide, self.attaque_en_cours, self.evolution, self.number_of_buildings, self.action_faite, self.compteur_construction_bat, self.barrack_x, self.barrack_y, self.world.towncenter_IA_posx, self.world.towncenter_IA_posy)
                pickle.dump(IA_dto,output)
                output.close()
        except Exception as e: print("Couldnt dump IA save in file", e)

        try:   #Soldier save
            with open(self.soldiers_save_file_path, "wb") as output:
                pickle.dump(self.soldiersDTO,output)
                output.close()
        except: print("Couldnt dump soldiers IA save in file") 

        try:   #horseman save
            with open(self.horseman_save_file_path, "wb") as output:
                pickle.dump(self.horsemenDTO,output)
                output.close()
        except: print("Couldnt dump horseman IA save in file")   
        
        try:   #villager save
            with open(self.villager_save_file_path, "wb") as output:
                pickle.dump(self.villagersDTO,output)
                output.close()
        except: print("Couldnt dump villager IA save in file") 
        
        try:   #archer save
            with open(self.archer_save_file_path, "wb") as output:
                pickle.dump(self.archersDTO,output)
                output.close()
        except: print("Couldnt dump archer IA save in file") 

    def restore(self):
        
        #IA restore
        try:    
            with open(self.IA_save_file_path, "rb") as input:
                restore_IA_dto = pickle.load(input)
                self.team = restore_IA_dto.team
                self.strategy = restore_IA_dto.strategy
                self.pop_vague = restore_IA_dto.pop_vague
                self.attaque_valide = restore_IA_dto.attaque_valide
                self.demande_valide = restore_IA_dto.demande_valide
                self.attaque_en_cours = restore_IA_dto.attaque_en_cours
                self.evolution = restore_IA_dto.evolution
                self.number_of_buildings = restore_IA_dto.number_of_buildings
                self.action_faite = restore_IA_dto.action_faite
                self.compteur_construction_bat = restore_IA_dto.compteur_construction_bat
                self.barrack_x = restore_IA_dto.barrack_x
                self.barrack_y = restore_IA_dto.barrack_y
                self.world.towncenter_IA_posx = restore_IA_dto.towncenter_IA_posx
                self.world.towncenter_IA_posy = restore_IA_dto.towncenter_IA_posy
                
                input.close()
        except Exception as e: print("An error occured while loading IA save:", e)

        try:    
            with open(self.soldiers_save_file_path, "rb") as input:
                restore_soldiers_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_soldiers_dto[x][y] != None:
                            currentsoldierDTO = restore_soldiers_dto[x][y]
                            SoldierIA(currentsoldierDTO.tile,self.world,self.camera,self, pv=currentsoldierDTO.pv)
                            self.ressource_manager.apply_cost_to_resource("Soldier", -1)
        
        except Exception as e: print("An error occured while loading soldier IA save:", e)


        try:    
            with open(self.horseman_save_file_path, "rb") as input:
                restore_horseman_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_horseman_dto[x][y] != None:
                            currenthorsemanDTO = restore_horseman_dto[x][y]
                            HorsemanIA(currenthorsemanDTO.tile,self.world,self.camera, self, currenthorsemanDTO.pv)
                            self.ressource_manager.apply_cost_to_resource("horseman", -1)
                
        except Exception as e: print("An error occured while loading horseman IA save:", e)
    
        
        try:    
            with open(self.villager_save_file_path, "rb") as input:
                restore_villager_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_villager_dto[x][y] != None:
                            currentvillagerDTO = restore_villager_dto[x][y]
                            VillagerIA(currentvillagerDTO.tile,self.world,self.camera, self, currentvillagerDTO.pv)
                            self.ressource_manager.apply_cost_to_resource("Villageois", -1)
        
        except Exception as e: print("An error occured while loading villager IA save:", e)
        
        
        try:    
            with open(self.archer_save_file_path, "rb") as input:
                restore_archer_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_archer_dto[x][y] != None:
                            currentarcherDTO = restore_archer_dto[x][y]
                            ArcherIA(currentarcherDTO.tile,self.world,self.camera, self, currentarcherDTO.pv)
                            self.ressource_manager.apply_cost_to_resource("Archer", -1)

        except Exception as e: print("An error occured while loading archer IA save:", e)

    def attack_batiment_IA(self,name):
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                if self.world.batiment[x][y] and self.world.batiment[x][y].name == name:
                    for w in self.warriors:
                        if w is not None and self.world.batiment[x][y] is not None:
                            if w.attack_bati == False :
                                w.create_path(x,y)


    #def menace_tonwcenter(self):
        #for unit_x in self.world.unites:
            #for unit in unit_x:
                #for w in self.warriors:
                    #if unit is not None and w is not None and isinstance(unit, Villager) == False:
                        #if distance(unit,towncenter) < 3:
                            #if unit is not None and w is not None:
                                #w.create_path(unit.tile["grid"][0],unit.tile["grid"][1])
                            #if unit.pv < 0:
                                #self.set_defense_pos()


    #def distance(self,tile1,tile2):



