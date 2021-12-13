from .soldier import Soldier

class Bigdaddy(Soldier):

    def __init__(self, tile, world, camera):
        super().__init__(tile, world, camera)
        self.name = "Bigdaddy"
        self.dmg = 1000
        self.pv = 100000