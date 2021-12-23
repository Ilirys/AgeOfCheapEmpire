import pickle
import pygame
import sys

from pygame.image import save
from DTO.workerDTO import workerDTO
from DTO.soldierDTO import soldierDTO
from DTO.horsemanDTO import horsemanDTO
from .definitions import *
from .world import World
from .utils import draw_text
from .camera import Camera
from .hud import Hud
from .minimap import Minimap
from .units import *
from .villager import *
from pygame import *
from .benchmark import Benchmark
from .workers import Worker
from .chat import Chat
from .Ressource import Ressource
from .soldier import Soldier
from .horseman import Horseman

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

        # Minimap
        self.minimap = Minimap(self.width, self.height)

        # entities
        self.entities = []
    
        #Camera
        self.camera = Camera(self.width, self.height)
        
        #World
        self.world = World(self.resource_manager, self.entities, self.hud, MAP_SIZE,MAP_SIZE,self.width,self.width, self.camera, self.minimap)

        #Benchmark
        self.benchmark = Benchmark(self.clock)

        #Chat
        self.chat = Chat(self.resource_manager, 15, 100, 200, 30)

        #Unité
        #Worker(self.world.world[0][0], self.world,self.camera)
        #Horseman(self.world.world[0][1], self.world,self.camera)
        #Soldier(self.world.world[1][0], self.world,self.camera)
        
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
            self.chat.handle_event(event)


    def update(self): 
        self.camera.update()
        for e in self.entities: e.update()
        self.hud.update()
        # self.minimap.update(self.world)
        self.world.update(self.camera)
        if BENCHMARK == 1: self.benchmark.update()

        self.chat.update()

    def draw(self): #Construction graphiques

        self.screen.fill(BLACK) #Arrière plan
        self.world.draw(self.screen, self.camera) #Fonction de dessin de la map
        draw_text(self.screen,'FPS = {}'.format(round(self.clock.get_fps())),25,WHITE,(10,70)) #Affichage des fps

        self.hud.draw(self.screen) #Affichage du hud
        self.minimap.draw(self.screen) #Affichage de la minimap
        self.chat.draw(self.screen) #Affichage du chat
        
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
                    self.world.workersDTO[x][y] = workerDTO(currentworker.name,currentworker.pv,currentworker.tile)
            
                if self.world.soldier[x][y] != None:
                    currentsoldier = self.world.soldier[x][y]
                    self.world.collision_matrix[currentsoldier.tile["grid"][1]][currentsoldier.tile["grid"][0]] = 1
                    self.world.world[currentsoldier.tile["grid"][0]][currentsoldier.tile["grid"][1]]["collision"] = False
                    self.world.soldierDTO[x][y] = soldierDTO(currentsoldier.name,currentsoldier.pv,currentsoldier.range,currentsoldier.dmg,currentsoldier.tile)
                
                if self.world.horseman[x][y] != None:
                    currenthorseman = self.world.horseman[x][y]
                    self.world.collision_matrix[currenthorseman.tile["grid"][1]][currenthorseman.tile["grid"][0]] = 1
                    self.world.world[currenthorseman.tile["grid"][0]][currenthorseman.tile["grid"][1]]["collision"] = False
                    self.world.horsemanDTO[x][y] = horsemanDTO(currenthorseman.name,currenthorseman.pv,currenthorseman.range,currenthorseman.dmg,currenthorseman.tile)
        
        try:   #Worker save
            with open(self.world.workers_save_file_path, "wb") as output:
                pickle.dump(self.world.workersDTO,output)
                output.close()
        except: print("Couldnt dump workers save in file")   

        try:   #Soldier save
            with open(self.world.soldiers_save_file_path, "wb") as output:
                pickle.dump(self.world.soldierDTO,output)
                output.close()
        except: print("Couldnt dump soldiers save in file") 

        try:   #horseman save
            with open(self.world.horseman_save_file_path, "wb") as output:
                pickle.dump(self.world.horsemanDTO,output)
                output.close()
        except: print("Couldnt dumpwhorseman save in file")   

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
                            self.world.resource_manager.apply_cost_to_resource("Villageois", -1) #Rembourser le cout du spawn en bouffe 
        except: 
            print("Created worker file")     

        try:    
            with open(self.world.soldiers_save_file_path, "rb") as input:
                restore_soldiers_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_soldiers_dto[x][y] != None:
                            currentsoldierDTO = restore_soldiers_dto[x][y]
                            Soldier(currentsoldierDTO.tile,self.world,self.camera)
                            self.world.resource_manager.apply_cost_to_resource("Soldier", -1)
        except: 
            print("Created soldier file") 

        try:    
            with open(self.world.horseman_save_file_path, "rb") as input:
                restore_horseman_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_horseman_dto[x][y] != None:
                            currenthorsemanDTO = restore_horseman_dto[x][y]
                            Horseman(currenthorsemanDTO.tile,self.world,self.camera)
                            self.world.resource_manager.apply_cost_to_resource("Horseman", -1)
        except: 
            print("Created horseman file")      


