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
        #self.towncenter =
        # self.player_towncenter =
        self.warriors = []
        self.villagers = []
        self.attacking = False


    def update(self):
        pass


    def attack_villagers(self):
        if self.attacking == False:
            for y in self.world.villager:
                for x in y:
                    for w in self.warriors:
                        if v.team != w.team:
                            w.create_path(x,y)
                            self.attacking = True          # pour attaquer unités une par une sans appeller create path en boucle
                            if self.world.villager[x][y].pv < 0 or w.dest_tile == w.tile:
                                self.attacking = False