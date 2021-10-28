import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import TILE_SIZE

from game.deplacement import lerp

class Worker:

    def __init__(self,tile,world,camera):
        self.world = world
        self.world.entities.append(self)
        self.camera = camera
        self.image = pygame.image.load('assets/sprites/villager/Villagerwalk001.png').convert_alpha()
        self.name = "villager"
        self.tile = tile

        # pathfinding 
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = self
        self.move_timer = pygame.time.get_ticks()
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]
        #selection
        self.selected = False
        self.hitbox = pygame.Rect(self.pos_x  + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)

        self.mouse_to_grid(0,0,self.camera.scroll)
        self.create_path(tile["grid"][0], tile["grid"][1])

    def create_path(self,x,y):
        searching_for_path = True
        while searching_for_path:
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

    def mouse_to_grid(self, x, y, scroll):
        # transform to world position (removing camera scroll and offset)
        world_x = x - scroll.x - self.world.grass_tiles.get_width()/2
        world_y = y - scroll.y
        # transform to cart (inverse of cart_to_iso)
        cart_y = (2*world_y - world_x)/2
        cart_x = cart_y + world_x
        # transform to grid coordinates
        grid_x = int(cart_x // TILE_SIZE)
        grid_y = int(cart_y // TILE_SIZE)

        if grid_x > 49: grid_x = 49
        if grid_x < 0: grid_x = 0
        if grid_y > 49: grid_y = 49
        if grid_y < 0: grid_y = 0

        return grid_x, grid_y            
    
    def update(self):
        now = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mouse_pos[0],mouse_pos[1],self.camera.scroll)
        self.hitbox.update(self.pos_x  + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)

        if self.hitbox.collidepoint(mouse_pos):
            if mouse_action[0]:
                self.selected = True
                

        if self.selected:
            if mouse_action[2]:
                print(grid_pos[0], grid_pos[1])
                self.create_path(grid_pos[0], grid_pos[1])
                self.selected = False   

        if self.path_index <= len(self.path) - 1:
            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.progression < 1:
                self.progression += (1/135)
                self.progression = round(self.progression,4)
            else:
                self.progression = 1    
            self.pos_x = round(lerp(self.tile["render_pos"][0], new_real_pos[0], self.progression),3)
            self.pos_y = round(lerp(self.tile["render_pos"][1], new_real_pos[1], self.progression),3)

            if  now - self.move_timer > 1000:  # update position in the world          
                self.change_tile(new_pos)
                self.path_index += 1
                self.progression = 0
                self.move_timer = now
  


                
