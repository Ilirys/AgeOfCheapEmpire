
from .definitions import LES_RESSOURCES as ress

class Ressource:

    def __init__(self, *args):
        if(len(args)==0):
            self.nbRessources = 0
            self.typeRessource = ""
        elif(len(args)==2):
            self.nbRessources = args[0]
            self.typeRessource = args[1]
    def getTypeRessource(self):
        return self.typeRessource

    def getNbRessources(self):
        return self.nbRessources

    def setTypeRessource(self, typeRess):
        self.typeRessource = typeRess

    def setNbRessources(self, nbRess):
        self.nbRessources = nbRess