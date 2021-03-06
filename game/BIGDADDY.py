import pygame

from .soldier import Soldier

class Bigdaddy(Soldier):

    def __init__(self, tile, world, camera, pv=100000,  team="blue"):
        super().__init__(tile, world, camera, pv, team)
        self.name = "Bigdaddy"
        self.dmg = 50
        self.animation_left = self.world.animation.bigdaddy_walk_left
        self.animation_right = self.world.animation.bigdaddy_walk_right
        self.animation_attack = self.world.animation.bigdaddy_attack_down_right
        self.animation_attack_up = self.world.animation.bigdaddy_attack_up_right
        self.animation_attack_ldown = self.world.animation.bigdaddy_attack_down_left
        self.animation_attack_left = self.world.animation.bigdaddy_attack_left
        self.animation_attack_uleft = self.world.animation.bigdaddy_attack_up_left
        self.animation_attack_right = self.world.animation.bigdaddy_attack_right
        self.animation_attack_uright = self.world.animation.bigdaddy_attack_up_right
        self.animation_attack_rdown = self.world.animation.bigdaddy_attack_down_right
        #self.animation_mort = self.world.animation.bigdaddy_mort

        self.image = pygame.image.load('assets/bigdaddy/img.png').convert_alpha()
        self.image_standby = pygame.image.load('assets/bigdaddy/img.png').convert_alpha()

        # pathfinding
        self.world.unites[tile["grid"][0]][tile["grid"][1]] = self
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = None
        if self.team == "blue":
            self.world.bigdaddy[tile["grid"][0]][tile["grid"][1]] = self

        # selection
        self.hitbox = pygame.Rect(self.pos_x + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 75, 28, 60)  # Overriden

    # Override
    def change_tile(self, new_tile):
        if not self.world.world[new_tile[0]][new_tile[1]]["collision"]:
            self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.unites[new_tile[0]][new_tile[1]] = self
            self.world.bigdaddy[self.tile["grid"][0]][self.tile["grid"][1]] = None
            self.world.bigdaddy[new_tile[0]][new_tile[1]] = self

            self.tile = self.world.world[new_tile[0]][new_tile[1]]
            self.render_pos_x = self.tile["render_pos"][0]
            self.render_pos_y = self.tile["render_pos"][1]

            self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
            self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True
            self.path_index += 1
        else:
            if self.dest_tile != 0:self.create_path(self.dest_tile["grid"][0], self.dest_tile["grid"][1])
            self.render_pos_x = self.pos_x
            self.render_pos_y = self.pos_y

                #Override
    def update_sprite(self):
       if self.walkdown_animation == True:
            if self.dest_tile !=0:
                if self.dest_tile["grid"][0] <= self.tile["grid"][0] and self.dest_tile["grid"][1] >= self.tile["grid"][1]:
                    self.temp += 0.2
                    self.image = self.animation_left[int(self.temp)]
                    if self.temp + 0.2 >= len(self.animation_left):
                        self.temp = 0
                else:
                    self.temp += 0.2
                    self.image = self.animation_right[int(self.temp)]
                    if self.temp + 0.2 >= len(self.animation_right):
                        self.temp = 0
       elif self.attack_ani == True and self.attack == True:
           if self.temp + 0.2 >= 9:
               self.temp = 0
           self.temp +=0.2
           if self.cible.tile["grid"][0] < self.tile["grid"][0] and self.cible.tile["grid"][1] < self.tile["grid"][1]:
               self.image = self.animation_attack_uright[int(self.temp)]
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
               self.temp= 0
       elif self.pv > 0: self.image = self.image_standby

   #Override
    def delete(self):
       self.world.entities.remove(self)

       self.world.collision_matrix[self.tile["grid"][1]][
           self.tile["grid"][0]] = 1  # Free the last tile from collision
       self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

       self.world.bigdaddy[self.tile["grid"][0]][self.tile["grid"][1]] = None
       self.world.unites[self.tile["grid"][0]][self.tile["grid"][1]] = None
       self.selected = False
       self.temp = 0
