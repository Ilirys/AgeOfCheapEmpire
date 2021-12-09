import pygame


class Animation:

    def __init__(self):
        self.villager_standby = self.animation_villager_standby()
        self.villager_walk = self.animation_villager_walk()
        self.villager_attack = self.animation_villager_attack()
        self.villager_farm = self.animation_villager_farm()
        self.soldier_walk = self.animation_soldier_walk()
        self.soldier_standby = self.animation_soldier_standby()
        self.soldier_attack = self.animation_soldier_attack()
        self.horseman_walk = self.animation_horseman_walk()
        self.horseman_standby = self.animation_horseman_standby()
        self.horseman_attack = self.animation_horseman_attack()
        self.archer_walk = self.animation_archer_walk()
        self.archer_attack = self.animation_archer_attack()
        self.archer_standby = self.animation_archer_standby()
        self.horseman_attack_up = self.animation_horseman_attack_up()
        self.horseman_attack_ldown = self.animation_horseman_attack_ldown()
        self.horseman_attack_left = self.animation_horseman_attack_left()
        self.horseman_attack_uleft = self.animation_horseman_attack_uleft()


    def animation_villager_attack(self):
        villager_attack = []
        villager_attack.append(pygame.image.load('assets/villager/Villageract001.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract002.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract003.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract004.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract005.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract006.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract007.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract008.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract009.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract010.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract011.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract012.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract013.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract014.png').convert_alpha())
        villager_attack.append(pygame.image.load('assets/villager/Villageract015.png').convert_alpha())
        return villager_attack

    def animation_villager_farm(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villageract001.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract002.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract003.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract004.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract005.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract006.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract007.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract008.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract009.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract010.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract011.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract012.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract013.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract014.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villageract015.png').convert_alpha())
        return villager_farm

    def animation_archer_attack(self):
        archer_attack = []
        archer_attack.append(pygame.image.load('assets/archer/Archerattack001.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack002.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack003.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack004.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack005.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack006.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack007.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack008.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack009.png').convert_alpha())
        archer_attack.append(pygame.image.load('assets/archer/Archerattack010.png').convert_alpha())
        return archer_attack

    def animation_horseman_attack(self):
        horseman_attack = []
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack001.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack002.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack003.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack004.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack005.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack006.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack007.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack008.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack009.png').convert_alpha())
        horseman_attack.append(pygame.image.load('assets/horseman/Cavalierattack010.png').convert_alpha())
        return horseman_attack

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
        img = pygame.image.load('assets/soldier/Halbadierwalk001.png').convert_alpha()
        return img

    def animation_soldier_walk(self):
        soldier_walk = []
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk001.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk002.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk003.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk004.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk005.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk006.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk007.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk008.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk009.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk010.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk011.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk012.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk013.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk014.png').convert_alpha())
        soldier_walk.append(pygame.image.load('assets\soldier\Halbadierwalk015.png').convert_alpha())
        return soldier_walk

    def animation_horseman_standby(self):
        img = pygame.image.load('assets/horseman/Cavalierwalk001.png').convert_alpha()
        return img

    def animation_horseman_walk(self):
        horseman_walk = []
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk001.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk002.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk003.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk004.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk005.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk006.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk007.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk008.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk009.png').convert_alpha())
        horseman_walk.append(pygame.image.load('assets/horseman/Cavalierwalk010.png').convert_alpha())
        return horseman_walk
    
    def animation_soldier_attack(self):
        soldier_attack = []
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack001.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack002.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack003.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack004.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack005.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack006.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack007.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack008.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack009.png').convert_alpha())
        soldier_attack.append(pygame.image.load('assets/soldier/Halbadierattack010.png').convert_alpha())
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

    def animation_horseman_attack_up(self):
        horseman_attack_up = []
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack041.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack042.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack043.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack044.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack045.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack046.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack047.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack048.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack049.png').convert_alpha())
        horseman_attack_up.append(pygame.image.load('assets/horseman/Cavalierattack050.png').convert_alpha())
        return horseman_attack_up


    def animation_horseman_attack_ldown(self):
        horseman_attack_ldown = []
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack011.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack012.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack013.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack014.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack015.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack016.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack017.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack018.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack019.png').convert_alpha())
        horseman_attack_ldown.append(pygame.image.load('assets/horseman/Cavalierattack020.png').convert_alpha())
        return horseman_attack_ldown

    def animation_horseman_attack_left(self):
        horseman_attack_left = []
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack021.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack022.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack023.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack024.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack025.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack026.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack027.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack028.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack029.png').convert_alpha())
        horseman_attack_left.append(pygame.image.load('assets/horseman/Cavalierattack030.png').convert_alpha())
        return horseman_attack_left

    def animation_horseman_attack_uleft(self):
        horseman_attack_uleft = []
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack031.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack032.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack033.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack034.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack035.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack036.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack037.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack038.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack039.png').convert_alpha())
        horseman_attack_uleft.append(pygame.image.load('assets/horseman/Cavalierattack040.png').convert_alpha())
        return horseman_attack_uleft