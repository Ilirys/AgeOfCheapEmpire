import random
from .Tile import Tile
from .definitions import *


class Bouquet:
    
    def __init__(self):
        self.n = MAP_SIZE
        self.random_spawn_wood = 5        #spawn permet de définir le nombre de "bouquet" de ressources
        self.random_spawn_stone = 1.5       #que l'on veut faire
        self.random_spawn_gold = 0.5
        self.random_spawn_fruit = 4
        self.debut_coeff_wood = 80        #debut/fin coeff permet de définir la taille des "bouquets"
        self.fin_coeff_wood = 100
        self.debut_coeff_other = 70
        self.fin_coeff_other = 93
        self.M = [["    " for i in range(self.n)] for j in range(self.n)]
        self.MM = [["" for i in range(self.n)] for j in range(self.n)]
        self.M1 = self.creation_map()


        
    
    def bouquet(self,type_ressource, r, grid_x, grid_y):
        if self.M[grid_x][grid_y] == "    ":
            if r >= 70 :
                self.M[grid_x][grid_y] = type_ressource
                if type_ressource == "wood":
                    if grid_x != self.n - 1:
                        coeff_regressif = random.randint(self.debut_coeff_wood,self.fin_coeff_wood) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x + 1, grid_y)
                    if grid_x != 0:
                        coeff_regressif = random.randint(self.debut_coeff_wood,self.fin_coeff_wood) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x - 1, grid_y)
                    if grid_y != self.n - 1:
                        coeff_regressif = random.randint(self.debut_coeff_wood,self.fin_coeff_wood) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x, grid_y + 1)
                    if grid_y != 0:
                        coeff_regressif = random.randint(self.debut_coeff_wood,self.fin_coeff_wood) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x, grid_y - 1)
                else :
                    if grid_x != self.n - 1:
                        coeff_regressif = random.randint(self.debut_coeff_other, self.fin_coeff_other) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x + 1, grid_y)
                    if grid_x != 0:
                        coeff_regressif = random.randint(self.debut_coeff_other, self.fin_coeff_other) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x - 1, grid_y)
                    if grid_y != self.n - 1:
                        coeff_regressif = random.randint(self.debut_coeff_other, self.fin_coeff_other) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x, grid_y + 1)
                    if grid_y != 0:
                        coeff_regressif = random.randint(self.debut_coeff_other, self.fin_coeff_other) * 0.01
                        self.bouquet(type_ressource, r * coeff_regressif, grid_x, grid_y - 1)


    def creation_map(self):
        for grid_x in range(self.n):
            for grid_y in range(self.n):
                random_choix_ressource = 100*random.random()
                if random_choix_ressource >= 100 - self.random_spawn_wood:
                    r = 100 * random.random()
                    self.bouquet("wood", r, grid_x, grid_y)
                elif random_choix_ressource >= 100 - self.random_spawn_wood - self.random_spawn_stone:
                    r = 100 * random.random()
                    self.bouquet("stone", r, grid_x, grid_y)
                elif random_choix_ressource >= 100 - self.random_spawn_wood - self.random_spawn_stone - self.random_spawn_gold:
                    r = 100 * random.random()
                    self.bouquet("gold", r, grid_x, grid_y)
                elif random_choix_ressource >= 100 - self.random_spawn_wood - self.random_spawn_stone - self.random_spawn_gold - self.random_spawn_fruit:
                    r = 100 * random.random()
                    self.bouquet("fruit", r, grid_x, grid_y)
        
        return self.M

    def bouquet_camp(self,type_ressource, r, grid_x, grid_y):
        if self.MM[grid_x][grid_y] == "":
            if r >= 50 :
                self.MM[grid_x][grid_y] = "wood"
                if grid_x != self.n - 1:
                    coeff_regressif = random.randint(90,100) * 0.01
                    self.bouquet_camp(type_ressource, r * coeff_regressif, grid_x + 1, grid_y)
                if grid_x != 0:
                    coeff_regressif = random.randint(90,100) * 0.01
                    self.bouquet_camp(type_ressource, r * coeff_regressif, grid_x - 1, grid_y)
                if grid_y != self.n - 1:
                    coeff_regressif = random.randint(90,100) * 0.01
                    self.bouquet_camp(type_ressource, r * coeff_regressif, grid_x, grid_y + 1)
                if grid_y != 0:
                    coeff_regressif = random.randint(90,100) * 0.01
                    self.bouquet_camp(type_ressource, r * coeff_regressif, grid_x, grid_y - 1)

    def creation_camp(self, grid_x, grid_y):
        self.bouquet_camp("wood", 100, grid_x, grid_y)
        return self.MM

