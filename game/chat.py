import pygame as pg

from game.BIGDADDY import Bigdaddy


pg.init()
pg.font.init()

COLOR_INACTIVE = pg.Color(127,127,127)
COLOR_ACTIVE = pg.Color(255,255,255)
FONT = pg.font.SysFont('arial', 20)


class Chat:

    def __init__(self, world, camera, resource_manager, x, y, w, h, text=''):
        self.world = world
        self.camera = camera
        self.resource_manager = resource_manager
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the chat rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    if self.text == "NINJALUI":
                        if self.resource_manager.resources["wood"] + 10000 <= 99999 :
                            self.resource_manager.resources["wood"] += 10000
                        else :
                            self.resource_manager.resources["wood"] = 99999

                        if self.resource_manager.resources["stone"] + 10000 <= 99999 :
                            self.resource_manager.resources["stone"] += 10000
                        else :
                            self.resource_manager.resources["stone"] = 99999

                        if self.resource_manager.resources["food"] + 10000 <= 99999 :
                            self.resource_manager.resources["food"] += 10000
                        else :
                            self.resource_manager.resources["food"] = 99999

                    elif self.text == "BIGDADDY":
                        print("SPAWN POWERFUL UNITS at town center")
                        if not(self.world.world[0][0]["collision"]) : 
                            Bigdaddy(self.world.world[0][0], self.world, self.camera)
                    
                    elif self.text == "STEROIDS":
                        print("training, building, farming are instantaneous for every players")


                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
