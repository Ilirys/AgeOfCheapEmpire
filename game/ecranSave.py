import pygame
import sys
from .utils import *
from .definitions import *
from pygame.locals import *



class Save:
    click = False

    def __init__(self, screen, clock, game):
        self.screen = screen
        self.clock = clock
        self.game = game
        self.width, self.height = self.screen.get_size()



    def ecran_options(self, event):  # fonction pour afficher l'écran de démarrage

        click = False
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                tmp = 1
                while (tmp == 1):
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                    image = pygame.image.load('assets/menu_options.png').convert_alpha()
                    self.screen.blit(image, (750, 390))

                    mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

                        button_1 = pygame.Rect(880, 519, 230, 52)  # les boutons (ici, invisibles) -> bouton quitter
                        button_2 = pygame.Rect(880, 579, 230, 52)  # -> bouton options
                        button_3 = pygame.Rect(880, 639, 230, 52)  # -> bouton save
                        button_4 = pygame.Rect(880, 699, 230, 52)  # -> bouton annuler

                        if button_1.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                            pygame.draw.rect(self.screen, (255, 255, 255), (880, 521, 228, 50), 3)
                            if click:
                                pygame.quit()
                                sys.exit()
                        if button_2.collidepoint((mx, my)):
                            pygame.draw.rect(self.screen, (255, 255, 255), (880, 583, 228, 50), 3)
                            # if click:
                            # page options
                        if button_3.collidepoint((mx, my)):
                            pygame.draw.rect(self.screen, (255, 255, 255), (880, 639, 228, 50), 3)
                            if click:
                                self.game.resource_manager.save()
                                self.game.save()
                                self.game.world.save()
                        if button_4.collidepoint((mx, my)):
                            pygame.draw.rect(self.screen, (255, 255, 255), (880, 699, 228, 50), 3)
                            if click:
                                tmp = 0

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
