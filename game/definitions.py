import pygame

#Saves
SAVED_GAME_FOLDER = "data/"

#Speed
DISPLACEMENT_SPEED = {"slow" : 0.5, "normal" : 1, "fast": 3, "potato_pc": 8}
CURRENT_SPEED = "potato_pc"

#Screen
BENCHMARK = 0
FULLSCREEN1 = 1
WIDTH, HEIGHT = 1300,1000  #La définition de l'écran facilement modifiable
FPS = 200

#Map
TILE_SIZE = 64
MAP_SIZE = 50

#Resource
LES_RESSOURCES = ["wood", "food", "gold", "stone"]
INIT_RESSOURCE = [2000, 1000, 10, 0]
NB_RESSOURCES = [60,100,30,40]  #Nombre de bois par arbres, de food par buisson, de gold etc

#Fonts
TAILLE_POLICE=40
DEFAUT_POLICE='assets/font/arialbd.ttf'

#Batiments
dicoBatiment = {"Towncenter" : ["assets/towncenter.png", 2, 0, 0], "House" : ["assets/house.png", 1, 0, 0], "Barrack" : ["assets/barrack.png", 2, 175, 128], None : ["", 1] }

#Colors
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GreenLight=(75,128,75,200)
Green=(20,100,20,235)
Grey=(128,128,128)
Gold=(200,200,128)
Brown=(70,33, 0)
Red=(175,0,0)
Blue=(0,128,255)