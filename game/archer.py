import pygame
from pygame import *
import math
from math import *
from units import *


class Archer(unite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.current_sprite = 0
        self.sprites.append(pygame.image.load(''))
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y]


    def update(self):
        distance = math.sqrt( (self.posArrivee[0]-self.posDepart[0])*(self.posArrivee[0]-self.posDepart[0]) + (self.posArrivee[1]-self.posDepart[1])*(self.posArrivee[1]-self.posDepart[1]) )
        if distance != 0:
            dt = 1 / distance
            if self.progression < 1:
                self.progression += self.speed * dt
            else:
                self.progression = 1
            self.pos_x = lerp(self.posDepart[0], self.posArrivee[0], self.progression)
            self.pos_y = lerp(self.posDepart[1], self.posArrivee[1], self.progression)


    def pos_darrivee(self,mx,my):
            self.posArrivee[0], self.posArrivee[1] = mx, my
            self.posDepart[0], self.posDepart[1] = (self.pos_x, self.pos_y)
            self.progression = 0
            self.update()

    def draw(self,window):
        window.blit(self.image, (self.pos_x - (50/2),self.pos_y - 100))

    def animation_walk_straight(self):
        self.movestraight_animation = True
        self.sprites = []

        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))
        self.sprites.append(pygame.image.load(''))

        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y]
        ########################"