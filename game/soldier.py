import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, TILE_SIZE
from math import *
from game.deplacement import lerp
from .workers import Worker

class Soldier(Worker):

    def __init__(self, tile, world, camera, pv=2000):
        super().__init__(tile, world, camera, pv)
        
        # Visual and audio effects
        self.name = "Soldier"
        self.animation = self.world.animation.soldier_walk
        self.animation_attack = self.world.animation.soldier_attack
        self.image = pygame.image.load('assets\soldier\Halbadierwalk001.png').convert_alpha()
        self.dmg = 5
        # pathfinding
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.soldier[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None

        # selection
        self.hitbox = pygame.Rect(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)
    



    #Override
    def change_tile(self, new_tile):
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[new_tile[0]][new_tile[1]] = self
        self.world.soldier[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.soldier[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]

    # #Override
    def update_sprite(self):
        if self.movestraight_animation == True:
            self.temp +=0.2
            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp= 0
        elif self.attack == True:
            self.temp += 0.2
            self.image = self.animation_attack[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation_attack):
                self.temp = 0
        else: self.image = self.world.animation.soldier_standby             

    #Override
    def delete(self):
        self.world.entities.remove(self)

        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1 #Free the last tile from collision
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

        self.world.soldier[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None 
        self.selected = False             
