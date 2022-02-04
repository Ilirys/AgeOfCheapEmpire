import pygame

#Population
PLAYER_POPULATION = 5

#Time-based settings
UNITS_SPAWN_TIME = 100

# IA 
IA_DECISION_TIME = 1000  #(L'IA prendra une decision chaque X ms au lieu de chaque frame, comme ça 0 perte de fps)
IA_POPULATION = 5
#Speed
DISPLACEMENT_SPEED = {"slow" : 0.5, "normal" : 1, "fast": 5, "veryfast": 8, "potato_pc": 100}


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
NB_RESSOURCES = [150,100,600,600]  #Nombre de bois par arbres, de food par buisson, de gold etc

#Fonts
TAILLE_POLICE=40
DEFAUT_POLICE='assets/font/arialbd.ttf'

#Batiments
dicoBatiment = {"Towncenter" : ["assets/towncenter.png", 2, 2400], "House" : ["assets/house.png", 1, 550], "Barrack" : ["assets/barrack.png", 2, 1200], "Storage" : ["assets/Stable128-64.png", 1, 600], "Farm" : ["assets/stable_tool.png", 2, 480], "Towncenter2" : ["assets/towncenter128-2.png", 2, 2400], "House2" : ["assets/House2.png", 1, 550], "Barrack2" : ["assets/barracks182-2.png", 2, 1200], "Storage2" : ["assets/Stable128-2.png", 1, 600], "Farm2" : ["assets/stable_tool2.png", 2, 480], None : ["", 1] }


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

EFFICIENCY = 1

def init():

    #Minimap
    global afficher_minimap
    afficher_minimap = "oui"

    #Menu options
    global case_coche
    case_coche = 1

    global clik
    clik = 0

    global clik_ia
    clik_ia = 0

    global clik_ress
    clik_ress = 0

    global INIT_RESSOURCE
    INIT_RESSOURCE = [200, 200, 0, 0]

    # Saves
    global SAVED_GAME_FOLDER
    SAVED_GAME_FOLDER = "data/"

    #SPEED
    global CURRENT_SPEED
    CURRENT_SPEED = "fast"

    #Images
    global IMAGE_MENU
    IMAGE_MENU = 'assets/menu_options.png'

    # Statut partie (0: en cours, 1: victoire, 2: défaite)
    global statut_partie
    statut_partie = 0

    #Choix IA
    global strat
    strat = ""
