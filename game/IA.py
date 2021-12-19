from pygame import *
from .Ressource import Ressource
from .soldierIA import SoldierIA
from .horsemanIA import HorsemanIA
from.archerIA import ArcherIA
from .villagerIA import VillagerIA


class IA:

    def __init__(self,team):
        self.team = team
        self.ressource_manager = Ressource()



    def update(self):
        pass
