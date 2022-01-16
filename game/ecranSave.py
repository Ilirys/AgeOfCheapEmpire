import pygame
import sys
import game.definitions as definitions
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
                btn = 1
                while tmp == 1:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                    image = pygame.image.load(definitions.IMAGE_MENU).convert_alpha()
                    self.screen.blit(image, (0,0))

                    mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

                    if btn == 1 :
                        button_1 = pygame.Rect(878, 494, 230, 48)  # les boutons (ici, invisibles) -> bouton quitter
                        button_3 = pygame.Rect(878, 554, 230, 48)  # -> bouton save
                        button_4 = pygame.Rect(878, 614, 230, 48)  # -> bouton annuler


                    if button_1.collidepoint((mx, my)):  # zone de collision des boutons et action quand cliqué
                        if btn == 1:
                            pygame.draw.rect(self.screen, (255, 255, 255), (877, 493, 228, 52), 3)
                        if click:
                            image2 = pygame.image.load('assets/black.png').convert_alpha()
                            self.screen.blit(image2, (0, 0))
                            definitions.IMAGE_MENU = 'assets/verif_quit.png'
                            btn = 2

                    if button_3.collidepoint((mx, my)):
                        if btn == 1 :
                            pygame.draw.rect(self.screen, (255, 255, 255), (877, 553, 228, 52), 3)
                        if click:
                            self.game.resource_manager.save()
                            self.game.save()
                            self.game.world.save()

                    if button_4.collidepoint((mx, my)):
                        if btn == 1 :
                            pygame.draw.rect(self.screen, (255, 255, 255), (877, 613, 228, 52), 3)
                        if click:
                            tmp = 0

                    if btn == 2:
                        button_oui = pygame.Rect(745, 665, 230, 50)  # -> bouton oui
                        #pygame.draw.rect(self.screen, (255, 230, 60), button_oui)
                        if button_oui.collidepoint((mx, my)):
                            pygame.draw.rect(self.screen, (255, 255, 255), (745, 663, 230, 53), 3)
                            if click:
                                pygame.quit()
                                sys.exit()

                    if btn == 2:
                        button_non = pygame.Rect(1005, 665, 230, 50)  # -> bouton non
                        #pygame.draw.rect(self.screen, (255, 215, 50), button_non)
                        if button_non.collidepoint((mx, my)):
                            pygame.draw.rect(self.screen, (255, 255, 255), (1004, 663, 230, 53), 3)
                            if click:
                                image2 = pygame.image.load('assets/black.png').convert_alpha()
                                self.screen.blit(image2, (0, 0))
                                definitions.IMAGE_MENU = 'assets/menu_options.png'
                                btn = 1

                    # dessin des boutons pour s'assurer de leur bonne position
                    #pygame.draw.rect(self.screen, (255, 215, 50), button_1)
                    #pygame.draw.rect(self.screen, (255, 215, 50), button_3)
                    #pygame.draw.rect(self.screen, (255, 215, 50), button_4)

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
