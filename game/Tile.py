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
    def __init__(self, xTile=0, yTile=0, empty=True, ressource="", id=-1, visible= False):
        self.xTile = xTile
        self.yTile = yTile
        self.empty = empty
        self.ressource = ressource
        self.idElem = id
        self.nomElement = ""
        self.tile_batiment = 0
        self.batiment_pv = None
        self.visible = False
        self.cpt = 0 # permet de savoir si le fog of war est dicipé 0= non 1 = oui (pas sûr de l'utilité)
        self.visibleIA = False


    def getCpt(self):
        return self.cpt

    def addCpt(self):
        self.cpt = 1

    def setVisible(self, monVisible):
        self.visible = monVisible

    def getVisible(self):
        return self.visible

    def setVisibleIA(self, monVisible):
        self.visibleIA = monVisible

    def getVisibleIA(self):
        return self.visibleIA

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