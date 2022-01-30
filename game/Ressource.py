import game.definitions as definitions
from .definitions import *
import pickle
class Ressource:

    def __init__(self, *args, team="blue", max_population= definitions.PLAYER_POPULATION, age=""):

        self.team=team
        self.max_population = max_population
        self.population = 0
        self.age = age
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
            "Barrack": {"wood": 175},
            "Storage": {"wood": 100},
            "Farm": {"wood": 60},
            "Villageois": {"food": 50},
            "Soldier": {"food": 17},
            "horseman": {"food": 17},
            "Archer": {"food": 17},
            "BIGDADDY": {"food": 30},
            "Passage_Age": {"gold": 1500},
            "Towncenter2": {},
            "House2": {"wood": 25},
            "Barrack2": {"wood": 175},
            "Storage2": {"wood": 100},
            "Farm2": {"wood": 200},
        }

        #Save
        self.save_file_path = definitions.SAVED_GAME_FOLDER + "ressourceManager" + str(self.team)

    def getTypeRessource(self):
        return self.typeRessource

    def getNbRessources(self):
        return self.nbRessources

    def setTypeRessource(self, typeRess):
        self.typeRessource = typeRess

    def setNbRessources(self, nbRess):
        self.nbRessources = nbRess


    def apply_cost_to_resource(self, building, add=1):
        for resource, cost in self.costs[building].items():
            self.resources[resource] -= cost * add

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
                self.max_population = res_manager.max_population
                self.age = res_manager.age
                input.close()
        except Exception as e: print("An error occured while loading resource save:", e)

        

    def save(self):
        try:    
            with open(self.save_file_path, "wb") as output:
                pickle.dump(self,output)
                output.close()
        except: print("Couldnt dump resource save in file") 
