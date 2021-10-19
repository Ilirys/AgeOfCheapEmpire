import pygame
import sys
from .definitions import *
from .world import World
from .utils import draw_text
from .camera import Camera
from .hud import Hud

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # hud
        self.hud = Hud(self.width, self.height)
    
        #World
        self.world = World(self.hud, MAP_SIZE,MAP_SIZE,self.width,self.width)

        #Camera
        self.camera = Camera(self.width, self.height)


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def events(self):
        for event in pygame.event.get(): # Si on clique sur la croix pour quitter, on arrete le jeu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self): 
        self.camera.update()
        self.hud.update()
        self.world.update(self.camera)

    def draw(self): #Construction graphiques

        self.screen.fill(BLACK) #Arrière plan
        self.world.draw(self.screen, self.camera) #Fonction de dessin de la map
        draw_text(self.screen,'FPS = {}'.format(round(self.clock.get_fps())),25,WHITE,(10,70)) #Affichage des fps

        self.hud.draw(self.screen) #Affichage du hud

        pygame.display.flip()

        

