import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, TILE_SIZE
from math import *
from game.deplacement import lerp
from .horseman import Horseman

class HorsemanIA(Horseman):
    def __init__(self,tile,world,camera,pv=2000,team="red"):
        super().__init__(tile,world,camera,pv,team)

    # override

    def update(self):

        # collision matrix (for pathfinding and buildings)
        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True

        # Animation update
        self.update_sprite()

        if self.dest_tile == self.tile:
            if self.attack:
                self.attack_ani = True
                self.cible.pv -= self.dmg
                # self.cible.create_path(self.tile["grid"][0],self.tile["grid"][1])
                if self.world.world[self.cible.tile["grid"][0]][self.cible.tile["grid"][1]] != \
                        self.world.world[self.temp_tile_a["grid"][0]][self.temp_tile_a["grid"][1]]:
                    if self.cible.dest_tile == self.cible.tile:
                        self.world.world[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]][
                            "collision"] = True
                        self.world.unites[self.cible.dest_tile["grid"][0]][
                            self.cible.dest_tile["grid"][1]] == self.cible
                        self.create_path(self.cible.tile["grid"][0], self.cible.tile["grid"][1])
                if self.cible.pv <= 0:
                    self.attack = False
                    self.attack_ani = False

        if self.path_index <= len(self.path) - 1:
            if self.dest_tile != self.tile:
                self.movestraight_animation = True

            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.progression < 1:
                self.progression += (1 / 135) * DISPLACEMENT_SPEED[CURRENT_SPEED]
                self.progression = round(self.progression, 4)
            else:
                self.progression = 1
            self.pos_x = round(lerp(self.tile["render_pos"][0], new_real_pos[0], self.progression), 3)
            self.pos_y = round(lerp(self.tile["render_pos"][1], new_real_pos[1], self.progression), 3)

            if self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[
                1]:  # now - self.move_timer > 1000:  # update position in the world
                self.world.collision_matrix[self.tile["grid"][1]][
                    self.tile["grid"][0]] = 1  # Free the last tile from collision
                self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False
                self.change_tile(new_pos)
                self.path_index += 1
                self.progression = 0

        else:
            self.movestraight_animation = False