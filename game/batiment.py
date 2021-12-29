import pygame 
from .definitions import *

class Batiment:
    
    def __init__(self, pos, name, resource_manager, pv=0, current_image=0):
        #Images
        self.image = pygame.image.load(dicoBatiment[name][0]).convert_alpha()
        self.ruin_image = pygame.image.load("assets/Rubble1.png").convert_alpha()
        self.small_ruin_image = pygame.image.load("assets/RubbleSmall1.png").convert_alpha()
        self.current_image = current_image
        self.images = [self.ruin_image, self.small_ruin_image, self.image]
        
        self.name = name
        self.pos = pos 
        self.taille = dicoBatiment[name][1]
        self.pv = pv
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_cooldown = pygame.time.get_ticks()
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)

    def update(self):
        pass

class Towncenter ( Batiment ):
 
    #Batiment.__init__(self, pos, "Towncenter", 2, resource_manager)

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
        now = pygame.time.get_ticks()
        print("lezgo")
        if now - self.resource_cooldown > 2000:
            self.resource_manager["food"] += 1
            self.resource_cooldown = now

    def save(self):
        pass 