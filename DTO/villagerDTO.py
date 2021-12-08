
class villagerDTO:
    def __init__(self, name, pv, range, dmg, tile):
        self.name = name
        self.pv = pv
        self.tile = tile
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]
        self.range = range
        self.dmg = dmg