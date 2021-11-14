
class workerDTO:
    def __init__(self,name,health_points,tile):
        self.name = name
        self.health_points = health_points 
        self.tile = tile
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]