import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, TILE_SIZE
from math import *
from game.deplacement import lerp
from .workers import Worker


class Horseman(Worker):

    def __init__(self, tile, world, camera, pv=2000):
        self.world = world
        self.world.entities.append(self)
        self.camera = camera

        self.tile = tile
        self.cases_libres = []
        # Visual and audio effects
        self.name = "horseman"
        self.range = 1
        self.dmg = 5
        self.pv = pv
        self.temp = 0
        self.animation = self.world.animation.horseman_walk
        self.movestraight_animation = True

        self.sound = pygame.mixer.Sound('Sounds/villager_select4.WAV')

        self.sprites = []
        self.current_sprite = 0
        self.sprites.append(pygame.image.load('assets\horseman\Scoutwalk001.png'))
        self.image = self.sprites[self.current_sprite]


        # pathfinding
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.horseman[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None
        
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]
        self.cible = self
        # selection
        self.selected = False
        self.hitbox = pygame.Rect(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 75, 28, 60) #Overriden
        iso_poly = self.tile["iso_poly"]
        self.iso_poly = None
        self.dest_tile = 0
        self.attack = False
        self.mouse_to_grid(0, 0, self.camera.scroll)
        self.create_path(tile["grid"][0], tile["grid"][1])
        self.movestraight_animation = False


    #Override
    def change_tile(self, new_tile):
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[new_tile[0]][new_tile[1]] = self
        self.world.horseman[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.horseman[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]

    #Override
    def update(self):

        # Updating mouse position and action and the grid_pos
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], self.camera.scroll)

        # Hitbox
        self.hitbox.update(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                           self.pos_y - self.image.get_height() + self.camera.scroll.y + 75, 28, 60)    #Overriden

        # Selection polygon
        pos_poly = [self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                    self.pos_y - self.image.get_height() + self.camera.scroll.y + 75]
        self.iso_poly = [(pos_poly[0] - 10, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 29),
                         (pos_poly[0] + 40, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 59)]

        # collision matrix (for pathfinding and buildings)
        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True

        # Animation update

        # update des animations
        self.animation

        self.update_sprite()

        self.cases_libres_a()


        if self.selected:
            if mouse_action[2]:
                self.create_path(grid_pos[0], grid_pos[1])
                self.selected = False
                self.world.hud.select_surface_empty = True
            if mouse_action[0]:
                self.selected = False
                self.world.hud.select_surface_empty = True    

        if self.dest_tile == self.tile:
            if self.attack:
                self.cible.pv -= self.dmg
                #self.animation = self.world.animation.horseman_attack
                print(self.cible.pv)

        if self.hitbox.collidepoint(mouse_pos):
            if mouse_action[0]:
                self.selected = True
                self.sound.play()

        if self.path_index <= len(self.path) - 1:
            self.animation
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

            if self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]:  # update position in the world
                self.change_tile(new_pos)
                self.cases_libres = []
                self.path_index += 1
                self.progression = 0



        else:
            self.movestraight_animation = False
    
    #Override
    def update_sprite(self):
        if self.movestraight_animation == True:
            self.temp += 0.2

            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp = 0
        else:
            self.image = self.world.animation.horseman_standby

            self.current_sprite = int(self.temp)
            if self.temp + 0.2 >= len(self.sprites):
                self.temp = 0
                self.movestraight_animation = False

    #Override
    def delete(self):
        self.world.entities.remove(self)

        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1 #Free the last tile from collision
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

        self.world.horseman[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None               
