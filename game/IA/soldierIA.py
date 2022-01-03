import json
import pygame
import random
from math import *
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game.definitions import CURRENT_SPEED, DISPLACEMENT_SPEED, SAVED_GAME_FOLDER, TILE_SIZE
from game.deplacement import lerp
import pickle
import DTO.soldierDTO
from ..soldier import Soldier


class SoldierIA(Soldier):
    def __init__(self,tile,world,camera, IA,pv=2000,team="red"):
        super().__init__(tile,world,camera, pv, team)
        self.image_standby = pygame.image.load('assets/soldierIA/Halbadierattack011V2.png').convert_alpha()
        self.attacker = 0
        self.attacked = False
        self.IA = IA
        self.IA.warriors.append(self)

    #override

    def update(self):

        if self.dest_tile == self.tile:
            if self.attacked == True :
                self.create_path(self.attacker.tile["grid"][0], self.attacker.tile["grid"][1])
                if self.world.world[self.cible.tile["grid"][0]][self.cible.tile["grid"][1]] != self.world.world[self.temp_tile_a["grid"][0]][self.temp_tile_a["grid"][1]]:
                    if self.cible.dest_tile == self.cible.tile:
                        self.world.world[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]]["collision"] = True
                        self.world.unites[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]] == self.cible
                        self.create_path(self.cible.tile["grid"][0],self.cible.tile["grid"][1])
            #self.create_path(15,15)



        #Updating mouse position and action and the grid_pos
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mouse_pos[0],mouse_pos[1],self.camera.scroll)

        #Hitbox
        self.hitbox.update(self.pos_x  + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)

        #Selection polygon
        pos_poly = [self.pos_x + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x + 47, self.pos_y - self.image.get_height() + self.camera.scroll.y + 50]
        self.iso_poly = [(pos_poly[0] - 10, pos_poly[1] +44), (pos_poly[0] + 15, pos_poly[1] + 29), (pos_poly[0] + 40, pos_poly[1] + 44), (pos_poly[0] + 15 , pos_poly[1] + 59)]

        # collision matrix (for pathfinding and buildings)
        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True

        # Animation update
        self.update_sprite()

        if self.selected:
            if mouse_action[0]:
                self.selected = False
                self.world.hud.select_surface_empty = True
                self.world.hud.display_building_icons = False


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

        if self.hitbox.collidepoint(mouse_pos):
            if mouse_action[0]:
                self.selected = True
                self.sound.play()

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

    def distance_tile(self,tile):
        return sqrt((self.tile["grid"][0] - tile["grid"][0])**2 + (self.tile["grid"][1] - tile["grid"][1])**2)


    def update_sprite(self):
        if self.movestraight_animation == True:
            self.temp += 0.2
            self.image = self.animation[int(self.temp)]
            if self.temp + 0.2 >= len(self.animation):
                self.temp = 0
        elif self.attack_ani == True and self.attack == True:
            self.temp += 0.2
            if self.temp + 0.2 < 10:
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
        else: self.image = self.image_standby