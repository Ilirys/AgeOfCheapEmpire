import pygame


class Animation:

    def __init__(self):
        self.villager_standby = self.animation_villager_standby()
        self.villager_walk = self.animation_villager_walk()
        self.soldier_walk = self.animation_soldier_walk()
        self.soldier_standby = self.animation_soldier_standby()
        self.horseman_walk = self.animation_horseman_walk()
        self.horseman_standby = self.animation_horseman_standby()
        self.soldier_attack = self.animation_soldier_attack()
        self.archer_walk = self.animation_archer_walk()
        self.archer_standby = self.animation_archer_standby()
        
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

    def animation_soldier_standby(self):
        img = pygame.image.load('assets/soldier/Axethrowerwalk001.png').convert_alpha()
        return img

    def animation_soldier_walk(self):
        soldier_walk = []
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk001.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk002.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk003.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk004.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk005.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk006.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk007.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk008.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk009.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk010.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk011.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk012.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk013.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Axethrowerwalk014.png').convert_alpha())
        return soldier_walk

    def animation_horseman_standby(self):
        img = pygame.image.load('assets/horseman/Scoutwalk001.png').convert_alpha()
        return img

    def animation_horseman_walk(self):
        horseman_walk = []
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk001.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk002.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk003.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk004.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk005.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk006.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk007.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk008.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk009.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Scoutwalk010.png').convert_alpha())
        return horseman_walk
    
    def animation_soldier_attack(self):
        soldier_attack = []
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack001.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack002.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack003.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack004.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack005.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack006.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack007.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack008.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack009.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack010.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack011.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack012.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack013.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack014.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Axethrowerattack015.png').convert_alpha())
        return soldier_attack

    def animation_archer_walk(self):
        archer_walk = []
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk001.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk002.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk003.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk004.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk005.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk006.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk007.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk008.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk009.png').convert_alpha())
        archer_walk.append(pygame.image.load('assets/archer/Archerwalk010.png').convert_alpha())
        return archer_walk

    def animation_archer_standby(self):
        img = pygame.image.load('assets/archer/Archerwalk001.png').convert_alpha()
        return img