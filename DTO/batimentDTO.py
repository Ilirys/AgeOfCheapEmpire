import pygame 

class TowncenterDTO: 
 
    def __init__(self, pos, pv, current_image): 
        self.pos = pos
        self.name = "Towncenter"
        self.pv = pv
        self.current_image = current_image
        
class HouseDTO: 
 
    def __init__(self, pos, pv, current_image): 
        self.pos = pos
        self.name = "House"
        self.pv = pv
        self.current_image = current_image

class BarrackDTO: 
 
    def __init__(self, pos, pv, current_image): 
        self.pos = pos
        self.name = "Barrack"
        self.pv = pv
        self.current_image = current_image

class StorageDTO:
 
    def __init__(self, pos, pv, current_image): 
        self.pos = pos
        self.name = "Storage"
        self.pv = pv
        self.current_image = current_image

class FarmDTO:
 
    def __init__(self, pos, pv, current_image): 
        self.pos = pos
        self.name = "Farm"
        self.pv = pv
        self.current_image = current_image