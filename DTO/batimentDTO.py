import pygame 

class TowncenterDTO: 
 
    def __init__(self, pos, pv, current_image,team="blue"): 
        self.pos = pos
        self.name = "Towncenter"
        self.pv = pv
        self.current_image = current_image
        self.team = team
        
class HouseDTO: 
 
    def __init__(self, pos, pv, current_image,team="blue"): 
        self.pos = pos
        self.name = "House"
        self.pv = pv
        self.current_image = current_image
        self.team = team

class BarrackDTO: 
 
    def __init__(self, pos, pv, current_image,team="blue"): 
        self.pos = pos
        self.name = "Barrack"
        self.pv = pv
        self.current_image = current_image
        self.team = team

class StorageDTO:
 
    def __init__(self, pos, pv, current_image,team="blue"): 
        self.pos = pos
        self.name = "Storage"
        self.pv = pv
        self.current_image = current_image
        self.team = team

class FarmDTO:
 
    def __init__(self, pos, pv, current_image,team="blue"): 
        self.pos = pos
        self.name = "Farm"
        self.pv = pv
        self.current_image = current_image
        self.team = team