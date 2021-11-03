import pygame


class Animation:

    def __init__(self):
        self.villager_standby = self.animation_villager_standby()
        self.villager_walk = self.animation_villager_walk()

    def animation_villager_standby(self):
        img = pygame.image.load('assets/sprites/villager/Villager.png').convert_alpha()
        return img

    def animation_villager_walk(self):
        villager_walk = []
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk001.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk002.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk003.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk004.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk005.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk006.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk007.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk008.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk009.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk010.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk011.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk012.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk013.png').convert_alpha())
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk014.png').convert_alpha())
        return villager_walk 