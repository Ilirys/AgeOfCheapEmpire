import pygame
import os 
from game import definitions
from game.game import Game


def main():

    running = True
    playing = True

    pygame.init()
    pygame.mixer.init() #son a implementer 
    SCREEN = pygame.display.set_mode((definitions.WIDTH, definitions.HEIGHT))
    pygame.display.set_caption("Age of Cheap Empire") #Nom du jeu affiché sur la fenetre
    clock = pygame.time.Clock()

    #implement menus

    #implement game
    game = Game(SCREEN,clock)

    while running:

        # start menu goes here
        while playing:
            # game loop here
            game.run()

#La fonction main() ne doit etre appelée que si on execute main.py, pas dans un autre fichier.py
if __name__ == "__main__":
    main()            










