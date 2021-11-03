import pygame
from game.definitions import WHITE
from .utils import draw_text
import os
import json
from datetime import datetime
class Benchmark:
    def __init__(self,clock):
        self.fps = 0
        self.time = 0
        self.clock = clock
        self.list = [100,200,300,400,500,600,700,800,900,1000]
        
        self.data = {
            
        }
        try:
            with open('data/benchmark.txt') as bench_file:
                self.data = json.load(bench_file)
        except:
            print("No benchmark files found")        


    def update(self):
        self.time = round(pygame.time.get_ticks() * 0.1)
        if(self.time in self.list ):
            self.fps += round(self.clock.get_fps())
            self.list.remove(self.time)
        if self.time == 1000: 
            now = datetime.now().strftime("%d/%m %H:%M:%S")
            self.data["     " + os.getlogin() + " " + now] = self.fps/10 
            with open('data/benchmark.txt','w') as bench_file:
                json.dump(self.data,bench_file)

    def draw(self,screen):
        draw_text(screen,'Benchmark   {}'.format(self.data).replace("{","").replace("}",""),20,(255,100,0),(10,100))
