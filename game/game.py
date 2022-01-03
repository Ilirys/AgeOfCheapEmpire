import pickle
import pygame
import sys

from pygame.image import save
from DTO.archerDTO import archerDTO
from DTO.villagerDTO import villagerDTO
from DTO.workerDTO import workerDTO
from DTO.soldierDTO import soldierDTO
from DTO.horsemanDTO import horsemanDTO
from game.IA.horsemanIA import HorsemanIA
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
from.archer import Archer
from .ecranSave import Save
from game.IA.IA import IA
from game.IA.soldierIA import SoldierIA
from game.IA.villagerIA import VillagerIA
from game.IA.archerIA import ArcherIA
from game.IA.horsemanIA import HorsemanIA
# from .archerIA import ArcherIA
# from .villagerIA import VillagerIA
# from .horsemanIA import HorsemanIA

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()



        #entities 
        self.entities = []
        
        # resource manager
        self.resource_manager = Ressource()
        self.ressource_manager_IA = Ressource()
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
        #self.benchmark = Benchmark(self.clock)

        #Chat
        self.chat = Chat(self.world, self.camera, self.resource_manager, 15, 100, 200, 30)

        #Menu
        self.ecran_options = Save(self.screen, self.clock, self)

        # IA
        self.IA = IA(self.world)

        #Unité
        # Worker(self.world.world[1][1], self.world,self.camera)
        # Horseman(self.world.world[0][1], self.world,self.camera)
        SoldierIA(self.world.world[1][0], self.world,self.camera, self.IA)
        # Villager(self.world.world[1][0], self.world,self.camera)
        # Archer(self.world.world[2][2], self.world,self.camera)
        
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
            self.chat.handle_event(event)
            self.ecran_options.ecran_options(event)


    def update(self):
        self.camera.update()
        for e in self.entities: e.update()
        self.hud.update()
        self.world.update(self.camera)

        self.IA.update()

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
                
                if self.world.villager[x][y] != None:
                    currentvillager = self.world.villager[x][y]
                    self.world.collision_matrix[currentvillager.tile["grid"][1]][currentvillager.tile["grid"][0]] = 1
                    self.world.world[currentvillager.tile["grid"][0]][currentvillager.tile["grid"][1]]["collision"] = False
                    self.world.villagerDTO[x][y] = villagerDTO(currentvillager.name,currentvillager.pv,currentvillager.range,currentvillager.dmg,currentvillager.tile)
                
                if self.world.archer[x][y] != None:
                    currentarcher = self.world.archer[x][y]
                    self.world.collision_matrix[currentarcher.tile["grid"][1]][currentarcher.tile["grid"][0]] = 1
                    self.world.world[currentarcher.tile["grid"][0]][currentarcher.tile["grid"][1]]["collision"] = False
                    self.world.archerDTO[x][y] = archerDTO(currentarcher.name,currentarcher.pv,currentarcher.range,currentarcher.dmg,currentarcher.tile)
        
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
        except: print("Couldnt dump horseman save in file")   
        
        try:   #villager save
            with open(self.world.villager_save_file_path, "wb") as output:
                pickle.dump(self.world.villagerDTO,output)
                output.close()
        except: print("Couldnt dump villager save in file") 
        
        try:   #archer save
            with open(self.world.archer_save_file_path, "wb") as output:
                pickle.dump(self.world.archerDTO,output)
                output.close()
        except: print("Couldnt dump archer save in file") 

    def restore(self):
        try:    
            with open(self.world.workers_save_file_path, "rb") as input:
                restore_workers_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_workers_dto[x][y] != None:
                            currentworkerDTO = restore_workers_dto[x][y]
                            Worker(currentworkerDTO.tile,self.world,self.camera,currentworkerDTO.health_points)
                            self.world.resource_manager.apply_cost_to_resource("Villageois", -1) #Rembourser le cout du spawn en bouffe 
        
        except Exception as e: print("An error occured while loading worker save:", e)
    

        try:    
            with open(self.world.soldiers_save_file_path, "rb") as input:
                restore_soldiers_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_soldiers_dto[x][y] != None:
                            currentsoldierDTO = restore_soldiers_dto[x][y]
                            Soldier(currentsoldierDTO.tile,self.world,self.camera, currentsoldierDTO.pv)
                            self.world.resource_manager.apply_cost_to_resource("Soldier", -1)
        
        except Exception as e: print("An error occured while loading soldier save:", e)


        try:    
            with open(self.world.horseman_save_file_path, "rb") as input:
                restore_horseman_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_horseman_dto[x][y] != None:
                            currenthorsemanDTO = restore_horseman_dto[x][y]
                            Horseman(currenthorsemanDTO.tile,self.world,self.camera, currenthorsemanDTO.pv)
                            self.world.resource_manager.apply_cost_to_resource("horseman", -1)
                
        except Exception as e: print("An error occured while loading horseman save:", e)
    
        
        try:    
            with open(self.world.villager_save_file_path, "rb") as input:
                restore_villager_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_villager_dto[x][y] != None:
                            currentvillagerDTO = restore_villager_dto[x][y]
                            Villager(currentvillagerDTO.tile,self.world,self.camera, currentvillagerDTO.pv)
                            self.world.resource_manager.apply_cost_to_resource("Villageois", -1)
        
        except Exception as e: print("An error occured while loading villager save:", e)
        
        
        try:    
            with open(self.world.archer_save_file_path, "rb") as input:
                restore_archer_dto = pickle.load(input)
                input.close()
                for x in range(self.world.grid_length_x):
                    for y in range(self.world.grid_length_y):
                        if restore_archer_dto[x][y] != None:
                            currentarcherDTO = restore_archer_dto[x][y]
                            Archer(currentarcherDTO.tile,self.world,self.camera, currentarcherDTO.pv)
                            self.world.resource_manager.apply_cost_to_resource("Archer", -1)

        except Exception as e: print("An error occured while loading archer save:", e)
     


