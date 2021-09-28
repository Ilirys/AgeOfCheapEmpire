import pygame
import sys
from .definitions import *
from .world import World

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.world = World(MAP_SIZE,MAP_SIZE,WIDTH,HEIGHT)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get(): # Si on clique sur la croix pour quitter, on arrete le jeu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self): #A faire
        pass

    def draw(self): #Construction graphiques

        self.screen.fill(BLACK) #Arrière plan
        self.screen.blit(self.world.grass_tiles,(0,0)) #Au lieu d'iterer pour tout les block de fond, ici herbe, on le fait une fois

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                
                #Test si la matrice carthésienne marche
                # sq = self.world.world[x][y]["cart_rect"]
                # rect = pygame.Rect(sq[0][0], sq[0][1],TILE_SIZE,TILE_SIZE)
                # pygame.draw.rect(self.screen,GREEN,rect,1)
                
                render_pos = self.world.world[x][y]["render_pos"]
                # self.screen.blit(self.world.tiles["grass"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))
                tile = self.world.world[x][y]["tile"]
                if tile != "":
                    self.screen.blit(self.world.tiles[tile], (render_pos[0] + self.width/2 +40 , render_pos[1] + self.height/4  -  (self.world.tiles[tile].get_height() - TILE_SIZE +30)))


                p = self.world.world[x][y]["iso_poly"]
                p = [(x + self.width/2, y + self.height/4) for x,y in p]
                pygame.draw.polygon(self.screen,GREEN,p,1)

        pygame.display.flip()

