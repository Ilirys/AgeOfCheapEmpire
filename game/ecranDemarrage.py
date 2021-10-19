import pygame
import sys
from .utils import *
from .definitions import *
from pygame.locals import *
from .ecranOptions import Options



class StartScreen:
    click = False
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

    def ecran_demarrage(self):   #fonction pour afficher l'écran de démarrage
        self.playing = True
        while self.playing:
 
            self.screen.fill((0,0,0)) #arrière plan
            
            afficher_image(self.screen, 'assets/ecran_demarrage.png', -100) #Image de AoE
            draw_text(self.screen, 'Main Menu', 30, WHITE, (5,5))
            mx, my = pygame.mouse.get_pos() #récupération des clics de souris

        
            button_1 = pygame.Rect(165, 447, 280, 40) #les boutons (ici, invisibles) -> bouton jouer
            button_2 = pygame.Rect(165, 635, 280, 40) # -> bouton options
        
            if button_1.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                if click:
                    self.playing=False
            if button_2.collidepoint((mx, my)):
                if click:
                    options = Options(self.screen, self.clock)
                    options.options()

            #dessin des boutons pour s'assurer de leur bonne position
            #pygame.draw.rect(self.screen, (255, 215, 50), button_1) 
            #pygame.draw.rect(self.screen, (255, 215, 50), button_2)

        

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

    #ecran_demarrage() 