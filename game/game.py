import pygame
import sys
from .definitions import *
from .world import World
from .utils import draw_text
from .camera import Camera

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        #World
        self.world = World(MAP_SIZE,MAP_SIZE,WIDTH,HEIGHT)

        #Camera
        self.camera = Camera(WIDTH, HEIGHT)

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

    def update(self): 
        self.camera.update()

    def draw(self): #Construction graphiques

        self.screen.fill(BLACK) #Arrière plan
        self.screen.blit(self.world.grass_tiles,(self.camera.scroll.x, self.camera.scroll.y)) #Au lieu d'iterer pour tout les block de fond, ici herbe, on le fait une fois

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                
                #Test si la matrice carthésienne marche
                # sq = self.world.world[x][y]["cart_rect"]
                # rect = pygame.Rect(sq[0][0], sq[0][1],TILE_SIZE,TILE_SIZE)
                # pygame.draw.rect(self.screen,GREEN,rect,1)
                
                render_pos = self.world.world[x][y]["render_pos"]
                # self.screen.blit(self.world.tiles["grass"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))
                extras = self.world.world[x][y]["extras"]
                if extras != "":
                    self.screen.blit(self.world.tiles[extras], (render_pos[0] + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x +40, render_pos[1] -  (self.world.tiles[extras].get_height() - TILE_SIZE + 30) +self.camera.scroll.y))


                #p = self.world.world[x][y]["iso_poly"]
                #p = [(x + self.width/2, y + self.height/4) for x,y in p]
                #pygame.draw.polygon(self.screen,GREEN,p,1)

        draw_text(self.screen,'FPS = {}'.format(round(self.clock.get_fps())),25,WHITE,(10,10))
    
        pygame.display.flip()

