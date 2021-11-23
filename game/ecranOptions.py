import pygame
import sys
from .utils import *
from .definitions import *
from pygame.locals import *
#from .ecranDemarrage import StartScreen
from .definitions import *


class Options:
    click = False
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

    def options(self): #accès à la page d'options
        aff = 1
        self.playing = True
        while self.playing:

            self.screen.fill((0,0,0))

            if (aff==1):
                afficher_image(self.screen, 'assets/ecran_options.png', -100)
                image = pygame.image.load('assets/ecran_options.png').convert_alpha()
                self.screen.blit(image, (0, 0))
            elif (aff==2):
                afficher_image(self.screen, 'assets/ecran_options2.png', -100)
                image = pygame.image.load('assets/ecran_options2.png').convert_alpha()
                self.screen.blit(image, (0, 0))


 
            draw_text(self.screen, 'Options', 30, WHITE, (20, 20))
            mx, my = pygame.mouse.get_pos()  # récupération des clics de souris

            button_ok = pygame.Rect(600, 900, 280, 40)  # les boutons (ici, invisibles) -> bouton ok
            button_normal = pygame.Rect(170, 250, 15, 15)
            button_fast = pygame.Rect(170, 350, 15, 15)

            if button_ok.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                pygame.draw.rect(self.screen, (255, 255, 255), (594, 902, 277, 40), 3)
                if click:
                    self.playing=False
            if button_normal.collidepoint((mx, my)):
                if click:
                    aff = 1
                    CURRENT_SPEED = "normal"
            if button_fast.collidepoint((mx, my)):
                if click:
                    aff = 2
                    CURRENT_SPEED = "fast"


            # dessin des boutons pour s'assurer de leur bonne position
            #commentez les 3 lignes pour enlever les rectangles jaunes
            #pygame.draw.rect(self.screen, (255, 215, 50), button_ok)
            #pygame.draw.rect(self.screen, (255, 215, 50), button_fast)
            # pygame.draw.rect(self.screen, (255, 215, 50), button_normal)

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
