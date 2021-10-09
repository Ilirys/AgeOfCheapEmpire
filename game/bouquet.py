import numpy as np
import random
from .Tile import Tile
from .definitions import *
class Bouquet:
    
    def __init__(self):
        self.n = MAP_SIZE
        self.random_wood = 8
        self.random_stone = 5
        self.random_gold = 2.5
        self.random_fruit = 5
        self.M = [["    " for i in range(self.n)] for j in range(self.n)]
        self.M1 = self.creation_map()


        
    
    def bouquet(self,type_ressource, r, grid_x, grid_y):
        if self.M[grid_x][grid_y] == "    ":
            if r >= 70 :
                self.M[grid_x][grid_y] = type_ressource
                if grid_x != self.n - 1:
                    coeff_regressif = random.randint(60,85) * 0.01
                    coeff_regressif += 0.15 if type_ressource == "wood" else 0
                    self.bouquet(type_ressource, r * coeff_regressif, grid_x + 1, grid_y)
                if grid_x != 0:
                    coeff_regressif = random.randint(60,85) * 0.01
                    coeff_regressif += 0.15 if type_ressource == "wood" else 0
                    self.bouquet(type_ressource, r * coeff_regressif, grid_x - 1, grid_y)
                if grid_y != self.n - 1:
                    coeff_regressif = random.randint(60,85) * 0.01
                    coeff_regressif += 0.15 if type_ressource == "wood" else 0
                    self.bouquet(type_ressource, r * coeff_regressif, grid_x, grid_y + 1)
                if grid_y != 0:
                    coeff_regressif = random.randint(60,85) * 0.01
                    coeff_regressif += 0.15 if type_ressource == "wood" else 0
                    self.bouquet(type_ressource, r * coeff_regressif, grid_x, grid_y - 1)

    def creation_map(self):
        for grid_x in range(self.n):
            for grid_y in range(self.n):
                r = 100*random.random()
                if r >= 100 - self.random_wood:
                    r = 100 * random.random()
                    self.bouquet("wood", r, grid_x, grid_y)
                elif r >= 100 - self.random_wood - self.random_stone:
                    r = 100 * random.random()
                    self.bouquet("stone", r, grid_x, grid_y)
                elif r >= 100 - self.random_wood - self.random_stone - self.random_gold:
                    r = 100 * random.random()
                    self.bouquet("gold", r, grid_x, grid_y)
                elif r >= 100 - self.random_wood - self.random_stone - self.random_gold - self.random_fruit:
                    r = 100 * random.random()
                    self.bouquet("fruit", r, grid_x, grid_y)
        
        return self.M            

