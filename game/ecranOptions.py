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


 
            draw_text(self.screen, 'Options', 30, WHITE, (20, 20))
            mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

            button_ok = pygame.Rect(600, 900, 280, 40)  # les boutons (ici, invisibles) -> bouton ok
            button_normal = pygame.Rect(170, 250, 15, 15)
            button_fast = pygame.Rect(170, 300, 15, 15)
            button_veryfast = pygame.Rect(170, 350, 15, 15)
            button_charg = pygame.Rect(900,900,280,40)

            if button_ok.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (594, 902, 277, 40), 3)
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

            if button_charg.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (255, 255, 255), (894, 902, 277, 40), 3)
                if click:
                    definitions.SAVE_GAME_FOLDER = "data/"




            # dessin des boutons pour s'assurer de leur bonne position
            # commentez les 3 lignes pour enlever les rectangles jaunes
            # pygame.draw.rect(self.screen, (255, 215, 50), button_ok)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_veryfast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_normal)

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
