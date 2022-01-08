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

    def __init__(self, tile, world, camera, pv=2000, team="blue"):
        super().__init__(tile, world, camera, pv,team)

        # Visual and audio effects
        self.name = "Archer"
        self.animation = self.world.animation.archer_walk
        self.animation_attack = self.world.animation.archer_attack
        self.animation_attack_up = self.world.animation.archer_attack_up
        self.animation_attack_ldown = self.world.animation.archer_attack_ldown
        self.animation_attack_left = self.world.animation.archer_attack_left
        self.animation_attack_uleft = self.world.animation.archer_attack_uleft
        self.animation_attack_right = self.world.animation.archer_attack_right
        self.animation_attack_uright = self.world.animation.archer_attack_uright
        self.animation_attack_rdown = self.world.animation.archer_attack_rdown
        self.animation_mort = self.world.animation.archer_mort
        self.image = pygame.image.load('assets/archer/Archerwalk001.png').convert_alpha()

        # pathfinding
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.archer[tile["grid"][0]][tile["grid"][1]] = self
        self.world.unites_combat[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None

        # selection
        self.hitbox = pygame.Rect(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)

        #override
        self.dmg = 2

    #override

    def create_path(self, x, y):
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
                self.attack = False
                searching_for_path = False
            elif (self.world.unites[x][y] != None or self.world.world[x][y]["tile"].tile_batiment != 0):  # Si la case contient une unitées, pathfinding attaque
                # On enleve la collision de la case du soldat (Or else can't get find_path to work)

                self.temp_tile = self.world.world[x][y]
                self.world.world[x][y]["collision"] = False
                self.world.collision_matrix[y][x] = 1

                self.grid = Grid(matrix=self.world.collision_matrix)
                self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
                self.end = self.grid.node(x, y)
                finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                self.path_index = 0
                self.path, runs = finder.find_path(self.start, self.end, self.grid)

                # On enleve le dernier element de la liste (Pour ne pas aller SUR l'unité) et on Attaque
                if self.world.unites[x][y] != None and self.world.unites[x][y].team != self.team:
                    self.cible = self.world.unites[x][y]
                    if self.dest_tile != self.tile:
                        for i in range(2):
                            if self.path:
                                self.path.pop()
                                if self.path:
                                    self.dest_tile = self.world.world[self.path[-1][0]][self.path[-1][-1]]
                    self.temp_tile_a = self.cible.tile
                    self.attack = True

                elif self.world.world[x][y]["tile"].tile_batiment != 0 and self.world.batiment[self.world.world[x][y]["tile"].tile_batiment["grid"][0]][self.world.world[x][y]["tile"].tile_batiment["grid"][1]].team != self.team:
                    self.cible = self.world.batiment[self.world.world[x][y]["tile"].tile_batiment["grid"][0]][self.world.world[x][y]["tile"].tile_batiment["grid"][1]]  #self.world.world[x][y]["tile"].tile_batiment

                    if self.dest_tile != self.tile:
                        for i in range(2):
                            if self.path:
                                self.path.pop()
                                if self.path:
                                    self.dest_tile = self.world.world[self.path[-1][0]][self.path[-1][-1]]
                    self.attack_bati = True
                self.progression = 0
                searching_for_path = False
                if self.temp_tile:  #Dans le cas ou on voulait aller a une case occupée, il faut remettre la collision de la case occupée a 1
                        self.world.world[self.temp_tile["grid"][0]][self.temp_tile["grid"][1]]["collision"] = True
                        self.world.collision_matrix[self.temp_tile["grid"][1]][self.temp_tile["grid"][0]] = 0
                        self.temp_tile = None

            else:
                break

    # Override
    def change_tile(self, new_tile):
        if not self.world.world[new_tile[0]][new_tile[1]]["collision"]:
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[new_tile[0]][new_tile[1]] = self
            self.world.archer[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.archer[new_tile[0]][new_tile[1]] = self

            self.tile = self.world.world[new_tile[0]][new_tile[1]]
            self.render_pos_x = self.tile["render_pos"][0]
            self.render_pos_y = self.tile["render_pos"][1]

            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
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
            if self.temp + 0.2 >= len(self.animation_attack):
                self.temp = 0
        elif self.pv > 0:
            self.image = self.world.animation.archer_standby
        # Override

    def delete(self):
        #if self.temp + 0.1 > 11 :
            #self.temp = 0
        #self.temp += 0.1
        #self.image = self.animation_mort[int(self.temp)]
        #if self.temp >= 10.9:

            self.world.entities.remove(self)

            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

            self.world.archer[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.selected = False
            self.temp = 0

