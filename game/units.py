from pygame import *
from math import *
import pygame
import math
from game.deplacement import *
from .camera import Camera

class unite():
    def __init__(self,camera):
        self.pv = 300  # Point de vie actuel
        self.force = 20

        self.camera = camera

        #self.cost
        #self.portee
        #self.ressource
        self.selection = False
        self.image = pygame.image.load('assets/sprites/villager/Villagerwalk001.png')
        self.rect = self.image.get_rect()
        self.pos_x = 300
        self.pos_y = 300
        self.rect.center = [self.pos_x,self.pos_y]
        self.posDepart = [self.pos_x, self.pos_y]
        self.posArrivee = [200, 400]
        self.speed = 2
        self.progression = 0

    def update(self):
        distance = math.sqrt((self.posArrivee[0] - self.posDepart[0]) * (self.posArrivee[0] - self.posDepart[0]) + (
                    self.posArrivee[1] - self.posDepart[1]) * (self.posArrivee[1] - self.posDepart[1]))
        if True:
            dt = 1 / distance
            if self.progression < 1:
                self.progression += self.speed * dt
            else:
                self.progression = 1
            self.pos_x = lerp(self.posDepart[0], self.posArrivee[0], 0.5)
            self.pos_y = lerp(self.posDepart[1], self.posArrivee[1], 0.5)
        

    def pos_darrivee(self, mx, my):
        self.posArrivee[0], self.posArrivee[1] = mx, my
        self.posDepart[0], self.posDepart[1] = (self.pos_x, self.pos_y)
        self.progression = 0
        self.update()

    def draw_unit(self,screen,camera):
        screen.blit(self.image, (self.pos_x + self.camera.scroll.x, self.pos_y + self.camera.scroll.y))


    def attaquer(self, unit1):
        if self.selection == True:
            if unit1.distance_unit(self, unit1) <= self.portee:
                unit1.pv = unit1.pv - self.force

    def distance_unit(unit2,unit1):
        return sqrt((unit1.rect.x - unit2.rect.x)**2 + (unit1.rect.y - unit2.rect.y)**2)