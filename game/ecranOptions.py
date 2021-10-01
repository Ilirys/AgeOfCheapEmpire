import pygame
import sys
from .font import *
from .definitions import *
from pygame.locals import *

class Options:
    click = False
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

    def options(self): #accès à la page d'options ----->>>>> NON COMMENCÉE
        self.playing = True
        while self.playing:
            self.screen.fill((0,0,0))
 
            afficher_texte(self.screen, 'Options', 10, 10, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.playing = False
                        '''
                        from .ecranDemarrage import StartScreen
                        ecranDemarrage = StartScreen(self.screen, self.clock)
                        ecranDemarrage.ecran_demarrage()
                        '''
        
            pygame.display.update()
            self.clock.tick(60)
