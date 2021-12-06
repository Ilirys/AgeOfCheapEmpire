import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, TILE_SIZE
from math import *
from game.deplacement import lerp
from .workers import Worker


class Archer(Worker):

    def __init__(self, tile, world, camera, pv=2000):
        super().__init__(tile, world, camera, pv=2000)

        # Visual and audio effects
        self.name = "Archer"
        self.animation = self.world.animation.archer_walk
        self.image = pygame.image.load('assets/archer/Archerwalk001.png').convert_alpha()

        # pathfinding
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.archer[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None

        # selection
        self.hitbox = pygame.Rect(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)

        #override
        self.dmg = 2

    #override
    def create_path(self,x,y):
        searching_for_path = True
        while searching_for_path:
            self.dest_tile = self.world.world[x][y]
            if not self.dest_tile["collision"]:
                self.grid = Grid(matrix=self.world.collision_matrix)
                self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
                self.end = self.grid.node(x, y)
                finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                self.path_index = 0
                self.path, runs = finder.find_path(self.start, self.end, self.grid)

                self.progression = 0

                searching_for_path = False
            elif (self.world.unites[x][y] != None): #Si la case contient une unitées, pathfinding attaque
                #On enleve la collision de la case du soldat (Or else can't get find_path to work)

                self.temp_tile = self.world.world[x][y]
                self.world.world[x][y]["collision"] = False
                self.world.collision_matrix[y][x] = 1

                self.grid = Grid(matrix=self.world.collision_matrix)
                self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
                self.end = self.grid.node(x, y)
                finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                self.path_index = 0
                self.path, runs = finder.find_path(self.start, self.end, self.grid)

                #On enleve le dernier element de la liste (Pour ne pas aller SUR l'unité) et on Attaque

                self.cible = self.world.unites[x][y]
                if self.dest_tile == self.tile:
                    self.attack = True
                    self.progression = 0
                    searching_for_path = False
                else :
                    for i in range(3):
                        self.path.pop()
                    self.dest_tile = self.world.world[self.path[-1][0]][self.path[-1][-1]]
                    self.attack = True
                    self.progression = 0
                    searching_for_path = False

            else:
                break

    # Override
    def change_tile(self, new_tile):
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[new_tile[0]][new_tile[1]] = self
        self.world.archer[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.archer[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]

    # #Override
    def update_sprite(self):
        if self.movestraight_animation == True:
            self.temp += 0.2
            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp = 0
        else:
            self.image = self.world.animation.archer_standby

        # Override

    def delete(self):
        self.world.entities.remove(self)

        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

        self.world.archer[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.selected = False