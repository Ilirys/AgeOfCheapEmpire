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
        self.horseman_attack_right = self.animation_horseman_attack_right()
        self.horseman_attack_uright = self.animation_horseman_attack_uright()
        self.horseman_attack_rdown = self.animation_horseman_attack_rdown()
        self.archer_attack_up = self.animation_archer_attack_up()
        self.archer_attack_ldown = self.animation_archer_attack_ldown()
        self.archer_attack_left = self.animation_archer_attack_left()
        self.archer_attack_uleft = self.animation_archer_attack_uleft()
        self.archer_attack_right = self.animation_archer_attack_right()
        self.archer_attack_uright = self.animation_archer_attack_uright()
        self.archer_attack_rdown = self.animation_archer_attack_rdown()
        self.soldier_attack_up = self.animation_soldier_attack_up()
        self.soldier_attack_ldown = self.animation_soldier_attack_ldown()
        self.soldier_attack_left = self.animation_soldier_attack_left()
        self.soldier_attack_uleft = self.animation_soldier_attack_uleft()
        self.soldier_attack_right = self.animation_soldier_attack_right()
        self.soldier_attack_uright = self.animation_soldier_attack_uright()
        self.soldier_attack_rdown = self.animation_soldier_attack_rdown()
        self.villager_mort = self.animation_villager_mort()
        self.horseman_mort = self.animation_horseman_mort()
        self.archer_mort = self.animation_archer_mort()
        self.soldier_mort = self.animation_soldier_mort()
        self.soldierIA_walk = self.animation_soldierIA_walk()
        self.villagerIA_walk = self.animation_villagerIA_walk()
        self.horsemanIA_walk = self.animation_horsemanIA_walk()
        self.archerIA_walk = self.animation_archerIA_walk()

        self.bigdaddy_standby = self.animation_bigdaddy_standby()
        self.bigdaddy_walk_left = self.animation_bigdaddy_walk_left()
        self.bigdaddy_walk_right = self.animation_bigdaddy_walk_right()
        self.bigdaddy_attack_right = self.animation_bigdaddy_attack_right()
        self.bigdaddy_attack_left = self.animation_bigdaddy_attack_left()
        self.bigdaddy_attack_down_left = self.animation_bigdaddy_attack_down_left()
        self.bigdaddy_attack_down_right = self.animation_bigdaddy_attack_down_right()
        self.bigdaddy_attack_up_left = self.animation_bigdaddy_attack_up_left()
        self.bigdaddy_attack_up_right = self.animation_bigdaddy_attack_up_right()

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
        villager_walk.append(pygame.image.load('assets/sprites/villager/Villagerwalk015.png').convert_alpha())
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


    def animation_horseman_attack_uright(self):
        horseman_attack_uright = []
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (1).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (2).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (3).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (4).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (5).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (6).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (7).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (8).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (9).png').convert_alpha())
        horseman_attack_uright.append(pygame.image.load('assets/horseman/Cavalierattack031r (10).png').convert_alpha())
        return horseman_attack_uright


    def animation_horseman_attack_right(self):
        horseman_attack_right = []
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (1).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (2).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (3).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (4).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (5).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (6).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (7).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (8).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (9).png').convert_alpha())
        horseman_attack_right.append(pygame.image.load('assets/horseman/Cavalierattack030r (10).png').convert_alpha())
        return horseman_attack_right


    def animation_horseman_attack_rdown(self):
        horseman_attack_rdown = []
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (1).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (2).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (3).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (4).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (5).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (6).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (7).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (8).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (9).png').convert_alpha())
        horseman_attack_rdown.append(pygame.image.load('assets/horseman/Cavalierattack020r (10).png').convert_alpha())
        return horseman_attack_rdown


    def animation_archer_attack_right(self):
        archer_attack_right = []
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (1).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (2).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (3).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (4).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (5).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (6).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (7).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (8).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (9).png').convert_alpha())
        archer_attack_right.append(pygame.image.load('assets/archer/Archerattack030r (10).png').convert_alpha())
        return archer_attack_right

    def animation_archer_attack_uright(self):
        archer_attack_uright = []
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (1).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (2).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (3).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (4).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (5).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (6).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (7).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (8).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (9).png').convert_alpha())
        archer_attack_uright.append(pygame.image.load('assets/archer/Archerattack040r (10).png').convert_alpha())
        return archer_attack_uright

    def animation_archer_attack_rdown(self):
        archer_attack_rdown = []
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (1).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (2).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (3).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (4).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (5).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (6).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (7).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (8).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (9).png').convert_alpha())
        archer_attack_rdown.append(pygame.image.load('assets/archer/Archerattack020r (10).png').convert_alpha())
        return archer_attack_rdown


    def animation_archer_attack_up(self):
        archer_attack_up = []
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack041.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack042.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack043.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack044.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack045.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack046.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack047.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack048.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack049.png').convert_alpha())
        archer_attack_up.append(pygame.image.load('assets/archer/Archerattack050.png').convert_alpha())
        return archer_attack_up


    def animation_archer_attack_ldown(self):
        archer_attack_ldown = []
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack011.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack012.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack013.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack014.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack015.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack016.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack017.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack018.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack019.png').convert_alpha())
        archer_attack_ldown.append(pygame.image.load('assets/archer/Archerattack020.png').convert_alpha())
        return archer_attack_ldown


    def animation_archer_attack_uleft(self):
        archer_attack_uleft = []
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack031.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack032.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack033.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack034.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack035.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack036.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack037.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack038.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack039.png').convert_alpha())
        archer_attack_uleft.append(pygame.image.load('assets/archer/Archerattack040.png').convert_alpha())
        return archer_attack_uleft

    def animation_archer_attack_left(self):
        archer_attack_left = []
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack021.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack022.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack023.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack024.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack025.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack026.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack027.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack028.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack029.png').convert_alpha())
        archer_attack_left.append(pygame.image.load('assets/archer/Archerattack030.png').convert_alpha())
        return archer_attack_left


    def animation_soldier_attack_uright(self):
        soldier_attack_uright = []
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (1).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (2).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (3).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (4).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (5).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (6).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (7).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (8).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (9).png').convert_alpha())
        soldier_attack_uright.append(pygame.image.load('assets/soldier/Halbadierattack040r (10).png').convert_alpha())
        return soldier_attack_uright


    def animation_soldier_attack_right(self):
        soldier_attack_right = []
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (1).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (2).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (3).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (4).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (5).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (6).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (7).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (8).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (9).png').convert_alpha())
        soldier_attack_right.append(pygame.image.load('assets/soldier/Halbadierattack030r (10).png').convert_alpha())
        return soldier_attack_right


    def animation_soldier_attack_rdown(self):
        soldier_attack_rdown = []
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (1).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (2).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (3).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (4).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (5).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (6).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (7).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (8).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (9).png').convert_alpha())
        soldier_attack_rdown.append(pygame.image.load('assets/soldier/Halbadierattack020r (10).png').convert_alpha())
        return soldier_attack_rdown


    def animation_soldier_attack_up(self):
        soldier_attack_up = []
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack041.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack042.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack043.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack044.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack045.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack046.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack047.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack048.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack049.png').convert_alpha())
        soldier_attack_up.append(pygame.image.load('assets/soldier/Halbadierattack050.png').convert_alpha())
        return soldier_attack_up


    def animation_soldier_attack_uleft(self):
        soldier_attack_uleft = []
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack031.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack032.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack033.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack034.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack035.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack036.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack037.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack038.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack039.png').convert_alpha())
        soldier_attack_uleft.append(pygame.image.load('assets/soldier/Halbadierattack040.png').convert_alpha())
        return soldier_attack_uleft

    def animation_soldier_attack_left(self):
        soldier_attack_left = []
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack021.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack022.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack023.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack024.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack025.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack026.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack027.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack028.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack029.png').convert_alpha())
        soldier_attack_left.append(pygame.image.load('assets/soldier/Halbadierattack030.png').convert_alpha())
        return soldier_attack_left


    def animation_soldier_attack_ldown(self):
        soldier_attack_ldown = []
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack011.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack012.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack013.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack014.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack015.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack016.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack017.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack018.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack019.png').convert_alpha())
        soldier_attack_ldown.append(pygame.image.load('assets/soldier/Halbadierattack020.png').convert_alpha())
        return soldier_attack_ldown

    def animation_villager_mort(self):
        villager_mort = []
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie001.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie002.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie003.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie004.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie005.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie006.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie007.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie008.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie009.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie010.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie011.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie012.png').convert_alpha())
        return villager_mort

    def animation_villager_mort(self):
        villager_mort = []
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie001.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie002.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie003.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie004.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie005.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie006.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie007.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie008.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie009.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie010.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie011.png').convert_alpha())
        villager_mort.append(pygame.image.load('assets/villager/Villagerdie012.png').convert_alpha())
        return villager_mort


    def animation_horseman_mort(self):
        horseman_mort = []
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie001.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie002.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie003.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie004.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie005.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie006.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie007.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie008.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie009.png').convert_alpha())
        horseman_mort.append(pygame.image.load('assets/horseman/Cavalierdie010.png').convert_alpha())
        return horseman_mort

    def animation_archer_mort(self):
        archer_mort = []
        archer_mort.append(pygame.image.load('assets/archer/Archerdie001.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie002.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie003.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie004.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie005.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie006.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie007.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie008.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie009.png').convert_alpha())
        archer_mort.append(pygame.image.load('assets/archer/Archerdie010.png').convert_alpha())
        return archer_mort

    def animation_soldier_mort(self):
        soldier_mort = []
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie001.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie002.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie003.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie004.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie005.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie006.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie007.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie008.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie009.png').convert_alpha())
        soldier_mort.append(pygame.image.load('assets/soldier/Halbadierdie010.png').convert_alpha())
        return soldier_mort



    def animation_soldierIA_walk(self):
        soldierIA_walk = []
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk001V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk002V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk003V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk004V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk005V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk006V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk007V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk008V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk009V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk010V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk011V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk012V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk013V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk014V2.png').convert_alpha())
        soldierIA_walk.append(pygame.image.load('assets\soldierIA\Halbadierwalk015V2.png').convert_alpha())
        return soldierIA_walk



    def animation_villagerIA_walk(self):
        villagerIA_walk = []
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk001V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk002V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk003V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk004V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk005V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk006V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk007V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk008V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk009V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk010V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk011V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk012V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk013V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk014V2.png').convert_alpha())
        villagerIA_walk.append(pygame.image.load('assets/villagerIA/Villagerwalk015V2.png').convert_alpha())
        return villagerIA_walk

    def animation_archerIA_walk(self):
        archerIA_walk = []
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk001V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk002V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk003V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk004V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk005V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk006V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk007V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk008V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk009V2.png').convert_alpha())
        archerIA_walk.append(pygame.image.load('assets/archerIA/Archerwalk010V2.png').convert_alpha())
        return archerIA_walk

    def animation_horsemanIA_walk(self):
        horsemanIA_walk = []
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk001V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk002V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk003V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk004V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk005V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk006V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk007V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk008V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk009V2.png').convert_alpha())
        horsemanIA_walk.append(pygame.image.load('assets/horsemanIA/Cavalierwalk010V2.png').convert_alpha())
        return horsemanIA_walk

    def animation_bigdaddy_standby(self):
        bigdaddy_standby = []
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img.png').convert_alpha())
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img_1.png').convert_alpha())
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img_2.png').convert_alpha())
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img_3.png').convert_alpha())
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img_4.png').convert_alpha())
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img_5.png').convert_alpha())
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img_6.png').convert_alpha())
        bigdaddy_standby.append(pygame.image.load('assets/bigdaddy/img_7.png').convert_alpha())
        return bigdaddy_standby

    def animation_bigdaddy_walk_right(self):
        bigdaddy_walk = []
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_12.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_13.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_14.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_15.png').convert_alpha())
        """bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_12.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_13.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_14.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_15.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_12.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_13.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_14.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_15.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_12.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_13.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_14.png').convert_alpha())
        bigdaddy_walk.append(pygame.image.load('assets/bigdaddy/img_15.png').convert_alpha())"""
        return bigdaddy_walk

    def animation_bigdaddy_walk_left(self):
        bigdaddy_walk = self.animation_bigdaddy_walk_right()
        for i in range(len(bigdaddy_walk)):
            bigdaddy_walk[i] = pygame.transform.flip(bigdaddy_walk[i], True, False)
        return bigdaddy_walk


    def animation_bigdaddy_attack_right(self):
        bigdaddy_attack = []
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_20.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_21.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_22.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_23.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_24.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_25.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_26.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_27.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_28.png').convert_alpha())
        return bigdaddy_attack

    def animation_bigdaddy_attack_left(self):
        bigdaddy_attack = self.animation_bigdaddy_attack_right()
        for i in range(len(bigdaddy_attack)):
            bigdaddy_attack[i] = pygame.transform.flip(bigdaddy_attack[i], True, False)
        return bigdaddy_attack

    def animation_bigdaddy_attack_up_right(self):
        bigdaddy_attack = []
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_29.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_30.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_31.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_32.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_33.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_34.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_35.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_36.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_37.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_38.png').convert_alpha())
        return bigdaddy_attack

    def animation_bigdaddy_attack_up_left(self):
        bigdaddy_attack = self.animation_bigdaddy_attack_up_right()
        for i in range(len(bigdaddy_attack)):
            bigdaddy_attack[i] = pygame.transform.flip(bigdaddy_attack[i], True, False)
        return bigdaddy_attack

    def animation_bigdaddy_attack_down_right(self):
        bigdaddy_attack = []
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_39.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_40.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_41.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_42.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_43.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_44.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_45.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_46.png').convert_alpha())
        bigdaddy_attack.append(pygame.image.load('assets/bigdaddy/img_47.png').convert_alpha())
        return bigdaddy_attack

    def animation_bigdaddy_attack_down_left(self):
        bigdaddy_attack = self.animation_bigdaddy_attack_down_right()
        for i in range(len(bigdaddy_attack)):
            bigdaddy_attack[i] = pygame.transform.flip(bigdaddy_attack[i], True, False)
        return bigdaddy_attack