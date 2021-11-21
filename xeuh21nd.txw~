import pygame
import os 
import _thread
from game import definitions
from game import ecranDemarrage
from game.game import Game
from game.font import *
from pygame.locals import *
from game.ecranDemarrage import StartScreen
from game.bouquet import Bouquet


def main():
    
    running = True
    playing = True

    pygame.init()
    pygame.mixer.init() #son a implementer 
    infoscreen = pygame.display.Info()
    if FULLSCREEN1 == 1: definitions.WIDTH, definitions.HEIGHT = infoscreen.current_w, infoscreen.current_h
    SCREEN = pygame.display.set_mode((definitions.WIDTH, definitions.HEIGHT),pygame.HWSURFACE | pygame.HWACCEL)
    pygame.display.set_caption("Age of Cheap Empire") #Nom du jeu affiché sur la fenetre	
    pygame.display.set_icon(pygame.image.load("assets/Icone.jpg").convert_alpha())
    clock = pygame.time.Clock()

    #implement menus

    #implement game
    print(SCREEN.get_size())
    game = Game(SCREEN,clock)
    startscreen = StartScreen(SCREEN, clock)

    while running:

        # start menu goes here
        #startscreen.ecran_demarrage()
        while playing:
            # game loop here
            game.run()

#La fonction main() ne doit etre appelée que si on execute main.py, pas dans un autre fichier.py
if __name__ == "__main__":
    main()            










