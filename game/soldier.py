import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import *
from math import *
from game.deplacement import lerp
from .workers import Worker

class Soldier(Worker):

    def __init__(self, tile, world, camera, pv=2000,  team="blue"):
        super().__init__(tile, world, camera, pv, team)
        
        # Visual and audio effects
        self.name = "Soldier"
        self.animation = self.world.animation.soldier_walk
        self.animation_attack = self.world.animation.soldier_attack
        self.animation_attack_up = self.world.animation.soldier_attack_up
        self.animation_attack_ldown = self.world.animation.soldier_attack_ldown
        self.animation_attack_left = self.world.animation.soldier_attack_left
        self.animation_attack_uleft = self.world.animation.soldier_attack_uleft
        self.animation_attack_right = self.world.animation.soldier_attack_right
        self.animation_attack_uright = self.world.animation.soldier_attack_uright
        self.animation_attack_rdown = self.world.animation.soldier_attack_rdown
        self.animation_mort = self.world.animation.soldier_mort

        self.image = pygame.image.load('assets\soldier\Halbadierwalk001.png').convert_alpha()
        self.dmg = 5
        # pathfinding

        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None
        if self.team == "blue":
            self.world.soldier[tile["grid"][0]][tile["grid"][1]] = self
        else:
            self.world.soldier[tile["grid"][0]][tile["grid"][1]] = None    

        # selection
        self.hitbox = pygame.Rect(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)
    



    #Override

    def change_tile(self, new_tile):
        if not self.world.world[new_tile[0]][new_tile[1]]["collision"]:        
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[new_tile[0]][new_tile[1]] = self
            self.world.soldier[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.soldier[new_tile[0]][new_tile[1]] = self

            self.tile = self.world.world[new_tile[0]][new_tile[1]]
            self.render_pos_x = self.tile["render_pos"][0]
            self.render_pos_y = self.tile["render_pos"][1]

            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
            self.path_index += 1
        else: 
            self.create_path(self.dest_tile["grid"][0], self.dest_tile["grid"][1])
            self.render_pos_x = self.pos_x
            self.render_pos_y = self.pos_y    

    # #Override
    def update_sprite(self):
        if self.walkdown_animation == True:
            self.temp += 0.2
            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp = 0
        elif self.attack_ani == True and self.attack == True:
            if self.temp + 0.2 >= 9:
                self.temp = 0
            self.temp += 0.2
            if self.cible.tile["grid"][0] < self.tile["grid"][0] and self.cible.tile["grid"][1] < self.tile["grid"][1]:
                self.image = self.animation_attack_up[int(self.temp)]
            elif self.cible.tile["grid"][0] > self.tile["grid"][0] and self.cible.tile["grid"][1] > self.tile["grid"][1]:
                self.image = self.animation_attack[int(self.temp)]
            elif self.cible.tile["grid"][0] == self.tile["grid"][0] and self.cible.tile["grid"][1] > self.tile["grid"][1]:
                self.image = self.animation_attack_ldown[int(self.temp)]
            elif self.cible.tile["grid"][0] < self.tile["grid"][0] and self.cible.tile["grid"][1] > self.tile["grid"][1]:
                self.image = self.animation_attack_left[int(self.temp)]
            elif self.cible.tile["grid"][0] < self.tile["grid"][0] and self.cible.tile["grid"][1] == self.tile["grid"][1]:
                self.image = self.animation_attack_uleft[int(self.temp)]
            elif self.cible.tile["grid"][0] > self.tile["grid"][0] and self.cible.tile["grid"][1] < self.tile["grid"][1]:
                self.image = self.animation_attack_right[int(self.temp)]
            elif self.cible.tile["grid"][0] == self.tile["grid"][0] and self.cible.tile["grid"][1] < self.tile["grid"][1]:
                self.image = self.animation_attack_uright[int(self.temp)]
            elif self.cible.tile["grid"][0] > self.tile["grid"][0] and self.cible.tile["grid"][1] == self.tile["grid"][1]:
                self.image = self.animation_attack_rdown[int(self.temp)]
            if self.temp + 0.2 >= 9:
                self.temp = 0
        elif self.pv > 0: self.image = self.world.animation.soldier_standby

    #Override
    def delete(self):
        #if self.temp + 0.1 > 11 :
            #self.temp = 0
        #self.temp += 0.1
        #self.image = self.animation_mort[int(self.temp)]
        #if self.temp >= 10.9:

            self.world.entities.remove(self)

            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1 #Free the last tile from collision
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

            self.world.soldier[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.selected = False
            self.temp = 0
