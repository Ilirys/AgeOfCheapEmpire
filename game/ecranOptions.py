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
                pygame.draw.rect(self.screen, (255, 215, 50), (1355, 338, 275, 38), 3)
            elif definitions.clik == 2:
                pygame.draw.rect(self.screen, (255, 215, 50), (1355, 438, 275, 39), 3)
            elif definitions.clik == 3:
                pygame.draw.rect(self.screen, (255, 215, 50), (1355, 536, 275, 39), 3)


            if definitions.clik_ia == 1:
                pygame.draw.rect(self.screen, (255, 215, 50), (567, 383, 275, 41), 3)
            elif definitions.clik_ia == 2:
                pygame.draw.rect(self.screen, (255, 215, 50), (909, 383, 275, 41), 3)
            elif definitions.clik_ia == 3:
                pygame.draw.rect(self.screen, (255, 215, 50), (908, 477, 275, 41), 3)
            elif definitions.clik_ia == 4:
                pygame.draw.rect(self.screen, (255, 215, 50), (565, 474, 275, 41), 3)


            draw_text(self.screen, 'Options', 30, WHITE, (20, 20))
            mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

            button_normal = pygame.Rect(174, 249, 22, 22) # les boutons (ici, invisibles) -> bouton ok
            button_fast = pygame.Rect(174, 299, 22, 22)
            button_veryfast = pygame.Rect(174, 350, 22, 22)

            button_ok = pygame.Rect(900, 900, 280, 40)

            button_save1 = pygame.Rect(1355, 338, 275, 38)
            button_save2 = pygame.Rect(1353, 438, 275, 38)
            button_save3 = pygame.Rect(1353, 536, 275, 38)

            button_sup1 = pygame.Rect(1666, 336, 45, 40)
            button_sup2 = pygame.Rect(1666, 438, 45, 40)
            button_sup3 = pygame.Rect(1666, 536, 45, 40)

            button_attaque = pygame.Rect(567, 383, 275, 38)
            button_defense = pygame.Rect(909, 383, 275, 38)
            button_blitz = pygame.Rect(908, 477, 275, 38)
            button_vague = pygame.Rect(565, 474, 275, 38)


            if button_ok.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (900, 900, 277, 42), 3)
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
                pygame.draw.rect(self.screen, (255, 255, 255), (1355, 338, 275, 38), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save1/"
                    definitions.clik = 1

            if button_save2.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (1353, 438, 276, 39), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save2/"
                    definitions.clik = 2

            if button_save3.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (1353, 536, 276, 39), 3)
                if click:
                    definitions.SAVED_GAME_FOLDER = "save3/"
                    definitions.clik = 3

            if button_sup1.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                if click:
                    image = pygame.image.load('assets/red.png').convert_alpha()
                    image.fill((255, 255, 255, 128), special_flags=BLEND_RGBA_MULT)
                    self.screen.blit(image, (1668, 338))
                    files1 = os.listdir("save1/")
                    for i in range(0, len(files1)):
                        os.remove("save1/" + '/' + files1[i])

            if button_sup2.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                if click:
                    image = pygame.image.load('assets/red.png').convert_alpha()
                    image.fill((255, 255, 255, 128), special_flags=BLEND_RGBA_MULT)
                    self.screen.blit(image, (1668, 438))
                    files2 = os.listdir("save2/")
                    for i in range(0, len(files2)):
                        os.remove("save2/" + '/' + files2[i])

            if button_sup3.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                if click:
                    image = pygame.image.load('assets/red.png').convert_alpha()
                    image.fill((255, 255, 255, 128), special_flags=BLEND_RGBA_MULT)
                    self.screen.blit(image, (1668, 536))
                    files3 = os.listdir("save3/")
                    for i in range(0, len(files3)):
                        os.remove("save3/" + '/' + files3[i])


            if button_attaque.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (567, 383, 275, 41), 3)
                if click:
                    definitions.strat = "attaque"
                    definitions.clik_ia = 1

            if button_defense.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (909, 383, 275, 41), 3)
                if click:
                    definitions.strat = "defense"
                    definitions.clik_ia = 2

            if button_blitz.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (908, 477, 275, 41), 3)
                if click:
                    definitions.strat = "blitz"
                    definitions.clik_ia = 3

            if button_vague.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (565, 474, 275, 41), 3)
                if click:
                    definitions.strat = "vague"
                    definitions.clik_ia = 4




            # dessin des boutons pour s'assurer de leur bonne position
            # commentez les 3 lignes pour enlever les rectangles jaunes
            #  pygame.draw.rect(self.screen, (255, 215, 50), button_ok)
            #  pygame.draw.rect(self.screen, (255, 215, 50), button_veryfast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_normal)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_fast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save1)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save2)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_save3)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_sup1)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_sup2)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_sup3)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_attaque)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_defense)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_blitz)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_vague)


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
