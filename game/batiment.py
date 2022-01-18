import pygame 
from .definitions import *

class Batiment:
    
    def __init__(self, pos, name, resource_manager, pv=0, current_image=0, team="blue", age=""):
        #Images
        self.name = name + age
        self.image = pygame.image.load(dicoBatiment[self.name][0]).convert_alpha()
        self.ruin_image = pygame.image.load("assets/Rubble1.png").convert_alpha()
        self.small_ruin_image = pygame.image.load("assets/RubbleSmall.png").convert_alpha()
        self.current_image = current_image
        self.images = [self.ruin_image, self.small_ruin_image, self.image]

        self.pos = pos 
        self.taille = dicoBatiment[self.name][1]
        self.pv = pv
        self.pv_max = dicoBatiment[self.name][2]
        self.team = team
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_cooldown = pygame.time.get_ticks()
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)

    def update(self):
        
        if self.name == "Farm":
            now = pygame.time.get_ticks()
            if (now - self.resource_cooldown) > 2000:
                self.resource_manager.resources["food"] += 1
                self.resource_cooldown = now
        else:
            pass

    def load_Age2_images(self):   
        if self.name == "Towncenter":
            image = pygame.image.load("assets/Towncenter128-2.png").convert_alpha()        
        if self.name == "House":
            image = pygame.image.load("assets/House2.png").convert_alpha()        
        if self.name == "Barrack":
            image = pygame.image.load("assets/barracks182-2.png").convert_alpha()        
        if self.name == "Farm":
            image = pygame.image.load("assets/stable_tool2.png").convert_alpha()        
        if self.name == "Storage":
            image = pygame.image.load("assets/Stable128-2.png").convert_alpha()
           
        self.images[2] = image 
        


class Towncenter ( Batiment ):
 
    def update(self): 
        pass

    def save(self):
        pass        
  
class House ( Batiment ):

    def update(self):
        pass

    def save(self):
        pass        

class Barrack ( Batiment ):

    def update(self): 
        pass

    def save(self):
        pass

class Storage ( Batiment ):
 
    def update(self): 
        pass

    def save(self):
        pass

class Farm ( Batiment ):
 
    def update(self): 
        pass

    def save(self):
        pass 