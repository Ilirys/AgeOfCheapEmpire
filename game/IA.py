from pygame import *
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
        self.towncenter = self.world.world[self.world.a2][self.world.b2]
        self.player_towncenter = self.world.world[self.world.a][self.world.b]
        self.warriors = []
        self.villagers = []
        self.attacking = False



    def update(self):
        self.attack_villagers()
        pass

    def attack_villagers(self):
        for villager_x in self.world.villager:
            for villager in villager_x:
                for w in self.warriors:
                    if villager is not None and w is not None:
                        if villager.team != w.team:
                            if w.attack == False :
                                if w.cible == 0 :
                                    w.create_path(villager.tile["grid"][0],villager.tile["grid"][1])
                                elif w.cible.isDead and self.world.villager :
                                    w.create_path(villager.tile["grid"][0], villager.tile["grid"][1])

    def attack_player_warriors(self):
            for unit_x in self.world.unites_combat:
                for unit in unit_x:
                    for w in self.warriors:
                        if unit is not None and w is not None:
                           if unit.team != w.team:
                                #print(unit.team)
                                if w.attack == False: # pour attaquer unités une par une sans appeller create path en boucle
                                    if w.cible == 0:
                                        w.create_path(unit.tile["grid"][0], unit.tile["grid"][1]) # attaquer la premiere unités sachant que
                                    elif w.cible.isDead and unit.tile != w.tile and unit.team != w.team:
                                        w.create_path(unit.tile["grid"][0], unit.tile["grid"][1])
                                        print(1)


    def attack_town_center(self):
        for w in self.warriors:
            if self.player_towncenter is not None and w is not None:
                if self.player_towncenter.pv > 0:
                    if self.world.batiment[self.world.a][self.world.b].team != w.team and w.attack == False:
                        w.create_path(self.player_towncenter["grid"][0], self.player_towncenter["grid"][1])



        pass

    def defend_town_center(self):
        pass