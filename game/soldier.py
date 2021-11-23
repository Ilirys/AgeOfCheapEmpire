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

    def __init__(self, tile, world, camera):
        super().__init__(tile,world,camera)
        self.world = world
        self.world.entities.append(self)
        self.camera = camera

        self.tile = tile
        self.cases_libres = []
        # Visual and audio effects
        self.name = "Soldier"
        self.range = 2
        self.dmg = 5
        self.pv = 2000
        self.temp = 0
        self.animation = self.world.animation.soldier_walk
        self.movestraight_animation = True

        self.sound = pygame.mixer.Sound('Sounds/villager_select4.WAV')


        self.sprites = []
        self.current_sprite = 0
        self.sprites.append(pygame.image.load('assets\soldier\Axethrowerwalk001.png'))
        self.image = self.sprites[self.current_sprite]



        # pathfinding
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.soldier[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None

        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]
        self.cible = self
        # selection
        self.selected = False
        self.hitbox = pygame.Rect(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)
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
        self.world.soldier[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.soldier[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]

    #Override
    def update_sprite(self):
        if self.movestraight_animation == True:
            self.temp += 0.2

            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp = 0
        else:
            self.image = self.world.animation.soldier_standby   #Override

            self.current_sprite = int(self.temp)
            if self.temp + 0.2 >= len(self.sprites):
                self.temp = 0
                self.movestraight_animation = False
