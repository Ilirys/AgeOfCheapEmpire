import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from game.deplacement import lerp

class Worker:

    def __init__(self,tile,world):
        self.world = world
        self.world.entities.append(self)
        self.image = pygame.image.load('assets/sprites/villager/Villagerwalk001.png').convert_alpha()
        self.name = "villager"
        self.tile = tile

        # pathfinding 
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = self
        self.move_timer = pygame.time.get_ticks()

        self.create_path()

    def create_path(self):
        searching_for_path = True
        while searching_for_path:
            x = random.randint(0,self.world.grid_length_x - 1) 
            y = random.randint(0,self.world.grid_length_y - 1) 
            dest_tile = self.world.world[x][y]
            if not dest_tile["collision"]:
                self.grid = Grid(matrix=self.world.collision_matrix)
                self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])    
                self.end = self.grid.node(x, y)  
                finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
                self.path_index = 0
                self.path, runs = finder.find_path(self.start, self.end, self.grid)

                self.progression = 0

                searching_for_path = False

    def change_tile(self,new_tile):
        self.world.workers[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.workers[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]

    
    def update(self):
        now = pygame.time.get_ticks()
        new_pos = self.path[self.path_index]
        new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]

        # print("ici" ,self.tile["render_pos"][0], self.tile["render_pos"][1])
        # print(new_real_pos[0],new_real_pos[1])

        if self.progression < 1:
            self.progression += (1/140)
            self.progression = round(self.progression,4)
        else:
            self.progression = 1
        print(self.progression)    
        self.pos_x = round(lerp(self.tile["render_pos"][0], new_real_pos[0], self.progression),3)
        self.pos_y = round(lerp(self.tile["render_pos"][1], new_real_pos[1], self.progression),3)
        #print(self.pos_x, self.pos_y)

        if now - self.move_timer > 1000:
            # new_pos = self.path[self.path_index]

            # update position in the world           
            self.change_tile(new_pos)
            self.path_index += 1
            self.progression = 0
            self.move_timer = now
            if self.path_index == len(self.path) - 1:
                self.create_path()