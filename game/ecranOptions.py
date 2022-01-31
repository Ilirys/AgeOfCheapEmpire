import pygame
import sys
import os
import game.definitions as definitions
from .utils import *
from .definitions import *
from pygame.locals import *


class Options:
    click = False
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

    def options(self): #accès à la page d'options
        self.playing = True
        while self.playing:

            self.screen.fill((0,0,0))

            if definitions.case_coche == 1:
                afficher_image(self.screen, 'assets/ecran_options.png', -100)
                image = pygame.image.load('assets/ecran_options.png').convert_alpha()
                self.screen.blit(image, (0, 0))
            elif definitions.case_coche == 2:
                afficher_image(self.screen, 'assets/ecran_options2.png', -100)
                image = pygame.image.load('assets/ecran_options2.png').convert_alpha()
                self.screen.blit(image, (0, 0))
            elif definitions.case_coche == 3:
                afficher_image(self.screen, 'assets/ecran_options3.png', -100)
                image = pygame.image.load('assets/ecran_options3.png').convert_alpha()
                self.screen.blit(image, (0, 0))

            if definitions.clik == 1:
                pygame.draw.rect(self.screen, (255, 215, 50), (1490, 236, 288, 45), 3)
            elif definitions.clik == 2:
                pygame.draw.rect(self.screen, (255, 215, 50), (1490, 301, 288, 45), 3)
            elif definitions.clik == 3:
                pygame.draw.rect(self.screen, (255, 215, 50), (1490, 367, 288, 45), 3)


            draw_text(self.screen, 'Options', 30, WHITE, (20, 20))
            mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

            button_normal = pygame.Rect(169, 249, 22, 22) # les boutons (ici, invisibles) -> bouton ok
            button_fast = pygame.Rect(169, 299, 22, 22)
            button_veryfast = pygame.Rect(169, 350, 22, 22)

            button_ok = pygame.Rect(925,915,285,40)

            button_save1 = pygame.Rect(1488, 235, 288, 54)
            button_save2 = pygame.Rect(1488, 300, 288, 54)
            button_save3 = pygame.Rect(1488, 366, 288, 54)

            button_sup1 = pygame.Rect(1799, 238, 45, 40)
            button_sup2 = pygame.Rect(1799, 303, 45, 40)
            button_sup3 = pygame.Rect(1799, 368, 45, 40)


            if button_ok.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (926, 919, 288, 42), 3)
                if click:
                    self.playing=False


            if button_normal.collidepoint((mx, my)):
                if click:
                    definitions.case_coche = 1
                    definitions.CURRENT_SPEED = "normal"

            if button_fast.collidepoint((mx, my)):
                if click:
                    definitions.case_coche = 3
                    definitions.CURRENT_SPEED = "fast"

            if button_veryfast.collidepoint((mx, my)):
                if click:
                    definitions.case_coche = 2
                    definitions.CURRENT_SPEED = "veryfast"


            if button_save1.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (1490, 236, 288, 45), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save1/"
                    definitions.clik = 1

            if button_save2.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (1490, 301, 288, 45), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save2/"
                    definitions.clik = 2

            if button_save3.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (1490, 367, 288, 45), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save3/"
                    definitions.clik = 3

            if button_sup1.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                if click:
                    image = pygame.image.load('assets/red.png').convert_alpha()
                    image.fill((255, 255, 255, 128), special_flags=BLEND_RGBA_MULT)
                    self.screen.blit(image, (1801, 238))
                    files1 = os.listdir("save1/")
                    for i in range(0, len(files1)):
                        os.remove("save1/" + '/' + files1[i])

            if button_sup2.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                if click:
                    image = pygame.image.load('assets/red.png').convert_alpha()
                    image.fill((255, 255, 255, 128), special_flags=BLEND_RGBA_MULT)
                    self.screen.blit(image, (1801, 303))
                    files2 = os.listdir("save2/")
                    for i in range(0, len(files2)):
                        os.remove("save2/" + '/' + files2[i])

            if button_sup3.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                if click:
                    image = pygame.image.load('assets/red.png').convert_alpha()
                    image.fill((255, 255, 255, 128), special_flags=BLEND_RGBA_MULT)
                    self.screen.blit(image, (1801, 368))
                    files3 = os.listdir("save3/")
                    for i in range(0, len(files3)):
                        os.remove("save3/" + '/' + files3[i])


            # dessin des boutons pour s'assurer de leur bonne position
            # commentez les 3 lignes pour enlever les rectangles jaunes
            # pygame.draw.rect(self.screen, (255, 215, 50), button_ok)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_veryfast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_normal)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_fast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save1)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save2)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save3)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_sup1)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_sup2)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_sup3)


            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

        
            pygame.display.update()
            self.clock.tick(60)
