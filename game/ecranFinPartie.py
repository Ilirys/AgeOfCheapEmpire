import pygame
import sys
from .utils import *
from .definitions import *
from pygame.locals import *
import game.definitions as definitions



class FinPartie:
    click = False

    def __init__(self, screen, clock, game):
        self.screen = screen
        self.clock = clock
        self.game = game
        self.width, self.height = self.screen.get_size()



    def ecran_fin_partie(self, event):  # fonction pour afficher l'écran de démarrage

        click = False
        tmp = 1
        while (tmp == 1):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if definitions.statut_partie == 2:
            #     image = pygame.image.load('assets/HUD/victory.png').convert_alpha()
            #     self.screen.blit(image, (512, 432))
            image = pygame.image.load('assets/HUD/defeat.png').convert_alpha()
            self.screen.blit(image, (223, 358))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            self.clock.tick(60)
