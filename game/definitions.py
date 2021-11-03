import pygame

#Speed
DISPLACEMENT_SPEED = {"slow" : 0.5, "normal" : 1, "fast": 3, "potato_pc": 8}
CURRENT_SPEED = "normal"

#Screen
BENCHMARK = 0
FULLSCREEN1 = 1
WIDTH, HEIGHT = 1300,1000  #La définition de l'écran facilement modifiable
FPS = 200

#Map
TILE_SIZE = 64
MAP_SIZE = 50

#Resource
LES_RESSOURCES = {"WOOD", "FOOD", "GOLD", "STONE"}
NB_RESSOURCES = [60,100,30,40]  #Nombre de bois par arbres, de food par buisson, de gold etc

#Fonts
TAILLE_POLICE=40
DEFAUT_POLICE='assets/font/arialbd.ttf'

#Colors
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)