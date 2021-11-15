
from .definitions import *

class Ressource:

    def __init__(self, *args):
        if(len(args)==0):
            self.nbRessources = 0
            self.typeRessource = ""
        elif(len(args)==2):
            self.nbRessources = args[0]
            self.typeRessource = args[1]
        
        # resources
        self.resources = {
            "wood": INIT_RESSOURCE[0],
            "food": INIT_RESSOURCE[1],
            "gold": INIT_RESSOURCE[2],
            "stone": INIT_RESSOURCE[3]
        }

        #costs
        self.costs = {
            "Towncenter": {},
            "House": {"wood": 25},
            "Barrack": {"wood": 175}
        }

    def getTypeRessource(self):
        return self.typeRessource

    def getNbRessources(self):
        return self.nbRessources

    def setTypeRessource(self, typeRess):
        self.typeRessource = typeRess

    def setNbRessources(self, nbRess):
        self.nbRessources = nbRess


    def apply_cost_to_resource(self, building):
        for resource, cost in self.costs[building].items():
            self.resources[resource] -= cost

    def is_affordable(self, building):
        affordable = True
        for resource, cost in self.costs[building].items():
            if cost > self.resources[resource]:
                affordable = False
        return affordable