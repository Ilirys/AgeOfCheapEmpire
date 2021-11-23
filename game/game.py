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
from .chat import Chat
from .Ressource import Ressource

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        #entities 
        self.entities = []
        
        # resource manager
        self.resource_manager = Ressource()

        # hud
        self.hud = Hud(self.resource_manager, self.width, self.height)

        # entities
        self.entities = []
    
        #World
        self.world = World(self.resource_manager, self.entities, self.hud, MAP_SIZE,MAP_SIZE,self.width,self.width)

        #Camera
        self.camera = Camera(self.width, self.height)

        #Benchmark
        self.benchmark = Benchmark(self.clock)

        #Chat
        self.chat = Chat(self.resource_manager, 15, 100, 200, 30)

        #Unité
        #Worker(self.world.world[0][0], self.world,self.camera)
        #Worker(self.world.world[0][1], self.world,self.camera)
        #Worker(self.world.world[1][0], self.world,self.camera)

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
            self.chat.handle_event(event)


    def update(self): 
        self.camera.update()
        for e in self.entities: e.update()
        self.hud.update()
        self.world.update(self.camera)
        if BENCHMARK == 1: self.benchmark.update()

        self.chat.update()

    def draw(self): #Construction graphiques

        self.screen.fill(BLACK) #Arrière plan
        self.world.draw(self.screen, self.camera) #Fonction de dessin de la map
        draw_text(self.screen,'FPS = {}'.format(round(self.clock.get_fps())),25,WHITE,(10,70)) #Affichage des fps

        self.hud.draw(self.screen) #Affichage du hud

        self.chat.draw(self.screen) #Affichage du chat
        
        if BENCHMARK == 1: self.benchmark.draw(self.screen)
        pygame.display.flip()

        

