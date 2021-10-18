import pygame
import sys
from .definitions import *


def draw_text(screen, text, size, colour, pos):
    font = pygame.font.SysFont(None,size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(topleft=pos)
    screen.blit(text_surface, text_rect)

def scale_image(image, w=None, h=None):
        if w == image.get_width() or w == image.get_height():
            pass
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

def afficher_image(screen, image, x = 0, y = 0):

        picture = pygame.image.load(image).convert_alpha()
        picture = scale_image(picture,WIDTH,HEIGHT)
        screen.blit(picture, (x,y))



    