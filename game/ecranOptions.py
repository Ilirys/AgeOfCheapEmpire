import pygame
import sys
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
                pygame.draw.rect(self.screen, (255, 215, 50), (1488, 235, 288, 45), 3)
            elif definitions.clik == 2:
                pygame.draw.rect(self.screen, (255, 215, 50), (1488, 300, 288, 45), 3)
            elif definitions.clik == 3:
                pygame.draw.rect(self.screen, (255, 215, 50), (1488, 366, 288, 45), 3)


            draw_text(self.screen, 'Options', 30, WHITE, (20, 20))
            mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

            button_normal = pygame.Rect(171, 251, 20, 20) # les boutons (ici, invisibles) -> bouton ok
            button_fast = pygame.Rect(171, 301, 20, 20)
            button_veryfast = pygame.Rect(171, 352, 20, 20)
            button_ok = pygame.Rect(925,915,285,40)
            button_save1 = pygame.Rect(1488, 235, 288, 54)
            button_save2 = pygame.Rect(1488, 300, 288, 54)
            button_save3 = pygame.Rect(1488, 366, 288, 54)


            if button_ok.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (925, 915, 288, 42), 3)
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
                pygame.draw.rect(self.screen, (255, 255, 255), (1488, 235, 288, 45), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save1/"
                    definitions.clik = 1

            if button_save2.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (1488, 300, 288, 45), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save2/"
                    definitions.clik = 2

            if button_save3.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (1488, 366, 288, 45), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save3/"
                    definitions.clik = 3


            # dessin des boutons pour s'assurer de leur bonne position
            # commentez les 3 lignes pour enlever les rectangles jaunes
            # pygame.draw.rect(self.screen, (255, 215, 50), button_ok)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_veryfast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_normal)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_fast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save1)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save2)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save3)

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
