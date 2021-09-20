import pygame
import os

from pygame.time import Clock

WIDTH, HEIGHT = 900, 500 #La définition de l'écran facilement modifiable, (0,0)= plein écran
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.display.set_caption("Age of Cheap Empire") #Nom du jeu affiché sur la fenetre

def drawGrid():
    blocksize = 20 #La taille d'un carré 
    for x in range(0,WIDTH,blocksize):
        for y in range(0,HEIGHT,blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize) # rect est un objet qui store des coordonnées rectangulaire. (A utiliser pour placer les batiments, tout déplacement..?)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def main():
    SCREEN.fill(GREEN)
    CLOCK = pygame.time.Clock()
    while True:
        drawGrid()
        CLOCK.tick(FPS)
        for event in pygame.event.get(): # Si on clique sur la croix pour quitter, on arrete le jeu
            if event.type == pygame.QUIT:
                pygame.quit()
                os.sys.exit()
        pygame.display.update()
    pygame.quit()   #Quite proprement en cas de plantage

             



#La fonction main() ne doit etre appelée que si on execute main.py, pas dans un autre fichier.py
if __name__ == "__main__":
    main()


