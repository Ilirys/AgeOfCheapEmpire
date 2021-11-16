
from .definitions import *
import pickle
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

        #Save
        self.save_file_path = SAVED_GAME_FOLDER + "ressourceManager"

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

    def restore_save(self):
        try:    
            with open(self.save_file_path, "rb") as input:
                res_manager = pickle.load(input)
                self.costs = res_manager.costs
                self.resources = res_manager.resources
                self.nbRessources = res_manager.nbRessources
                self.typeRessource = res_manager.typeRessource
                print(self.resources["wood"])
                input.close()
        except: 
            print("Created file")
        

    def save(self):
        try:    
            with open(self.save_file_path, "wb") as output:
                pickle.dump(self,output)
                output.close()
        except: print("Couldnt dump in file") 
