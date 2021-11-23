import pygame 

class Towncenter: 
 
    def __init__(self, pos, resource_manager): 
        image = pygame.image.load("assets/towncenter.png").convert_alpha()
        self.image = image 
        self.name = "Towncenter"
        self.pos = pos 
        self.taille = 2
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
 
    def update(self): 
        now = pygame.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["wood"] += 1
            self.resource_cooldown = now

    def save(self):
        pass        
  
class House: 
 
    def __init__(self, pos, resource_manager): 
        image = pygame.image.load("assets/house.png").convert_alpha() 
        self.image = image 
        self.name = "House"
        self.pos = pos 
        self.taille = 1
        self.rect = self.image.get_rect(topleft=pos) 
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
 
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["stone"] += 1
            self.resource_cooldown = now

    def save(self):
        pass        

class Barrack: 
 
    def __init__(self, pos, resource_manager): 
        image = pygame.image.load("assets/barrack.png").convert_alpha()
        self.image = image 
        self.name = "Barrack"
        self.pos = pos 
        self.taille = 2
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()

    def update(self): 
        now = pygame.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["food"] += 1
            self.resource_cooldown = now

    def save(self):
        pass        