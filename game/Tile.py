from .Ressource import Ressource
class Tile:
    '''
    xTile : position sur axe des X
    yTile : position sur axe des Y
    empty : permet de savoir si il y a un batiment ou une ressource sur la case
    ressource : définie la ressource sur la case
    idElem : définie l'ID de l'élément sur la case
    '''

    #Constructeur sans parametre qui initialise tous les attributs
    def __init__(self, *args):
        if(len(args)==0):
            self.xTile = 0
            self.yTile = 0
            self.empty = True
            self.ressource = Ressource.__init__()
            self.idElem = -1
            self.nomElement = ""
            self.tile_batiment = 0
        elif(len(args)==5):
            self.xTile = args[0]
            self.yTile = args[1]
            self.empty = args[2]
            self.ressource = args[3]
            self.idElem = args[4]
            self.nomElement = ""

    def isEmpty(self):
        return self.empty

    def getRessource(self):
        return self.ressource

    def setRessource(self, ressource):
        self.ressource = ressource

    def reduceRessource(self, nbRessources):
        self.ressource = self.ressource - nbRessources

    def setEmpty(self,empty):
        self.empty = empty

    def setIdElement(self,idElem):
        self.idElem = idElem

    def getIdElement(self):
        return self.idElem