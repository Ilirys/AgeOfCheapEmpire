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
        self.towncenter = None
        self.player_towncenter = None
        self.warriors = []
        self.villagers = []
        self.attacking = False



    def update(self):
        self.attack_villagers()
        pass

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


    def attack_player_warriors(self):
        if self.attacking == False:
            for unit_x in self.world.units:
                for unit in unit_x:
                    if unit not in self.world.villager:
                        for w in self.warriors:
                            if unit is not None and w is not None:
                                if unit.team != w.team:
                                    w.create_path(unit.tile["grid"][0], unit.tile["grid"][1])
                                    self.attacking = True  # pour attaquer unités une par une sans appeller create path en boucle
                                    if unit.pv < 0 or w.dest_tile == w.tile:
                                        self.attacking = False

    def attack_town_center(self):
        for w in self.warriors:
            if self.player_towncenter is not None and w is not None:
                if self.player_towncenter.team != w.team:
                    w.create_path(self.player_towncenter.tile["grid"][0], self.player_towncenter.tile["grid"][1])
                    self.attacking = True  # pour attaquer unités une par une sans appeller create path en boucle
                    if self.player_towncenter.pv < 0 or w.dest_tile == w.tile:
                        self.attacking = False
        pass

    def defend_town_center(self):
        pass