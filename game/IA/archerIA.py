import pygame
import random
import game.definitions as definitions
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from ..definitions import *
from math import *
from game.deplacement import lerp
from ..archer import Archer

class ArcherIA(Archer):

    def __init__(self,tile,world,camera, IA, pv=2000,team="red"):
        super().__init__(tile,world,camera,pv,team)
        self.IA = IA
        self.busy = False
        self.attacked = False
        self.attacker = 0
        self.IA.ressource_manager.apply_cost_to_resource(self.name)
        self.IA.ressource_manager.population += 1
        self.IA.warriors.append(self)
        self.image_standby = pygame.image.load('assets/archerIA/Archerwalk001V2.png').convert_alpha()
        self.animation = self.world.animation.archerIA_walk
        self.animation_attack = self.world.animation.archerIA_attack
        self.animation_attack_up = self.world.animation.archerIA_attack_up
        self.animation_attack_ldown = self.world.animation.archerIA_attack_ldown
        self.animation_attack_left = self.world.animation.archerIA_attack_left
        self.animation_attack_uleft = self.world.animation.archerIA_attack_uleft
        self.animation_attack_right = self.world.animation.archerIA_attack_right
        self.animation_attack_uright = self.world.animation.archerIA_attack_uright
        self.animation_attack_rdown = self.world.animation.archerIA_attack_rdown

        #Lists
        self.IA.warriors.append(self)
        self.IA.archers[tile["grid"][0]][tile["grid"][1]] = self

    # override

    def update(self):
        # collision matrix (for pathfinding and buildings)


        if self.attack == False and self.attack_bati == False and self.attacked == False:
            if self.tile == self.dest_tile:
                self.dest_tile = 0


        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True

        # Animation update
        self.update_sprite()

        if self.dest_tile == self.tile:
            if self.attack:
                self.attack_ani = True
                if self.cible != 0 and self.cible is not None:
                    self.cible.pv -= self.dmg
                # self.cible.create_path(self.tile["grid"][0],self.tile["grid"][1])
                if self.world.world[self.cible.tile["grid"][0]][self.cible.tile["grid"][1]] != self.world.world[self.temp_tile_a["grid"][0]][self.temp_tile_a["grid"][1]]:
                    #if self.cible.dest_tile == self.cible.tile:
                        #self.world.world[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]]["collision"] = True
                        #self.world.unites[self.cible.dest_tile["grid"][0]][self.cible.dest_tile["grid"][1]] == self.cible
                        if self.cible is not None and self.cible != 0:
                            self.create_path(self.cible.tile["grid"][0], self.cible.tile["grid"][1])
                        self.cible.dest_tile = 0
                if self.cible is None or self.cible.pv <= 0:
                    self.attack = False
                    #self.cible.attacked = False
                    self.attack_ani = False
                    self.cible = 0
            elif self.attack_bati:
                self.walkdown_animation = False
                self.attack_ani = True
                if self.cible is not None and self.cible != 0:
                    self.cible.pv -= self.dmg
                    if self.cible is None or self.cible.pv <= 0:
                        self.attack = False
                        self.attack_ani = False


        if self.path_index <= len(self.path) - 1:
            if self.dest_tile != self.tile:
                self.walkdown_animation = True

            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.progression < 1:
                self.progression += (1 / 135) * definitions.DISPLACEMENT_SPEED[definitions.CURRENT_SPEED]
                self.progression = round(self.progression, 4)
            else:
                self.progression = 1
            self.pos_x = round(lerp(self.tile["render_pos"][0], new_real_pos[0], self.progression), 3)
            self.pos_y = round(lerp(self.tile["render_pos"][1], new_real_pos[1], self.progression), 3)

            if self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]:  # now - self.move_timer > 1000:  # update position in the world
                self.world.collision_matrix[self.tile["grid"][1]][
                    self.tile["grid"][0]] = 1  # Free the last tile from collision
                self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False
                self.change_tile(new_pos)
                self.progression = 0

        else:
            self.walkdown_animation = False



    #override
    def change_tile(self, new_tile):
        if not self.world.world[new_tile[0]][new_tile[1]]["collision"]:
            self.IA.archers[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.IA.archers[new_tile[0]][new_tile[1]] = self
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[new_tile[0]][new_tile[1]] = self

            self.tile = self.world.world[new_tile[0]][new_tile[1]]
            self.render_pos_x = self.tile["render_pos"][0]
            self.render_pos_y = self.tile["render_pos"][1]

            # collision matrix (for pathfinding and buildings)
            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
            self.path_index += 1
        else:
            self.create_path(self.dest_tile["grid"][0], self.dest_tile["grid"][1])
            print(1)
            self.render_pos_x = self.pos_x
            self.render_pos_y = self.pos_y

    def delete(self):
        
        
        self.IA.ressource_manager.population -= 1  

        self.world.entities.remove(self)

        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

        self.IA.archers[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.selected = False
        self.temp = 0           

