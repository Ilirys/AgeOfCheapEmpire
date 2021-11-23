import pygame
import sys
from .utils import *
from .definitions import *
from pygame.locals import *


class Save:
    click = False

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

    def ecran_options(self):  # fonction pour afficher l'écran de démarrage
        self.playing = True
        while self.playing:

            self.screen.fill((0, 0, 0))  # arrière plan

            image = pygame.image.load('assets/menu_options.png').convert_alpha()
            self.screen.blit(image, (750, 390))

            mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

            button_1 = pygame.Rect(898, 510, 176, 35)  # les boutons (ici, invisibles) -> bouton quitter
            button_2 = pygame.Rect(898, 560, 176, 35)  # -> bouton charger
            button_3 = pygame.Rect(898, 605, 176, 35)  # -> bouton save
            button_4 = pygame.Rect(898, 655, 176, 35)  # -> bouton annuler

            if button_1.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (896, 518, 180, 40), 3)
                if click:
                    pygame.quit()
                    sys.exit()
            if button_2.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (255, 255, 255), (896, 568, 180, 40), 3)
                # if click:
                # charger sauvegarde
            if button_3.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (255, 255, 255), (896, 613, 180, 40), 3)
                # if click:
                # save david
            if button_4.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (255, 255, 255), (896, 663, 180, 40), 3)
                # if click:
                # annuler


            # dessin des boutons pour s'assurer de leur bonne position
            # pygame.draw.rect(self.screen, (255, 215, 50), button_1)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_2)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_3)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_4)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.clock.tick(60)

    # ecran_demarrage()
