import pygame
from pygame.constants import HWSURFACE 
from .utils import *


class Hud:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.hud_colour = (198, 155, 93, 175)

        #Screen sized hud
        self.hudmoi_surface = pygame.Surface((width,height),pygame.SRCALPHA)
        
        # resouces hud (Text box top left. Should be changed)
        self.resouces_surface = pygame.Surface((width*0.475, height * 0.06), pygame.SRCALPHA)
        self.resources_rect = self.resouces_surface.get_rect(topleft=(0, 0))
        
        # building hud (Bottom left)
        self.build_surface = pygame.Surface((width * 0.32, height * 0.21), pygame.SRCALPHA)
        self.build_rect = self.build_surface.get_rect(topleft=(0, self.height * 0.79))
        #self.build_surface.fill(self.hud_colour)

        # select hud (Bottom right)
        self.select_surface = pygame.Surface((width * 0.595, height * 0.209), pygame.SRCALPHA)
        self.select_surface.fill(self.hud_colour)
        #self.select_surface.fill((255,0,0,175))


        self.images = self.load_images()
        self.tiles = self.create_build_hud()

        self.selected_tile = None

        

    def create_build_hud(self):
        font = pygame.font.SysFont(None,25)     #next 3 lines draw the ressources hud 
        text_surface = font.render("WOOD:                      FOOD:                   GOLD:                       STONE:                           UNITS:", True, WHITE)
        self.resouces_surface.blit(text_surface,(0,self.resouces_surface.get_height()//3))

        #The whole hud image, considering spliting it..?
        self.hudmoi_surface.blit(self.images["smallhud"],(0,0))

        render_pos = [0, self.height-self.height * 0.21 + 40]
        object_width = self.build_surface.get_width() // 7

        tiles = []

        for image_name, image in self.images.items():

            pos = render_pos.copy()
            pos = [pos[0] + 20, pos[1]]
            image_tmp = image.copy()
            image_scale = self.scale_image(image_tmp, w=object_width)
            rect = image_scale.get_rect(topleft=pos)            

            tiles.append(
                {
                    "name": image_name,
                    "icon": image_scale,
                    "image": self.images[image_name],
                    "rect": rect
                }
            )

            render_pos[0] += self.build_surface.get_width() // 7

        return tiles

    def create_ressource_hud(self,screen):
        ressource_object_width = self.resouces_surface.get_width 
        for resource in ["WOOD:", " FOOD:", "  GOLD:", "   STONE:", "  UNITS:"]:
            draw_text(screen, resource, 30, (255, 255, 255), (pos, 20))    

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()

        if mouse_action[2]:
            self.selected_tile = None

        for tile in self.tiles:
            if tile["rect"].collidepoint(mouse_pos):
                if mouse_action[0]:
                    self.selected_tile = tile


    def draw(self, screen):

        #The whole hud image (screen sized)
        screen.blit(self.hudmoi_surface,(0,0))

        # build pannel hud (Bottom left)
        screen.blit(self.build_surface, (0, self.height-self.height * 0.21))

        #select hud (Bottom right)
            #screen.blit(self.select_surface, (self.width*0.405 , self.height*0.79))
        
        # resources (Text box top right. Should be changed)
        screen.blit(self.resouces_surface, (0,0))
        
        for tile in self.tiles:
            screen.blit(tile["icon"], tile["rect"].topleft)

    
    def load_images(self):

        # read images
        towncenter = pygame.image.load("assets/Towncenter.png").convert_alpha()
        grass = pygame.image.load("assets/grass.png").convert_alpha()
        hud1300x1000 = pygame.image.load("assets/HUD/Hud_Villageois_AgePierre_1300-1000.png").convert_alpha()
        hud1300x1000 = scale_image(hud1300x1000,self.width,self.height)

        images = {
            "towncenter": towncenter,
            "grass": grass,
            "smallhud" : hud1300x1000
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
