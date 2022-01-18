"""from pygame import *
from .Ressource import Ressource
from .soldierIA import SoldierIA
from .horsemanIA import HorsemanIA
from.archerIA import ArcherIA
from .villagerIA import VillagerIA
from .world import World


class IA:

    def __init__(self,world,team="red"):
        self.team = team
        self.world = world
        self.towncenter = self.world.batiment[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy]
        self.player_towncenter = self.world.batiment[self.world.towncenter_posx][self.world.towncenter_posy]
        self.warriors = []
        self.villagers = []
        self.attacking = False
        self.ressource_manager = Ressource()
        self.position_defense = self.world.world[self.world.towncenter_IA_posx][self.world.towncenter_IA_posy]



    def update(self):
        self.attack_town_center()
        pass

    def attack_villagers(self):
        self.attacking = True
        for villager_x in self.world.villager:
            for villager in villager_x:
                for w in self.warriors:
                    if villager is not None and w is not None:
                        if w.attack == False :
                            if w.cible == 0 :
                                w.create_path(villager.tile["grid"][0],villager.tile["grid"][1])
                            elif w.cible.isDead and self.world.villager :
                                w.create_path(villager.tile["grid"][0], villager.tile["grid"][1])


    def attack_player_warriors(self):
            self.attacking = True
            for unit_x in self.world.unites_combat:
                for unit in unit_x:
                    for w in self.warriors:
                        if unit is not None and w is not None:
                            #print(unit.team)
                            if w.attack == False: # pour attaquer unités une par une sans appeller create path en boucle
                                if w.cible == 0:
                                    w.create_path(unit.tile["grid"][0], unit.tile["grid"][1]) # attaquer la premiere unités sachant que
                                elif w.cible.isDead and self.world.unites_combat:
                                    w.create_path(unit.tile["grid"][0], unit.tile["grid"][1])
                                    print(1)


    def attack_town_center(self):
        self.attacking = True
        for w in self.warriors:
            #print(1)
            if self.player_towncenter is not None and w is not None:
                #print(2)
                if self.player_towncenter.pv > 0:
                    if self.player_towncenter.team != w.team and w.attack_bati == False:
                        w.create_path(self.world.towncenter_posx, self.world.towncenter_posy)
                        print(w.cible.pv)



    def annul_attack(self):
        for w in self.warriors:
            if w.attack == True:
                w.attack = False
                self.attacking = False

    def defend_town_center(self):
        for w in self.warriors:
            for i in range (len(self.warriors)) :
                w.create_path(self.position_defense["grid"][0]+i,self.position_defense["grid"][1])
                if self.world.world[self.position_defense["grid"][0]+i][self.position_defense["grid"][1]]["collision"]:
                    w.create_path(self.position_defense["grid"][0], self.position_defense["grid"][1]+i)




    def set_defense_pos(self):
        if self.world.towncenter_IA_posx < 25 and self.world.towncenter_IA_posy < 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx + 2][self.world.towncenter_IA_posy + 2]

        if self.world.towncenter_IA_posx > 25 and self.world.towncenter_IA_posy < 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx + 2][self.world.towncenter_IA_posy + 2]

        if self.world.towncenter_IA_posx < 25 and self.world.towncenter_IA_posy < 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx + 2][self.world.towncenter_IA_posy + 2]

        if self.world.towncenter_IA_posx < 25 and self.world.towncenter_IA_posy < 25:
            self.position_defense = self.world.world[self.world.towncenter_IA_posx + 2][self.world.towncenter_IA_posy + 2]"""

