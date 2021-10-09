import pygame 
from .utils import *


class Hud:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.hud_colour = (198, 155, 93, 175)

        # resouces hud
        self.resouces_surface = pygame.Surface((width, height * 0.02), pygame.SRCALPHA)
        self.resources_rect = self.resouces_surface.get_rect(topleft=(0, 0))
        self.resouces_surface.fill(self.hud_colour)

        # building hud
        self.build_surface = pygame.Surface((width * 0.32, height * 0.21), pygame.SRCALPHA)
        self.build_rect = self.build_surface.get_rect(topleft=(self.width * 0.67, self.height * 0.79))
        self.build_surface.fill(self.hud_colour)

        self.images = self.load_images()
        self.tiles = self.create_build_hud()

        self.selected_tile = None

    def create_build_hud(self):

        render_pos = [25, self.height-self.height * 0.17]
        object_width = self.build_surface.get_width() // 8

        tiles = []

        for image_name, image in self.images.items():

            pos = render_pos.copy()
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

            render_pos[0] += image_scale.get_width() + 8

        return tiles

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

        afficher_image(screen, 'assets/HUD/Hud_Villageois_AgePierre_1300-1000.png')

        # build hud
        screen.blit(self.build_surface, (0, self.height-self.height * 0.21))

        for tile in self.tiles:
            screen.blit(tile["icon"], tile["rect"].topleft)

        # resources
        pos = 10
        for resource in ["WOOD:", " FOOD:", "  GOLD:", "   STONE:", "  UNITS:"]:
            draw_text(screen, resource, 30, (255, 255, 255), (pos, 20))
            pos += 100

    
    def load_images(self):

        # read images
        towncenter = pygame.image.load("assets/Towncenter.png")
        grass = pygame.image.load("assets/grass.png")
         
        

        images = {
            "towncenter": towncenter,
            "grass": grass
        }
        return images

    def scale_image(self, image, w=None, h=None):

        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pygame.transform.scale(image, (int(w), int(h)))
        elif w == None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pygame.transform.scale(image, (int(w), int(h)))
        else:
            image = pygame.transform.scale(image, (int(w), int(h)))

        return image
