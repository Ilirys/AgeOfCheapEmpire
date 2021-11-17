import pygame
from pygame.constants import HWSURFACE 
from .utils import *


class Hud:

    def __init__(self, resource_manager, width, height):

        self.resource_manager = resource_manager
        self.width = width
        self.height = height

        self.hud_colour = (198, 155, 93, 175)

        self.images = self.load_images()
        self.images_hud = self.load_images_hud()
        self.images_scale = self.load_images_scale()

        #Screen sized hud 
        self.hudmoi_surface = pygame.Surface((width,height),pygame.SRCALPHA) 

        # resouces hud (Text box top left. Should be changed) 
        self.resources_surface = pygame.Surface((width*0.42, height * 0.07), pygame.SRCALPHA)
        self.resources_rect = self.resources_surface.get_rect(topleft=(0, 0))

        # age hud
        self.age_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.age_rect = self.age_surface.get_rect(topleft=(0, 0))
        self.age_surface.blit(self.images_hud["hudAge"],(0,0))

        # building hud (Bottom left) 
        self.build_surface = pygame.Surface((width * 0.32, height * 0.21), pygame.SRCALPHA)
        self.build_rect = self.build_surface.get_rect(topleft=(0, self.height * 0.79))
        self.build_surface.fill(self.hud_colour)

        # select hud (Bottom right) 
        self.select_surface = pygame.Surface((width * 0.595, height * 0.209), pygame.SRCALPHA)
        self.select_rect = self.select_surface.get_rect(topleft=(self.width * 0.35, self.height * 0.79))
        self.select_surface.fill(self.hud_colour)
        #self.select_surface.fill((255,0,0,175))

        self.tiles = self.create_build_hud()
        self.create_ressource_hud()

        self.selected_tile = None
        self.examined_tile = None

        

    def create_build_hud(self):

        #The whole hud image, considering spliting it..? 
        self.hudmoi_surface.blit(self.images_hud["smallhud"],(0,0))
        render_pos = [0, self.height-self.height * 0.21 + 35]
        object_width = self.build_surface.get_width() // 10

        tiles = []

        for image_name, image in self.images.items():

            pos = render_pos.copy()
            pos = [pos[0] + 10, pos[1]]
            image_tmp = image.copy()
            image_scale = self.scale_image(image_tmp, w=object_width)
            rect = image_scale.get_rect(topleft=pos)            

            tiles.append(
                {
                    "name": image_name,
                    "icon": image_scale,
                    "image": self.images[image_name],
                    "rect": rect,
                    "affordable": True
                }
            )

            render_pos[0] += self.build_surface.get_width() // 7

        return tiles
    
    def create_ressource_hud(self):
        self.resources_surface.blit(self.images_hud["hudRessources"],(0,0))


    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()

        if mouse_action[2]:
            self.selected_tile = None

        for tile in self.tiles:
             if self.resource_manager.is_affordable(tile["name"]):
                tile["affordable"] = True
             else:
                tile["affordable"] = False
             if tile["rect"].collidepoint(mouse_pos) and tile["affordable"]:
                if mouse_action[0]:
                    self.selected_tile = tile


    def draw(self, screen):

        #The whole hud image (screen sized) 
        screen.blit(self.hudmoi_surface,(0,0))
        screen.blit(self.resources_surface,(0,0))
 
        # build pannel hud (Bottom left) 
        screen.blit(self.build_surface, (0, self.height-self.height * 0.21)) 

        #select hud (Bottom right) 
        #screen.blit(self.select_surface, (self.width*0.405 , self.height*0.79)) 

        # resources (Text box top right. Should be changed) 
        screen.blit(self.resources_surface, (0,0))
        pos = 75
        for resource, resource_value in self.resource_manager.resources.items():
            txt = str(resource_value)
            draw_text(screen, txt, 30, (255, 255, 255), (pos, 22))
            pos += 108
        
        for tile in self.tiles:
            screen.blit(tile["icon"], tile["rect"].topleft)

    
    def load_images(self):

        # read images
        Towncenter = pygame.image.load("assets/towncenter.png").convert_alpha()
        House = pygame.image.load("assets/house.png").convert_alpha()
        Barrack = pygame.image.load("assets/barrack.png").convert_alpha()
        smallhud = pygame.image.load("assets/HUD/Hud_Villageois_1920-1080.png").convert_alpha()
        hudRessources = pygame.image.load("assets/HUD/Hud1v1.png").convert_alpha()
        hudAge = pygame.image.load("assets/HUD/Hud1v1_Age.png").convert_alpha()

        images = {
            "Towncenter": Towncenter,
            "House": House,
            "Barrack": Barrack
        }
        return images

    def load_images_scale(self):

        # read images
        Towncenter = pygame.image.load("assets/towncenter.png").convert_alpha()
        House = pygame.image.load("assets/house.png").convert_alpha()
        Barrack = pygame.image.load("assets/barrack.png").convert_alpha()
        smallhud = pygame.image.load("assets/HUD/Hud_Villageois_1920-1080.png").convert_alpha()
        hudRessources = pygame.image.load("assets/HUD/Hud1v1.png").convert_alpha()
        hudAge = pygame.image.load("assets/HUD/Hud1v1_Age.png").convert_alpha()

        images = {
            "Towncenter": Towncenter,
            "House": House,
            "Barrack": Barrack
        }
        return images

    def load_images_hud(self):

        # read images
        smallhud = pygame.image.load("assets/HUD/Hud_Villageois_1920-1080.png").convert_alpha()
        hudRessources = pygame.image.load("assets/HUD/Hud1v1.png").convert_alpha()
        hudAge = pygame.image.load("assets/HUD/Hud1v1_Age.png").convert_alpha()

        images = {
            "smallhud": smallhud,
            "hudRessources": hudRessources,
            "hudAge": hudAge
        }
        return images

    def scale_image(self, image, w=None, h=None):

        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pygame.transform.scale(image, (int(w), int(h))).convert_alpha()
        elif w == None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pygame.transform.scale(image, (int(w), int(h))).convert_alpha()
        else:
            image = pygame.transform.scale(image, (int(w), int(h))).convert_alpha()

        return image
