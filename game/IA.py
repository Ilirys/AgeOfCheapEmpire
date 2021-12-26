from pygame import *
from .Ressource import Ressource
from .soldierIA import SoldierIA
from .horsemanIA import HorsemanIA
from.archerIA import ArcherIA
from .villagerIA import VillagerIA
from .world import World


class IA:

    def __init__(self,team):
        self.team = team
        self.player_towncenter = 0
        self.warriors = []
        self.villagers = []



    def update(self):
        pass
    