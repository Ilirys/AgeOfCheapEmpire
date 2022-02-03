import pygame


class Animation:

    def __init__(self):
        self.villager_standby = self.animation_villager_standby()
        self.villager_walk = self.animation_villager_walk()
        self.villager_attack = self.animation_villager_attack()
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
        self.soldierIA_attack_up = self.animation_soldierIA_attack_up()
        self.soldierIA_attack_ldown = self.animation_soldierIA_attack_ldown()
        self.soldierIA_attack_left = self.animation_soldierIA_attack_left()
        self.soldierIA_attack_uleft = self.animation_soldierIA_attack_uleft()
        self.soldierIA_attack_right = self.animation_soldierIA_attack_right()
        self.soldierIA_attack_uright = self.animation_soldierIA_attack_uright()
        self.soldierIA_attack_rdown = self.animation_soldierIA_attack_rdown()
        self.soldierIA_attack = self.animation_soldierIA_attack()
        self.archerIA_attack_up = self.animation_archerIA_attack_up()
        self.archerIA_attack_ldown = self.animation_archerIA_attack_ldown()
        self.archerIA_attack_left = self.animation_archerIA_attack_left()
        self.archerIA_attack_uleft = self.animation_archerIA_attack_uleft()
        self.archerIA_attack_right = self.animation_archerIA_attack_right()
        self.archerIA_attack_uright = self.animation_archerIA_attack_uright()
        self.archerIA_attack_rdown = self.animation_archerIA_attack_rdown()
        self.archerIA_attack = self.animation_archerIA_attack()
        self.horsemanIA_attack_up = self.animation_horsemanIA_attack_up()
        self.horsemanIA_attack_ldown = self.animation_horsemanIA_attack_ldown()
        self.horsemanIA_attack_left = self.animation_horsemanIA_attack_left()
        self.horsemanIA_attack_uleft = self.animation_horsemanIA_attack_uleft()
        self.horsemanIA_attack_right = self.animation_horsemanIA_attack_right()
        self.horsemanIA_attack_uright = self.animation_horsemanIA_attack_uright()
        self.horsemanIA_attack_rdown = self.animation_horsemanIA_attack_rdown()
        self.horsemanIA_attack = self.animation_horsemanIA_attack()
        self.villager_farm = self.animation_worker_farm()
        self.villager_farm_up = self.animation_worker_farm_up()
        self.villager_farm_uleft = self.animation_worker_farm_uleft()
        self.villager_farm_ldown = self.animation_worker_farm_ldown()
        self.villager_farm_left = self.animation_worker_farm_left()
        self.villager_farm_uright = self.animation_worker_farm_uright()
        self.villager_farm_right = self.animation_worker_farm_right()
        self.villager_farm_rdown = self.animation_worker_farm_rdown()
        self.villagerIA_farm = self.animation_workerIA_farm()
        self.villagerIA_farm_up = self.animation_workerIA_farm_up()
        self.villagerIA_farm_uleft = self.animation_workerIA_farm_uleft()
        self.villagerIA_farm_ldown = self.animation_workerIA_farm_ldown()
        self.villagerIA_farm_left = self.animation_workerIA_farm_left()
        self.villagerIA_farm_uright = self.animation_workerIA_farm_uright()
        self.villagerIA_farm_right = self.animation_workerIA_farm_right()
        self.villagerIA_farm_rdown = self.animation_workerIA_farm_rdown()



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


    def animation_soldierIA_attack(self):
        soldierIA_attack = []
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack001.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack002.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack003.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack004.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack005.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack006.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack007.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack008.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack009.png').convert_alpha())
        soldierIA_attack.append(pygame.image.load('assets/soldierIA/Halbadierattack010.png').convert_alpha())
        return soldierIA_attack


    def animation_soldierIA_attack_right(self):
        soldierIA_attack_right = []
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack021V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack022V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack023V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack024V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack025V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack026V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack027V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack028V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack029V2.png').convert_alpha())
        soldierIA_attack_right.append(pygame.image.load('assets/soldierIA/Halbadierattack030V2.png').convert_alpha())
        return soldierIA_attack_right


    def animation_soldierIA_attack_rdown(self):
        soldierIA_attack_rdown = []
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack011V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack012V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack013V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack014V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack015V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack016V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack017V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack018V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack019V2.png').convert_alpha())
        soldierIA_attack_rdown.append(pygame.image.load('assets/soldierIA/Halbadierattack020V2.png').convert_alpha())
        return soldierIA_attack_rdown


    def animation_soldierIA_attack_up(self):
        soldierIA_attack_up = []
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack041.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack042.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack043.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack044.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack045.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack046.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack047.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack048.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack049.png').convert_alpha())
        soldierIA_attack_up.append(pygame.image.load('assets/soldierIA/Halbadierattack050.png').convert_alpha())
        return soldierIA_attack_up


    def animation_soldierIA_attack_uleft(self):
        soldierIA_attack_uleft = []
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack031.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack032.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack033.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack034.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack035.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack036.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack037.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack038.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack039.png').convert_alpha())
        soldierIA_attack_uleft.append(pygame.image.load('assets/soldierIA/Halbadierattack040.png').convert_alpha())
        return soldierIA_attack_uleft

    def animation_soldierIA_attack_left(self):
        soldierIA_attack_left = []
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack021.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack022.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack023.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack024.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack025.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack026.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack027.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack028.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack029.png').convert_alpha())
        soldierIA_attack_left.append(pygame.image.load('assets/soldierIA/Halbadierattack030.png').convert_alpha())
        return soldierIA_attack_left


    def animation_soldierIA_attack_ldown(self):
        soldierIA_attack_ldown = []
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack011.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack012.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack013.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack014.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack015.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack016.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack017.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack018.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack019.png').convert_alpha())
        soldierIA_attack_ldown.append(pygame.image.load('assets/soldierIA/Halbadierattack020.png').convert_alpha())
        return soldierIA_attack_ldown

    def animation_soldierIA_attack_uright(self):
        soldierIA_attack_uright = []
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack031V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack032V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack033V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack034V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack035V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack036V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack037V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack038V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack039V2.png').convert_alpha())
        soldierIA_attack_uright.append(pygame.image.load('assets/soldierIA/Halbadierattack040V2.png').convert_alpha())
        return soldierIA_attack_uright

    def animation_archerIA_attack(self):
        archerIA_attack = []
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack001.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack002.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack003.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack004.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack005.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack006.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack007.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack008.png').convert_alpha())
        archerIA_attack.append(pygame.image.load('assets/archerIA/Archerattack009.png').convert_alpha())
        return archerIA_attack

    def animation_archerIA_attack_right(self):
        archerIA_attack_right = []
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack021V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack022V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack023V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack024V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack025V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack026V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack027V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack028V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack029V2.png').convert_alpha())
        archerIA_attack_right.append(pygame.image.load('assets/archerIA/Archerattack030V2.png').convert_alpha())
        return archerIA_attack_right

    def animation_archerIA_attack_rdown(self):
        archerIA_attack_rdown = []
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack011V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack012V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack013V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack014V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack015V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack016V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack017V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack018V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack019V2.png').convert_alpha())
        archerIA_attack_rdown.append(pygame.image.load('assets/archerIA/Archerattack020V2.png').convert_alpha())
        return archerIA_attack_rdown

    def animation_archerIA_attack_up(self):
        archerIA_attack_up = []
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack041.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack042.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack043.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack044.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack045.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack046.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack047.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack048.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack049.png').convert_alpha())
        archerIA_attack_up.append(pygame.image.load('assets/archerIA/Archerattack050.png').convert_alpha())
        return archerIA_attack_up

    def animation_archerIA_attack_uleft(self):
        archerIA_attack_uleft = []
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack031.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack032.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack033.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack034.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack035.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack036.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack037.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack038.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack039.png').convert_alpha())
        archerIA_attack_uleft.append(pygame.image.load('assets/archerIA/Archerattack040.png').convert_alpha())
        return archerIA_attack_uleft

    def animation_archerIA_attack_left(self):
        archerIA_attack_left = []
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack021.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack022.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack023.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack024.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack025.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack026.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack027.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack028.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack029.png').convert_alpha())
        archerIA_attack_left.append(pygame.image.load('assets/archerIA/Archerattack030.png').convert_alpha())
        return archerIA_attack_left

    def animation_archerIA_attack_ldown(self):
        archerIA_attack_ldown = []
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack011.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack012.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack013.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack014.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack015.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack016.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack017.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack018.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack019.png').convert_alpha())
        archerIA_attack_ldown.append(pygame.image.load('assets/archerIA/Archerattack020.png').convert_alpha())
        return archerIA_attack_ldown

    def animation_archerIA_attack_uright(self):
        archerIA_attack_uright = []
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack031V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack032V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack033V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack034V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack035V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack036V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack037V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack038V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack039V2.png').convert_alpha())
        archerIA_attack_uright.append(pygame.image.load('assets/archerIA/Archerattack040V2.png').convert_alpha())
        return archerIA_attack_uright


    def animation_horsemanIA_attack(self):
        horsemanIA_attack = []
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack001.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack002.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack003.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack004.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack005.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack006.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack007.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack008.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack009.png').convert_alpha())
        horsemanIA_attack.append(pygame.image.load('assets/horsemanIA/Cavalierattack010.png').convert_alpha())
        return horsemanIA_attack

    def animation_horsemanIA_attack_right(self):
        horsemanIA_attack_right = []
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack021V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack022V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack023V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack024V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack025V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack026V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack027V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack028V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack029V2.png').convert_alpha())
        horsemanIA_attack_right.append(pygame.image.load('assets/horsemanIA/Cavalierattack030V2.png').convert_alpha())
        return horsemanIA_attack_right

    def animation_horsemanIA_attack_rdown(self):
        horsemanIA_attack_rdown = []
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack011V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack012V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack013V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack014V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack015V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack016V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack017V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack018V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack019V2.png').convert_alpha())
        horsemanIA_attack_rdown.append(pygame.image.load('assets/horsemanIA/Cavalierattack020V2.png').convert_alpha())
        return horsemanIA_attack_rdown

    def animation_horsemanIA_attack_up(self):
        horsemanIA_attack_up = []
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack041.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack042.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack043.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack044.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack045.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack046.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack047.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack048.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack049.png').convert_alpha())
        horsemanIA_attack_up.append(pygame.image.load('assets/horsemanIA/Cavalierattack050.png').convert_alpha())
        return horsemanIA_attack_up

    def animation_horsemanIA_attack_uleft(self):
        horsemanIA_attack_uleft = []
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack031.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack032.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack033.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack034.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack035.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack036.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack037.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack038.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack039.png').convert_alpha())
        horsemanIA_attack_uleft.append(pygame.image.load('assets/horsemanIA/Cavalierattack040.png').convert_alpha())
        return horsemanIA_attack_uleft

    def animation_horsemanIA_attack_left(self):
        horsemanIA_attack_left = []
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack021.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack022.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack023.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack024.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack025.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack026.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack027.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack028.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack029.png').convert_alpha())
        horsemanIA_attack_left.append(pygame.image.load('assets/horsemanIA/Cavalierattack030.png').convert_alpha())
        return horsemanIA_attack_left

    def animation_horsemanIA_attack_ldown(self):
        horsemanIA_attack_ldown = []
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack011.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack012.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack013.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack014.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack015.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack016.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack017.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack018.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack019.png').convert_alpha())
        horsemanIA_attack_ldown.append(pygame.image.load('assets/horsemanIA/Cavalierattack020.png').convert_alpha())
        return horsemanIA_attack_ldown

    def animation_horsemanIA_attack_uright(self):
        horsemanIA_attack_uright = []
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack031V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack032V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack033V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack034V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack035V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack036V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack037V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack038V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack039V2.png').convert_alpha())
        horsemanIA_attack_uright.append(pygame.image.load('assets/horsemanIA/Cavalierattack040V2.png').convert_alpha())
        return horsemanIA_attack_uright


    def animation_worker_farm(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack001.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack002.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack003.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack004.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack005.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack006.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack007.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack008.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack009.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack010.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack011.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack012.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack013.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack014.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack015.png').convert_alpha())
        return villager_farm



    def animation_worker_farm_ldown(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack016.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack017.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack018.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack019.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack020.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack021.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack022.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack023.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack024.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack025.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack026.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack027.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack028.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack029.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack030.png').convert_alpha())
        return villager_farm


    def animation_worker_farm_left(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack031.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack032.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack033.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack034.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack035.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack036.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack037.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack038.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack039.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack040.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack041.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack042.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack043.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack044.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack045.png').convert_alpha())
        return villager_farm

    def animation_worker_farm_uleft(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack046.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack047.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack048.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack049.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack050.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack051.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack052.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack053.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack054.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack055.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack056.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack057.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack058.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack059.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack060.png').convert_alpha())
        return villager_farm

    def animation_worker_farm_up(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack061.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack062.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack063.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack064.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack065.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack066.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack067.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack068.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack069.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack070.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack071.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack072.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack073.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack074.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack075.png').convert_alpha())
        return villager_farm


    def animation_worker_farm_rdown(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack016V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack017V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack018V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack019V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack020V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack021V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack022V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack023V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack024V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack025V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack026V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack027V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack028V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack029V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack030V2.png').convert_alpha())
        return villager_farm


    def animation_worker_farm_right(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack031V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack032V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack033V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack034V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack035V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack036V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack037V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack038V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack039V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack040V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack041V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack042V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack043V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack044V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack045V2.png').convert_alpha())
        return villager_farm

    def animation_worker_farm_uright(self):
        villager_farm = []
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack046V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack047V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack048V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack049V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack050V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack051V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack052V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack053V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack054V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack055V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack056V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack057V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack058V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack059V2.png').convert_alpha())
        villager_farm.append(pygame.image.load('assets/villager/Villagerattack060V2.png').convert_alpha())
        return villager_farm




    def animation_workerIA_farm(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack001.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack002.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack003.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack004.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack005.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack006.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack007.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack008.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack009.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack010.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack011.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack012.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack013.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack014.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack015.png').convert_alpha())
        return villagerIA_farm



    def animation_workerIA_farm_ldown(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack016.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack017.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack018.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack019.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack020.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack021.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack022.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack023.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack024.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack025.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack026.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack027.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack028.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack029.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack030.png').convert_alpha())
        return villagerIA_farm


    def animation_workerIA_farm_left(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack031.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack032.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack033.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack034.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack035.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack036.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack037.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack038.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack039.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack040.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack041.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack042.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack043.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack044.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack045.png').convert_alpha())
        return villagerIA_farm

    def animation_workerIA_farm_uleft(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack046.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack047.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack048.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack049.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack050.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack051.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack052.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack053.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack054.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack055.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack056.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack057.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack058.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack059.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack060.png').convert_alpha())
        return villagerIA_farm

    def animation_workerIA_farm_up(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack061.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack062.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack063.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack064.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack065.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack066.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack067.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack068.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack069.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack070.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack071.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack072.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack073.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack074.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack075.png').convert_alpha())
        return villagerIA_farm


    def animation_workerIA_farm_rdown(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack016V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack017V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack018V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack019V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack020V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack021V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack022V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack023V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack024V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack025V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack026V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack027V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack028V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack029V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack030V2.png').convert_alpha())
        return villagerIA_farm


    def animation_workerIA_farm_right(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack031V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack032V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack033V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack034V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack035V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack036V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack037V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack038V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack039V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack040V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack041V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack042V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack043V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack044V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack045V2.png').convert_alpha())
        return villagerIA_farm

    def animation_workerIA_farm_uright(self):
        villagerIA_farm = []
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack046V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack047V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack048V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack049V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack050V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack051V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack052V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack053V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack054V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack055V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack056V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack057V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack058V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack059V2.png').convert_alpha())
        villagerIA_farm.append(pygame.image.load('assets/villagerIA/Villagerattack060V2.png').convert_alpha())
        return villagerIA_farm