import pygame
import sys
from .font import *
from .definitions import *
from pygame.locals import *



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
            afficher_texte(self.screen, 'Main Menu', 10, 10, 5)
            mx, my = pygame.mouse.get_pos() #récupération des clics de souris

        
            button_1 = pygame.Rect(165, 447, 280, 40) #les boutons (ici, invisibles) -> bouton jouer
            button_2 = pygame.Rect(165, 635, 280, 40) # -> bouton options
        
            if button_1.collidepoint((mx, my)): #zone de collision des boutons et action quand cliqué
                if click:
                    self.playing=False
            if button_2.collidepoint((mx, my)):
                if click:
                    self.options()

            #pygame.draw.rect(self.screen, (255, 215, 50), button_1) #dessin des boutons pour s'assurer de leur bonne position
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
                        self.ecran_demarrage()
        
            pygame.display.update()
            self.clock.tick(60)

    #ecran_demarrage() 