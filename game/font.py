import pygame
import sys
from .definitions import *

def afficher_texte(screen, text, x = 0, y = 0, size = TAILLE_POLICE, color = WHITE, font_type = DEFAUT_POLICE):

        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

def afficher_image(screen, image, x = 0, y = 0):

        picture = pygame.image.load(image).convert()
        screen.blit(picture, (x,y))




