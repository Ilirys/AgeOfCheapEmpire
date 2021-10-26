import pygame
import sys
from .definitions import *
from .world import World
from .utils import draw_text
from .camera import Camera
from .hud import Hud
from .units import *
from .villager import *
from pygame import *
from .benchmark import Benchmark
from .workers import Worker

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        #entities 
        self.entities = []
        
        # hud
        self.hud = Hud(self.width, self.height)
    
        #World
        self.world = World(self.entities,self.hud, MAP_SIZE,MAP_SIZE,self.width,self.width)
        for _ in range(1): Worker(self.world.world[25][25], self.world)

        #Camera
        self.camera = Camera(self.width, self.height)

        #Benchmark
        self.benchmark = Benchmark(self.clock)

        #Unité
        self.unit = unite(self.camera)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def events(self):
        for event in pygame.event.get(): # Si on clique sur la croix pour quitter, on arrete le jeu
            mx,my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.unit.pos_darrivee(mx,my)


    def update(self): 
        self.camera.update()
        for e in self.entities: e.update()
        self.hud.update()
        self.world.update(self.camera)
        self.unit.update()
        if BENCHMARK == 1: self.benchmark.update()

    def draw(self): #Construction graphiques

        self.screen.fill(BLACK) #Arrière plan
        self.world.draw(self.screen, self.camera) #Fonction de dessin de la map
        draw_text(self.screen,'FPS = {}'.format(round(self.clock.get_fps())),25,WHITE,(10,70)) #Affichage des fps

        self.hud.draw(self.screen) #Affichage du hud
        
        self.unit.draw_unit(self.screen,self.camera)
        
        if BENCHMARK == 1: self.benchmark.draw(self.screen)
        pygame.display.flip()

        

