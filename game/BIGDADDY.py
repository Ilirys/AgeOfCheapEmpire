from .soldier import Soldier

class Bigdaddy(Soldier):

    def __init__(self, tile, world, camera, pv=100000,  team="blue"):
        super().__init__(tile, world, camera, pv, team)
        self.name = "Bigdaddy"
        self.dmg = 1000