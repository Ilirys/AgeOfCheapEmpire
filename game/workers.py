import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, TILE_SIZE

from game.deplacement import lerp

class Worker:

    def __init__(self,tile,world,camera):
        self.world = world
        self.world.entities.append(self)
        self.camera = camera
        self.tile = tile

        #Visual and audio effects
        self.name = "villager"
        self.image = pygame.image.load('assets/sprites/villager/Villager.png').convert_alpha()
        self.temp = 0
        self.animation = self.world.animation.villager_walk
        self.movestraight_animation = True
        self.sound = pygame.mixer.Sound('Sounds/villager_select4.WAV')

        # pathfinding 
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = self
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]

        #path et path_index PAS INITIALISE (revoir cette initialisation)
        self.path_index = 0
        self.path = "0"

        #selection
        self.selected = False
        self.hitbox = pygame.Rect(self.pos_x  + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)
        iso_poly = self.tile["iso_poly"]
        self.iso_poly = None
            
        self.mouse_to_grid(0,0,self.camera.scroll)
        self.create_path(tile["grid"][0], tile["grid"][1])

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
            else: break    

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
        
        #Updating mouse position and action and the grid_pos 
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mouse_pos[0],mouse_pos[1],self.camera.scroll)
        
        #Hitbox
        self.hitbox.update(self.pos_x  + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)
        
        #Selection polygon
        pos_poly = [self.pos_x + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50]
        self.iso_poly = [(pos_poly[0] - 10, pos_poly[1] +44), (pos_poly[0] + 15, pos_poly[1] + 29), (pos_poly[0] + 40, pos_poly[1] + 44), (pos_poly[0] + 15 , pos_poly[1] + 59)]
        
        #collision matrix (for pathfinding and buildings)
        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
        
        #Animation update
        self.update_sprite()
                
        if self.selected:
            if mouse_action[2]:
                print(grid_pos[0], grid_pos[1])
                self.create_path(grid_pos[0], grid_pos[1])
                self.selected = False
            if mouse_action[0]:
                self.selected = False

        if self.hitbox.collidepoint(mouse_pos):
            if mouse_action[0]:
                self.selected = True
                self.sound.play()

        if self.path_index <= len(self.path) - 1:
            #animation
            self.movestraight_animation = True

            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.progression < 1:
                self.progression += (1/135) * DISPLACEMENT_SPEED[CURRENT_SPEED]
                self.progression = round(self.progression,4)
            else:
                self.progression = 1    
            self.pos_x = round(lerp(self.tile["render_pos"][0], new_real_pos[0], self.progression),3)
            self.pos_y = round(lerp(self.tile["render_pos"][1], new_real_pos[1], self.progression),3)
            

            if  self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]: #now - self.move_timer > 1000:  # update position in the world          
                self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1 #Free the last tile from collision
                self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False
                self.change_tile(new_pos)
                self.path_index += 1
                self.progression = 0
        else:
            self.movestraight_animation = False
        
                

    def update_sprite(self):
        if self.movestraight_animation == True:
            self.temp +=0.2
            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp= 0
        else: self.image = self.world.animation.villager_standby        


  


                