import pickle
import pygame
import sys

from pygame.image import save

from DTO.workerDTO import workerDTO
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
        self.resource_manager.restore_save()
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

        #Unité
        #Worker(self.world.world[0][1], self.world,self.camera)
        #Worker(self.world.world[1][0], self.world,self.camera)

        #Save
        self.restore()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def events(self):
        for event in pygame.event.get(): # Si on clique sur la croix pour quitter, on arrete le jeu
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.resource_manager.save()
                self.save()
                self.world.save()
                pygame.quit()
                sys.exit()


    def update(self): 
        self.camera.update()
        for e in self.entities: e.update()
        self.hud.update()
        self.world.update(self.camera)
        if BENCHMARK == 1: self.benchmark.update()

    def draw(self): #Construction graphiques

        self.screen.fill(BLACK) #Arrière plan
        self.world.draw(self.screen, self.camera) #Fonction de dessin de la map
        draw_text(self.screen,'FPS = {}'.format(round(self.clock.get_fps())),25,WHITE,(10,70)) #Affichage des fps

        self.hud.draw(self.screen) #Affichage du hud
        
        if BENCHMARK == 1: self.benchmark.draw(self.screen)
        pygame.display.flip()


    # Save of workers. Can't move those methods to world.py due to Worker needing a world
    def save(self):
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                if self.world.workers[x][y] != None:
                    currentworker = self.world.workers[x][y]
                    self.world.collision_matrix[currentworker.tile["grid"][1]][currentworker.tile["grid"][0]] = 1
                    self.world.world[currentworker.tile["grid"][0]][currentworker.tile["grid"][1]]["collision"] = False
                    self.world.workersDTO[x][y] = workerDTO(currentworker.name,currentworker.health_points,currentworker.tile)
        
        try:   #Worker save
            with open(self.world.workers_save_file_path, "wb") as output:
                pickle.dump(self.world.workersDTO,output)
                output.close()
        except: print("Couldnt dump workers save in file")   

    def restore(self):
        try:    
            with open(self.world.workers_save_file_path, "rb") as input:
                restore_workers_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_workers_dto[x][y] != None:
                            currentworkerDTO = restore_workers_dto[x][y]
                            Worker(currentworkerDTO.tile,self.world,self.camera)
        except: 
            print("Created worker file")      


