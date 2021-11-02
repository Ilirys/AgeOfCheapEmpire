import pygame 

class Towncenter: 
 
    def __init__(self, pos): 
        image = pygame.image.load("assets/towncenter.png").convert_alpha()
        self.image = image 
        self.name = "Towncenter" 
        self.rect = self.image.get_rect(topleft=pos) 
        self.counter = 0 
 
    def update(self): 
        self.counter += 1 
  
class House: 
 
    def __init__(self, pos): 
        image = pygame.image.load("assets/house.png").convert_alpha() 
        self.image = image 
        self.name = "House" 
        self.rect = self.image.get_rect(topleft=pos) 
        self.counter = 0 
 
    def update(self): 
        self.counter += 1